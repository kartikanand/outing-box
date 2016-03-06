import random
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from outingbox.models import Box, Activity, Address, Category, SubZone, Zone, MetroStation, MetroLineColor, UserBookmark

from faker import Faker
fake = Faker()

def get_fake_users(count=1):
    user_list = []
    for i in range(count):
        user_list.append(get_fake_user())

    return user_list

def get_fake_boxes(count=1):
    box_list = []
    for i in range(count):
        box_list.append(get_fake_box())

    return box_list

def get_fake_categories(count=1):
    category_list = []
    for i in range(count):
        category_list.append(get_fake_category())

    return category_list

def get_fake_activities(count=1):
    activity_list = []
    for i in range(count):
        activity_list.append(get_fake_activity())

    return activity_list

def get_fake_sub_zones(count=1, zone=None):
    sub_zone_list = []
    for i in range(count):
        sub_zone_list.append(get_fake_sub_zone(zone=zone))

    return sub_zone_list

def get_fake_zone(count=1):
    zone_list = []
    for i in range(count):
        zone_list.append(get_fake_zone())

    return zone_list

def get_fake_addresses(count=1):
    address_list = []
    for i in range(count):
        address_list.append(get_fake_address())

    return address_list

def get_fake_metro_stations(count=1):
    metro_station_list = []
    for i in range(count):
        metro_station_list.append(get_fake_metro_station())

    return metro_station_list

def get_fake_user_and_credentials():
    profile = fake.simple_profile()
    username = profile['username']
    passwd = fake.word()
    email = profile['mail']
    user = User.objects.create_user(username, email, passwd)
    return (user, username, passwd)

def get_fake_box():
    box = Box(title=fake.word())
    box.save()

    return box

def get_fake_activity(categories=[], sub_zones=[]):
    activity = Activity(
        title=fake.word(),
        address=get_fake_address(sub_zones),
        description = fake.text(),
        person_of_contact = fake.name(),
        contact_numbers = [fake.phone_number(), fake.phone_number()],
        cost = random.randint(1, 5),
        email = fake.email(),
        website = fake.url(),
        facebook=fake.url(),
        twitter = fake.url(),
        linkedin = fake.url(),
    )
    activity.save()

    if not categories:
        categories = get_fake_categories(count=2)

    for category in categories:
        activity.category.add(category)

    return activity

def get_fake_category(box=None):
    category = Category(title=fake.word())
    category.save()

    if box:
        category.box.add(box)

    return category

def get_fake_address(zone=None, sub_zones=[], metro_stations=[]):
    if not zone:
        zone = get_fake_zone()

    address = Address(
        title = fake.word(),
        zone = zone,
        address_line1 = fake.street_address(),
        address_line2 = fake.street_address(),
        pin_code = random.randint(110001, 110099)
    )
    address.save()

    if not metro_stations:
        metro_stations = get_fake_metro_stations(count=2)

    for metro_station in metro_stations:
        address.metro_station.add(metro_station)

    if not sub_zones:
        sub_zones = get_fake_sub_zones(count=2, zone=zone)

    for sub_zone in sub_zones:
        address.sub_zone.add(sub_zone)

    return address

def get_fake_sub_zone(zone=None):
    if not zone:
        zone = get_fake_zone()

    sub_zone = SubZone(title=fake.word(), zone=zone)
    sub_zone.save()

    return sub_zone

def get_fake_zone():
    zone = Zone(title=fake.word())
    zone.save()

    return zone

def get_fake_metro_station():
    metro_line_color = MetroLineColor(title=fake.color_name(), color=fake.safe_hex_color())
    metro_line_color.save()

    metro_station = MetroStation(title=fake.word(), color=metro_line_color)
    metro_station.save()

    return metro_station

def get_user_bookmarks(user):
    try:
        user_bookmarks = user.userbookmark.bookmarks.all()
    except ObjectDoesNotExist:
        user_bookmarks = []

    return user_bookmarks

def get_user_rating(user, activity):
    try:
        user_rating = user.userrating_set.get(activity=activity).rating
    except UserRating.DoesNotExist:
        user_rating = None

    return user_rating
