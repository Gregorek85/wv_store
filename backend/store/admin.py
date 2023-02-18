from django.contrib import admin
from .models import Picture, Item
from django.apps import apps


class PictureInline(admin.StackedInline):
    model = Picture


@admin.register(Item)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PictureInline]


###Register all models except 'picture':
class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)


models = apps.get_models()
for model in models:
    if "picture" not in model._meta.model_name:
        # print(model._meta.model_name)
        # print(model._meta.app_label)
        admin_class = type("AdminClass", (ListAdminMixin, admin.ModelAdmin), {})
        try:
            admin.site.register(model, admin_class)
        except admin.sites.AlreadyRegistered:
            pass
