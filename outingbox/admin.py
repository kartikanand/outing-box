from django.contrib import admin
from .models import Zone, SubZone, MetroStation, Address, ParentCategory, Category, Activity, Box, UserRating, FeaturedActivity, ImageGallery

class ImageGalleryInlineAdmin(admin.TabularInline):
    model = ImageGallery

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    inlines = [
        ImageGalleryInlineAdmin,
    ]

    filter_horizontal = ['category']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    filter_horizontal = ['sub_zone', 'metro_station']

admin.site.register(Zone)
admin.site.register(SubZone)
admin.site.register(MetroStation)
admin.site.register(ParentCategory)
admin.site.register(Category)
admin.site.register(Box)
admin.site.register(UserRating)
admin.site.register(FeaturedActivity)
