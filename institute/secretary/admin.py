from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Term)
admin.site.register(Lesson)
admin.site.register(SecretaryRegister)
admin.site.register(StudentSiteRegister)
admin.site.register(TeacherSiteRegister)
admin.site.register(SecretarySiteRegister)


