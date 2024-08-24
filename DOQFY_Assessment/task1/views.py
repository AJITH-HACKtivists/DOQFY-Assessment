from django.shortcuts import render
from django.views.generic import TemplateView
from .modelforms import UrlModelForm
from .models import UrlModel

# Create your views here.
class UrlShortFormGenerator(TemplateView):
    template_name = 'task1/task1.html'
    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = UrlModelForm()
        context['form'] = form
        urls_list = list(UrlModel.objects.all().order_by("-id").values())
        context['urls_list'] = urls_list
        return self.render_to_response(context)



    def post(self,request, *args, **kwargs ):
        form = UrlModelForm(request.POST)
        if form.is_valid():
            form.save()
            form=UrlModelForm()
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['urls_list'] = list(UrlModel.objects.all().order_by("-id").values())
        return self.render_to_response(context)
