import os
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.postgres.fields import ArrayField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import QueryDict
from location_field.models.plain import PlainLocationField
from .managers import SubZoneManager, CategoryManager

class BaseTitleMixin():
    def __str__(self):
        return self.title

class AbstractBaseModel(models.Model):
    title = models.CharField(
        max_length=128,
        help_text="<b>This field cannot be blank</b>. Enter title. (For Address title, enter Activity title itself)Max length: 128."
    )

    class Meta:
        abstract = True

class AbstractBaseURLModel(AbstractBaseModel):
    url_name = models.SlugField(
        max_length=128,
        default='',
        editable=False,
        help_text='Non-Editable. Used for making URLs'
    )

    def save(self, *args, **kwargs):
        self.url_name = slugify(self.title)
        super().save(*args, **kwargs)

    def get_url(self, view_name):
        kwargs = {
            'title': self.url_name,
            'id': self.pk
        }

        return reverse(view_name, kwargs=kwargs)

    class Meta:
        abstract = True

class Zone(BaseTitleMixin, AbstractBaseModel):
    class Meta:
        verbose_name = "Zone"
        verbose_name_plural = "Zones"

class SubZone(BaseTitleMixin, AbstractBaseModel):
    zone = models.ForeignKey(Zone)
    objects = SubZoneManager()

    def get_activities(self):
        return ', '.join([address.activity.title for address in self.address_set.all()])
    get_activities.short_description = 'Activities'

    class Meta:
        verbose_name = "Sub-Zone"
        verbose_name_plural = "Sub-Zones"

class MetroLineColor(BaseTitleMixin, AbstractBaseModel):
    color = models.CharField(max_length=7, default="#000")

    class Meta:
        verbose_name = "Metro line color"
        verbose_name_plural = "Metro line colors"        

class MetroStation(BaseTitleMixin, models.Model):
    title = models.CharField(
        max_length=128,
        help_text="<b>This field cannot be blank</b>. Max length: 128."
    )

    color = models.ForeignKey(MetroLineColor, null=True)

    class Meta:
        verbose_name = "Metro Station"
        verbose_name_plural = "Metro Stations"

class Address(BaseTitleMixin, AbstractBaseModel):
    address_line1 = models.CharField(
        max_length=128,
        help_text="<b>This field cannot be blank</b>. Max length: 128"
    )

    address_line2 = models.CharField(
        max_length=128,
        help_text="<b>This field cannot be blank</b>. Max length: 128",
        blank=True
    )

    sub_zone = models.ManyToManyField(
        SubZone,
        help_text="<b>This field cannot be blank</b>. Enter list of sub-zones. Put all relevant sub-zones, but be consistent in format. Choose multiple from the list, or create a new one. For eg. 'sector 18 noida, noida'."
    )

    zone = models.ForeignKey(
        Zone,
        help_text="<b>This field cannot be blank</b>. Choose from selected Zones, or create a new Zone."
    )

    pin_code = models.IntegerField(
        default=0, 
        blank=True,
        null=True,
        help_text="<i>This field may be blank</i>. Enter Pin Code in six digit format. For eg. 110001"
    )

    metro_station = models.ManyToManyField(
        MetroStation,
        blank=True,
        help_text="<b>This field can be blank</b>. Enter list of nearest metro stations. Choose multiple from the list, or create a new one. For eg. 'Rajiv Chowk Station, Mandi House Station'."
    )

    map_address = models.CharField(
        max_length=255,
        help_text='<b>This is only a helper field</b>. Enter address here, and we will populate latitude and longitude into map automatically',
        blank=True
    )

    location = PlainLocationField(based_fields=[map_address], zoom=15, blank=True, null=True)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

class Place(models.Model):
    address = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=[address], zoom=15)

class Box(BaseTitleMixin, AbstractBaseURLModel):
    featured_image = models.ImageField(upload_to='photos/box/', default='photos/activity/featured/featured.png')
    cover_image = models.ImageField(upload_to='photos/box/', default='photos/activity/featured/featured.png')

    def get_absolute_url(self):
        return self.get_url('box')

    class Meta:
        verbose_name = "Box"
        verbose_name_plural = "Boxes"

class Category(BaseTitleMixin, AbstractBaseModel):
    box = models.ManyToManyField(
        Box,
        help_text="Select Box from List",
        blank=True,
        default=None
    )

    def get_absolute_url(self):
        q = QueryDict(mutable=True)
        q.update({'c': self.id})

        return "{}?{}".format(reverse('search'), q.urlencode())

    objects = CategoryManager()

    def get_activities(self):
        return ', '.join([activity.title for activity in self.activity_set.all()])
    get_activities.short_description = 'Activities'

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Activity(BaseTitleMixin, AbstractBaseURLModel):
    address = models.OneToOneField(Address)

    category = models.ManyToManyField(
        Category,
        help_text="<b>This field cannot be blank</b>. Enter list of categories. Put all relevant categories, but be consistent in format. For eg. 'bowling, pool'."
    )

    description = models.TextField(
        blank=True,
        help_text="<i>This field may be blank</i>. Enter long description here. No limit. Can be used for listing unique features not covered by any other field."
    )

    rating = models.DecimalField(
        default=0.0,
        editable=False,
        max_digits=2,
        decimal_places=1,
        help_text='Non-Editable. Will be changed automatically'
    )

    votes = models.IntegerField(
        default=0, 
        editable=False,
        help_text='Non-Editable. Will be changed automatically'
    )

    cost = models.IntegerField(
        default=0,
        help_text='<b>This field cannot be blank</b>. 1-5 Point System. 1 for lowest and 5 highest.'
    )

    person_of_contact = models.CharField(
        max_length=128, 
        blank=True, 
        null=True,
        help_text="<i>This field may be blank</i>. Enter name of person of contact. For Eg. Mr. ABC XYZ. Max length: 128"
    )

    contact_numbers = ArrayField(
        models.CharField(max_length=50),
        help_text="<b>This field cannot be blank</b>. Enter list of contact numbers. Max 15 digit number, include +91- for mobile numbers, and std-code (011-) for landlines. Be consistent."
    )

    email = models.EmailField(
        blank=True, 
        null=True,
        help_text="<i>This field may be blank</i>. Enter one email id."
    )

    website = models.URLField(
        blank=True, 
        null=True, 
        help_text="<i>This field may be blank</i>. Enter one website url. Don't put 'http://' in front."
    )

    facebook = models.URLField(
        blank=True, 
        null=True, 
        help_text="<i>This field may be blank</i>. Enter facebook page url. Don't put 'http://' in front."
    )

    twitter = models.URLField(
        blank=True, 
        null=True, 
        help_text="<i>This field may be blank</i>. Enter twitter url. Don't put 'http://' in front."
    )

    linkedin = models.URLField(
        blank=True, 
        null=True, 
        help_text="<i>This field may be blank</i>. Enter linkedin url. Don't put 'http://' in front."
    )

    featured_image = models.ImageField(upload_to='photos/activity/featured/', default='photos/activity/featured/featured.png')

    def get_subzones(self):
        return ', '.join([sub_zone.title for sub_zone in self.address.sub_zone.all()])
    get_subzones.short_description = 'Sub Zones'

    def get_categories(self):
        return ', '.join([category.title for category in self.category.all()])
    get_categories.short_description = 'Categories'

    def get_address(self):
        address = self.address.address_line1
        
        address_line2 = self.address.address_line2
        if address_line2:
            address = address + " " + address_line2

        return address
    get_address.short_description = 'Address'

    def get_absolute_url(self):
        return self.get_url('activity')

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
        ordering = ['id']

class UserBookmark(models.Model):
    user = models.OneToOneField(User)
    bookmarks = models.ManyToManyField(Activity)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Bookmark"
        verbose_name_plural = "User Bookmarks"

class UserRating(models.Model):
    user = models.ForeignKey(User)
    activity = models.ForeignKey(Activity)
    rating = models.IntegerField()

    def __str__(self):
        return "{0} : {1} : {2}".format(self.user.username, self.activity.title, self.rating)

    class Meta:
        verbose_name = 'User Rating'
        verbose_name_plural = 'User Ratings'

class UserReview(models.Model):
    user = models.ForeignKey(User, editable=False)
    activity = models.ForeignKey(Activity, editable=False)
    pub_date = models.DateTimeField(editable=False)
    review = models.TextField(editable=False)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return "{0} : {1} : {2}".format(self.user.username, self.activity.title, self.pub_date)

    class Meta:
        verbose_name = 'User Review'
        verbose_name_plural = 'User Reviews'
        
class FeaturedActivity(models.Model):
    featured_1 = models.ForeignKey(Activity, related_name='featured_1')
    featured_2 = models.ForeignKey(Activity, related_name='featured_2')
    featured_3 = models.ForeignKey(Activity, related_name='featured_3')
    featured_4 = models.ForeignKey(Activity, related_name='featured_4')

    def __str__(self):
        return "Featured Activities"

    class Meta:
        verbose_name = 'Featured Activity'
        verbose_name_plural = 'Featured Activities'

def activity_gallery_upload_to(instance, filename):
    if instance.activity.url_name:
        return os.path.join('photos', 'activity', str(instance.activity.id), 'photos', filename)
    else:
        return None

class ImageGallery(models.Model):
    activity = models.ForeignKey(Activity, related_name='photos')
    image = models.ImageField(upload_to=activity_gallery_upload_to)

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

class Feedback(models.Model):
    name = models.CharField(max_length=128)
    message = models.TextField(max_length=1024)
    email = models.EmailField()

    def __str__(self):
        return "{0} - {1}".format(self.name, self.email)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
