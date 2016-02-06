from django.db import models

class NameValueListMixin():
    def all_name_value_list(self):
        return [{'name': obj.title, 'value': obj.id} for obj in super().get_queryset()]

class SubZoneManager(NameValueListMixin, models.Manager):
    pass

class CategoryManager(NameValueListMixin, models.Manager):
    pass
