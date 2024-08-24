from typing import Iterable
from django.db import models
import re;
from django.core.exceptions import ValidationError;
import random
import string

def generate_short_url(url):
    pattern = re.compile(r'https?://([^/]+)\.(?:com|org|net|edu|in|co|gov|biz|info|io|[a-z]{2,})')
    match = pattern.search(url)
    if match:
        return match.group(1)
    else:
         characters = string.ascii_letters + string.digits  # Includes letters and digits
         return ''.join(random.choice(characters) for _ in range(8))

def custom_url_validator(value):
    # Regex for URL validation (you can modify the pattern based on requirements)
    url_regex = re.compile(
        r'^(https?|ftp):\/\/'  # Protocols (http, https, ftp)
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # Domain
        r'localhost|'  # Allow localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IPv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPv6
        r'(?::\d+)?'  # Optional port
        r'(\/?|[\/?]\S*)$', re.IGNORECASE)  # Path
        
    if not re.match(url_regex, value):
        raise ValidationError('Invalid URL format')
    


# Create your models here.
class UrlModel(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=500, validators=[custom_url_validator],unique=True)
    short_url = models.URLField(max_length=200)

    def save(self, *args, **kwargs):
        self.short_url = generate_short_url(self.url)
        while UrlModel.objects.filter(short_url=self.short_url).exists():
            self.short_url = generate_short_url(self.url)
            self.short_url = self.short_url+str(random.random())
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.url} --> {self.short_url}'