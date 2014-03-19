from django.contrib import admin
from models import Category, Editorial


class EditorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'active')
    save_on_top = True
    list_filter = ('active',)

admin.site.register(Editorial, EditorialAdmin)
