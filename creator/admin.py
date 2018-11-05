from django.contrib import admin
from .models import months
from .models import weeks
from .models import content

# Register your models here.

admin.site.register(months)
admin.site.register(weeks)
admin.site.register(content)
