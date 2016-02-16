import sys, os
sys.path.append('/home/kartik/projects/outing-box-project')

from django.conf import settings

import django
django.setup()

def import_data():
    from outingbox.models import ParentCategory
    main_parent_category_1 = ParentCategory()
    main_parent_category_1.title = 'xxx'
    main_parent_category_1.save()

    from outingbox.models import Category

    main_category_1 = Category()
    main_category_1.title = 'Art Galleries'
    main_category_1.url_name = 'art-galleries'
    main_category_1.parent_category = main_parent_category_1
    main_category_1.save()

    main_category_2 = Category()
    main_category_2.title = 'Bowling'
    main_category_2.url_name = 'bowling'
    main_category_2.parent_category = main_parent_category_1
    main_category_2.save()

    main_category_3 = Category()
    main_category_3.title = 'Pool'
    main_category_3.url_name = 'pool'
    main_category_3.parent_category = main_parent_category_1
    main_category_3.save()

    main_category_4 = Category()
    main_category_4.title = 'Camping'
    main_category_4.url_name = 'camping'
    main_category_4.parent_category = main_parent_category_1
    main_category_4.save()

    main_category_5 = Category()
    main_category_5.title = 'Water Park'
    main_category_5.url_name = 'water-park'
    main_category_5.parent_category = main_parent_category_1
    main_category_5.save()

    main_category_6 = Category()
    main_category_6.title = 'Ice Skating'
    main_category_6.url_name = 'ice-skating'
    main_category_6.parent_category = main_parent_category_1
    main_category_6.save()

    main_category_7 = Category()
    main_category_7.title = 'Pilates'
    main_category_7.url_name = 'pilates'
    main_category_7.parent_category = main_parent_category_1
    main_category_7.save()

    main_category_8 = Category()
    main_category_8.title = 'Naturopathy'
    main_category_8.url_name = 'naturopathy'
    main_category_8.parent_category = main_parent_category_1
    main_category_8.save()

    main_category_9 = Category()
    main_category_9.title = 'Yoga'
    main_category_9.url_name = 'yoga'
    main_category_9.parent_category = main_parent_category_1
    main_category_9.save()

    main_category_10 = Category()
    main_category_10.title = 'Board Game'
    main_category_10.url_name = 'board-game'
    main_category_10.parent_category = main_parent_category_1
    main_category_10.save()

    main_category_11 = Category()
    main_category_11.title = 'Para Gliding'
    main_category_11.url_name = 'para-gliding'
    main_category_11.parent_category = main_parent_category_1
    main_category_11.save()

    main_category_12 = Category()
    main_category_12.title = 'Para Motoring'
    main_category_12.url_name = 'para-motoring'
    main_category_12.parent_category = main_parent_category_1
    main_category_12.save()

    main_category_13 = Category()
    main_category_13.title = 'Zumba'
    main_category_13.url_name = 'zumba'
    main_category_13.parent_category = main_parent_category_1
    main_category_13.save()

    main_category_14 = Category()
    main_category_14.title = 'Bollywood Dance'
    main_category_14.url_name = 'bollywood-dance'
    main_category_14.parent_category = main_parent_category_1
    main_category_14.save()

    main_category_15 = Category()
    main_category_15.title = 'Contemporary Dance'
    main_category_15.url_name = 'contemporary-dance'
    main_category_15.parent_category = main_parent_category_1
    main_category_15.save()

    main_category_16 = Category()
    main_category_16.title = 'Hip Hop Dance'
    main_category_16.url_name = 'hip-hop-dance'
    main_category_16.parent_category = main_parent_category_1
    main_category_16.save()

    main_category_17 = Category()
    main_category_17.title = 'Aerobics'
    main_category_17.url_name = 'aerobics'
    main_category_17.parent_category = main_parent_category_1
    main_category_17.save()

    main_category_18 = Category()
    main_category_18.title = 'Salsa'
    main_category_18.url_name = 'salsa'
    main_category_18.parent_category = main_parent_category_1
    main_category_18.save()

    main_category_19 = Category()
    main_category_19.title = 'Wedding Choreography'
    main_category_19.url_name = 'wedding-choreography'
    main_category_19.parent_category = main_parent_category_1
    main_category_19.save()

    main_category_20 = Category()
    main_category_20.title = 'Belly Dance'
    main_category_20.url_name = 'belly-dance'
    main_category_20.parent_category = main_parent_category_1
    main_category_20.save()

    main_category_21 = Category()
    main_category_21.title = 'Yoga'
    main_category_21.url_name = 'yoga'
    main_category_21.parent_category = main_parent_category_1
    main_category_21.save()

    main_category_22 = Category()
    main_category_22.title = 'Martial Arts'
    main_category_22.url_name = 'martial-arts'
    main_category_22.parent_category = main_parent_category_1
    main_category_22.save()

    main_category_23 = Category()
    main_category_23.title = 'Self Defence'
    main_category_23.url_name = 'self-defence'
    main_category_23.parent_category = main_parent_category_1
    main_category_23.save()

    main_category_24 = Category()
    main_category_24.title = 'B Boying and Break Dance'
    main_category_24.url_name = 'b-boying-and-break-dance'
    main_category_24.parent_category = main_parent_category_1
    main_category_24.save()

    main_category_25 = Category()
    main_category_25.title = 'Jazz Dance'
    main_category_25.url_name = 'jazz-dance'
    main_category_25.parent_category = main_parent_category_1
    main_category_25.save()

    main_category_26 = Category()
    main_category_26.title = 'Gymnastics'
    main_category_26.url_name = 'gymnastics'
    main_category_26.parent_category = main_parent_category_1
    main_category_26.save()

    main_category_27 = Category()
    main_category_27.title = 'Go Karting'
    main_category_27.url_name = 'go-karting'
    main_category_27.parent_category = main_parent_category_1
    main_category_27.save()

    main_category_28 = Category()
    main_category_28.title = 'Paintball'
    main_category_28.url_name = 'paintball'
    main_category_28.parent_category = main_parent_category_1
    main_category_28.save()

    main_category_29 = Category()
    main_category_29.title = 'Arcade'
    main_category_29.url_name = 'arcade'
    main_category_29.parent_category = main_parent_category_1
    main_category_29.save()

    main_category_30 = Category()
    main_category_30.title = 'Amusement Park'
    main_category_30.url_name = 'amusement-park'
    main_category_30.parent_category = main_parent_category_1
    main_category_30.save()

    # Processing model: Zone

    from outingbox.models import Zone

    main_zone_1 = Zone()
    main_zone_1.title = 'NCR'
    main_zone_1.url_name = 'ncr'
    main_zone_1.save()

    # Processing model: SubZone

    from outingbox.models import SubZone

    main_subzone_1 = SubZone()
    main_subzone_1.title = 'East Delhi'
    main_subzone_1.url_name = 'east-delhi'
    main_subzone_1.zone = main_zone_1
    main_subzone_1.save()

    main_subzone_2 = SubZone()
    main_subzone_2.title = 'Mayur Vihar'
    main_subzone_2.url_name = 'mayur-vihar'
    main_subzone_2.zone = main_zone_1
    main_subzone_2.save()

    main_subzone_3 = SubZone()
    main_subzone_3.title = 'Mayur Vihar Phase 1'
    main_subzone_3.url_name = 'mayur-vihar-phase-1'
    main_subzone_3.zone = main_zone_1
    main_subzone_3.save()

    main_subzone_4 = SubZone()
    main_subzone_4.title = 'Gurgaon'
    main_subzone_4.url_name = 'gurgaon'
    main_subzone_4.zone = main_zone_1
    main_subzone_4.save()

    main_subzone_5 = SubZone()
    main_subzone_5.title = 'South Delhi'
    main_subzone_5.url_name = 'south-delhi'
    main_subzone_5.zone = main_zone_1
    main_subzone_5.save()

    main_subzone_6 = SubZone()
    main_subzone_6.title = 'Noida'
    main_subzone_6.url_name = 'noida'
    main_subzone_6.zone = main_zone_1
    main_subzone_6.save()

    main_subzone_7 = SubZone()
    main_subzone_7.title = 'Kapashera'
    main_subzone_7.url_name = 'kapashera'
    main_subzone_7.zone = main_zone_1
    main_subzone_7.save()

    main_subzone_8 = SubZone()
    main_subzone_8.title = 'West Delhi'
    main_subzone_8.url_name = 'west-delhi'
    main_subzone_8.zone = main_zone_1
    main_subzone_8.save()

    main_subzone_9 = SubZone()
    main_subzone_9.title = 'Kapas Hera'
    main_subzone_9.url_name = 'kapas-hera'
    main_subzone_9.zone = main_zone_1
    main_subzone_9.save()

    main_subzone_10 = SubZone()
    main_subzone_10.title = 'GT Karnal Road'
    main_subzone_10.url_name = 'gt-karnal-road'
    main_subzone_10.zone = main_zone_1
    main_subzone_10.save()

    main_subzone_11 = SubZone()
    main_subzone_11.title = 'GTB Memorial'
    main_subzone_11.url_name = 'gtb-memorial'
    main_subzone_11.zone = main_zone_1
    main_subzone_11.save()

    main_subzone_12 = SubZone()
    main_subzone_12.title = 'Narela'
    main_subzone_12.url_name = 'narela'
    main_subzone_12.zone = main_zone_1
    main_subzone_12.save()

    main_subzone_13 = SubZone()
    main_subzone_13.title = 'North West Delhi'
    main_subzone_13.url_name = 'north-west-delhi'
    main_subzone_13.zone = main_zone_1
    main_subzone_13.save()

    main_subzone_14 = SubZone()
    main_subzone_14.title = 'Alipur'
    main_subzone_14.url_name = 'alipur'
    main_subzone_14.zone = main_zone_1
    main_subzone_14.save()

    main_subzone_15 = SubZone()
    main_subzone_15.title = 'North Delhi'
    main_subzone_15.url_name = 'north-delhi'
    main_subzone_15.zone = main_zone_1
    main_subzone_15.save()

    main_subzone_16 = SubZone()
    main_subzone_16.title = 'Sector 29 Gurgaon'
    main_subzone_16.url_name = 'sector-29-gurgaon'
    main_subzone_16.zone = main_zone_1
    main_subzone_16.save()

    main_subzone_17 = SubZone()
    main_subzone_17.title = 'South West Delhi'
    main_subzone_17.url_name = 'south-west-delhi'
    main_subzone_17.zone = main_zone_1
    main_subzone_17.save()

    main_subzone_18 = SubZone()
    main_subzone_18.title = 'Kalindi Kunj'
    main_subzone_18.url_name = 'kalindi-kunj'
    main_subzone_18.zone = main_zone_1
    main_subzone_18.save()

    main_subzone_19 = SubZone()
    main_subzone_19.title = 'Okhla'
    main_subzone_19.url_name = 'okhla'
    main_subzone_19.zone = main_zone_1
    main_subzone_19.save()

    main_subzone_20 = SubZone()
    main_subzone_20.title = 'South Delhi'
    main_subzone_20.url_name = 'south-delhi'
    main_subzone_20.zone = main_zone_1
    main_subzone_20.save()

    main_subzone_21 = SubZone()
    main_subzone_21.title = 'Sector 38 Noida'
    main_subzone_21.url_name = 'sector-38-noida'
    main_subzone_21.zone = main_zone_1
    main_subzone_21.save()

    main_subzone_22 = SubZone()
    main_subzone_22.title = 'Noida'
    main_subzone_22.url_name = 'noida'
    main_subzone_22.zone = main_zone_1
    main_subzone_22.save()

    main_subzone_23 = SubZone()
    main_subzone_23.title = 'Sector 10 Rohini'
    main_subzone_23.url_name = 'sector-10-rohini'
    main_subzone_23.zone = main_zone_1
    main_subzone_23.save()

    main_subzone_24 = SubZone()
    main_subzone_24.title = 'Rohini'
    main_subzone_24.url_name = 'rohini'
    main_subzone_24.zone = main_zone_1
    main_subzone_24.save()

    main_subzone_25 = SubZone()
    main_subzone_25.title = 'Rithala '
    main_subzone_25.url_name = 'rithala'
    main_subzone_25.zone = main_zone_1
    main_subzone_25.save()

    main_subzone_26 = SubZone()
    main_subzone_26.title = 'Haryana'
    main_subzone_26.url_name = 'haryana'
    main_subzone_26.zone = main_zone_1
    main_subzone_26.save()

    main_subzone_27 = SubZone()
    main_subzone_27.title = 'Sonepat'
    main_subzone_27.url_name = 'sonepat'
    main_subzone_27.zone = main_zone_1
    main_subzone_27.save()

    main_subzone_28 = SubZone()
    main_subzone_28.title = 'NH 1'
    main_subzone_28.url_name = 'nh-1'
    main_subzone_28.zone = main_zone_1
    main_subzone_28.save()

    main_subzone_29 = SubZone()
    main_subzone_29.title = 'National Highway 1'
    main_subzone_29.url_name = 'national-highway-1'
    main_subzone_29.zone = main_zone_1
    main_subzone_29.save()

    main_subzone_30 = SubZone()
    main_subzone_30.title = 'Ghaziabad'
    main_subzone_30.url_name = 'ghaziabad'
    main_subzone_30.zone = main_zone_1
    main_subzone_30.save()

    main_subzone_31 = SubZone()
    main_subzone_31.title = 'Delhi Meerut Highway'
    main_subzone_31.url_name = 'delhi-meerut-highway'
    main_subzone_31.zone = main_zone_1
    main_subzone_31.save()

    main_subzone_32 = SubZone()
    main_subzone_32.title = 'Duhai'
    main_subzone_32.url_name = 'duhai'
    main_subzone_32.zone = main_zone_1
    main_subzone_32.save()

    main_subzone_33 = SubZone()
    main_subzone_33.title = 'Bahadurgarh'
    main_subzone_33.url_name = 'bahadurgarh'
    main_subzone_33.zone = main_zone_1
    main_subzone_33.save()

    main_subzone_34 = SubZone()
    main_subzone_34.title = 'Bahadurgarh'
    main_subzone_34.url_name = 'bahadurgarh'
    main_subzone_34.zone = main_zone_1
    main_subzone_34.save()

    main_subzone_35 = SubZone()
    main_subzone_35.title = 'Delhi-Rohtak Road'
    main_subzone_35.url_name = 'delhi-rohtak-road'
    main_subzone_35.zone = main_zone_1
    main_subzone_35.save()

    main_subzone_36 = SubZone()
    main_subzone_36.title = 'Delhi Jaipur Expressway'
    main_subzone_36.url_name = 'delhi-jaipur-expressway'
    main_subzone_36.zone = main_zone_1
    main_subzone_36.save()

    main_subzone_37 = SubZone()
    main_subzone_37.title = ' Nh-8'
    main_subzone_37.url_name = 'nh-8'
    main_subzone_37.zone = main_zone_1
    main_subzone_37.save()

    main_subzone_38 = SubZone()
    main_subzone_38.title = 'Gurgaon'
    main_subzone_38.url_name = 'gurgaon'
    main_subzone_38.zone = main_zone_1
    main_subzone_38.save()

    main_subzone_39 = SubZone()
    main_subzone_39.title = 'Sector 25A Noida'
    main_subzone_39.url_name = 'sector-25a-noida'
    main_subzone_39.zone = main_zone_1
    main_subzone_39.save()

    main_subzone_40 = SubZone()
    main_subzone_40.title = 'Faridabad'
    main_subzone_40.url_name = 'faridabad'
    main_subzone_40.zone = main_zone_1
    main_subzone_40.save()

    main_subzone_41 = SubZone()
    main_subzone_41.title = 'Saket'
    main_subzone_41.url_name = 'saket'
    main_subzone_41.zone = main_zone_1
    main_subzone_41.save()

    main_subzone_42 = SubZone()
    main_subzone_42.title = 'Tilak Nagar'
    main_subzone_42.url_name = 'tilak-nagar'
    main_subzone_42.zone = main_zone_1
    main_subzone_42.save()

    main_subzone_43 = SubZone()
    main_subzone_43.title = 'Chattarpur'
    main_subzone_43.url_name = 'chattarpur'
    main_subzone_43.zone = main_zone_1
    main_subzone_43.save()

    main_subzone_44 = SubZone()
    main_subzone_44.title = 'Sector 18 Noida'
    main_subzone_44.url_name = 'sector-18-noida'
    main_subzone_44.zone = main_zone_1
    main_subzone_44.save()

    main_subzone_45 = SubZone()
    main_subzone_45.title = 'Botanical Garden'
    main_subzone_45.url_name = 'botanical-garden'
    main_subzone_45.zone = main_zone_1
    main_subzone_45.save()

    main_subzone_46 = SubZone()
    main_subzone_46.title = 'Sector 16 Noida'
    main_subzone_46.url_name = 'sector-16-noida'
    main_subzone_46.zone = main_zone_1
    main_subzone_46.save()

    main_subzone_47 = SubZone()
    main_subzone_47.title = 'Sector 17 Gurgaon'
    main_subzone_47.url_name = 'sector-17-gurgaon'
    main_subzone_47.zone = main_zone_1
    main_subzone_47.save()

    main_subzone_48 = SubZone()
    main_subzone_48.title = 'Sector 18 Gurgaon'
    main_subzone_48.url_name = 'sector-18-gurgaon'
    main_subzone_48.zone = main_zone_1
    main_subzone_48.save()

    main_subzone_49 = SubZone()
    main_subzone_49.title = 'Sector 15 Gurgaon'
    main_subzone_49.url_name = 'sector-15-gurgaon'
    main_subzone_49.zone = main_zone_1
    main_subzone_49.save()

    main_subzone_50 = SubZone()
    main_subzone_50.title = 'Kalkaji'
    main_subzone_50.url_name = 'kalkaji'
    main_subzone_50.zone = main_zone_1
    main_subzone_50.save()

    main_subzone_51 = SubZone()
    main_subzone_51.title = 'Nehru Place'
    main_subzone_51.url_name = 'nehru-place'
    main_subzone_51.zone = main_zone_1
    main_subzone_51.save()

    main_subzone_52 = SubZone()
    main_subzone_52.title = 'Lajpat Nagar'
    main_subzone_52.url_name = 'lajpat-nagar'
    main_subzone_52.zone = main_zone_1
    main_subzone_52.save()

    main_subzone_53 = SubZone()
    main_subzone_53.title = 'Hauz Khas'
    main_subzone_53.url_name = 'hauz-khas'
    main_subzone_53.zone = main_zone_1
    main_subzone_53.save()

    main_subzone_54 = SubZone()
    main_subzone_54.title = 'Tughlakabad'
    main_subzone_54.url_name = 'tughlakabad'
    main_subzone_54.zone = main_zone_1
    main_subzone_54.save()

    main_subzone_55 = SubZone()
    main_subzone_55.title = 'Badarpur'
    main_subzone_55.url_name = 'badarpur'
    main_subzone_55.zone = main_zone_1
    main_subzone_55.save()

    main_subzone_56 = SubZone()
    main_subzone_56.title = 'IGI Airport'
    main_subzone_56.url_name = 'igi-airport'
    main_subzone_56.zone = main_zone_1
    main_subzone_56.save()

    main_subzone_57 = SubZone()
    main_subzone_57.title = 'Sohna'
    main_subzone_57.url_name = 'sohna'
    main_subzone_57.zone = main_zone_1
    main_subzone_57.save()

    main_subzone_58 = SubZone()
    main_subzone_58.title = 'Sector 44 Gurgaon'
    main_subzone_58.url_name = 'sector-44-gurgaon'
    main_subzone_58.zone = main_zone_1
    main_subzone_58.save()

    main_subzone_59 = SubZone()
    main_subzone_59.title = 'DLF Phase '
    main_subzone_59.url_name = 'dlf-phase'
    main_subzone_59.zone = main_zone_1
    main_subzone_59.save()

    main_subzone_60 = SubZone()
    main_subzone_60.title = 'DLF Phase 4'
    main_subzone_60.url_name = 'dlf-phase-4'
    main_subzone_60.zone = main_zone_1
    main_subzone_60.save()

    main_subzone_61 = SubZone()
    main_subzone_61.title = 'Rajiv Chowk'
    main_subzone_61.url_name = 'rajiv-chowk'
    main_subzone_61.zone = main_zone_1
    main_subzone_61.save()

    main_subzone_62 = SubZone()
    main_subzone_62.title = 'Connaught place'
    main_subzone_62.url_name = 'connaught-place'
    main_subzone_62.zone = main_zone_1
    main_subzone_62.save()

    main_subzone_63 = SubZone()
    main_subzone_63.title = 'CP'
    main_subzone_63.url_name = 'cp'
    main_subzone_63.zone = main_zone_1
    main_subzone_63.save()

    main_subzone_64 = SubZone()
    main_subzone_64.title = 'Rouse Avenue'
    main_subzone_64.url_name = 'rouse-avenue'
    main_subzone_64.zone = main_zone_1
    main_subzone_64.save()

    main_subzone_65 = SubZone()
    main_subzone_65.title = 'Kailash Colony'
    main_subzone_65.url_name = 'kailash-colony'
    main_subzone_65.zone = main_zone_1
    main_subzone_65.save()

    main_subzone_66 = SubZone()
    main_subzone_66.title = 'South Delhi'
    main_subzone_66.url_name = 'south-delhi'
    main_subzone_66.zone = main_zone_1
    main_subzone_66.save()

    main_subzone_67 = SubZone()
    main_subzone_67.title = 'Lakshmi Nagar'
    main_subzone_67.url_name = 'lakshmi-nagar'
    main_subzone_67.zone = main_zone_1
    main_subzone_67.save()

    main_subzone_68 = SubZone()
    main_subzone_68.title = 'East Delhi'
    main_subzone_68.url_name = 'east-delhi'
    main_subzone_68.zone = main_zone_1
    main_subzone_68.save()

    main_subzone_69 = SubZone()
    main_subzone_69.title = 'Sushant Lok'
    main_subzone_69.url_name = 'sushant-lok'
    main_subzone_69.zone = main_zone_1
    main_subzone_69.save()

    main_subzone_70 = SubZone()
    main_subzone_70.title = 'Sector 43 Gurgaon'
    main_subzone_70.url_name = 'sector-43-gurgaon'
    main_subzone_70.zone = main_zone_1
    main_subzone_70.save()

    main_subzone_71 = SubZone()
    main_subzone_71.title = 'DLF Phase 1'
    main_subzone_71.url_name = 'dlf-phase-1'
    main_subzone_71.zone = main_zone_1
    main_subzone_71.save()

    main_subzone_72 = SubZone()
    main_subzone_72.title = 'Sector 6 Gurgaon'
    main_subzone_72.url_name = 'sector-6-gurgaon'
    main_subzone_72.zone = main_zone_1
    main_subzone_72.save()

    main_subzone_73 = SubZone()
    main_subzone_73.title = 'Karkardooma'
    main_subzone_73.url_name = 'karkardooma'
    main_subzone_73.zone = main_zone_1
    main_subzone_73.save()

    main_subzone_74 = SubZone()
    main_subzone_74.title = 'Siri Fort'
    main_subzone_74.url_name = 'siri-fort'
    main_subzone_74.zone = main_zone_1
    main_subzone_74.save()

    main_subzone_75 = SubZone()
    main_subzone_75.title = 'Rajouri Garden'
    main_subzone_75.url_name = 'rajouri-garden'
    main_subzone_75.zone = main_zone_1
    main_subzone_75.save()

    main_subzone_76 = SubZone()
    main_subzone_76.title = 'Green Park'
    main_subzone_76.url_name = 'green-park'
    main_subzone_76.zone = main_zone_1
    main_subzone_76.save()

    main_subzone_77 = SubZone()
    main_subzone_77.title = 'Malviya Nagar'
    main_subzone_77.url_name = 'malviya-nagar'
    main_subzone_77.zone = main_zone_1
    main_subzone_77.save()

    main_subzone_78 = SubZone()
    main_subzone_78.title = 'Sector 24 Gurgaon'
    main_subzone_78.url_name = 'sector-24-gurgaon'
    main_subzone_78.zone = main_zone_1
    main_subzone_78.save()

    main_subzone_79 = SubZone()
    main_subzone_79.title = 'Ambience Mall'
    main_subzone_79.url_name = 'ambience-mall'
    main_subzone_79.zone = main_zone_1
    main_subzone_79.save()

    main_subzone_80 = SubZone()
    main_subzone_80.title = 'Panchsheel Park'
    main_subzone_80.url_name = 'panchsheel-park'
    main_subzone_80.zone = main_zone_1
    main_subzone_80.save()

    main_subzone_81 = SubZone()
    main_subzone_81.title = 'NFC'
    main_subzone_81.url_name = 'nfc'
    main_subzone_81.zone = main_zone_1
    main_subzone_81.save()

    main_subzone_82 = SubZone()
    main_subzone_82.title = 'New Friends Colony'
    main_subzone_82.url_name = 'new-friends-colony'
    main_subzone_82.zone = main_zone_1
    main_subzone_82.save()

    main_subzone_83 = SubZone()
    main_subzone_83.title = 'Defence Colony'
    main_subzone_83.url_name = 'defence-colony'
    main_subzone_83.zone = main_zone_1
    main_subzone_83.save()

    main_subzone_84 = SubZone()
    main_subzone_84.title = 'Lodhi Road'
    main_subzone_84.url_name = 'lodhi-road'
    main_subzone_84.zone = main_zone_1
    main_subzone_84.save()

    main_subzone_85 = SubZone()
    main_subzone_85.title = 'Jor Bagh'
    main_subzone_85.url_name = 'jor-bagh'
    main_subzone_85.zone = main_zone_1
    main_subzone_85.save()

    main_subzone_86 = SubZone()
    main_subzone_86.title = 'JLN Stadium'
    main_subzone_86.url_name = 'jln-stadium'
    main_subzone_86.zone = main_zone_1
    main_subzone_86.save()

    main_subzone_87 = SubZone()
    main_subzone_87.title = 'Pandav Nagar Ext.'
    main_subzone_87.url_name = 'pandav-nagar-ext'
    main_subzone_87.zone = main_zone_1
    main_subzone_87.save()

    main_subzone_88 = SubZone()
    main_subzone_88.title = 'Noida Sector 44'
    main_subzone_88.url_name = 'noida-sector-44'
    main_subzone_88.zone = main_zone_1
    main_subzone_88.save()

    main_subzone_89 = SubZone()
    main_subzone_89.title = 'Golf Course'
    main_subzone_89.url_name = 'golf-course'
    main_subzone_89.zone = main_zone_1
    main_subzone_89.save()

    main_subzone_90 = SubZone()
    main_subzone_90.title = 'Su'
    main_subzone_90.url_name = 'su'
    main_subzone_90.zone = main_zone_1
    main_subzone_90.save()

    main_subzone_91 = SubZone()
    main_subzone_91.title = 'Subhash Nagar'
    main_subzone_91.url_name = 'subhash-nagar'
    main_subzone_91.zone = main_zone_1
    main_subzone_91.save()

    # Processing model: Place

    from outingbox.models import Place

    main_place_1 = Place()
    main_place_1.address = 'aapno ghar'
    main_place_1.location = '28.386775,76.974399'
    main_place_1.save()

    main_place_2 = Place()
    main_place_2.address = 'bluo vasant kunj'
    main_place_2.location = '28.502705,77.097512'
    main_place_2.save()

    main_place_3 = Place()
    main_place_3.address = 'Kapashera Estate, Old Delhi Gurgaon Road, Opp. Kapshera Bus Stand'
    main_place_3.location = '28.525481,77.084136'
    main_place_3.save()

    main_place_4 = Place()
    main_place_4.address = 'Fun N Food Village,Kapashera Estate, Old Delhi Gurgaon Road, Opp. Kapshera Bus Stand'
    main_place_4.location = '28.525481,77.084136'
    main_place_4.save()

    main_place_5 = Place()
    main_place_5.address = 'Fun and Food Village'
    main_place_5.location = '28.524374,77.083415'
    main_place_5.save()

    main_place_6 = Place()
    main_place_6.address = 'Fun N Food Village'
    main_place_6.location = '28.523910,77.084727'
    main_place_6.save()

    main_place_7 = Place()
    main_place_7.address = 'appu ghar,Gurgaon'
    main_place_7.location = '28.462200,77.071474'
    main_place_7.save()

    main_place_8 = Place()
    main_place_8.address = 'delhirides'
    main_place_8.location = '28.545555,77.309635'
    main_place_8.save()

    main_place_9 = Place()
    main_place_9.address = 'A- 265, Andheria Modh,Near Kishan Haat,New Delhi'
    main_place_9.location = '28.613939,77.209021'
    main_place_9.save()

    main_place_10 = Place()
    main_place_10.address = 'A- 265, Andheria Modh,Near Kishan Haat,New Delhi'
    main_place_10.location = '28.613939,77.209021'
    main_place_10.save()

    main_place_11 = Place()
    main_place_11.address = 'A- 265, Andheria Modh,Near Kishan Haat,New Delhi'
    main_place_11.location = '28.613939,77.209021'
    main_place_11.save()

    main_place_12 = Place()
    main_place_12.address = 'Shop No. 239&240, 1st Floor, DLF Place Mall, Saket, New Delhi'
    main_place_12.location = '28.524579,77.206615'
    main_place_12.save()

    main_place_13 = Place()
    main_place_13.address = 'NH. 8, Behind Sector 15, Gurgaon, Haryana 122001, India'
    main_place_13.location = '28.458089,77.041191'
    main_place_13.save()

    main_place_14 = Place()
    main_place_14.address = 'E-238, Amar Colony, Lajpat Nagar 4, New Delhi'
    main_place_14.location = '28.561197,77.241680'
    main_place_14.save()

    main_place_15 = Place()
    main_place_15.address = ' 505, Ring Road Mall, Sector 3, Rohini, New Delhi'
    main_place_15.location = '28.698277,77.116007'
    main_place_15.save()

    main_place_16 = Place()
    main_place_16.address = 'just chill water park,new delhi'
    main_place_16.location = '28.850358,77.128133'
    main_place_16.save()

    main_place_17 = Place()
    main_place_17.address = 'adventure island,rohini'
    main_place_17.location = '28.723728,77.113592'
    main_place_17.save()

    main_place_18 = Place()
    main_place_18.address = 'jurassic park inn,sonepat'
    main_place_18.location = '29.008682,77.081989'
    main_place_18.save()

    main_place_19 = Place()
    main_place_19.address = 'club platinum resort,'
    main_place_19.location = '28.670857,77.085852'
    main_place_19.save()

    main_place_20 = Place()
    main_place_20.address = 'Shop No-309, Spice World, 2nd Flr, Sector 25 A, Noida'
    main_place_20.location = '28.535516,77.391026'
    main_place_20.save()

    main_place_21 = Place()
    main_place_21.address = 'Shop No-309, Spice World, 2nd Flr, Sector 25 A, Noida'
    main_place_21.location = '28.535516,77.391026'
    main_place_21.save()

    main_place_22 = Place()
    main_place_22.address = 'M.G.F Metropolitan Mall, Mehrauli'
    main_place_22.location = '28.529568,77.220172'
    main_place_22.save()

    main_place_23 = Place()
    main_place_23.address = '4, Aurobindo Marg, New Delhi'
    main_place_23.location = '28.546344,77.202296'
    main_place_23.save()

    main_place_24 = Place()
    main_place_24.address = 'Building No. 105, Plot No. 2A, Sector 38 A, Noida'
    main_place_24.location = '28.562308,77.329571'
    main_place_24.save()

    main_place_25 = Place()
    main_place_25.address = '2nd Floor, Pacific Mall, Tagore Garden, New Delhi'
    main_place_25.location = '28.643895,77.112830'
    main_place_25.save()

    main_place_26 = Place()
    main_place_26.address = 'Ug-17, Ansal Plaza, Greater Noida'
    main_place_26.location = '28.535902,77.392013'
    main_place_26.save()

    main_place_27 = Place()
    main_place_27.address = 'A-38, Mohan Cooperative Industrial Estate,, Near Pind Balluchi Restaurant, Main Mathura Road, New Delhi'
    main_place_27.location = '28.611238,77.240114'
    main_place_27.save()

    main_place_28 = Place()
    main_place_28.address = 'A-38, Mohan Co-Operative Industrial Estate, Mathura Road, Badarpur,Delhi'
    main_place_28.location = '28.469887,77.305907'
    main_place_28.save()

    main_place_29 = Place()
    main_place_29.address = 'Dynamic House, Opp Petrol Bunk, Dadri Main Road, Sector-41, Noida'
    main_place_29.location = '28.561075,77.363055'
    main_place_29.save()

    main_place_30 = Place()
    main_place_30.address = 'wonder speedways,noida'
    main_place_30.location = '28.564066,77.325414'
    main_place_30.save()

    main_place_31 = Place()
    main_place_31.address = 'Westin Resort, Sohna, Gurgaon'
    main_place_31.location = '28.248699,77.063512'
    main_place_31.save()

    main_place_32 = Place()
    main_place_32.address = 'F9 Go-Karting, Sector 17-18 Link Road, Gurgaon'
    main_place_32.location = '28.423184,77.188572'
    main_place_32.save()

    main_place_33 = Place()
    main_place_33.address = 'F9 Go Karting Gurgaon'
    main_place_33.location = '28.459497,77.026638'
    main_place_33.save()

    main_place_34 = Place()
    main_place_34.address = 'F9 Go Karting Gurgaon'
    main_place_34.location = '28.459497,77.026638'
    main_place_34.save()

    main_place_35 = Place()
    main_place_35.address = 'luxmi plaza gurgaon'
    main_place_35.location = '28.465048,77.507700'
    main_place_35.save()

    main_place_36 = Place()
    main_place_36.address = 'F9 Go Karting Gurgaon'
    main_place_36.location = '28.465067,77.507711'
    main_place_36.save()

    main_place_37 = Place()
    main_place_37.address = 'Sohna Gugaon'
    main_place_37.location = '28.237296, 77.149235'
    main_place_37.save()

    main_place_38 = Place()
    main_place_38.address = 'Pacific Mall, Subhash Nagar, 110027'
    main_place_38.location = '18.501079,73.872429'
    main_place_38.save()

    main_place_39 = Place()
    main_place_39.address = 'City Mall, Sector 12 Faridabad'
    main_place_39.location = '28.570434,77.337280'
    main_place_39.save()

    main_place_40 = Place()
    main_place_40.address = 'City Mall, Sector 12 Faridabad'
    main_place_40.location = '28.570434,77.337280'
    main_place_40.save()

    main_place_41 = Place()
    main_place_41.address = 'M-22, Greater Kailash 1, Delhi'
    main_place_41.location = '28.552320,77.235405'
    main_place_41.save()

    main_place_42 = Place()
    main_place_42.address = 'Mind Cafe'
    main_place_42.location = '28.468281,77.083210'
    main_place_42.save()

    main_place_43 = Place()
    main_place_43.address = 'Iyengar Yoga Centre, new delhi'
    main_place_43.location = '28.629935, 77.236802'
    main_place_43.save()

    main_place_44 = Place()
    main_place_44.address = 'Sivanand'
    main_place_44.location = '28.553610, 77.242764'
    main_place_44.save()

    main_place_45 = Place()
    main_place_45.address = 'the yoga studio,'
    main_place_45.location = '28.550435,77.206611'
    main_place_45.save()

    main_place_46 = Place()
    main_place_46.address = 'Kedarnath Yoga'
    main_place_46.location = '28.465526, 77.079122'
    main_place_46.save()

    main_place_47 = Place()
    main_place_47.address = 'Universal Yoga Group'
    main_place_47.location = '28.475262, 77.025490'
    main_place_47.save()

    main_place_48 = Place()
    main_place_48.address = 'Universal Yoga Group'
    main_place_48.location = '28.613939,77.209021'
    main_place_48.save()

    main_place_49 = Place()
    main_place_49.address = 'Yogakul'
    main_place_49.location = '28.548664, 77.214060'
    main_place_49.save()

    main_place_50 = Place()
    main_place_50.address = 'AtreYoga'
    main_place_50.location = '28.548121, 77.211445'
    main_place_50.save()

    main_place_51 = Place()
    main_place_51.address = 'Studio Prana'
    main_place_51.location = '28.606984, 77.294454'
    main_place_51.save()

    main_place_52 = Place()
    main_place_52.address = 'Studio Prana'
    main_place_52.location = '28.606984, 77.294454'
    main_place_52.save()

    main_place_53 = Place()
    main_place_53.address = 'Navadha Yoga Centre'
    main_place_53.location = '28.531865, 77.208166'
    main_place_53.save()

    main_place_54 = Place()
    main_place_54.address = 'iSkate'
    main_place_54.location = '28.503812,77.097349'
    main_place_54.save()

    main_place_55 = Place()
    main_place_55.address = 'Art alive gallery'
    main_place_55.location = '28.542863, 77.215889'
    main_place_55.save()

    main_place_56 = Place()
    main_place_56.address = 'Dhoomimal art gallery'
    main_place_56.location = '28.632732, 77.217847'
    main_place_56.save()

    main_place_57 = Place()
    main_place_57.address = 'Gallery Espace'
    main_place_57.location = '28.561436, 77.267981'
    main_place_57.save()

    main_place_58 = Place()
    main_place_58.address = 'Vadhera Art '
    main_place_58.location = '28.570746, 77.235820'
    main_place_58.save()

    main_place_59 = Place()
    main_place_59.address = 'Vadhera Art '
    main_place_59.location = '28.568649, 77.234525'
    main_place_59.save()

    main_place_60 = Place()
    main_place_60.address = 'Visual Art Gallery'
    main_place_60.location = '28.589890, 77.225225'
    main_place_60.save()

    main_place_61 = Place()
    main_place_61.address = 'S11/C3, Pandav Nagar Ext, New Delhi 110092'
    main_place_61.location = '28.620798,77.283030'
    main_place_61.save()

    main_place_62 = Place()
    main_place_62.address = 'Green View Resedency C-254, Sector-44 Near - Challera Market, Noida'
    main_place_62.location = '28.535516,77.391026'
    main_place_62.save()

    # Processing model: Activity

    from outingbox.models import Activity
    from outingbox.models import Address

    main_address_1 = Address()
    main_address_1.title = 'SPLASH-The Water Park'
    main_address_1.location = None
    main_address_1.pin_code = 110036
    main_address_1.zone = main_zone_1
    main_address_1.address_line1 = 'Main GT Karnal Road Near Palla Moad ,Alipur,Delhi'
    main_address_1.save()

    main_activity_1 = Activity()
    main_activity_1.address = main_address_1
    main_activity_1.title = 'SPLASH-The Water Park'
    main_activity_1.description = ''
    main_activity_1.rating = 0
    main_activity_1.votes = 0
    main_activity_1.person_of_contact = ''
    main_activity_1.contact_numbers = ['01127708503', '9250055222']
    main_activity_1.cost = 3
    main_activity_1.email = 'enquiry@splashwaterpark.co.in'
    main_activity_1.website = 'http://www.splashwaterpark.co.in'
    main_activity_1.facebook = None
    main_activity_1.twitter = None
    main_activity_1.url_name = 'splash-the-water-park'
    main_activity_1.save()

    main_activity_1.category.add(main_category_5)
    main_activity_1.category.add(main_category_30)

    main_address_1.sub_zone.add(main_subzone_10)
    main_address_1.sub_zone.add(main_subzone_14)
    main_address_1.sub_zone.add(main_subzone_15)

    main_address_2 = Address()
    main_address_2.title = 'Fun N Food Village'
    main_address_2.location = main_place_6.location
    main_address_2.pin_code = 110037
    main_address_2.zone = main_zone_1
    main_address_2.address_line1 = 'Kapashera Estate, Old Delhi Gurgaon Road, Opp. Kapshera Bus Stand'
    main_address_2.save()

    main_activity_2 = Activity()
    main_activity_2.address = main_address_2
    main_activity_2.title = 'Fun N Food Village'
    main_activity_2.description = ''
    main_activity_2.rating = 0
    main_activity_2.votes = 0
    main_activity_2.person_of_contact = 'Vijay Gupta'
    main_activity_2.contact_numbers = ['011-43260099', '09990006521', '09990006522']
    main_activity_2.cost = 4
    main_activity_2.email = 'info.delhi@funnfood.com'
    main_activity_2.website = 'http://www.funnfood.com'
    main_activity_2.facebook = 'https://www.facebook.com/FunNFoodVillage'
    main_activity_2.twitter = ''
    main_activity_2.url_name = 'fun-n-food-village'
    main_activity_2.save()

    main_activity_2.category.add(main_category_5)
    main_activity_2.category.add(main_category_30)


    main_address_2.sub_zone.add(main_subzone_4)
    main_address_2.sub_zone.add(main_subzone_7)
    main_address_2.sub_zone.add(main_subzone_8)
    main_address_2.sub_zone.add(main_subzone_9)

    main_address_3 = Address()
    main_address_3.title = 'Jurasik Park Inn'
    main_address_3.location = main_place_18.location
    main_address_3.pin_code = 131021
    main_address_3.zone = main_zone_1
    main_address_3.address_line1 = 'GT Karnal Road, National Highway 1, Sonepat, Haryana  '
    main_address_3.save()

    main_activity_3 = Activity()
    main_activity_3.address = main_address_3
    main_activity_3.title = 'Jurasik Park Inn'
    main_activity_3.description = ''
    main_activity_3.rating = 0
    main_activity_3.votes = 0
    main_activity_3.person_of_contact = ''
    main_activity_3.contact_numbers = ['08882388843', '01147082702', '01147082703 ']
    main_activity_3.cost = 3
    main_activity_3.email = 'info@jurasikparkinn.com'
    main_activity_3.website = 'http://www.jurasikparkinn.com'
    main_activity_3.facebook = 'https://www.facebook.com/JurasikParkInn.Official'
    main_activity_3.twitter = ''
    main_activity_3.url_name = 'jurasik-park-inn'
    main_activity_3.save()

    main_activity_3.category.add(main_category_5)
    main_activity_3.category.add(main_category_27)
    main_activity_3.category.add(main_category_30)

    main_address_3.sub_zone.add(main_subzone_10)
    main_address_3.sub_zone.add(main_subzone_26)
    main_address_3.sub_zone.add(main_subzone_27)
    main_address_3.sub_zone.add(main_subzone_28)
    main_address_3.sub_zone.add(main_subzone_29)

    main_address_4 = Address()
    main_address_4.title = 'Amoeba'
    main_address_4.location = main_place_21.location
    main_address_4.pin_code = 201301
    main_address_4.zone = main_zone_1
    main_address_4.address_line1 = 'Shop No-309, Spice World, 2nd Flr, Sector 25 A, Noida'
    main_address_4.save()

    main_activity_4 = Activity()
    main_activity_4.address = main_address_4
    main_activity_4.title = 'Amoeba'
    main_activity_4.description = ''
    main_activity_4.rating = 0
    main_activity_4.votes = 0
    main_activity_4.person_of_contact = ''
    main_activity_4.contact_numbers = ['01203128733', '01204366400']
    main_activity_4.cost = 3
    main_activity_4.email = ''
    main_activity_4.website = 'http://www.hmleisure.com/centre/details/amoeba-noida-spice-world'
    main_activity_4.facebook = ''
    main_activity_4.twitter = ''
    main_activity_4.url_name = 'amoeba'
    main_activity_4.save()

    main_activity_4.category.add(main_category_2)
    main_activity_4.category.add(main_category_3)
    main_activity_4.category.add(main_category_29)

    main_address_4.sub_zone.add(main_subzone_22)
    main_address_4.sub_zone.add(main_subzone_39)

    main_address_5 = Address()
    main_address_5.title = 'Just Chill Water Park'
    main_address_5.location = main_place_16.location
    main_address_5.pin_code = 110040
    main_address_5.zone = main_zone_1
    main_address_5.address_line1 = 'Main GT Karnal Road near GTB, Memorial Delhi - 110040 (India)'
    main_address_5.save()

    main_activity_5 = Activity()
    main_activity_5.address = main_address_5
    main_activity_5.title = 'Just Chill Water Park'
    main_activity_5.description = ''
    main_activity_5.rating = 0
    main_activity_5.votes = 0
    main_activity_5.person_of_contact = 'Mr. Amit'
    main_activity_5.contact_numbers = ['09910499774 ']
    main_activity_5.cost = 2
    main_activity_5.email = 'justchillwp@gmail.com'
    main_activity_5.website = 'http://www.justchillwaterpark.com'
    main_activity_5.facebook = 'https://www.facebook.com/justchillwaterpark?rf=154117894729340'
    main_activity_5.twitter = ''
    main_activity_5.url_name = 'just-chill-water-park'
    main_activity_5.save()

    main_activity_5.category.add(main_category_5)
    main_activity_5.category.add(main_category_30)

    main_address_5.sub_zone.add(main_subzone_10)
    main_address_5.sub_zone.add(main_subzone_11)
    main_address_5.sub_zone.add(main_subzone_12)
    main_address_5.sub_zone.add(main_subzone_13)

    main_address_6 = Address()
    main_address_6.title = 'Worlds of Wonder'
    main_address_6.location = None
    main_address_6.pin_code = 201301
    main_address_6.zone = main_zone_1
    main_address_6.address_line1 = 'Sector 38, Noida, Uttar Pradesh '
    main_address_6.save()

    main_activity_6 = Activity()
    main_activity_6.address = main_address_6
    main_activity_6.title = 'Worlds of Wonder'
    main_activity_6.description = ''
    main_activity_6.rating = 0
    main_activity_6.votes = 0
    main_activity_6.person_of_contact = ''
    main_activity_6.contact_numbers = ['0120-4015011', '1800-103-1415']
    main_activity_6.cost = 4
    main_activity_6.email = 'info@worldsofwonder.in'
    main_activity_6.website = 'http://www.worldsofwonder.in'
    main_activity_6.facebook = 'https://www.facebook.com/worldsofwonder'
    main_activity_6.twitter = ''
    main_activity_6.url_name = 'worlds-of-wonder'
    main_activity_6.save()

    main_activity_6.category.add(main_category_5)
    main_activity_6.category.add(main_category_30)


    main_address_6.sub_zone.add(main_subzone_21)
    main_address_6.sub_zone.add(main_subzone_22)

    main_address_7 = Address()
    main_address_7.title = 'BluO'
    main_address_7.location = main_place_2.location
    main_address_7.pin_code = 0
    main_address_7.zone = main_zone_1
    main_address_7.address_line1 = 'Level 1, Ambience Mall, Nelson Mandela Marg, Vasant Kunj'
    main_address_7.save()

    main_activity_7 = Activity()
    main_activity_7.address = main_address_7
    main_activity_7.title = 'BluO'
    main_activity_7.description = ''
    main_activity_7.rating = 0
    main_activity_7.votes = 0
    main_activity_7.person_of_contact = ''
    main_activity_7.contact_numbers = ['9810270160']
    main_activity_7.cost = 0
    main_activity_7.email = 'bluo.ambi@pvrbluo.com'
    main_activity_7.website = 'http://www.pvrbluo.com/'
    main_activity_7.facebook = None
    main_activity_7.twitter = None
    main_activity_7.url_name = 'bluo'
    main_activity_7.save()

    main_activity_7.category.add(main_category_2)
    main_activity_7.category.add(main_category_3)
    main_address_7.sub_zone.add(main_subzone_5)

    main_address_8 = Address()
    main_address_8.title = 'Wonder Speedway'
    main_address_8.location = main_place_30.location
    main_address_8.pin_code = 201301
    main_address_8.zone = main_zone_1
    main_address_8.address_line1 = 'Worlds of Wonder, A-2, Sector-38, Noida, Uttar Pradesh '
    main_address_8.save()

    main_activity_8 = Activity()
    main_activity_8.address = main_address_8
    main_activity_8.title = 'Wonder Speedway'
    main_activity_8.description = ''
    main_activity_8.rating = 0
    main_activity_8.votes = 0
    main_activity_8.person_of_contact = ''
    main_activity_8.contact_numbers = ['9968146687', '0120-4650451']
    main_activity_8.cost = 4
    main_activity_8.email = 'meher@wonderspeedway.com'
    main_activity_8.website = 'http://wonderspeedway.com/'
    main_activity_8.facebook = 'https://www.facebook.com/pages/Wonder-Speedway/1411637735732912'
    main_activity_8.twitter = ''
    main_activity_8.url_name = 'wonder-speedway'
    main_activity_8.save()

    main_activity_8.category.add(main_category_27)


    main_address_8.sub_zone.add(main_subzone_6)
    main_address_8.sub_zone.add(main_subzone_21)
    main_address_8.sub_zone.add(main_subzone_44)
    main_address_8.sub_zone.add(main_subzone_45)
    main_address_8.sub_zone.add(main_subzone_46)

    main_address_9 = Address()
    main_address_9.title = 'DelhiRides'
    main_address_9.location = main_place_8.location
    main_address_9.pin_code = 110025
    main_address_9.zone = main_zone_1
    main_address_9.address_line1 = 'Kalindi Kunj Road, Kalindi Kunj Park, Okhla, New Delhi'
    main_address_9.save()

    main_activity_9 = Activity()
    main_activity_9.address = main_address_9
    main_activity_9.title = 'DelhiRides'
    main_activity_9.description = 'Delhi Rides is situated in Delhi. Offering double dose of thrill and delights. Delhi Rides has everything to take you to the next level of entertainment.'
    main_activity_9.rating = 0
    main_activity_9.votes = 0
    main_activity_9.person_of_contact = ''
    main_activity_9.contact_numbers = ['011-64659291', '09873715909', '09540231938']
    main_activity_9.cost = 2
    main_activity_9.email = 'delhirides@gmail.com'
    main_activity_9.website = 'http://www.delhirides.in'
    main_activity_9.facebook = 'https://www.facebook.com/delhirides.in?fref=ts'
    main_activity_9.twitter = ''
    main_activity_9.url_name = 'delhirides'
    main_activity_9.save()

    main_activity_9.category.add(main_category_5)
    main_activity_9.category.add(main_category_30)

    main_address_9.sub_zone.add(main_subzone_18)
    main_address_9.sub_zone.add(main_subzone_19)
    main_address_9.sub_zone.add(main_subzone_20)

    main_address_10 = Address()
    main_address_10.title = 'Aapno Ghar Amusement & Water Park'
    main_address_10.location = main_place_1.location
    main_address_10.pin_code = 122001
    main_address_10.zone = main_zone_1
    main_address_10.address_line1 = '43rd Milestone, Main Delhi Jaipur Expressway, Nh-8, Sector-77,Gurgaon'
    main_address_10.save()

    main_activity_10 = Activity()
    main_activity_10.address = main_address_10
    main_activity_10.title = 'Aapno Ghar Amusement & Water Park'
    main_activity_10.description = ''
    main_activity_10.rating = 0
    main_activity_10.votes = 0
    main_activity_10.person_of_contact = 'Mr. Ravi'
    main_activity_10.contact_numbers = ['01242371281', '9717283535', '9650687778']
    main_activity_10.cost = 3
    main_activity_10.email = 'info@aapnoghar.com'
    main_activity_10.website = 'http://www.aapnoghar.com'
    main_activity_10.facebook = None
    main_activity_10.twitter = None
    main_activity_10.url_name = 'aapno-ghar-amusement-water-park'
    main_activity_10.save()

    main_activity_10.category.add(main_category_5)
    main_activity_10.category.add(main_category_30)


    main_address_10.sub_zone.add(main_subzone_26)
    main_address_10.sub_zone.add(main_subzone_36)
    main_address_10.sub_zone.add(main_subzone_37)
    main_address_10.sub_zone.add(main_subzone_38)

    main_address_11 = Address()
    main_address_11.title = 'Drizzling Land'
    main_address_11.location = None
    main_address_11.pin_code = 201206
    main_address_11.zone = main_zone_1
    main_address_11.address_line1 = '8th Mile Stone, Delhi-Meerut Highway(NH-58), Duhai,Ghaziabad'
    main_address_11.save()

    main_activity_11 = Activity()
    main_activity_11.address = main_address_11
    main_activity_11.title = 'Drizzling Land'
    main_activity_11.description = ''
    main_activity_11.rating = 0
    main_activity_11.votes = 0
    main_activity_11.person_of_contact = 'Mr. Manish Sharma'
    main_activity_11.contact_numbers = ['0120-2675513', '0120-2675514', '09650597345', '09650597341 ']
    main_activity_11.cost = 3
    main_activity_11.email = 'manish.trufill@gmail.com'
    main_activity_11.website = 'http://www.drizzlingland.com/'
    main_activity_11.facebook = ''
    main_activity_11.twitter = ''
    main_activity_11.url_name = 'drizzling-land'
    main_activity_11.save()

    main_activity_11.category.add(main_category_5)
    main_activity_11.category.add(main_category_30)

    main_address_11.sub_zone.add(main_subzone_30)
    main_address_11.sub_zone.add(main_subzone_31)
    main_address_11.sub_zone.add(main_subzone_32)

    main_address_12 = Address()
    main_address_12.title = 'Adventure Island'
    main_address_12.location = main_place_17.location
    main_address_12.pin_code = 110085
    main_address_12.zone = main_zone_1
    main_address_12.address_line1 = 'Unitech Amusement Parks Ltd. Opposite Rithala Metro Station,Sector-10, Rohini, New Delhi'
    main_address_12.save()

    main_activity_12 = Activity()
    main_activity_12.address = main_address_12
    main_activity_12.title = 'Adventure Island'
    main_activity_12.description = "Spread over 62 acres of sprawling land…..Adventure Island is India's 1st world-class amusement park. Adventure Island has features that attract people from far and wide....amazing rides, a picturesque lake , rain dance , magic show and lot more!"
    main_activity_12.rating = 0
    main_activity_12.votes = 0
    main_activity_12.person_of_contact = ''
    main_activity_12.contact_numbers = ['01147041111']
    main_activity_12.cost = 3
    main_activity_12.email = 'frontoffice@uaplindia.com'
    main_activity_12.website = ''
    main_activity_12.facebook = 'https://www.facebook.com/funatadventureisland/info?tab=overview'
    main_activity_12.twitter = ''
    main_activity_12.url_name = 'adventure-island'
    main_activity_12.save()

    main_activity_12.category.add(main_category_30)

    main_address_12.sub_zone.add(main_subzone_23)
    main_address_12.sub_zone.add(main_subzone_24)
    main_address_12.sub_zone.add(main_subzone_25)

    main_address_13 = Address()
    main_address_13.title = 'OYSTERS Beach Park-Appu Ghar'
    main_address_13.location = main_place_7.location
    main_address_13.pin_code = 122001
    main_address_13.zone = main_zone_1
    main_address_13.address_line1 = 'Sector 29, Adjacent to Huda City Metro Station, Gurgaon'
    main_address_13.save()

    main_activity_13 = Activity()
    main_activity_13.address = main_address_13
    main_activity_13.title = 'OYSTERS Beach Park-Appu Ghar'
    main_activity_13.description = ''
    main_activity_13.rating = 0
    main_activity_13.votes = 0
    main_activity_13.person_of_contact = ''
    main_activity_13.contact_numbers = ['01244891000 ']
    main_activity_13.cost = 3
    main_activity_13.email = 'branding@appughar.com'
    main_activity_13.website = 'http://www.oystersbeach.com'
    main_activity_13.facebook = 'https://www.facebook.com/oystersappughar'
    main_activity_13.twitter = ''
    main_activity_13.url_name = 'oysters-beach-park-appu-ghar'
    main_activity_13.save()

    main_activity_13.category.add(main_category_5)

    main_address_13.sub_zone.add(main_subzone_4)
    main_address_13.sub_zone.add(main_subzone_16)
    main_address_13.sub_zone.add(main_subzone_17)

    main_address_14 = Address()
    main_address_14.title = 'Shootout Zone'
    main_address_14.location = main_place_11.location
    main_address_14.pin_code = 110074
    main_address_14.zone = main_zone_1
    main_address_14.address_line1 = 'A- 265, Andheria Modh,Near Kishan Haat,New Delhi'
    main_address_14.save()

    main_activity_14 = Activity()
    main_activity_14.address = main_address_14
    main_activity_14.title = 'Shootout Zone'
    main_activity_14.description = ''
    main_activity_14.rating = 0
    main_activity_14.votes = 0
    main_activity_14.person_of_contact = 'Sanjeet Dagar'
    main_activity_14.contact_numbers = ['09810012506', '09811007094']
    main_activity_14.cost = 3
    main_activity_14.email = 'dagarsanjeet6@gmail.com'
    main_activity_14.website = 'http://www.shootoutzone.com'
    main_activity_14.facebook = ''
    main_activity_14.twitter = ''
    main_activity_14.url_name = 'shootout-zone'
    main_activity_14.save()

    main_activity_14.category.add(main_category_28)

    main_address_14.sub_zone.add(main_subzone_5)
    main_address_14.sub_zone.add(main_subzone_17)
    main_address_14.sub_zone.add(main_subzone_43)

    main_address_15 = Address()
    main_address_15.title = 'City Bowl'
    main_address_15.location = None
    main_address_15.pin_code = 121003
    main_address_15.zone = main_zone_1
    main_address_15.address_line1 = '14/5, Mahindra Sterling Compound, Mathura Road, Faridabad'
    main_address_15.save()

    main_activity_15 = Activity()
    main_activity_15.address = main_address_15
    main_activity_15.title = 'City Bowl'
    main_activity_15.description = ''
    main_activity_15.rating = 0
    main_activity_15.votes = 0
    main_activity_15.person_of_contact = 'Raanti Dev Gupta'
    main_activity_15.contact_numbers = ['01294315317', '09810002980']
    main_activity_15.cost = 3
    main_activity_15.email = 'raanti@citybowlindia.com'
    main_activity_15.website = 'http://www.citybowlindia.com'
    main_activity_15.facebook = ''
    main_activity_15.twitter = ''
    main_activity_15.url_name = 'city-bowl'
    main_activity_15.save()

    main_activity_15.category.add(main_category_2)
    main_activity_15.category.add(main_category_3)

    main_address_15.sub_zone.add(main_subzone_40)

    main_address_16 = Address()
    main_address_16.title = '32nd Milestone'
    main_address_16.location = main_place_13.location
    main_address_16.pin_code = 122001
    main_address_16.zone = main_zone_1
    main_address_16.address_line1 = 'NH. 8, Behind Sector 15, Gurgaon, Haryana 122001, India'
    main_address_16.save()

    main_activity_16 = Activity()
    main_activity_16.address = main_address_16
    main_activity_16.title = '32nd Milestone'
    main_activity_16.description = ''
    main_activity_16.rating = 0
    main_activity_16.votes = 0
    main_activity_16.person_of_contact = 'Mr. Ayush Tiwari'
    main_activity_16.contact_numbers = ['07838294041', '01244870400']
    main_activity_16.cost = 3
    main_activity_16.email = 'ayush.tiwari@32ndmilestone.com'
    main_activity_16.website = 'http://www.32ndmilestone.com/'
    main_activity_16.facebook = ''
    main_activity_16.twitter = ''
    main_activity_16.url_name = '32nd-milestone'
    main_activity_16.save()

    main_activity_16.category.add(main_category_2)
    main_activity_16.category.add(main_category_27)



    main_address_16.sub_zone.add(main_subzone_4)
    main_address_16.sub_zone.add(main_subzone_37)
    main_address_16.sub_zone.add(main_subzone_49)

    main_address_17 = Address()
    main_address_17.title = 'Amoeba'
    main_address_17.location = main_place_22.location
    main_address_17.pin_code = 122001
    main_address_17.zone = main_zone_1
    main_address_17.address_line1 = 'M.G.F Metropolitan Mall, 2nd floor, Mehrauli Gurgaon Road'
    main_address_17.save()

    main_activity_17 = Activity()
    main_activity_17.address = main_address_17
    main_activity_17.title = 'Amoeba'
    main_activity_17.description = 'Amoeba is a complete family entertainer, providing bowling, a playground, and an arcade'
    main_activity_17.rating = 0
    main_activity_17.votes = 0
    main_activity_17.person_of_contact = 'Surender'
    main_activity_17.contact_numbers = ['08742983884', '01244265892']
    main_activity_17.cost = 3
    main_activity_17.email = 'joy.amoeba@gmail.com'
    main_activity_17.website = 'http://www.hmleisure.com/'
    main_activity_17.facebook = ''
    main_activity_17.twitter = ''
    main_activity_17.url_name = 'amoeba'
    main_activity_17.save()

    main_activity_17.category.add(main_category_2)
    main_activity_17.category.add(main_category_29)


    main_address_17.sub_zone.add(main_subzone_4)
    main_address_17.sub_zone.add(main_subzone_5)

    main_address_18 = Address()
    main_address_18.title = 'Essex Farms Future Bowl'
    main_address_18.location = main_place_23.location
    main_address_18.pin_code = 110016
    main_address_18.zone = main_zone_1
    main_address_18.address_line1 = '4, Aurobindo Marg, New Delhi'
    main_address_18.save()

    main_activity_18 = Activity()
    main_activity_18.address = main_address_18
    main_activity_18.title = 'Essex Farms Future Bowl'
    main_activity_18.description = ''
    main_activity_18.rating = 0
    main_activity_18.votes = 0
    main_activity_18.person_of_contact = ''
    main_activity_18.contact_numbers = ['9899003311, 01126528080']
    main_activity_18.cost = 3
    main_activity_18.email = 'futurebowl@essexfarms.com'
    main_activity_18.website = 'http://www.essexfarms.com/bowl.html'
    main_activity_18.facebook = ''
    main_activity_18.twitter = ''
    main_activity_18.url_name = 'essex-farms-future-bowl'
    main_activity_18.save()

    main_activity_18.category.add(main_category_2)
    main_activity_18.category.add(main_category_3)
    main_activity_18.category.add(main_category_29)

    main_address_18.sub_zone.add(main_subzone_5)
    main_address_18.sub_zone.add(main_subzone_53)

    main_address_19 = Address()
    main_address_19.title = 'Every Other Day (Appu Ghar Express)'
    main_address_19.location = main_place_24.location
    main_address_19.pin_code = 201301
    main_address_19.zone = main_zone_1
    main_address_19.address_line1 = 'Building No. 105, Plot No. 2A, Sector 38 A, Noida'
    main_address_19.save()

    main_activity_19 = Activity()
    main_activity_19.address = main_address_19
    main_activity_19.title = 'Every Other Day (Appu Ghar Express)'
    main_activity_19.description = ''
    main_activity_19.rating = 0
    main_activity_19.votes = 0
    main_activity_19.person_of_contact = 'Mr. Ashish Bhardwaj'
    main_activity_19.contact_numbers = ['01204247560', '08527991150']
    main_activity_19.cost = 3
    main_activity_19.email = 'ashish@appughar.com'
    main_activity_19.website = 'http://www.appugharexpress.com/bowling_bonanza.html'
    main_activity_19.facebook = ''
    main_activity_19.twitter = ''
    main_activity_19.url_name = 'every-other-day-appu-ghar-express'
    main_activity_19.save()

    main_activity_19.category.add(main_category_2)
    main_activity_19.category.add(main_category_3)

    main_address_19.sub_zone.add(main_subzone_6)
    main_address_19.sub_zone.add(main_subzone_21)

    main_address_20 = Address()
    main_address_20.title = 'Versus Gaming Zone'
    main_address_20.location = main_place_25.location
    main_address_20.pin_code = 110027
    main_address_20.zone = main_zone_1
    main_address_20.address_line1 = '2nd Floor, Pacific Mall, Tagore Garden, New Delhi'
    main_address_20.save()

    main_activity_20 = Activity()
    main_activity_20.address = main_address_20
    main_activity_20.title = 'Versus Gaming Zone'
    main_activity_20.description = 'The finest 8-lane bowling alley with hi-end graphic games, third person shooting games, imported heavy duty pool tables, dynamic air hockey and much more. The bowling alley offers the best engineered & highest performing bowling alley in India from the latest model of Brunswick worldwide GS® Series for the fanatic gaming junkies. An ideal hangout area, it comprises of no less than 40 arcade games, air hockey, pool table & a golf simulator, not to mention a bowling alley with 8-state of the art bowling lanes & to further up-size your excitement, you can even create your own private VIP bowling zone for special occasions.'
    main_activity_20.rating = 0
    main_activity_20.votes = 0
    main_activity_20.person_of_contact = 'Devender Shah'
    main_activity_20.contact_numbers = ['01145719207', '09650078976']
    main_activity_20.cost = 3
    main_activity_20.email = 'versusdelhi@cinemax.co.in'
    main_activity_20.website = 'http://www.facebook.com/versusgamingzone'
    main_activity_20.facebook = ''
    main_activity_20.twitter = ''
    main_activity_20.url_name = 'versus-gaming-zone'
    main_activity_20.save()

    main_activity_20.category.add(main_category_2)
    main_activity_20.category.add(main_category_3)
    main_activity_20.category.add(main_category_29)

    main_address_20.sub_zone.add(main_subzone_42)

    main_address_21 = Address()
    main_address_21.title = 'F9 Go Karting'
    main_address_21.location = main_place_36.location
    main_address_21.pin_code = 122001
    main_address_21.zone = main_zone_1
    main_address_21.address_line1 = 'Sector 17-18 Link Road, 1.8 Kms. from IFFCO Chowk,Gurgaon'
    main_address_21.save()

    main_activity_21 = Activity()
    main_activity_21.address = main_address_21
    main_activity_21.title = 'F9 Go Karting'
    main_activity_21.description = ''
    main_activity_21.rating = 0
    main_activity_21.votes = 0
    main_activity_21.person_of_contact = 'S.K. Tyagi '
    main_activity_21.contact_numbers = ['09818048655', '08826738655']
    main_activity_21.cost = 3
    main_activity_21.email = 'f9gokarting@gmail.com'
    main_activity_21.website = 'http://www.f9gokarting.com/'
    main_activity_21.facebook = 'https://www.facebook.com/pages/F9-Go-Karting/644569965648721?fref=ts'
    main_activity_21.twitter = ''
    main_activity_21.url_name = 'f9-go-karting'
    main_activity_21.save()

    main_activity_21.category.add(main_category_27)

    main_address_21.sub_zone.add(main_subzone_4)
    main_address_21.sub_zone.add(main_subzone_47)
    main_address_21.sub_zone.add(main_subzone_48)

    main_address_22 = Address()
    main_address_22.title = 'Sivananda Yoga '
    main_address_22.location = main_place_44.location
    main_address_22.pin_code = 110048
    main_address_22.zone = main_zone_1
    main_address_22.address_line1 = 'Sivananda Yoga, Vedanta Nataraja Centre,  A - 41, Kailash Colony,  New Delhi '
    main_address_22.save()

    main_activity_22 = Activity()
    main_activity_22.address = main_address_22
    main_activity_22.title = 'Sivananda Yoga '
    main_activity_22.description = ''
    main_activity_22.rating = 0
    main_activity_22.votes = 0
    main_activity_22.person_of_contact = ''
    main_activity_22.contact_numbers = ['011–32069070', '011-29230962', '08860954455']
    main_activity_22.cost = 4
    main_activity_22.email = 'delhi@sivananda.org'
    main_activity_22.website = 'http://www.sivananda.org.in/delhi/'
    main_activity_22.facebook = 'http://www.facebook.com/sivanandayoga.9.newdelhi'
    main_activity_22.twitter = ''
    main_activity_22.url_name = 'sivananda-yoga'
    main_activity_22.save()

    main_activity_22.category.add(main_category_9)

    main_address_22.sub_zone.add(main_subzone_65)
    main_address_22.sub_zone.add(main_subzone_66)

    main_address_23 = Address()
    main_address_23.title = 'Bikram Yoga '
    main_address_23.location = None
    main_address_23.pin_code = 110027
    main_address_23.zone = main_zone_1
    main_address_23.address_line1 = 'A 24 ,Vishal enclave, Rajouri Garden,New Delhi'
    main_address_23.save()

    main_activity_23 = Activity()
    main_activity_23.address = main_address_23
    main_activity_23.title = 'Bikram Yoga '
    main_activity_23.description = ''
    main_activity_23.rating = 0
    main_activity_23.votes = 0
    main_activity_23.person_of_contact = ''
    main_activity_23.contact_numbers = ['09650020333']
    main_activity_23.cost = 3
    main_activity_23.email = ''
    main_activity_23.website = 'http://www.bikramyoga.com'
    main_activity_23.facebook = 'https://www.facebook.com/bikramyogadelhi?ref=br_rs'
    main_activity_23.twitter = ''
    main_activity_23.url_name = 'bikram-yoga'
    main_activity_23.save()

    main_activity_23.category.add(main_category_9)

    main_address_23.sub_zone.add(main_subzone_8)
    main_address_23.sub_zone.add(main_subzone_75)

    main_address_24 = Address()
    main_address_24.title = 'AtréYoga Studio'
    main_address_24.location = main_place_50.location
    main_address_24.pin_code = 110049
    main_address_24.zone = main_zone_1
    main_address_24.address_line1 = '252-A, Second floor, Nanak Bhavan, Shahpur Jat, New Delhi '
    main_address_24.save()

    main_activity_24 = Activity()
    main_activity_24.address = main_address_24
    main_activity_24.title = 'AtréYoga Studio'
    main_activity_24.description = ''
    main_activity_24.rating = 0
    main_activity_24.votes = 0
    main_activity_24.person_of_contact = ''
    main_activity_24.contact_numbers = ['09958937036']
    main_activity_24.cost = 4
    main_activity_24.email = 'info@atreyogastudio.com'
    main_activity_24.website = 'http://www.atreyogastudio.com'
    main_activity_24.facebook = 'https://www.facebook.com/atreyogastudio?ref=br_rs'
    main_activity_24.twitter = ''
    main_activity_24.url_name = 'atreyoga-studio'
    main_activity_24.save()

    main_activity_24.category.add(main_category_9)

    main_address_24.sub_zone.add(main_subzone_5)
    main_address_24.sub_zone.add(main_subzone_53)

    main_address_25 = Address()
    main_address_25.title = 'F.o.G - Federation of Gamers'
    main_address_25.location = main_place_12.location
    main_address_25.pin_code = 110017
    main_address_25.zone = main_zone_1
    main_address_25.address_line1 = 'Shop No. 239&240, 1st Floor, DLF Place Mall, Saket, New Delhi'
    main_address_25.save()

    main_activity_25 = Activity()
    main_activity_25.address = main_address_25
    main_activity_25.title = 'F.o.G - Federation of Gamers'
    main_activity_25.description = "F.o.G (Federation of Gamers) is a gaming lounge where casual gamers can come to play the latest games on the newest consoles hooked upto big HD TV's. Along with gaming we have a\r\n\r\nsmall café where we serve French Fries, Chicken Nuggets, Pasta, Sandwiches etc. \r\n\r\nF.o.G has been the destination of choice for many birthday parties, for which we have tailor-made food and gaming packages. \r\n\r\nAs a gaming destination our aim has been to promote gaming amongst the youth and thus host gaming tournaments every month at F.o.G. Participants can compete with other avid gamers to stand a chance to take home a sizable prize. \r\n\r\nStandard Pricing: Rs.60/per 10mins/ per person \r\n\r\nFood and Gaming Combos (starting at): Rs. 440/per person \r\n\r\nBirthday Packages (gaming + food): Rs.700/per person"
    main_activity_25.rating = 0
    main_activity_25.votes = 0
    main_activity_25.person_of_contact = 'Ganesh Tripathi'
    main_activity_25.contact_numbers = ['0114632360']
    main_activity_25.cost = 3
    main_activity_25.email = 'info@thefog.in'
    main_activity_25.website = 'http://thefog.in/'
    main_activity_25.facebook = 'https://www.facebook.com/fedgamers?ref=settings'
    main_activity_25.twitter = ''
    main_activity_25.url_name = 'fog-federation-of-gamers'
    main_activity_25.save()

    main_activity_25.category.add(main_category_29)

    main_address_25.sub_zone.add(main_subzone_5)
    main_address_25.sub_zone.add(main_subzone_41)

    main_address_26 = Address()
    main_address_26.title = 'Delhi Dance Academy'
    main_address_26.location = main_place_14.location
    main_address_26.pin_code = 0
    main_address_26.zone = main_zone_1
    main_address_26.address_line1 = 'E-238, Amar Colony, Lajpat Nagar 4, New Delhi'
    main_address_26.save()

    main_activity_26 = Activity()
    main_activity_26.address = main_address_26
    main_activity_26.title = 'Delhi Dance Academy'
    main_activity_26.description = 'Delhi Dance Academy is one of the better known names for high quality dance education, has been featured on almost every lifestyle TV channel and newspaper as the best in its field and has been awarded “The Best Dance Academy in Delhi” in Jan 2014 at the Brands Academy Business and Service Excellence Awards. \r\nIt stands as Delhi’s most visible dance institute on the Internet with 84,588 visits in all of 2013, of which 46,981 were from Delhi and also one with the highest social appeal/interaction and with excellent user reviews on Facebook and on Trip Advisor. \r\n\r\nThe emphasis at Delhi Dance Academy has always been on providing education that matters, on managing the centers professionally – starting and ending classes on time, providing a comfortable environment to students, choosing well trained, professional instructors and so on. \r\nThough there are hiccups in running multiple centers to 100% perfection, DDA has done very well in standardizing the process, using technology for managing the institutes.'
    main_activity_26.rating = 0
    main_activity_26.votes = 0
    main_activity_26.person_of_contact = 'Anant'
    main_activity_26.contact_numbers = ['01141012909', '09953835088']
    main_activity_26.cost = 3
    main_activity_26.email = ''
    main_activity_26.website = 'http://www.delhidanceacademy.in'
    main_activity_26.facebook = 'http://www.Facebook.com/DelhiDanceAcademy'
    main_activity_26.twitter = 'https://twitter.com/dancedelhi'
    main_activity_26.url_name = 'delhi-dance-academy'
    main_activity_26.save()

    main_activity_26.category.add(main_category_26)
    main_activity_26.category.add(main_category_25)
    main_activity_26.category.add(main_category_24)
    main_activity_26.category.add(main_category_23)
    main_activity_26.category.add(main_category_22)
    main_activity_26.category.add(main_category_21)
    main_activity_26.category.add(main_category_20)
    main_activity_26.category.add(main_category_19)
    main_activity_26.category.add(main_category_18)
    main_activity_26.category.add(main_category_17)
    main_activity_26.category.add(main_category_16)
    main_activity_26.category.add(main_category_15)
    main_activity_26.category.add(main_category_14)
    main_activity_26.category.add(main_category_13)

    main_address_26.sub_zone.add(main_subzone_5)
    main_address_26.sub_zone.add(main_subzone_52)

    main_address_27 = Address()
    main_address_27.title = 'Big Dance Center'
    main_address_27.location = main_place_15.location
    main_address_27.pin_code = 110085
    main_address_27.zone = main_zone_1
    main_address_27.address_line1 = ' 505, Ring Road Mall, Sector 3, Rohini, New Delhi'
    main_address_27.save()

    main_activity_27 = Activity()
    main_activity_27.address = main_address_27
    main_activity_27.title = 'Big Dance Center'
    main_activity_27.description = ''
    main_activity_27.rating = 0
    main_activity_27.votes = 0
    main_activity_27.person_of_contact = ''
    main_activity_27.contact_numbers = ['01147090148', '01147090149', '01147090150']
    main_activity_27.cost = 3
    main_activity_27.email = 'info@bigdancecentre.com'
    main_activity_27.website = 'http://www.bigdancecentre.com'
    main_activity_27.facebook = 'http://www.facebook.com/bigdancecentreindia'
    main_activity_27.twitter = 'https://twitter.com/bigdancecentre'
    main_activity_27.url_name = 'big-dance-center'
    main_activity_27.save()

    main_activity_27.category.add(main_category_14)
    main_activity_27.category.add(main_category_15)
    main_activity_27.category.add(main_category_16)
    main_activity_27.category.add(main_category_18)
    main_activity_27.category.add(main_category_24)
    main_activity_27.category.add(main_category_25)

    main_address_27.sub_zone.add(main_subzone_13)
    main_address_27.sub_zone.add(main_subzone_15)
    main_address_27.sub_zone.add(main_subzone_24)

    main_address_28 = Address()
    main_address_28.title = 'Skittle Bowling Arena'
    main_address_28.location = main_place_26.location
    main_address_28.pin_code = 201308
    main_address_28.zone = main_zone_1
    main_address_28.address_line1 = 'Ug-17, Ansal Plaza, Greater Noida'
    main_address_28.save()

    main_activity_28 = Activity()
    main_activity_28.address = main_address_28
    main_activity_28.title = 'Skittle Bowling Arena'
    main_activity_28.description = ''
    main_activity_28.rating = 0
    main_activity_28.votes = 0
    main_activity_28.person_of_contact = ''
    main_activity_28.contact_numbers = ['09711615321', '01204291729']
    main_activity_28.cost = 3
    main_activity_28.email = 'play@skittlebowling.com'
    main_activity_28.website = 'http://www.skittlebowling.com'
    main_activity_28.facebook = ''
    main_activity_28.twitter = ''
    main_activity_28.url_name = 'skittle-bowling-arena'
    main_activity_28.save()

    main_activity_28.category.add(main_category_2)
    main_activity_28.category.add(main_category_3)
    main_activity_28.category.add(main_category_29)

    main_address_28.sub_zone.add(main_subzone_6)

    main_address_29 = Address()
    main_address_29.title = 'Fun N Fair'
    main_address_29.location = main_place_27.location
    main_address_29.pin_code = 110044
    main_address_29.zone = main_zone_1
    main_address_29.address_line1 = 'A-38, Mohan Cooperative Industrial Estate,, Near Pind Balluchi Restaurant, Main Mathura Road,, New Delhi, Delhi '
    main_address_29.save()

    main_activity_29 = Activity()
    main_activity_29.address = main_address_29
    main_activity_29.title = 'Fun N Fair'
    main_activity_29.description = ''
    main_activity_29.rating = 0
    main_activity_29.votes = 0
    main_activity_29.person_of_contact = ''
    main_activity_29.contact_numbers = ['01126959563', '01126959591', '09555673242']
    main_activity_29.cost = 3
    main_activity_29.email = 'funnfair11@gmail.com'
    main_activity_29.website = 'http://www.fun-fair.qapacity.com/'
    main_activity_29.facebook = 'https://www.facebook.com/funnfair'
    main_activity_29.twitter = ''
    main_activity_29.url_name = 'fun-n-fair'
    main_activity_29.save()

    main_activity_29.category.add(main_category_2)
    main_activity_29.category.add(main_category_3)
    main_activity_29.category.add(main_category_29)


    main_address_29.sub_zone.add(main_subzone_54)
    main_address_29.sub_zone.add(main_subzone_55)

    main_address_30 = Address()
    main_address_30.title = 'Planet Bowling'
    main_address_30.location = main_place_28.location
    main_address_30.pin_code = 110044
    main_address_30.zone = main_zone_1
    main_address_30.address_line1 = 'A-38, Mohan Co-Operative Industrial Estate, Mathura Road, Badarpur,Delhi'
    main_address_30.save()

    main_activity_30 = Activity()
    main_activity_30.address = main_address_30
    main_activity_30.title = 'Planet Bowling'
    main_activity_30.description = ''
    main_activity_30.rating = 0
    main_activity_30.votes = 0
    main_activity_30.person_of_contact = ''
    main_activity_30.contact_numbers = ['01126959563', '01126959665']
    main_activity_30.cost = 3
    main_activity_30.email = ''
    main_activity_30.website = ''
    main_activity_30.facebook = ''
    main_activity_30.twitter = ''
    main_activity_30.url_name = 'planet-bowling'
    main_activity_30.save()

    main_activity_30.category.add(main_category_2)
    main_activity_30.category.add(main_category_3)


    main_address_30.sub_zone.add(main_subzone_54)
    main_address_30.sub_zone.add(main_subzone_55)

    main_address_31 = Address()
    main_address_31.title = 'Glued Entertainment'
    main_address_31.location = main_place_29.location
    main_address_31.pin_code = 201301
    main_address_31.zone = main_zone_1
    main_address_31.address_line1 = 'Dynamic House, Opp Petrol Bunk, Dadri Main Road, Sector-41, Noida, Uttar Pradesh '
    main_address_31.save()

    main_activity_31 = Activity()
    main_activity_31.address = main_address_31
    main_activity_31.title = 'Glued Entertainment'
    main_activity_31.description = 'Glued, Gaming and Sports Lounge, is an unusual combination of gaming ,sports & entertainment offering its customer’s a break, TO LIVE FOR !!'
    main_activity_31.rating = 0
    main_activity_31.votes = 0
    main_activity_31.person_of_contact = ''
    main_activity_31.contact_numbers = ['098913', '39974']
    main_activity_31.cost = 3
    main_activity_31.email = ''
    main_activity_31.website = ''
    main_activity_31.facebook = 'https://www.facebook.com/gluednoida'
    main_activity_31.twitter = ''
    main_activity_31.url_name = 'glued-entertainment'
    main_activity_31.save()

    main_activity_31.category.add(main_category_2)
    main_activity_31.category.add(main_category_3)
    main_activity_31.category.add(main_category_29)

    main_address_31.sub_zone.add(main_subzone_22)

    main_address_32 = Address()
    main_address_32.title = 'Flyboy'
    main_address_32.location = main_place_37.location
    main_address_32.pin_code = 122001
    main_address_32.zone = main_zone_1
    main_address_32.address_line1 = 'Po – Daula, Karanki, Vatika Complex, next to the Westin Sohna Resort & Spa, Sohna, Gurgaon'
    main_address_32.save()

    main_activity_32 = Activity()
    main_activity_32.address = main_address_32
    main_activity_32.title = 'Flyboy'
    main_activity_32.description = ''
    main_activity_32.rating = 0
    main_activity_32.votes = 0
    main_activity_32.person_of_contact = 'Mr. Shantanu'
    main_activity_32.contact_numbers = ['09871510510']
    main_activity_32.cost = 5
    main_activity_32.email = 'info@flyboy.in'
    main_activity_32.website = 'http://www.flyboy.in/'
    main_activity_32.facebook = 'https://www.facebook.com/pages/Flyboy-Aviation/263546580354464'
    main_activity_32.twitter = 'https://twitter.com/flyboyaviation'
    main_activity_32.url_name = 'flyboy'
    main_activity_32.save()

    main_activity_32.category.add(main_category_12)

    main_address_32.sub_zone.add(main_subzone_4)
    main_address_32.sub_zone.add(main_subzone_57)

    main_address_33 = Address()
    main_address_33.title = 'Arnos Den'
    main_address_33.location = main_place_38.location
    main_address_33.pin_code = 110027
    main_address_33.zone = main_zone_1
    main_address_33.address_line1 = 'Pacific Mall, Subhash Nagar     '
    main_address_33.save()

    main_activity_33 = Activity()
    main_activity_33.address = main_address_33
    main_activity_33.title = 'Arnos Den'
    main_activity_33.description = ''
    main_activity_33.rating = 0
    main_activity_33.votes = 0
    main_activity_33.person_of_contact = ''
    main_activity_33.contact_numbers = ['09910994870']
    main_activity_33.cost = 3
    main_activity_33.email = 'anjali@arnosden.com'
    main_activity_33.website = ''
    main_activity_33.facebook = ''
    main_activity_33.twitter = ''
    main_activity_33.url_name = 'arnos-den'
    main_activity_33.save()

    main_activity_33.category.add(main_category_3)

    main_address_33.sub_zone.add(main_subzone_42)

    main_address_34 = Address()
    main_address_34.title = 'Fun Zone'
    main_address_34.location = main_place_40.location
    main_address_34.pin_code = 121101
    main_address_34.zone = main_zone_1
    main_address_34.address_line1 = 'City Mall, Sector 12 Faridabad  '
    main_address_34.save()

    main_activity_34 = Activity()
    main_activity_34.address = main_address_34
    main_activity_34.title = 'Fun Zone'
    main_activity_34.description = ''
    main_activity_34.rating = 0
    main_activity_34.votes = 0
    main_activity_34.person_of_contact = 'Mr. Raj'
    main_activity_34.contact_numbers = ['09211699658']
    main_activity_34.cost = 3
    main_activity_34.email = 'melodieskidszone25@yahoo.com'
    main_activity_34.website = ''
    main_activity_34.facebook = ''
    main_activity_34.twitter = ''
    main_activity_34.url_name = 'fun-zone'
    main_activity_34.save()

    main_activity_34.category.add(main_category_29)

    main_address_34.sub_zone.add(main_subzone_40)
    main_address_34.sub_zone.add(main_subzone_55)

    main_address_35 = Address()
    main_address_35.title = 'Pool World'
    main_address_35.location = main_place_41.location
    main_address_35.pin_code = 0
    main_address_35.zone = main_zone_1
    main_address_35.address_line1 = 'M-22, Greater Kailash 1, Delhi'
    main_address_35.save()

    main_activity_35 = Activity()
    main_activity_35.address = main_address_35
    main_activity_35.title = 'Pool World'
    main_activity_35.description = 'Pool World is based in M Block market of Greater Kailash, 2 of Delhi. They conduct classes for Pool & Snooker both. However, the cost of coaching is on per hour basis and it is open 7 days a week.'
    main_activity_35.rating = 0
    main_activity_35.votes = 0
    main_activity_35.person_of_contact = ''
    main_activity_35.contact_numbers = ['09891545424']
    main_activity_35.cost = 3
    main_activity_35.email = ''
    main_activity_35.website = ''
    main_activity_35.facebook = ''
    main_activity_35.twitter = ''
    main_activity_35.url_name = 'pool-world'
    main_activity_35.save()

    main_activity_35.category.add(main_category_3)

    main_address_35.sub_zone.add(main_subzone_5)

    main_address_36 = Address()
    main_address_36.title = 'The Mind Cafe'
    main_address_36.location = main_place_42.location
    main_address_36.pin_code = 122002
    main_address_36.zone = main_zone_1
    main_address_36.address_line1 = '2nd Floor, Cross Point,  Opp. Galleria Market, DLF Phase 4, Gurgaon (HR)'
    main_address_36.save()

    main_activity_36 = Activity()
    main_activity_36.address = main_address_36
    main_activity_36.title = 'The Mind Cafe'
    main_activity_36.description = "The Mind Cafe is Singapore's award winning board games cafe which has been awarded by Singapore Book of Records for widest collection of board games. The Mind Cafe is the first and the only of its kind in India and the outlet amenities include a well-stocked library of international board games, the largest collection in India, along with a range of dining options. The Mind Cafe is an ideal meeting place where families, colleagues and friends meet up for board games over good food, snacks and drinks. The Mind Cafe has delectable multi-cuisine menu with large variety of food and beverages on offer."
    main_activity_36.rating = 0
    main_activity_36.votes = 0
    main_activity_36.person_of_contact = ''
    main_activity_36.contact_numbers = ['0124-4088830', '09873441161']
    main_activity_36.cost = 3
    main_activity_36.email = ''
    main_activity_36.website = 'http://www.themindcafe.co.in/index.php'
    main_activity_36.facebook = 'https://www.facebook.com/MindCafeIndia'
    main_activity_36.twitter = ''
    main_activity_36.url_name = 'the-mind-cafe'
    main_activity_36.save()

    main_activity_36.category.add(main_category_10)

    main_address_36.sub_zone.add(main_subzone_4)
    main_address_36.sub_zone.add(main_subzone_60)

    main_address_37 = Address()
    main_address_37.title = 'Yogakshema - Iyengar Yoga Centre'
    main_address_37.location = main_place_43.location
    main_address_37.pin_code = 110002
    main_address_37.zone = main_zone_1
    main_address_37.address_line1 = 'Plot No.65,66,67, Deendayal Upadhyay Marg, Rouse Avenue, New Delhi '
    main_address_37.save()

    main_activity_37 = Activity()
    main_activity_37.address = main_address_37
    main_activity_37.title = 'Yogakshema - Iyengar Yoga Centre'
    main_activity_37.description = ''
    main_activity_37.rating = 0
    main_activity_37.votes = 0
    main_activity_37.person_of_contact = ''
    main_activity_37.contact_numbers = ['011-23234356', '011-2323', '4357']
    main_activity_37.cost = 3
    main_activity_37.email = 'info@iyengaryogakshema.org'
    main_activity_37.website = 'http://www.iyengaryogakshema.org/'
    main_activity_37.facebook = 'https://www.facebook.com/yogakshemadelhi?fref=nf'
    main_activity_37.twitter = ''
    main_activity_37.url_name = 'yogakshema-iyengar-yoga-centre'
    main_activity_37.save()

    main_activity_37.category.add(main_category_9)

    main_address_37.sub_zone.add(main_subzone_61)
    main_address_37.sub_zone.add(main_subzone_62)
    main_address_37.sub_zone.add(main_subzone_63)
    main_address_37.sub_zone.add(main_subzone_64)

    main_address_38 = Address()
    main_address_38.title = 'The Yoga Studio'
    main_address_38.location = main_place_45.location
    main_address_38.pin_code = 110016
    main_address_38.zone = main_zone_1
    main_address_38.address_line1 = ' # D-43,Hauz Khas, New Delhi, Delhi '
    main_address_38.save()

    main_activity_38 = Activity()
    main_activity_38.address = main_address_38
    main_activity_38.title = 'The Yoga Studio'
    main_activity_38.description = ''
    main_activity_38.rating = 0
    main_activity_38.votes = 0
    main_activity_38.person_of_contact = ''
    main_activity_38.contact_numbers = ['09811131368', '09899950200']
    main_activity_38.cost = 3
    main_activity_38.email = 'contact@theyogastudio.info'
    main_activity_38.website = 'http://www.theyogastudio.info/'
    main_activity_38.facebook = 'https://www.facebook.com/seemasondhiyogastudio'
    main_activity_38.twitter = ''
    main_activity_38.url_name = 'the-yoga-studio'
    main_activity_38.save()

    main_activity_38.category.add(main_category_21)


    main_address_38.sub_zone.add(main_subzone_5)
    main_address_38.sub_zone.add(main_subzone_53)

    main_address_39 = Address()
    main_address_39.title = 'Anandyogam'
    main_address_39.location = None
    main_address_39.pin_code = 110092
    main_address_39.zone = main_zone_1
    main_address_39.address_line1 = 'House No. 1, Block- J & K Ext- 1, Lakshmi Nagar, New Delhi'
    main_address_39.save()

    main_activity_39 = Activity()
    main_activity_39.address = main_address_39
    main_activity_39.title = 'Anandyogam'
    main_activity_39.description = ''
    main_activity_39.rating = 0
    main_activity_39.votes = 0
    main_activity_39.person_of_contact = ''
    main_activity_39.contact_numbers = ['09899183279']
    main_activity_39.cost = 3
    main_activity_39.email = 'anandashramballia@rediffmail.com'
    main_activity_39.website = ''
    main_activity_39.facebook = 'https://www.facebook.com/Anandyogam'
    main_activity_39.twitter = ''
    main_activity_39.url_name = 'anandyogam'
    main_activity_39.save()

    main_activity_39.category.add(main_category_9)

    main_address_39.sub_zone.add(main_subzone_67)
    main_address_39.sub_zone.add(main_subzone_68)

    main_address_40 = Address()
    main_address_40.title = 'Universal Yoga Group'
    main_address_40.location = main_place_47.location
    main_address_40.pin_code = 122001
    main_address_40.zone = main_zone_1
    main_address_40.address_line1 = 'D4/ 27 DLF phase 1 Gurgaon Village, Sector 6 Gurgaon'
    main_address_40.save()

    main_activity_40 = Activity()
    main_activity_40.address = main_address_40
    main_activity_40.title = 'Universal Yoga Group'
    main_activity_40.description = ''
    main_activity_40.rating = 0
    main_activity_40.votes = 0
    main_activity_40.person_of_contact = ''
    main_activity_40.contact_numbers = ['09350070549']
    main_activity_40.cost = 3
    main_activity_40.email = 'info@universalyoga.in'
    main_activity_40.website = 'http://www.universalyoga.in/'
    main_activity_40.facebook = 'https://www.facebook.com/UniversalYogaGroup'
    main_activity_40.twitter = ''
    main_activity_40.url_name = 'universal-yoga-group'
    main_activity_40.save()

    main_activity_40.category.add(main_category_9)

    main_address_40.sub_zone.add(main_subzone_4)
    main_address_40.sub_zone.add(main_subzone_71)
    main_address_40.sub_zone.add(main_subzone_72)

    main_address_41 = Address()
    main_address_41.title = 'Kedarnath Centre for Yoga and Naturopathy'
    main_address_41.location = main_place_46.location
    main_address_41.pin_code = 122001
    main_address_41.zone = main_zone_1
    main_address_41.address_line1 = 'C 1815, Sushant Lok Phase 1,Gurgaon'
    main_address_41.save()

    main_activity_41 = Activity()
    main_activity_41.address = main_address_41
    main_activity_41.title = 'Kedarnath Centre for Yoga and Naturopathy'
    main_activity_41.description = ''
    main_activity_41.rating = 0
    main_activity_41.votes = 0
    main_activity_41.person_of_contact = ''
    main_activity_41.contact_numbers = ['09810281808', '09971848805']
    main_activity_41.cost = 3
    main_activity_41.email = 'contact@kedarnathyoga.com'
    main_activity_41.website = 'http://www.kedarnathyoga.com'
    main_activity_41.facebook = 'https://www.facebook.com/pages/Kedarnath-yoga-centre/466565750123432'
    main_activity_41.twitter = 'https://twitter.com/yogaathomeindia'
    main_activity_41.url_name = 'kedarnath-centre-for-yoga-and-naturopathy'
    main_activity_41.save()

    main_activity_41.category.add(main_category_8)
    main_activity_41.category.add(main_category_21)

    main_address_41.sub_zone.add(main_subzone_69)
    main_address_41.sub_zone.add(main_subzone_70)

    main_address_42 = Address()
    main_address_42.title = 'Universal Yoga Group'
    main_address_42.location = main_place_48.location
    main_address_42.pin_code = 110092
    main_address_42.zone = main_zone_1
    main_address_42.address_line1 = 'X- 22 , karkardooma, Institutional Area,lower ground floor, IP Extension Part II, Vikas Marg, Delhi '
    main_address_42.save()

    main_activity_42 = Activity()
    main_activity_42.address = main_address_42
    main_activity_42.title = 'Universal Yoga Group'
    main_activity_42.description = ''
    main_activity_42.rating = 0
    main_activity_42.votes = 0
    main_activity_42.person_of_contact = ''
    main_activity_42.contact_numbers = ['09350070549']
    main_activity_42.cost = 4
    main_activity_42.email = 'info@universalyoga.in'
    main_activity_42.website = 'http://www.universalyoga.in'
    main_activity_42.facebook = 'https://www.facebook.com/UniversalYogaGroup'
    main_activity_42.twitter = ''
    main_activity_42.url_name = 'universal-yoga-group'
    main_activity_42.save()

    main_activity_42.category.add(main_category_9)

    main_address_42.sub_zone.add(main_subzone_1)
    main_address_42.sub_zone.add(main_subzone_73)

    main_address_43 = Address()
    main_address_43.title = 'Studio Pranå'
    main_address_43.location = main_place_52.location
    main_address_43.pin_code = 110091
    main_address_43.zone = main_zone_1
    main_address_43.address_line1 = '#37, Second Floor, Pratap Nagar, Main Acharya Niketan Market, Mayur Vihar, Phase - I, New Delhi '
    main_address_43.save()

    main_activity_43 = Activity()
    main_activity_43.address = main_address_43
    main_activity_43.title = 'Studio Pranå'
    main_activity_43.description = ''
    main_activity_43.rating = 0
    main_activity_43.votes = 0
    main_activity_43.person_of_contact = ''
    main_activity_43.contact_numbers = ['09810172485', '09716308893']
    main_activity_43.cost = 4
    main_activity_43.email = 'voyageabsolute@gmail.com'
    main_activity_43.website = 'http://www.studioprana.in/'
    main_activity_43.facebook = 'https://www.facebook.com/studiopran'
    main_activity_43.twitter = ''
    main_activity_43.url_name = 'studio-prana'
    main_activity_43.save()

    main_activity_43.category.add(main_category_7)
    main_activity_43.category.add(main_category_9)

    main_address_43.sub_zone.add(main_subzone_1)
    main_address_43.sub_zone.add(main_subzone_2)
    main_address_43.sub_zone.add(main_subzone_3)

    main_address_44 = Address()
    main_address_44.title = 'The Pilates Studio'
    main_address_44.location = None
    main_address_44.pin_code = 110016
    main_address_44.zone = main_zone_1
    main_address_44.address_line1 = 'K-19 Green Park Main, New Delhi, India'
    main_address_44.save()

    main_activity_44 = Activity()
    main_activity_44.address = main_address_44
    main_activity_44.title = 'The Pilates Studio'
    main_activity_44.description = ''
    main_activity_44.rating = 0
    main_activity_44.votes = 0
    main_activity_44.person_of_contact = ''
    main_activity_44.contact_numbers = ['09811202480']
    main_activity_44.cost = 4
    main_activity_44.email = ''
    main_activity_44.website = ''
    main_activity_44.facebook = 'https://www.facebook.com/pages/The-Pilates-StudioNew-Delhi/221975111200344?ref=br_rs'
    main_activity_44.twitter = ''
    main_activity_44.url_name = 'the-pilates-studio'
    main_activity_44.save()

    main_activity_44.category.add(main_category_7)
    main_activity_44.category.add(main_category_9)

    main_address_44.sub_zone.add(main_subzone_5)
    main_address_44.sub_zone.add(main_subzone_76)

    main_address_45 = Address()
    main_address_45.title = 'Navdha Yoga Center'
    main_address_45.location = main_place_53.location
    main_address_45.pin_code = 110017
    main_address_45.zone = main_zone_1
    main_address_45.address_line1 = 'L-76, Malviya Nagar, New Delhi, Delhi '
    main_address_45.save()

    main_activity_45 = Activity()
    main_activity_45.address = main_address_45
    main_activity_45.title = 'Navdha Yoga Center'
    main_activity_45.description = ''
    main_activity_45.rating = 0
    main_activity_45.votes = 0
    main_activity_45.person_of_contact = ''
    main_activity_45.contact_numbers = ['09654231889', '09711801895']
    main_activity_45.cost = 4
    main_activity_45.email = ''
    main_activity_45.website = 'http://navadhayoga.com/'
    main_activity_45.facebook = 'https://www.facebook.com/pages/Navadha-Yoga/217244035112068?ref=br_rs'
    main_activity_45.twitter = ''
    main_activity_45.url_name = 'navdha-yoga-center'
    main_activity_45.save()

    main_activity_45.category.add(main_category_7)
    main_activity_45.category.add(main_category_9)

    main_address_45.sub_zone.add(main_subzone_5)
    main_address_45.sub_zone.add(main_subzone_77)

    main_address_46 = Address()
    main_address_46.title = 'iSkate'
    main_address_46.location = main_place_54.location
    main_address_46.pin_code = 122002
    main_address_46.zone = main_zone_1
    main_address_46.address_line1 = '6th Floor, Ambience Mall, National Highway 8, Ambience Island, DLF Phase 3, Sector 24 Gurgaon, Haryana '
    main_address_46.save()

    main_activity_46 = Activity()
    main_activity_46.address = main_address_46
    main_activity_46.title = 'iSkate'
    main_activity_46.description = ''
    main_activity_46.rating = 0
    main_activity_46.votes = 0
    main_activity_46.person_of_contact = 'Mr. Nibin'
    main_activity_46.contact_numbers = ['0124-4610606', '09958436009']
    main_activity_46.cost = 5
    main_activity_46.email = 'info@iskate.co.in'
    main_activity_46.website = 'http://www.iskate.co.in/'
    main_activity_46.facebook = 'http://www.facebook.com/iskateIndia'
    main_activity_46.twitter = ''
    main_activity_46.url_name = 'iskate'
    main_activity_46.save()

    main_activity_46.category.add(main_category_6)

    main_address_46.sub_zone.add(main_subzone_28)
    main_address_46.sub_zone.add(main_subzone_78)
    main_address_46.sub_zone.add(main_subzone_79)

    main_address_47 = Address()
    main_address_47.title = 'Yogakul'
    main_address_47.location = main_place_49.location
    main_address_47.pin_code = 110049
    main_address_47.zone = main_zone_1
    main_address_47.address_line1 = '110, First Floor, Shahpur Jat, Siri Fort, New Delhi,India'
    main_address_47.save()

    main_activity_47 = Activity()
    main_activity_47.address = main_address_47
    main_activity_47.title = 'Yogakul'
    main_activity_47.description = ''
    main_activity_47.rating = 0
    main_activity_47.votes = 0
    main_activity_47.person_of_contact = ''
    main_activity_47.contact_numbers = ['09711825994']
    main_activity_47.cost = 3
    main_activity_47.email = ''
    main_activity_47.website = 'http://www.yogakul.com'
    main_activity_47.facebook = 'https://www.facebook.com/yogakulstudio?ref=br_rs'
    main_activity_47.twitter = ''
    main_activity_47.url_name = 'yogakul'
    main_activity_47.save()

    main_activity_47.category.add(main_category_9)

    main_address_47.sub_zone.add(main_subzone_5)
    main_address_47.sub_zone.add(main_subzone_74)

    main_address_48 = Address()
    main_address_48.title = 'Club Platinum Resort'
    main_address_48.location = None
    main_address_48.pin_code = 124505
    main_address_48.zone = main_zone_1
    main_address_48.address_line1 = 'Assaudha Mod,Delhi-Rohtak Road,Bahadurgarh,Haryana'
    main_address_48.save()

    main_activity_48 = Activity()
    main_activity_48.address = main_address_48
    main_activity_48.title = 'Club Platinum Resort'
    main_activity_48.description = ''
    main_activity_48.rating = 0
    main_activity_48.votes = 0
    main_activity_48.person_of_contact = 'Mr. Udit Chadha'
    main_activity_48.contact_numbers = ['8447693142']
    main_activity_48.cost = 3
    main_activity_48.email = 'clubplatinumresort@gmail.com'
    main_activity_48.website = 'http://www.clubplatinumresorts.com'
    main_activity_48.facebook = ''
    main_activity_48.twitter = ''
    main_activity_48.url_name = 'club-platinum-resort'
    main_activity_48.save()

    main_activity_48.category.add(main_category_5)
    main_activity_48.category.add(main_category_30)


    main_address_48.sub_zone.add(main_subzone_26)
    main_address_48.sub_zone.add(main_subzone_34)
    main_address_48.sub_zone.add(main_subzone_35)

    main_address_49 = Address()
    main_address_49.title = 'Dhoomimal Art Centre'
    main_address_49.location = main_place_56.location
    main_address_49.pin_code = 110001
    main_address_49.zone = main_zone_1
    main_address_49.address_line1 = 'A8, Connanught Place, New Delhi'
    main_address_49.save()

    main_activity_49 = Activity()
    main_activity_49.address = main_address_49
    main_activity_49.title = 'Dhoomimal Art Centre'
    main_activity_49.description = ''
    main_activity_49.rating = 0
    main_activity_49.votes = 0
    main_activity_49.person_of_contact = ''
    main_activity_49.contact_numbers = ['011-23324492', '011-23713025', '011-4151617']
    main_activity_49.cost = 1
    main_activity_49.email = 'info@dhoomimalartcentre.com'
    main_activity_49.website = 'http://www.dhoomimalartcentre.com'
    main_activity_49.facebook = 'http://www.facebook.com/DhoomimalGallery'
    main_activity_49.twitter = ''
    main_activity_49.url_name = 'dhoomimal-art-centre'
    main_activity_49.save()

    main_activity_49.category.add(main_category_1)

    main_address_49.sub_zone.add(main_subzone_61)
    main_address_49.sub_zone.add(main_subzone_62)
    main_address_49.sub_zone.add(main_subzone_63)

    main_address_50 = Address()
    main_address_50.title = 'Art Alive Gallery'
    main_address_50.location = main_place_55.location
    main_address_50.pin_code = 110017
    main_address_50.zone = main_zone_1
    main_address_50.address_line1 = 'S-221 Panchsheel Park, New Delhi'
    main_address_50.save()

    main_activity_50 = Activity()
    main_activity_50.address = main_address_50
    main_activity_50.title = 'Art Alive Gallery'
    main_activity_50.description = ''
    main_activity_50.rating = 0
    main_activity_50.votes = 0
    main_activity_50.person_of_contact = ''
    main_activity_50.contact_numbers = ['011-41639000', '011-41638050']
    main_activity_50.cost = 1
    main_activity_50.email = 'info@artalivegallery.com'
    main_activity_50.website = 'http://www.artalivegallery.com/'
    main_activity_50.facebook = 'https://www.facebook.com/pages/Art-Alive-Gallery/1458750674340639'
    main_activity_50.twitter = ''
    main_activity_50.url_name = 'art-alive-gallery'
    main_activity_50.save()

    main_activity_50.category.add(main_category_1)

    main_address_50.sub_zone.add(main_subzone_5)
    main_address_50.sub_zone.add(main_subzone_80)

    main_address_51 = Address()
    main_address_51.title = 'Gallery Espace'
    main_address_51.location = main_place_57.location
    main_address_51.pin_code = 110025
    main_address_51.zone = main_zone_1
    main_address_51.address_line1 = '16 Community Centre New Friends Colony New Delhi '
    main_address_51.save()

    main_activity_51 = Activity()
    main_activity_51.address = main_address_51
    main_activity_51.title = 'Gallery Espace'
    main_activity_51.description = ''
    main_activity_51.rating = 0
    main_activity_51.votes = 0
    main_activity_51.person_of_contact = 'Ms. Neerah'
    main_activity_51.contact_numbers = ['011-26923287', '011-26326267', '011-26922947']
    main_activity_51.cost = 0
    main_activity_51.email = 'art@galleryespace.com'
    main_activity_51.website = 'http://www.galleryespace.com'
    main_activity_51.facebook = 'http://www.facebook.com/GalleryEspace'
    main_activity_51.twitter = ''
    main_activity_51.url_name = 'gallery-espace'
    main_activity_51.save()

    main_activity_51.category.add(main_category_1)


    main_address_51.sub_zone.add(main_subzone_81)
    main_address_51.sub_zone.add(main_subzone_82)

    main_address_52 = Address()
    main_address_52.title = 'Vadhera Art Gallery'
    main_address_52.location = main_place_58.location
    main_address_52.pin_code = 110024
    main_address_52.zone = main_zone_1
    main_address_52.address_line1 = 'D-40 Defence Colony New Delhi '
    main_address_52.save()

    main_activity_52 = Activity()
    main_activity_52.address = main_address_52
    main_activity_52.title = 'Vadhera Art Gallery'
    main_activity_52.description = ''
    main_activity_52.rating = 0
    main_activity_52.votes = 0
    main_activity_52.person_of_contact = ''
    main_activity_52.contact_numbers = ['011-24622545', '011-24615368']
    main_activity_52.cost = 0
    main_activity_52.email = 'art@vadehraart.com'
    main_activity_52.website = 'http://www.vadehraart.com/'
    main_activity_52.facebook = 'https://www.facebook.com/vadehraart'
    main_activity_52.twitter = ''
    main_activity_52.url_name = 'vadhera-art-gallery'
    main_activity_52.save()

    main_activity_52.category.add(main_category_1)

    main_address_52.sub_zone.add(main_subzone_5)
    main_address_52.sub_zone.add(main_subzone_83)

    main_address_53 = Address()
    main_address_53.title = 'Vadhera Art Gallery'
    main_address_53.location = main_place_59.location
    main_address_53.pin_code = 110024
    main_address_53.zone = main_zone_1
    main_address_53.address_line1 = 'D-53 Defence Colony New Delhi '
    main_address_53.save()

    main_activity_53 = Activity()
    main_activity_53.address = main_address_53
    main_activity_53.title = 'Vadhera Art Gallery'
    main_activity_53.description = ''
    main_activity_53.rating = 0
    main_activity_53.votes = 0
    main_activity_53.person_of_contact = ''
    main_activity_53.contact_numbers = ['011-65474005', '011-65474006']
    main_activity_53.cost = 0
    main_activity_53.email = 'art@vadehraart.com'
    main_activity_53.website = 'http://www.vadehraart.com/'
    main_activity_53.facebook = 'https://www.facebook.com/vadehraart'
    main_activity_53.twitter = ''
    main_activity_53.url_name = 'vadhera-art-gallery'
    main_activity_53.save()

    main_activity_53.category.add(main_category_1)

    main_address_53.sub_zone.add(main_subzone_5)
    main_address_53.sub_zone.add(main_subzone_83)

    main_address_54 = Address()
    main_address_54.title = 'Visual Arts Gallery'
    main_address_54.location = main_place_60.location
    main_address_54.pin_code = 110003
    main_address_54.zone = main_zone_1
    main_address_54.address_line1 = 'Habitat World at India Habitat Centre  Lodhi Road  New Delhi '
    main_address_54.save()

    main_activity_54 = Activity()
    main_activity_54.address = main_address_54
    main_activity_54.title = 'Visual Arts Gallery'
    main_activity_54.description = ''
    main_activity_54.rating = 0
    main_activity_54.votes = 0
    main_activity_54.person_of_contact = ''
    main_activity_54.contact_numbers = ['011-43662024']
    main_activity_54.cost = 0
    main_activity_54.email = 'habitatworld@oldworldhospitality.com'
    main_activity_54.website = 'http://www.indiahabitat.org/vag'
    main_activity_54.facebook = 'https://www.facebook.com/pages/Visual-Arts-Gallery/526772930797596'
    main_activity_54.twitter = ''
    main_activity_54.url_name = 'visual-arts-gallery'
    main_activity_54.save()

    main_activity_54.category.add(main_category_1)


    main_address_54.sub_zone.add(main_subzone_84)
    main_address_54.sub_zone.add(main_subzone_85)
    main_address_54.sub_zone.add(main_subzone_86)

    main_address_55 = Address()
    main_address_55.title = 'Rockshot Paintball Sports'
    main_address_55.location = main_place_61.location
    main_address_55.pin_code = 110092
    main_address_55.zone = main_zone_1
    main_address_55.address_line1 = 'S11/C3, Pandav Nagar Ext, New Delhi'
    main_address_55.save()

    main_activity_55 = Activity()
    main_activity_55.address = main_address_55
    main_activity_55.title = 'Rockshot Paintball Sports'
    main_activity_55.description = ''
    main_activity_55.rating = 0
    main_activity_55.votes = 0
    main_activity_55.person_of_contact = 'Akash Thapa'
    main_activity_55.contact_numbers = ['9818215877']
    main_activity_55.cost = 3
    main_activity_55.email = 'rockshotpaintballsportsco@gmail.com'
    main_activity_55.website = 'http://www.rockshotpaintballsports.com'
    main_activity_55.facebook = 'https://www.facebook.com/pages/Rockshot-Paintball-Sports/502558346441184?fref=ts'
    main_activity_55.twitter = ''
    main_activity_55.url_name = 'rockshot-paintball-sports'
    main_activity_55.save()

    main_activity_55.category.add(main_category_28)


    main_address_55.sub_zone.add(main_subzone_1)
    main_address_55.sub_zone.add(main_subzone_87)

    main_address_56 = Address()
    main_address_56.title = 'Rockshot Paintball Sports'
    main_address_56.location = main_place_62.location
    main_address_56.pin_code = 0
    main_address_56.zone = main_zone_1
    main_address_56.address_line1 = 'Green View Resedency C-254, Sector-44 Near - Challera Market, Noida'
    main_address_56.save()

    main_activity_56 = Activity()
    main_activity_56.address = main_address_56
    main_activity_56.title = 'Rockshot Paintball Sports'
    main_activity_56.description = ''
    main_activity_56.rating = 0
    main_activity_56.votes = 0
    main_activity_56.person_of_contact = 'Akash Thapa'
    main_activity_56.contact_numbers = ['9818215877']
    main_activity_56.cost = 3
    main_activity_56.email = 'rockshotpaintballsportsco@gmail.com'
    main_activity_56.website = 'http://www.rockshotpaintballsports.com'
    main_activity_56.facebook = 'https://www.facebook.com/pages/Rockshot-Paintball-Sports/502558346441184'
    main_activity_56.twitter = ''
    main_activity_56.url_name = 'rockshot-paintball-sports'
    main_activity_56.save()

    main_activity_56.category.add(main_category_28)


    main_address_56.sub_zone.add(main_subzone_22)
    main_address_56.sub_zone.add(main_subzone_88)
    main_address_56.sub_zone.add(main_subzone_89)

    main_address_57 = Address()
    main_address_57.title = 'Lock n Load Paintball'
    main_address_57.location = main_place_38.location
    main_address_57.pin_code = 110018
    main_address_57.zone = main_zone_1
    main_address_57.address_line1 = 'Pacific Mall, Subhash Nagar, New Delhi'
    main_address_57.save()

    main_activity_57 = Activity()
    main_activity_57.address = main_address_57
    main_activity_57.title = 'Lock n Load Paintball'
    main_activity_57.description = ''
    main_activity_57.rating = 0
    main_activity_57.votes = 0
    main_activity_57.person_of_contact = 'Mr. Karamjit Bawa'
    main_activity_57.contact_numbers = ['9873444019']
    main_activity_57.cost = 3
    main_activity_57.email = 'karamjitbawa@kaarma.in'
    main_activity_57.website = ''
    main_activity_57.facebook = 'https://www.facebook.com/pages/LocknLoad-Paintball/298881570184537'
    main_activity_57.twitter = ''
    main_activity_57.url_name = 'lock-n-load-paintball'
    main_activity_57.save()

    main_activity_57.category.add(main_category_28)

    main_address_57.sub_zone.add(main_subzone_42)
    main_address_57.sub_zone.add(main_subzone_75)
    main_address_57.sub_zone.add(main_subzone_91)


if __name__ == "__main__":
    import_data()
