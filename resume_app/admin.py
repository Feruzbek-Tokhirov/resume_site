from django.contrib import admin
from .models import About, Category, Portfolio, Service, Resume_work, Contact, Education
# Register your models here.
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(Service)
admin.site.register(Resume_work)
admin.site.register(Education)

