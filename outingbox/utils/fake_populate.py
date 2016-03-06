import sys, os
sys.path.append('/home/kartik/projects/outing-box-project')

from django.conf import settings

import random

import django
django.setup()

def add_metro_station_colors():
    from outingbox.models import MetroStation, MetroLineColor
    import json

    color_json = {}
    with open('out') as f:
        color_json = json.load(f)

    for metro_station in MetroStation.objects.all():
        line_color = color_json[metro_station.title] 
        mcolor = MetroLineColor.objects.filter(title__icontains=line_color)
        if mcolor.count() > 0:
            metro_station.color = mcolor[0]
            metro_station.save()
        else:
            print("Not found for {0}", metro_station.title)

def add_metro_stations():
    from outingbox.models import MetroStation

    for metro_station_title, _ in MetroStation._meta.get_field('title').choices:
        metro_station = MetroStation(title=metro_station_title)
        metro_station.save()

def add_fake_sub_zone(num_sub_zones, fake):
    from outingbox.models import SubZone, Zone

    for i in range(num_sub_zones):
        sub_zone = SubZone(
            title=fake.city(),
            zone=Zone.objects.get(pk=1)
        )
        sub_zone.save()

def add_fake_category(num_category, fake):
    from outingbox.models import Category, ParentCategory
    from outingbox.models import Box

    for i in range(num_category):
        category = Category(
            title=fake.word(),
            parent_category=ParentCategory.objects.get(pk=random.randint(1, 7))
        )
        category.save()

        boxes = Box.objects.all()
        for box in random.sample(set(boxes), 2):
            category.box.add(box)

def add_rating():
    from outingbox.models import Activity

    for activity in Activity.objects.all():
        activity.rating = (random.randint(0, 50))/10
        activity.votes = 1
        activity.cost = random.randint(1, 5)
        activity.save()

def add_fake_activity(num_activity, fake):
    from outingbox.models import Zone, SubZone, Category, Activity, Address, MetroStation

    for i in range(num_activity):

        activity_title = fake.company()

        zone = Zone.objects.get(pk=1)

        address = Address(
            title = activity_title,
            zone = zone,
            address_line1 = fake.street_address(),
            address_line2 = fake.street_address(),
            pin_code = random.randint(110001, 110099)
        )
        address.save()

        metro_stations = MetroStation.objects.all()
        for metro_station in random.sample(set(metro_stations), 2):
            address.metro_station.add(metro_station)

        sub_zones = SubZone.objects.all()
        for sub_zone in random.sample(set(sub_zones), 2):
            address.sub_zone.add(sub_zone)

        activity = Activity(
            title=activity_title,
            address=address,
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

        categories = Category.objects.all()
        for category in random.sample(set(categories), 2):
            activity.category.add(category)

def main():
    from faker import Faker
    fake = Faker()

    add_metro_station_colors()

    #add_metro_stations()

    #add_fake_sub_zone(50, fake)
    #add_fake_category(50, fake)

    #add_fake_activity(100, fake)

    add_rating()

if __name__ == "__main__":
    main()
