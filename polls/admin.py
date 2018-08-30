from django.contrib import admin

# Register your models here, so that questions can be added through Django Admin.
from .models import Question

admin.site.register(Question)
