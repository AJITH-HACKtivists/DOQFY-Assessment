from django.views.generic import TemplateView
from .modelforms import SnippetModelForm
from django.utils.text import slugify
from django.urls import reverse
from .models import SnippetModel
from django.http import Http404
from django.core.exceptions import ValidationError
from django.db import DatabaseError
import jwt

# Create your views here.

class CreateContentTemplate(TemplateView):
    template_name='task2/task2.html'
    def get(self, request,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SnippetModelForm()
        context['errors'] = {}
        context['form'] = form
        return self.render_to_response(context)
    
    def post(self,request,*args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = SnippetModelForm(request.POST)
        context['errors'] = {}
        if form.is_valid():
            try:
              snippet = form.save(commit=False)
              snippet.save()
              sharable_url = slugify(snippet.text[:10] + '-' + str(snippet.id))
              snippet.shareable_url=sharable_url
              snippet.save()
              form = SnippetModelForm()
              context['sharable_url'] = request.build_absolute_uri(reverse('view_snippet', args=[snippet.shareable_url]))
            except ValidationError as ve:
                context['errors']['validation'] = str(ve)
            except DatabaseError as de:
                context['errors']['database'] = 'Database error occurred: ' + str(de)
            except Exception as e:
                context['errors']['unexpected'] = 'An unexpected error occurred: ' + str(e)
            
        context['form'] = form
        return self.render_to_response(context)
    

class ViewSnippetContent(TemplateView):
    template_name = 'task2/viewsnippetcontent.html'
    def get(self, request,*args,**kwargs):
        slug = kwargs.get('slug')
        context = super().get_context_data(**kwargs)
        slug_data = SnippetModel.objects.filter(shareable_url = slug).first()

        if slug_data:
            if not slug_data.secret_key:
                context['text'] = slug_data.text   
        else:
             raise Http404("Snippet not found")
        encode = jwt.encode({"text":"testing"}, 'secret', algorithm="HS256")
        decoded_data = jwt.decode(encode, 'secret', algorithms=['HS256'])
        print(decoded_data)
        
        # Render the template with a message if a secret key is required
        return self.render_to_response(context)
    
    def post(self, request,*args,**kwargs):
        slug = kwargs.get('slug')
        context = self.get_context_data(**kwargs)
        slug_data = SnippetModel.objects.filter(shareable_url = slug).first()
        if slug_data:
            secret_key = request.POST.get('secret_key')
            try:
                text = slug_data.decrypt_text(key=secret_key)
                if text:
                    context['text'] = text
                else:
                    context['error'] = 'Enter a valid Secret Key'
            except Exception as e:
                context['error'] = 'An unexpected error occurred: ' + str(e)
        else:
            context['error'] = 'Something went wrong please try after sometime'    

        return self.render_to_response(context)

         

                
