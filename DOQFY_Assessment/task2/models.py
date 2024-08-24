from django.db import models
import jwt
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

class SnippetModel(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    secret_key = models.CharField(max_length=256, blank=True, null=True)
    shareable_url = models.SlugField(unique=True, max_length=50)

    def save(self, *args, **kwargs):
        if self.secret_key and not self.shareable_url and self.secret_key.strip()!='':
            try:
                self.text = jwt.encode({"text":self.text}, self.secret_key, algorithm="HS256")
            except Exception as e:
                raise ValidationError(f"Error encoding text: {e}")
        super().save(*args, **kwargs)

    def decrypt_text(self, key):
        """Decrypt (decode) the text using the stored key."""
        if key:
            try:
                decoded_data = jwt.decode(self.text, key, algorithms=['HS256'])
                return decoded_data.get('text', '')
            except jwt.ExpiredSignatureError:
                raise ValidationError(_('Signature has expired'))
            except jwt.InvalidTokenError:
                raise ValidationError(_('Invalid token'))
        return ''

    def __str__(self):
        return f'Snippet {self.shareable_url}'
