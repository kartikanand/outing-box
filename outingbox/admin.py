from django.contrib import admin
from .models import Zone, SubZone, MetroStation, Address, Category, Activity, Box, UserRating, FeaturedActivity, ImageGallery, Feedback, UserReview

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

@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    ordering = ('is_published', 'pub_date')
    list_display = ('user', 'activity', 'pub_date', 'is_published')
    readonly_fields = ('user', 'activity', 'pub_date', 'review')

admin.site.register(Zone)
admin.site.register(SubZone)
admin.site.register(MetroStation)
admin.site.register(Category)
admin.site.register(Box)
admin.site.register(UserRating)
admin.site.register(Feedback)
admin.site.register(FeaturedActivity)
