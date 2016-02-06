from django.apps import AppConfig
from watson import search as watson

class OutingBoxMainConfig(AppConfig):
    name = 'outingbox'
    verbose_name = 'Outing Box'

    # register models for Django Watson
    def ready(self):
        activity_model = self.get_model('Activity')
        watson.register(activity_model, fields=(
            'address__address_line1',
            'address__address_line2',
            'address__sub_zone',
            'address__zone',
            'address__metro_station',
            'category',
            'category__parent_category'
            )
        )
