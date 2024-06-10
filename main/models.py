from django.db import models
from .validators import validate_file_extension,validate_file_extension_svg
from django.utils.html import mark_safe
from solo.models import SingletonModel

class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Site Name')
    site_description = models.TextField(max_length=255, blank=True, null=True)
    site_logo = models.FileField(upload_to='svg/', validators=[validate_file_extension_svg], default="", blank=True)
    

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"