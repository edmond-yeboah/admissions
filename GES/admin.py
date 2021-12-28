from django.contrib import admin
from .models import hnd_programs,diploma_programs,degree_programs,school,degree_type

# Register your models here.

admin.site.register(school)
admin.site.register(degree_programs)
admin.site.register(hnd_programs)
admin.site.register(diploma_programs)
admin.site.register(degree_type)
