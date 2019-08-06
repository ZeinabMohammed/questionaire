from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Question)
admin.site.register(MultipleChoices)
admin.site.register(TextAnswer)
admin.site.register(File)
admin.site.register(CheckBox)