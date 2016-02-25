import sys, os
sys.path.append('/home/kartik/projects/outing-box-project')

from django.conf import settings

import random

import django
django.setup()

from decimal import Decimal

def import_data():
    # Processing model: Zone

    from outingbox.models import Zone

    outingbox_zone_1 = Zone()
    outingbox_zone_1.title = 'Delhi NCR'
    outingbox_zone_1.save()

    outingbox_zone_2 = Zone()
    outingbox_zone_2.title = 'NCR'
    outingbox_zone_2.save()

    # Processing model: SubZone

    from outingbox.models import SubZone

    outingbox_subzone_1 = SubZone()
    outingbox_subzone_1.title = 'Rajouri Garden'
    outingbox_subzone_1.zone = outingbox_zone_1
    outingbox_subzone_1.save()

    outingbox_subzone_2 = SubZone()
    outingbox_subzone_2.title = 'Subhash Nagar'
    outingbox_subzone_2.zone = outingbox_zone_1
    outingbox_subzone_2.save()

    outingbox_subzone_3 = SubZone()
    outingbox_subzone_3.title = 'Kapashera'
    outingbox_subzone_3.zone = outingbox_zone_1
    outingbox_subzone_3.save()

    outingbox_subzone_4 = SubZone()
    outingbox_subzone_4.title = 'Sector 25A Noida'
    outingbox_subzone_4.zone = outingbox_zone_1
    outingbox_subzone_4.save()

    outingbox_subzone_5 = SubZone()
    outingbox_subzone_5.title = 'East Delhi'
    outingbox_subzone_5.zone = outingbox_zone_2
    outingbox_subzone_5.save()

    outingbox_subzone_6 = SubZone()
    outingbox_subzone_6.title = 'Mayur Vihar'
    outingbox_subzone_6.zone = outingbox_zone_2
    outingbox_subzone_6.save()

    outingbox_subzone_7 = SubZone()
    outingbox_subzone_7.title = 'Mayur Vihar Phase 1'
    outingbox_subzone_7.zone = outingbox_zone_2
    outingbox_subzone_7.save()

    outingbox_subzone_8 = SubZone()
    outingbox_subzone_8.title = 'Gurgaon'
    outingbox_subzone_8.zone = outingbox_zone_2
    outingbox_subzone_8.save()

    outingbox_subzone_9 = SubZone()
    outingbox_subzone_9.title = 'South Delhi'
    outingbox_subzone_9.zone = outingbox_zone_2
    outingbox_subzone_9.save()

    outingbox_subzone_10 = SubZone()
    outingbox_subzone_10.title = 'West Delhi'
    outingbox_subzone_10.zone = outingbox_zone_2
    outingbox_subzone_10.save()

    outingbox_subzone_11 = SubZone()
    outingbox_subzone_11.title = 'GT Karnal Road'
    outingbox_subzone_11.zone = outingbox_zone_2
    outingbox_subzone_11.save()

    outingbox_subzone_12 = SubZone()
    outingbox_subzone_12.title = 'GTB Memorial'
    outingbox_subzone_12.zone = outingbox_zone_2
    outingbox_subzone_12.save()

    outingbox_subzone_13 = SubZone()
    outingbox_subzone_13.title = 'Narela'
    outingbox_subzone_13.zone = outingbox_zone_2
    outingbox_subzone_13.save()

    outingbox_subzone_14 = SubZone()
    outingbox_subzone_14.title = 'North West Delhi'
    outingbox_subzone_14.zone = outingbox_zone_2
    outingbox_subzone_14.save()

    outingbox_subzone_15 = SubZone()
    outingbox_subzone_15.title = 'Alipur'
    outingbox_subzone_15.zone = outingbox_zone_2
    outingbox_subzone_15.save()

    outingbox_subzone_16 = SubZone()
    outingbox_subzone_16.title = 'North Delhi'
    outingbox_subzone_16.zone = outingbox_zone_2
    outingbox_subzone_16.save()

    outingbox_subzone_17 = SubZone()
    outingbox_subzone_17.title = 'Sector 29 Gurgaon'
    outingbox_subzone_17.zone = outingbox_zone_2
    outingbox_subzone_17.save()

    outingbox_subzone_18 = SubZone()
    outingbox_subzone_18.title = 'South West Delhi'
    outingbox_subzone_18.zone = outingbox_zone_2
    outingbox_subzone_18.save()

    outingbox_subzone_19 = SubZone()
    outingbox_subzone_19.title = 'Kalindi Kunj'
    outingbox_subzone_19.zone = outingbox_zone_2
    outingbox_subzone_19.save()

    outingbox_subzone_20 = SubZone()
    outingbox_subzone_20.title = 'Okhla'
    outingbox_subzone_20.zone = outingbox_zone_2
    outingbox_subzone_20.save()

    outingbox_subzone_21 = SubZone()
    outingbox_subzone_21.title = 'Sector 38 Noida'
    outingbox_subzone_21.zone = outingbox_zone_2
    outingbox_subzone_21.save()

    outingbox_subzone_22 = SubZone()
    outingbox_subzone_22.title = 'Noida'
    outingbox_subzone_22.zone = outingbox_zone_2
    outingbox_subzone_22.save()

    outingbox_subzone_23 = SubZone()
    outingbox_subzone_23.title = 'Sector 10 Rohini'
    outingbox_subzone_23.zone = outingbox_zone_2
    outingbox_subzone_23.save()

    outingbox_subzone_24 = SubZone()
    outingbox_subzone_24.title = 'Rohini'
    outingbox_subzone_24.zone = outingbox_zone_2
    outingbox_subzone_24.save()

    outingbox_subzone_25 = SubZone()
    outingbox_subzone_25.title = 'Rithala '
    outingbox_subzone_25.zone = outingbox_zone_2
    outingbox_subzone_25.save()

    outingbox_subzone_26 = SubZone()
    outingbox_subzone_26.title = 'Haryana'
    outingbox_subzone_26.zone = outingbox_zone_2
    outingbox_subzone_26.save()

    outingbox_subzone_27 = SubZone()
    outingbox_subzone_27.title = 'Sonepat'
    outingbox_subzone_27.zone = outingbox_zone_2
    outingbox_subzone_27.save()

    outingbox_subzone_28 = SubZone()
    outingbox_subzone_28.title = 'NH 1'
    outingbox_subzone_28.zone = outingbox_zone_2
    outingbox_subzone_28.save()

    outingbox_subzone_29 = SubZone()
    outingbox_subzone_29.title = 'National Highway 1'
    outingbox_subzone_29.zone = outingbox_zone_2
    outingbox_subzone_29.save()

    outingbox_subzone_30 = SubZone()
    outingbox_subzone_30.title = 'Ghaziabad'
    outingbox_subzone_30.zone = outingbox_zone_2
    outingbox_subzone_30.save()

    outingbox_subzone_31 = SubZone()
    outingbox_subzone_31.title = 'Delhi Meerut Highway'
    outingbox_subzone_31.zone = outingbox_zone_2
    outingbox_subzone_31.save()

    outingbox_subzone_32 = SubZone()
    outingbox_subzone_32.title = 'Duhai'
    outingbox_subzone_32.zone = outingbox_zone_2
    outingbox_subzone_32.save()

    outingbox_subzone_33 = SubZone()
    outingbox_subzone_33.title = 'Bahadurgarh'
    outingbox_subzone_33.zone = outingbox_zone_2
    outingbox_subzone_33.save()

    outingbox_subzone_34 = SubZone()
    outingbox_subzone_34.title = 'Delhi Jaipur Expressway'
    outingbox_subzone_34.zone = outingbox_zone_2
    outingbox_subzone_34.save()

    outingbox_subzone_35 = SubZone()
    outingbox_subzone_35.title = ' Nh-8'
    outingbox_subzone_35.zone = outingbox_zone_2
    outingbox_subzone_35.save()

    outingbox_subzone_36 = SubZone()
    outingbox_subzone_36.title = 'Faridabad'
    outingbox_subzone_36.zone = outingbox_zone_2
    outingbox_subzone_36.save()

    outingbox_subzone_37 = SubZone()
    outingbox_subzone_37.title = 'Saket'
    outingbox_subzone_37.zone = outingbox_zone_2
    outingbox_subzone_37.save()

    outingbox_subzone_38 = SubZone()
    outingbox_subzone_38.title = 'Tilak Nagar'
    outingbox_subzone_38.zone = outingbox_zone_2
    outingbox_subzone_38.save()

    outingbox_subzone_39 = SubZone()
    outingbox_subzone_39.title = 'Chattarpur'
    outingbox_subzone_39.zone = outingbox_zone_2
    outingbox_subzone_39.save()

    outingbox_subzone_40 = SubZone()
    outingbox_subzone_40.title = 'Sector 18 Noida'
    outingbox_subzone_40.zone = outingbox_zone_2
    outingbox_subzone_40.save()

    outingbox_subzone_41 = SubZone()
    outingbox_subzone_41.title = 'Botanical Garden'
    outingbox_subzone_41.zone = outingbox_zone_2
    outingbox_subzone_41.save()

    outingbox_subzone_42 = SubZone()
    outingbox_subzone_42.title = 'Sector 16 Noida'
    outingbox_subzone_42.zone = outingbox_zone_2
    outingbox_subzone_42.save()

    outingbox_subzone_43 = SubZone()
    outingbox_subzone_43.title = 'Sector 17 Gurgaon'
    outingbox_subzone_43.zone = outingbox_zone_2
    outingbox_subzone_43.save()

    outingbox_subzone_44 = SubZone()
    outingbox_subzone_44.title = 'Sector 18 Gurgaon'
    outingbox_subzone_44.zone = outingbox_zone_2
    outingbox_subzone_44.save()

    outingbox_subzone_45 = SubZone()
    outingbox_subzone_45.title = 'Sector 15 Gurgaon'
    outingbox_subzone_45.zone = outingbox_zone_2
    outingbox_subzone_45.save()

    outingbox_subzone_46 = SubZone()
    outingbox_subzone_46.title = 'Lajpat Nagar'
    outingbox_subzone_46.zone = outingbox_zone_2
    outingbox_subzone_46.save()

    outingbox_subzone_47 = SubZone()
    outingbox_subzone_47.title = 'Hauz Khas'
    outingbox_subzone_47.zone = outingbox_zone_2
    outingbox_subzone_47.save()

    outingbox_subzone_48 = SubZone()
    outingbox_subzone_48.title = 'Tughlakabad'
    outingbox_subzone_48.zone = outingbox_zone_2
    outingbox_subzone_48.save()

    outingbox_subzone_49 = SubZone()
    outingbox_subzone_49.title = 'Badarpur'
    outingbox_subzone_49.zone = outingbox_zone_2
    outingbox_subzone_49.save()

    outingbox_subzone_50 = SubZone()
    outingbox_subzone_50.title = 'Sohna'
    outingbox_subzone_50.zone = outingbox_zone_2
    outingbox_subzone_50.save()

    outingbox_subzone_51 = SubZone()
    outingbox_subzone_51.title = 'DLF Phase 4'
    outingbox_subzone_51.zone = outingbox_zone_2
    outingbox_subzone_51.save()

    outingbox_subzone_52 = SubZone()
    outingbox_subzone_52.title = 'Rajiv Chowk'
    outingbox_subzone_52.zone = outingbox_zone_2
    outingbox_subzone_52.save()

    outingbox_subzone_53 = SubZone()
    outingbox_subzone_53.title = 'Connaught place'
    outingbox_subzone_53.zone = outingbox_zone_2
    outingbox_subzone_53.save()

    outingbox_subzone_54 = SubZone()
    outingbox_subzone_54.title = 'CP'
    outingbox_subzone_54.zone = outingbox_zone_2
    outingbox_subzone_54.save()

    outingbox_subzone_55 = SubZone()
    outingbox_subzone_55.title = 'Rouse Avenue'
    outingbox_subzone_55.zone = outingbox_zone_2
    outingbox_subzone_55.save()

    outingbox_subzone_56 = SubZone()
    outingbox_subzone_56.title = 'Kailash Colony'
    outingbox_subzone_56.zone = outingbox_zone_2
    outingbox_subzone_56.save()

    outingbox_subzone_57 = SubZone()
    outingbox_subzone_57.title = 'Lakshmi Nagar'
    outingbox_subzone_57.zone = outingbox_zone_2
    outingbox_subzone_57.save()

    outingbox_subzone_58 = SubZone()
    outingbox_subzone_58.title = 'Sushant Lok'
    outingbox_subzone_58.zone = outingbox_zone_2
    outingbox_subzone_58.save()

    outingbox_subzone_59 = SubZone()
    outingbox_subzone_59.title = 'Sector 43 Gurgaon'
    outingbox_subzone_59.zone = outingbox_zone_2
    outingbox_subzone_59.save()

    outingbox_subzone_60 = SubZone()
    outingbox_subzone_60.title = 'DLF Phase 1'
    outingbox_subzone_60.zone = outingbox_zone_2
    outingbox_subzone_60.save()

    outingbox_subzone_61 = SubZone()
    outingbox_subzone_61.title = 'Sector 6 Gurgaon'
    outingbox_subzone_61.zone = outingbox_zone_2
    outingbox_subzone_61.save()

    outingbox_subzone_62 = SubZone()
    outingbox_subzone_62.title = 'Karkardooma'
    outingbox_subzone_62.zone = outingbox_zone_2
    outingbox_subzone_62.save()

    outingbox_subzone_63 = SubZone()
    outingbox_subzone_63.title = 'Siri Fort'
    outingbox_subzone_63.zone = outingbox_zone_2
    outingbox_subzone_63.save()

    outingbox_subzone_64 = SubZone()
    outingbox_subzone_64.title = 'Green Park'
    outingbox_subzone_64.zone = outingbox_zone_2
    outingbox_subzone_64.save()

    outingbox_subzone_65 = SubZone()
    outingbox_subzone_65.title = 'Malviya Nagar'
    outingbox_subzone_65.zone = outingbox_zone_2
    outingbox_subzone_65.save()

    outingbox_subzone_66 = SubZone()
    outingbox_subzone_66.title = 'Sector 24 Gurgaon'
    outingbox_subzone_66.zone = outingbox_zone_2
    outingbox_subzone_66.save()

    outingbox_subzone_67 = SubZone()
    outingbox_subzone_67.title = 'Ambience Mall'
    outingbox_subzone_67.zone = outingbox_zone_2
    outingbox_subzone_67.save()

    outingbox_subzone_68 = SubZone()
    outingbox_subzone_68.title = 'Panchsheel Park'
    outingbox_subzone_68.zone = outingbox_zone_2
    outingbox_subzone_68.save()

    outingbox_subzone_69 = SubZone()
    outingbox_subzone_69.title = 'NFC'
    outingbox_subzone_69.zone = outingbox_zone_2
    outingbox_subzone_69.save()

    outingbox_subzone_70 = SubZone()
    outingbox_subzone_70.title = 'New Friends Colony'
    outingbox_subzone_70.zone = outingbox_zone_2
    outingbox_subzone_70.save()

    outingbox_subzone_71 = SubZone()
    outingbox_subzone_71.title = 'Defence Colony'
    outingbox_subzone_71.zone = outingbox_zone_2
    outingbox_subzone_71.save()

    outingbox_subzone_72 = SubZone()
    outingbox_subzone_72.title = 'Lodhi Road'
    outingbox_subzone_72.zone = outingbox_zone_2
    outingbox_subzone_72.save()

    outingbox_subzone_73 = SubZone()
    outingbox_subzone_73.title = 'Jor Bagh'
    outingbox_subzone_73.zone = outingbox_zone_2
    outingbox_subzone_73.save()

    outingbox_subzone_74 = SubZone()
    outingbox_subzone_74.title = 'JLN Stadium'
    outingbox_subzone_74.zone = outingbox_zone_2
    outingbox_subzone_74.save()

    outingbox_subzone_75 = SubZone()
    outingbox_subzone_75.title = 'Noida Sector 44'
    outingbox_subzone_75.zone = outingbox_zone_2
    outingbox_subzone_75.save()

    outingbox_subzone_76 = SubZone()
    outingbox_subzone_76.title = 'Golf Course'
    outingbox_subzone_76.zone = outingbox_zone_2
    outingbox_subzone_76.save()

    outingbox_subzone_77 = SubZone()
    outingbox_subzone_77.title = 'Pragati Maidan'
    outingbox_subzone_77.zone = outingbox_zone_1
    outingbox_subzone_77.save()

    outingbox_subzone_78 = SubZone()
    outingbox_subzone_78.title = 'NDMC'
    outingbox_subzone_78.zone = outingbox_zone_1
    outingbox_subzone_78.save()

    outingbox_subzone_79 = SubZone()
    outingbox_subzone_79.title = 'Race Course'
    outingbox_subzone_79.zone = outingbox_zone_1
    outingbox_subzone_79.save()

    outingbox_subzone_80 = SubZone()
    outingbox_subzone_80.title = 'Teen Murti House'
    outingbox_subzone_80.zone = outingbox_zone_1
    outingbox_subzone_80.save()

    outingbox_subzone_81 = SubZone()
    outingbox_subzone_81.title = 'Delhi'
    outingbox_subzone_81.zone = outingbox_zone_1
    outingbox_subzone_81.save()

    outingbox_subzone_82 = SubZone()
    outingbox_subzone_82.title = 'Pandav Nagar Ext'
    outingbox_subzone_82.zone = outingbox_zone_2
    outingbox_subzone_82.save()

    outingbox_subzone_83 = SubZone()
    outingbox_subzone_83.title = 'Delhi Rohtak Road'
    outingbox_subzone_83.zone = outingbox_zone_2
    outingbox_subzone_83.save()

    # Processing model: MetroLineColor

    from outingbox.models import MetroLineColor

    outingbox_metrolinecolor_1 = MetroLineColor()
    outingbox_metrolinecolor_1.title = 'green'
    outingbox_metrolinecolor_1.color = 'green'
    outingbox_metrolinecolor_1.save()

    outingbox_metrolinecolor_2 = MetroLineColor()
    outingbox_metrolinecolor_2.title = 'red'
    outingbox_metrolinecolor_2.color = '#fb4f4f'
    outingbox_metrolinecolor_2.save()

    outingbox_metrolinecolor_3 = MetroLineColor()
    outingbox_metrolinecolor_3.title = 'yellow'
    outingbox_metrolinecolor_3.color = '#fbc93d'
    outingbox_metrolinecolor_3.save()

    outingbox_metrolinecolor_4 = MetroLineColor()
    outingbox_metrolinecolor_4.title = 'blue'
    outingbox_metrolinecolor_4.color = '#2e8ece'
    outingbox_metrolinecolor_4.save()

    outingbox_metrolinecolor_5 = MetroLineColor()
    outingbox_metrolinecolor_5.title = 'violet'
    outingbox_metrolinecolor_5.color = '#8e44ad'
    outingbox_metrolinecolor_5.save()

    outingbox_metrolinecolor_6 = MetroLineColor()
    outingbox_metrolinecolor_6.title = 'orange'
    outingbox_metrolinecolor_6.color = '#f39c12'
    outingbox_metrolinecolor_6.save()

    # Processing model: MetroStation

    from outingbox.models import MetroStation

    outingbox_metrostation_1 = MetroStation()
    outingbox_metrostation_1.title = 'Neelam Chowk Ajronda'
    outingbox_metrostation_1.color = outingbox_metrolinecolor_5
    outingbox_metrostation_1.save()

    outingbox_metrostation_2 = MetroStation()
    outingbox_metrostation_2.title = 'Adarsh Nagar'
    outingbox_metrostation_2.color = outingbox_metrolinecolor_3
    outingbox_metrostation_2.save()

    outingbox_metrostation_3 = MetroStation()
    outingbox_metrostation_3.title = 'AIIMS'
    outingbox_metrostation_3.color = outingbox_metrolinecolor_3
    outingbox_metrostation_3.save()

    outingbox_metrostation_4 = MetroStation()
    outingbox_metrostation_4.title = 'Akshardham'
    outingbox_metrostation_4.color = outingbox_metrolinecolor_4
    outingbox_metrostation_4.save()

    outingbox_metrostation_5 = MetroStation()
    outingbox_metrostation_5.title = 'Anand Vihar'
    outingbox_metrostation_5.color = outingbox_metrolinecolor_4
    outingbox_metrostation_5.save()

    outingbox_metrostation_6 = MetroStation()
    outingbox_metrostation_6.title = 'Arjan Garh'
    outingbox_metrostation_6.color = outingbox_metrolinecolor_3
    outingbox_metrostation_6.save()

    outingbox_metrostation_7 = MetroStation()
    outingbox_metrostation_7.title = 'Ashok Park Main'
    outingbox_metrostation_7.color = outingbox_metrolinecolor_1
    outingbox_metrostation_7.save()

    outingbox_metrostation_8 = MetroStation()
    outingbox_metrostation_8.title = 'Azadpur'
    outingbox_metrostation_8.color = outingbox_metrolinecolor_3
    outingbox_metrostation_8.save()

    outingbox_metrostation_9 = MetroStation()
    outingbox_metrostation_9.title = 'Badarpur'
    outingbox_metrostation_9.color = outingbox_metrolinecolor_5
    outingbox_metrostation_9.save()

    outingbox_metrostation_10 = MetroStation()
    outingbox_metrostation_10.title = 'Barakhambha Road'
    outingbox_metrostation_10.color = outingbox_metrolinecolor_4
    outingbox_metrostation_10.save()

    outingbox_metrostation_11 = MetroStation()
    outingbox_metrostation_11.title = 'Botanical Garden'
    outingbox_metrostation_11.color = outingbox_metrolinecolor_4
    outingbox_metrostation_11.save()

    outingbox_metrostation_12 = MetroStation()
    outingbox_metrostation_12.title = 'Central Secretariat'
    outingbox_metrostation_12.color = outingbox_metrolinecolor_3
    outingbox_metrostation_12.save()

    outingbox_metrostation_13 = MetroStation()
    outingbox_metrostation_13.title = 'Chandni Chowk'
    outingbox_metrostation_13.color = outingbox_metrolinecolor_3
    outingbox_metrostation_13.save()

    outingbox_metrostation_14 = MetroStation()
    outingbox_metrostation_14.title = 'Chhatarpur'
    outingbox_metrostation_14.color = outingbox_metrolinecolor_3
    outingbox_metrostation_14.save()

    outingbox_metrostation_15 = MetroStation()
    outingbox_metrostation_15.title = 'Chawri Bazar'
    outingbox_metrostation_15.color = outingbox_metrolinecolor_3
    outingbox_metrostation_15.save()

    outingbox_metrostation_16 = MetroStation()
    outingbox_metrostation_16.title = 'Civil Lines'
    outingbox_metrostation_16.color = outingbox_metrolinecolor_3
    outingbox_metrostation_16.save()

    outingbox_metrostation_17 = MetroStation()
    outingbox_metrostation_17.title = 'Delhi Aerocity'
    outingbox_metrostation_17.color = outingbox_metrolinecolor_6
    outingbox_metrostation_17.save()

    outingbox_metrostation_18 = MetroStation()
    outingbox_metrostation_18.title = 'Dhaula Kuan'
    outingbox_metrostation_18.color = outingbox_metrolinecolor_6
    outingbox_metrostation_18.save()

    outingbox_metrostation_19 = MetroStation()
    outingbox_metrostation_19.title = 'Dilshad Garden'
    outingbox_metrostation_19.color = outingbox_metrolinecolor_2
    outingbox_metrostation_19.save()

    outingbox_metrostation_20 = MetroStation()
    outingbox_metrostation_20.title = 'Dwarka'
    outingbox_metrostation_20.color = outingbox_metrolinecolor_4
    outingbox_metrostation_20.save()

    outingbox_metrostation_21 = MetroStation()
    outingbox_metrostation_21.title = 'Dwarka Morh'
    outingbox_metrostation_21.color = outingbox_metrolinecolor_4
    outingbox_metrostation_21.save()

    outingbox_metrostation_22 = MetroStation()
    outingbox_metrostation_22.title = 'Dwarka Sector 10'
    outingbox_metrostation_22.color = outingbox_metrolinecolor_4
    outingbox_metrostation_22.save()

    outingbox_metrostation_23 = MetroStation()
    outingbox_metrostation_23.title = 'Dwarka Sector 11'
    outingbox_metrostation_23.color = outingbox_metrolinecolor_4
    outingbox_metrostation_23.save()

    outingbox_metrostation_24 = MetroStation()
    outingbox_metrostation_24.title = 'Dwarka Sector 12'
    outingbox_metrostation_24.color = outingbox_metrolinecolor_4
    outingbox_metrostation_24.save()

    outingbox_metrostation_25 = MetroStation()
    outingbox_metrostation_25.title = 'Dwarka Sector 13'
    outingbox_metrostation_25.color = outingbox_metrolinecolor_4
    outingbox_metrostation_25.save()

    outingbox_metrostation_26 = MetroStation()
    outingbox_metrostation_26.title = 'Dwarka Sector 14'
    outingbox_metrostation_26.color = outingbox_metrolinecolor_4
    outingbox_metrostation_26.save()

    outingbox_metrostation_27 = MetroStation()
    outingbox_metrostation_27.title = 'Dwarka Sector 21'
    outingbox_metrostation_27.color = outingbox_metrolinecolor_4
    outingbox_metrostation_27.save()

    outingbox_metrostation_28 = MetroStation()
    outingbox_metrostation_28.title = 'Dwarka Sector 8'
    outingbox_metrostation_28.color = outingbox_metrolinecolor_4
    outingbox_metrostation_28.save()

    outingbox_metrostation_29 = MetroStation()
    outingbox_metrostation_29.title = 'Dwarka Sector 9'
    outingbox_metrostation_29.color = outingbox_metrolinecolor_4
    outingbox_metrostation_29.save()

    outingbox_metrostation_30 = MetroStation()
    outingbox_metrostation_30.title = 'Ghitorni'
    outingbox_metrostation_30.color = outingbox_metrolinecolor_3
    outingbox_metrostation_30.save()

    outingbox_metrostation_31 = MetroStation()
    outingbox_metrostation_31.title = 'Govind Puri'
    outingbox_metrostation_31.color = outingbox_metrolinecolor_5
    outingbox_metrostation_31.save()

    outingbox_metrostation_32 = MetroStation()
    outingbox_metrostation_32.title = 'Green Park'
    outingbox_metrostation_32.color = outingbox_metrolinecolor_3
    outingbox_metrostation_32.save()

    outingbox_metrostation_33 = MetroStation()
    outingbox_metrostation_33.title = 'GTB Nagar'
    outingbox_metrostation_33.color = outingbox_metrolinecolor_3
    outingbox_metrostation_33.save()

    outingbox_metrostation_34 = MetroStation()
    outingbox_metrostation_34.title = 'Guru Dronacharya'
    outingbox_metrostation_34.color = outingbox_metrolinecolor_3
    outingbox_metrostation_34.save()

    outingbox_metrostation_35 = MetroStation()
    outingbox_metrostation_35.title = 'Hauz Khas'
    outingbox_metrostation_35.color = outingbox_metrolinecolor_3
    outingbox_metrostation_35.save()

    outingbox_metrostation_36 = MetroStation()
    outingbox_metrostation_36.title = 'HUDA City Centre'
    outingbox_metrostation_36.color = outingbox_metrolinecolor_3
    outingbox_metrostation_36.save()

    outingbox_metrostation_37 = MetroStation()
    outingbox_metrostation_37.title = 'IFFCO Chowk'
    outingbox_metrostation_37.color = outingbox_metrolinecolor_3
    outingbox_metrostation_37.save()

    outingbox_metrostation_38 = MetroStation()
    outingbox_metrostation_38.title = 'INA'
    outingbox_metrostation_38.color = outingbox_metrolinecolor_3
    outingbox_metrostation_38.save()

    outingbox_metrostation_39 = MetroStation()
    outingbox_metrostation_39.title = 'Inderlok'
    outingbox_metrostation_39.color = outingbox_metrolinecolor_2
    outingbox_metrostation_39.save()

    outingbox_metrostation_40 = MetroStation()
    outingbox_metrostation_40.title = 'Indira Gandhi International Airport'
    outingbox_metrostation_40.color = outingbox_metrolinecolor_6
    outingbox_metrostation_40.save()

    outingbox_metrostation_41 = MetroStation()
    outingbox_metrostation_41.title = 'Indraprastha'
    outingbox_metrostation_41.color = outingbox_metrolinecolor_4
    outingbox_metrostation_41.save()

    outingbox_metrostation_42 = MetroStation()
    outingbox_metrostation_42.title = 'Jahangirpuri'
    outingbox_metrostation_42.color = outingbox_metrolinecolor_3
    outingbox_metrostation_42.save()

    outingbox_metrostation_43 = MetroStation()
    outingbox_metrostation_43.title = 'Janakpuri East'
    outingbox_metrostation_43.color = outingbox_metrolinecolor_4
    outingbox_metrostation_43.save()

    outingbox_metrostation_44 = MetroStation()
    outingbox_metrostation_44.title = 'Janakpuri West'
    outingbox_metrostation_44.color = outingbox_metrolinecolor_4
    outingbox_metrostation_44.save()

    outingbox_metrostation_45 = MetroStation()
    outingbox_metrostation_45.title = 'Jangpura'
    outingbox_metrostation_45.color = outingbox_metrolinecolor_5
    outingbox_metrostation_45.save()

    outingbox_metrostation_46 = MetroStation()
    outingbox_metrostation_46.title = 'Jasola Apollo'
    outingbox_metrostation_46.color = outingbox_metrolinecolor_5
    outingbox_metrostation_46.save()

    outingbox_metrostation_47 = MetroStation()
    outingbox_metrostation_47.title = 'Jawaharlal Nehru Stadium'
    outingbox_metrostation_47.color = outingbox_metrolinecolor_5
    outingbox_metrostation_47.save()

    outingbox_metrostation_48 = MetroStation()
    outingbox_metrostation_48.title = 'Jhandewalan'
    outingbox_metrostation_48.color = outingbox_metrolinecolor_4
    outingbox_metrostation_48.save()

    outingbox_metrostation_49 = MetroStation()
    outingbox_metrostation_49.title = 'Jhilmil'
    outingbox_metrostation_49.color = outingbox_metrolinecolor_2
    outingbox_metrostation_49.save()

    outingbox_metrostation_50 = MetroStation()
    outingbox_metrostation_50.title = 'Jor Bagh'
    outingbox_metrostation_50.color = outingbox_metrolinecolor_3
    outingbox_metrostation_50.save()

    outingbox_metrostation_51 = MetroStation()
    outingbox_metrostation_51.title = 'Kailash Colony'
    outingbox_metrostation_51.color = outingbox_metrolinecolor_5
    outingbox_metrostation_51.save()

    outingbox_metrostation_52 = MetroStation()
    outingbox_metrostation_52.title = 'Kalkaji Mandir'
    outingbox_metrostation_52.color = outingbox_metrolinecolor_5
    outingbox_metrostation_52.save()

    outingbox_metrostation_53 = MetroStation()
    outingbox_metrostation_53.title = 'Kanhiya Nagar'
    outingbox_metrostation_53.color = outingbox_metrolinecolor_2
    outingbox_metrostation_53.save()

    outingbox_metrostation_54 = MetroStation()
    outingbox_metrostation_54.title = 'Karkarduma'
    outingbox_metrostation_54.color = outingbox_metrolinecolor_4
    outingbox_metrostation_54.save()

    outingbox_metrostation_55 = MetroStation()
    outingbox_metrostation_55.title = 'Karol Bagh'
    outingbox_metrostation_55.color = outingbox_metrolinecolor_4
    outingbox_metrostation_55.save()

    outingbox_metrostation_56 = MetroStation()
    outingbox_metrostation_56.title = 'Kashmere Gate'
    outingbox_metrostation_56.color = outingbox_metrolinecolor_2
    outingbox_metrostation_56.save()

    outingbox_metrostation_57 = MetroStation()
    outingbox_metrostation_57.title = 'Kaushambi'
    outingbox_metrostation_57.color = outingbox_metrolinecolor_4
    outingbox_metrostation_57.save()

    outingbox_metrostation_58 = MetroStation()
    outingbox_metrostation_58.title = 'Keshav Puram'
    outingbox_metrostation_58.color = outingbox_metrolinecolor_2
    outingbox_metrostation_58.save()

    outingbox_metrostation_59 = MetroStation()
    outingbox_metrostation_59.title = 'Khan Market'
    outingbox_metrostation_59.color = outingbox_metrolinecolor_5
    outingbox_metrostation_59.save()

    outingbox_metrostation_60 = MetroStation()
    outingbox_metrostation_60.title = 'Kirti Nagar'
    outingbox_metrostation_60.color = outingbox_metrolinecolor_4
    outingbox_metrostation_60.save()

    outingbox_metrostation_61 = MetroStation()
    outingbox_metrostation_61.title = 'Kohat Enclave'
    outingbox_metrostation_61.color = outingbox_metrolinecolor_2
    outingbox_metrostation_61.save()

    outingbox_metrostation_62 = MetroStation()
    outingbox_metrostation_62.title = 'Lajpat Nagar'
    outingbox_metrostation_62.color = outingbox_metrolinecolor_5
    outingbox_metrostation_62.save()

    outingbox_metrostation_63 = MetroStation()
    outingbox_metrostation_63.title = 'Laxmi Nagar'
    outingbox_metrostation_63.color = outingbox_metrolinecolor_4
    outingbox_metrostation_63.save()

    outingbox_metrostation_64 = MetroStation()
    outingbox_metrostation_64.title = 'Madipur'
    outingbox_metrostation_64.color = outingbox_metrolinecolor_1
    outingbox_metrostation_64.save()

    outingbox_metrostation_65 = MetroStation()
    outingbox_metrostation_65.title = 'Malviya Nagar'
    outingbox_metrostation_65.color = outingbox_metrolinecolor_3
    outingbox_metrostation_65.save()

    outingbox_metrostation_66 = MetroStation()
    outingbox_metrostation_66.title = 'Mandi House'
    outingbox_metrostation_66.color = outingbox_metrolinecolor_4
    outingbox_metrostation_66.save()

    outingbox_metrostation_67 = MetroStation()
    outingbox_metrostation_67.title = 'Mansarovar Park'
    outingbox_metrostation_67.color = outingbox_metrolinecolor_2
    outingbox_metrostation_67.save()

    outingbox_metrostation_68 = MetroStation()
    outingbox_metrostation_68.title = 'Mayur Vihar -I'
    outingbox_metrostation_68.color = outingbox_metrolinecolor_4
    outingbox_metrostation_68.save()

    outingbox_metrostation_69 = MetroStation()
    outingbox_metrostation_69.title = 'Mayur Vihar Extension'
    outingbox_metrostation_69.color = outingbox_metrolinecolor_4
    outingbox_metrostation_69.save()

    outingbox_metrostation_70 = MetroStation()
    outingbox_metrostation_70.title = 'MG Road'
    outingbox_metrostation_70.color = outingbox_metrolinecolor_3
    outingbox_metrostation_70.save()

    outingbox_metrostation_71 = MetroStation()
    outingbox_metrostation_71.title = 'Model Town'
    outingbox_metrostation_71.color = outingbox_metrolinecolor_3
    outingbox_metrostation_71.save()

    outingbox_metrostation_72 = MetroStation()
    outingbox_metrostation_72.title = 'Mohan Estate'
    outingbox_metrostation_72.color = outingbox_metrolinecolor_5
    outingbox_metrostation_72.save()

    outingbox_metrostation_73 = MetroStation()
    outingbox_metrostation_73.title = 'Moolchand'
    outingbox_metrostation_73.color = outingbox_metrolinecolor_5
    outingbox_metrostation_73.save()

    outingbox_metrostation_74 = MetroStation()
    outingbox_metrostation_74.title = 'Moti Nagar'
    outingbox_metrostation_74.color = outingbox_metrolinecolor_4
    outingbox_metrostation_74.save()

    outingbox_metrostation_75 = MetroStation()
    outingbox_metrostation_75.title = 'Mundka'
    outingbox_metrostation_75.color = outingbox_metrolinecolor_1
    outingbox_metrostation_75.save()

    outingbox_metrostation_76 = MetroStation()
    outingbox_metrostation_76.title = 'Nangloi'
    outingbox_metrostation_76.color = outingbox_metrolinecolor_1
    outingbox_metrostation_76.save()

    outingbox_metrostation_77 = MetroStation()
    outingbox_metrostation_77.title = 'Nangloi Railway station'
    outingbox_metrostation_77.color = outingbox_metrolinecolor_1
    outingbox_metrostation_77.save()

    outingbox_metrostation_78 = MetroStation()
    outingbox_metrostation_78.title = 'Nawada'
    outingbox_metrostation_78.color = outingbox_metrolinecolor_4
    outingbox_metrostation_78.save()

    outingbox_metrostation_79 = MetroStation()
    outingbox_metrostation_79.title = 'Nehru Place'
    outingbox_metrostation_79.color = outingbox_metrolinecolor_5
    outingbox_metrostation_79.save()

    outingbox_metrostation_80 = MetroStation()
    outingbox_metrostation_80.title = 'Netaji Subhash Place'
    outingbox_metrostation_80.color = outingbox_metrolinecolor_2
    outingbox_metrostation_80.save()

    outingbox_metrostation_81 = MetroStation()
    outingbox_metrostation_81.title = 'New Ashok Nagar'
    outingbox_metrostation_81.color = outingbox_metrolinecolor_4
    outingbox_metrostation_81.save()

    outingbox_metrostation_82 = MetroStation()
    outingbox_metrostation_82.title = 'New Delhi'
    outingbox_metrostation_82.color = outingbox_metrolinecolor_3
    outingbox_metrostation_82.save()

    outingbox_metrostation_83 = MetroStation()
    outingbox_metrostation_83.title = 'Nirman Vihar'
    outingbox_metrostation_83.color = outingbox_metrolinecolor_4
    outingbox_metrostation_83.save()

    outingbox_metrostation_84 = MetroStation()
    outingbox_metrostation_84.title = 'Noida City Centre'
    outingbox_metrostation_84.color = outingbox_metrolinecolor_4
    outingbox_metrostation_84.save()

    outingbox_metrostation_85 = MetroStation()
    outingbox_metrostation_85.title = 'Noida Golf Course'
    outingbox_metrostation_85.color = outingbox_metrolinecolor_4
    outingbox_metrostation_85.save()

    outingbox_metrostation_86 = MetroStation()
    outingbox_metrostation_86.title = 'Noida Sector 15'
    outingbox_metrostation_86.color = outingbox_metrolinecolor_4
    outingbox_metrostation_86.save()

    outingbox_metrostation_87 = MetroStation()
    outingbox_metrostation_87.title = 'Noida Sector 16'
    outingbox_metrostation_87.color = outingbox_metrolinecolor_4
    outingbox_metrostation_87.save()

    outingbox_metrostation_88 = MetroStation()
    outingbox_metrostation_88.title = 'Noida Sector 18'
    outingbox_metrostation_88.color = outingbox_metrolinecolor_4
    outingbox_metrostation_88.save()

    outingbox_metrostation_89 = MetroStation()
    outingbox_metrostation_89.title = 'Okhla'
    outingbox_metrostation_89.color = outingbox_metrolinecolor_5
    outingbox_metrostation_89.save()

    outingbox_metrostation_90 = MetroStation()
    outingbox_metrostation_90.title = 'Paschim Vihar East'
    outingbox_metrostation_90.color = outingbox_metrolinecolor_1
    outingbox_metrostation_90.save()

    outingbox_metrostation_91 = MetroStation()
    outingbox_metrostation_91.title = 'Paschim Vihar West'
    outingbox_metrostation_91.color = outingbox_metrolinecolor_1
    outingbox_metrostation_91.save()

    outingbox_metrostation_92 = MetroStation()
    outingbox_metrostation_92.title = 'Patel Chowk'
    outingbox_metrostation_92.color = outingbox_metrolinecolor_3
    outingbox_metrostation_92.save()

    outingbox_metrostation_93 = MetroStation()
    outingbox_metrostation_93.title = 'Patel Nagar'
    outingbox_metrostation_93.color = outingbox_metrolinecolor_4
    outingbox_metrostation_93.save()

    outingbox_metrostation_94 = MetroStation()
    outingbox_metrostation_94.title = 'Peera Garhi'
    outingbox_metrostation_94.color = outingbox_metrolinecolor_1
    outingbox_metrostation_94.save()

    outingbox_metrostation_95 = MetroStation()
    outingbox_metrostation_95.title = 'Pitam Pura'
    outingbox_metrostation_95.color = outingbox_metrolinecolor_2
    outingbox_metrostation_95.save()

    outingbox_metrostation_96 = MetroStation()
    outingbox_metrostation_96.title = 'Pragati Maidan'
    outingbox_metrostation_96.color = outingbox_metrolinecolor_4
    outingbox_metrostation_96.save()

    outingbox_metrostation_97 = MetroStation()
    outingbox_metrostation_97.title = 'Pratap Nagar'
    outingbox_metrostation_97.color = outingbox_metrolinecolor_2
    outingbox_metrostation_97.save()

    outingbox_metrostation_98 = MetroStation()
    outingbox_metrostation_98.title = 'Preet Vihar'
    outingbox_metrostation_98.color = outingbox_metrolinecolor_4
    outingbox_metrostation_98.save()

    outingbox_metrostation_99 = MetroStation()
    outingbox_metrostation_99.title = 'Pul Bangash'
    outingbox_metrostation_99.color = outingbox_metrolinecolor_2
    outingbox_metrostation_99.save()

    outingbox_metrostation_100 = MetroStation()
    outingbox_metrostation_100.title = 'Punjabi Bagh East'
    outingbox_metrostation_100.color = outingbox_metrolinecolor_1
    outingbox_metrostation_100.save()

    outingbox_metrostation_101 = MetroStation()
    outingbox_metrostation_101.title = 'Qutab Minar'
    outingbox_metrostation_101.color = outingbox_metrolinecolor_3
    outingbox_metrostation_101.save()

    outingbox_metrostation_102 = MetroStation()
    outingbox_metrostation_102.title = 'Race Course'
    outingbox_metrostation_102.color = outingbox_metrolinecolor_3
    outingbox_metrostation_102.save()

    outingbox_metrostation_103 = MetroStation()
    outingbox_metrostation_103.title = 'Rajdhani Park'
    outingbox_metrostation_103.color = outingbox_metrolinecolor_1
    outingbox_metrostation_103.save()

    outingbox_metrostation_104 = MetroStation()
    outingbox_metrostation_104.title = 'Rajendra Place'
    outingbox_metrostation_104.color = outingbox_metrolinecolor_4
    outingbox_metrostation_104.save()

    outingbox_metrostation_105 = MetroStation()
    outingbox_metrostation_105.title = 'Rajiv Chowk'
    outingbox_metrostation_105.color = outingbox_metrolinecolor_3
    outingbox_metrostation_105.save()

    outingbox_metrostation_106 = MetroStation()
    outingbox_metrostation_106.title = 'Rajouri Garden'
    outingbox_metrostation_106.color = outingbox_metrolinecolor_4
    outingbox_metrostation_106.save()

    outingbox_metrostation_107 = MetroStation()
    outingbox_metrostation_107.title = 'Ramakrishna Ashram Marg'
    outingbox_metrostation_107.color = outingbox_metrolinecolor_4
    outingbox_metrostation_107.save()

    outingbox_metrostation_108 = MetroStation()
    outingbox_metrostation_108.title = 'Ramesh Nagar'
    outingbox_metrostation_108.color = outingbox_metrolinecolor_4
    outingbox_metrostation_108.save()

    outingbox_metrostation_109 = MetroStation()
    outingbox_metrostation_109.title = 'Rithala'
    outingbox_metrostation_109.color = outingbox_metrolinecolor_2
    outingbox_metrostation_109.save()

    outingbox_metrostation_110 = MetroStation()
    outingbox_metrostation_110.title = 'Rohini East'
    outingbox_metrostation_110.color = outingbox_metrolinecolor_2
    outingbox_metrostation_110.save()

    outingbox_metrostation_111 = MetroStation()
    outingbox_metrostation_111.title = 'Rohini West'
    outingbox_metrostation_111.color = outingbox_metrolinecolor_2
    outingbox_metrostation_111.save()

    outingbox_metrostation_112 = MetroStation()
    outingbox_metrostation_112.title = 'Saket'
    outingbox_metrostation_112.color = outingbox_metrolinecolor_3
    outingbox_metrostation_112.save()

    outingbox_metrostation_113 = MetroStation()
    outingbox_metrostation_113.title = 'Sarita Vihar'
    outingbox_metrostation_113.color = outingbox_metrolinecolor_5
    outingbox_metrostation_113.save()

    outingbox_metrostation_114 = MetroStation()
    outingbox_metrostation_114.title = 'Satguru Ramsingh Marg'
    outingbox_metrostation_114.color = outingbox_metrolinecolor_1
    outingbox_metrostation_114.save()

    outingbox_metrostation_115 = MetroStation()
    outingbox_metrostation_115.title = 'Seelampur'
    outingbox_metrostation_115.color = outingbox_metrolinecolor_2
    outingbox_metrostation_115.save()

    outingbox_metrostation_116 = MetroStation()
    outingbox_metrostation_116.title = 'Shadipur'
    outingbox_metrostation_116.color = outingbox_metrolinecolor_4
    outingbox_metrostation_116.save()

    outingbox_metrostation_117 = MetroStation()
    outingbox_metrostation_117.title = 'Shahdara'
    outingbox_metrostation_117.color = outingbox_metrolinecolor_2
    outingbox_metrostation_117.save()

    outingbox_metrostation_118 = MetroStation()
    outingbox_metrostation_118.title = 'Shastri Nagar'
    outingbox_metrostation_118.color = outingbox_metrolinecolor_2
    outingbox_metrostation_118.save()

    outingbox_metrostation_119 = MetroStation()
    outingbox_metrostation_119.title = 'Shastri Park'
    outingbox_metrostation_119.color = outingbox_metrolinecolor_2
    outingbox_metrostation_119.save()

    outingbox_metrostation_120 = MetroStation()
    outingbox_metrostation_120.title = 'Shivaji Park'
    outingbox_metrostation_120.color = outingbox_metrolinecolor_1
    outingbox_metrostation_120.save()

    outingbox_metrostation_121 = MetroStation()
    outingbox_metrostation_121.title = 'Shivaji Stadium'
    outingbox_metrostation_121.color = outingbox_metrolinecolor_6
    outingbox_metrostation_121.save()

    outingbox_metrostation_122 = MetroStation()
    outingbox_metrostation_122.title = 'Sikandarpur'
    outingbox_metrostation_122.color = outingbox_metrolinecolor_3
    outingbox_metrostation_122.save()

    outingbox_metrostation_123 = MetroStation()
    outingbox_metrostation_123.title = 'Subhash Nagar'
    outingbox_metrostation_123.color = outingbox_metrolinecolor_4
    outingbox_metrostation_123.save()

    outingbox_metrostation_124 = MetroStation()
    outingbox_metrostation_124.title = 'Sultanpur'
    outingbox_metrostation_124.color = outingbox_metrolinecolor_3
    outingbox_metrostation_124.save()

    outingbox_metrostation_125 = MetroStation()
    outingbox_metrostation_125.title = 'Surajmal Stadium'
    outingbox_metrostation_125.color = outingbox_metrolinecolor_1
    outingbox_metrostation_125.save()

    outingbox_metrostation_126 = MetroStation()
    outingbox_metrostation_126.title = 'Tagore Garden'
    outingbox_metrostation_126.color = outingbox_metrolinecolor_4
    outingbox_metrostation_126.save()

    outingbox_metrostation_127 = MetroStation()
    outingbox_metrostation_127.title = 'Tilak Nagar'
    outingbox_metrostation_127.color = outingbox_metrolinecolor_4
    outingbox_metrostation_127.save()

    outingbox_metrostation_128 = MetroStation()
    outingbox_metrostation_128.title = 'Tis Hazari'
    outingbox_metrostation_128.color = outingbox_metrolinecolor_2
    outingbox_metrostation_128.save()

    outingbox_metrostation_129 = MetroStation()
    outingbox_metrostation_129.title = 'Tughlakabad'
    outingbox_metrostation_129.color = outingbox_metrolinecolor_5
    outingbox_metrostation_129.save()

    outingbox_metrostation_130 = MetroStation()
    outingbox_metrostation_130.title = 'Udyog Bhawan'
    outingbox_metrostation_130.color = outingbox_metrolinecolor_3
    outingbox_metrostation_130.save()

    outingbox_metrostation_131 = MetroStation()
    outingbox_metrostation_131.title = 'Udyog Nagar'
    outingbox_metrostation_131.color = outingbox_metrolinecolor_1
    outingbox_metrostation_131.save()

    outingbox_metrostation_132 = MetroStation()
    outingbox_metrostation_132.title = 'Uttam Nagar East'
    outingbox_metrostation_132.color = outingbox_metrolinecolor_4
    outingbox_metrostation_132.save()

    outingbox_metrostation_133 = MetroStation()
    outingbox_metrostation_133.title = 'Uttam Nagar West'
    outingbox_metrostation_133.color = outingbox_metrolinecolor_4
    outingbox_metrostation_133.save()

    outingbox_metrostation_134 = MetroStation()
    outingbox_metrostation_134.title = 'Vaishali'
    outingbox_metrostation_134.color = outingbox_metrolinecolor_4
    outingbox_metrostation_134.save()

    outingbox_metrostation_135 = MetroStation()
    outingbox_metrostation_135.title = 'Vidhan Sabha'
    outingbox_metrostation_135.color = outingbox_metrolinecolor_3
    outingbox_metrostation_135.save()

    outingbox_metrostation_136 = MetroStation()
    outingbox_metrostation_136.title = 'Vishwa Vidyalaya'
    outingbox_metrostation_136.color = outingbox_metrolinecolor_3
    outingbox_metrostation_136.save()

    outingbox_metrostation_137 = MetroStation()
    outingbox_metrostation_137.title = 'Welcome'
    outingbox_metrostation_137.color = outingbox_metrolinecolor_2
    outingbox_metrostation_137.save()

    outingbox_metrostation_138 = MetroStation()
    outingbox_metrostation_138.title = 'Yamuna Bank'
    outingbox_metrostation_138.color = outingbox_metrolinecolor_4
    outingbox_metrostation_138.save()

    outingbox_metrostation_139 = MetroStation()
    outingbox_metrostation_139.title = 'Akshardham'
    outingbox_metrostation_139.color = outingbox_metrolinecolor_4
    outingbox_metrostation_139.save()

    # Processing model: Address

    from outingbox.models import Address

    outingbox_address_1 = Address()
    outingbox_address_1.title = 'Worlds of Wonder'
    outingbox_address_1.address_line1 = 'Sector 38, Noida, Uttar Pradesh '
    outingbox_address_1.address_line2 = ''
    outingbox_address_1.zone = outingbox_zone_2
    outingbox_address_1.pin_code = 201301
    outingbox_address_1.map_address = ''
    outingbox_address_1.location = ''
    outingbox_address_1.save()

    outingbox_address_1.sub_zone.add(outingbox_subzone_21)
    outingbox_address_1.sub_zone.add(outingbox_subzone_22)
    outingbox_address_1.metro_station.add(outingbox_metrostation_88)

    outingbox_address_2 = Address()
    outingbox_address_2.title = 'City Bowl'
    outingbox_address_2.address_line1 = '14/5, Mahindra Sterling Compound, Mathura Road, Faridabad'
    outingbox_address_2.address_line2 = ''
    outingbox_address_2.zone = outingbox_zone_2
    outingbox_address_2.pin_code = 121003
    outingbox_address_2.map_address = ''
    outingbox_address_2.location = None
    outingbox_address_2.save()

    outingbox_address_2.sub_zone.add(outingbox_subzone_36)

    outingbox_address_3 = Address()
    outingbox_address_3.title = 'Art Alive Gallery'
    outingbox_address_3.address_line1 = 'S-221 Panchsheel Park, New Delhi'
    outingbox_address_3.address_line2 = ''
    outingbox_address_3.zone = outingbox_zone_2
    outingbox_address_3.pin_code = 110017
    outingbox_address_3.map_address = ''
    outingbox_address_3.location = '28.542863,77.215889'
    outingbox_address_3.save()

    outingbox_address_3.sub_zone.add(outingbox_subzone_9)
    outingbox_address_3.sub_zone.add(outingbox_subzone_68)
    outingbox_address_3.sub_zone.add(outingbox_subzone_81)
    outingbox_address_3.metro_station.add(outingbox_metrostation_35)

    outingbox_address_4 = Address()
    outingbox_address_4.title = 'Dhoomimal Art Centre'
    outingbox_address_4.address_line1 = 'A8, Connanught Place, New Delhi'
    outingbox_address_4.address_line2 = ''
    outingbox_address_4.zone = outingbox_zone_2
    outingbox_address_4.pin_code = 110001
    outingbox_address_4.map_address = ''
    outingbox_address_4.location = '28.632732,77.217847'
    outingbox_address_4.save()

    outingbox_address_4.sub_zone.add(outingbox_subzone_52)
    outingbox_address_4.sub_zone.add(outingbox_subzone_53)
    outingbox_address_4.sub_zone.add(outingbox_subzone_54)
    outingbox_address_4.sub_zone.add(outingbox_subzone_81)
    outingbox_address_4.metro_station.add(outingbox_metrostation_105)

    outingbox_address_5 = Address()
    outingbox_address_5.title = 'Yogakul'
    outingbox_address_5.address_line1 = '110, First Floor, Shahpur Jat, Siri Fort, New Delhi,India'
    outingbox_address_5.address_line2 = ''
    outingbox_address_5.zone = outingbox_zone_2
    outingbox_address_5.pin_code = 110049
    outingbox_address_5.map_address = ''
    outingbox_address_5.location = '28.548664,77.214060'
    outingbox_address_5.save()

    outingbox_address_5.sub_zone.add(outingbox_subzone_9)
    outingbox_address_5.sub_zone.add(outingbox_subzone_63)
    outingbox_address_5.sub_zone.add(outingbox_subzone_81)
    outingbox_address_5.metro_station.add(outingbox_metrostation_32)

    outingbox_address_6 = Address()
    outingbox_address_6.title = 'Club Platinum Resort'
    outingbox_address_6.address_line1 = 'Assaudha Mod,Delhi-Rohtak Road,Bahadurgarh,Haryana'
    outingbox_address_6.address_line2 = ''
    outingbox_address_6.zone = outingbox_zone_2
    outingbox_address_6.pin_code = 124505
    outingbox_address_6.map_address = ''
    outingbox_address_6.location = ''
    outingbox_address_6.save()

    outingbox_address_6.sub_zone.add(outingbox_subzone_26)
    outingbox_address_6.sub_zone.add(outingbox_subzone_33)
    outingbox_address_6.sub_zone.add(outingbox_subzone_83)
    outingbox_address_6.metro_station.add(outingbox_metrostation_70)
    outingbox_address_6.metro_station.add(outingbox_metrostation_75)

    outingbox_address_7 = Address()
    outingbox_address_7.title = 'Navdha Yoga Center'
    outingbox_address_7.address_line1 = 'L-76, Malviya Nagar, New Delhi, Delhi '
    outingbox_address_7.address_line2 = ''
    outingbox_address_7.zone = outingbox_zone_2
    outingbox_address_7.pin_code = 110017
    outingbox_address_7.map_address = ''
    outingbox_address_7.location = '28.531865,77.208166'
    outingbox_address_7.save()

    outingbox_address_7.sub_zone.add(outingbox_subzone_9)
    outingbox_address_7.sub_zone.add(outingbox_subzone_65)
    outingbox_address_7.sub_zone.add(outingbox_subzone_81)
    outingbox_address_7.metro_station.add(outingbox_metrostation_65)

    outingbox_address_8 = Address()
    outingbox_address_8.title = 'iSkate'
    outingbox_address_8.address_line1 = '6th Floor, Ambience Mall, National Highway 8, Ambience Island, DLF Phase 3, Sector 24 Gurgaon, Haryana '
    outingbox_address_8.address_line2 = ''
    outingbox_address_8.zone = outingbox_zone_2
    outingbox_address_8.pin_code = 122002
    outingbox_address_8.map_address = ''
    outingbox_address_8.location = '28.503812,77.097349'
    outingbox_address_8.save()

    outingbox_address_8.sub_zone.add(outingbox_subzone_28)
    outingbox_address_8.sub_zone.add(outingbox_subzone_66)
    outingbox_address_8.sub_zone.add(outingbox_subzone_67)
    outingbox_address_8.metro_station.add(outingbox_metrostation_122)

    outingbox_address_9 = Address()
    outingbox_address_9.title = 'The Pilates Studio'
    outingbox_address_9.address_line1 = 'K-19 Green Park Main, New Delhi, India'
    outingbox_address_9.address_line2 = ''
    outingbox_address_9.zone = outingbox_zone_2
    outingbox_address_9.pin_code = 110016
    outingbox_address_9.map_address = ''
    outingbox_address_9.location = ''
    outingbox_address_9.save()

    outingbox_address_9.sub_zone.add(outingbox_subzone_9)
    outingbox_address_9.sub_zone.add(outingbox_subzone_64)
    outingbox_address_9.sub_zone.add(outingbox_subzone_81)
    outingbox_address_9.metro_station.add(outingbox_metrostation_32)

    outingbox_address_10 = Address()
    outingbox_address_10.title = 'Universal Yoga Group'
    outingbox_address_10.address_line1 = 'X- 22 , karkardooma, Institutional Area,lower ground floor, IP Extension Part II, Vikas Marg, Delhi '
    outingbox_address_10.address_line2 = ''
    outingbox_address_10.zone = outingbox_zone_2
    outingbox_address_10.pin_code = 110092
    outingbox_address_10.map_address = ''
    outingbox_address_10.location = '28.613939,77.209021'
    outingbox_address_10.save()

    outingbox_address_10.sub_zone.add(outingbox_subzone_5)
    outingbox_address_10.sub_zone.add(outingbox_subzone_62)
    outingbox_address_10.sub_zone.add(outingbox_subzone_81)
    outingbox_address_10.metro_station.add(outingbox_metrostation_116)

    outingbox_address_11 = Address()
    outingbox_address_11.title = 'DelhiRides'
    outingbox_address_11.address_line1 = 'Kalindi Kunj Road, Kalindi Kunj Park, Okhla, New Delhi'
    outingbox_address_11.address_line2 = ''
    outingbox_address_11.zone = outingbox_zone_2
    outingbox_address_11.pin_code = 110025
    outingbox_address_11.map_address = ''
    outingbox_address_11.location = '28.545555,77.309635'
    outingbox_address_11.save()

    outingbox_address_11.sub_zone.add(outingbox_subzone_9)
    outingbox_address_11.sub_zone.add(outingbox_subzone_19)
    outingbox_address_11.sub_zone.add(outingbox_subzone_20)
    outingbox_address_11.sub_zone.add(outingbox_subzone_81)
    outingbox_address_11.metro_station.add(outingbox_metrostation_89)

    outingbox_address_12 = Address()
    outingbox_address_12.title = 'Sivananda Yoga '
    outingbox_address_12.address_line1 = 'Sivananda Yoga, Vedanta Nataraja Centre,  A - 41, Kailash Colony,  New Delhi '
    outingbox_address_12.address_line2 = ''
    outingbox_address_12.zone = outingbox_zone_2
    outingbox_address_12.pin_code = 110048
    outingbox_address_12.map_address = ''
    outingbox_address_12.location = '28.553610,77.242764'
    outingbox_address_12.save()

    outingbox_address_12.sub_zone.add(outingbox_subzone_9)
    outingbox_address_12.sub_zone.add(outingbox_subzone_56)
    outingbox_address_12.sub_zone.add(outingbox_subzone_81)
    outingbox_address_12.metro_station.add(outingbox_metrostation_51)

    outingbox_address_13 = Address()
    outingbox_address_13.title = 'Kedarnath Centre for Yoga and Naturopathy'
    outingbox_address_13.address_line1 = 'C 1815, Sushant Lok Phase 1,Gurgaon'
    outingbox_address_13.address_line2 = ''
    outingbox_address_13.zone = outingbox_zone_2
    outingbox_address_13.pin_code = 122001
    outingbox_address_13.map_address = ''
    outingbox_address_13.location = '28.465526,77.079122'
    outingbox_address_13.save()

    outingbox_address_13.sub_zone.add(outingbox_subzone_58)
    outingbox_address_13.sub_zone.add(outingbox_subzone_59)
    outingbox_address_13.metro_station.add(outingbox_metrostation_37)

    outingbox_address_14 = Address()
    outingbox_address_14.title = 'Universal Yoga Group'
    outingbox_address_14.address_line1 = 'D4/ 27 DLF phase 1 Gurgaon Village, Sector 6 Gurgaon'
    outingbox_address_14.address_line2 = ''
    outingbox_address_14.zone = outingbox_zone_2
    outingbox_address_14.pin_code = 122001
    outingbox_address_14.map_address = ''
    outingbox_address_14.location = '28.475262,77.025490'
    outingbox_address_14.save()

    outingbox_address_14.sub_zone.add(outingbox_subzone_8)
    outingbox_address_14.sub_zone.add(outingbox_subzone_60)
    outingbox_address_14.sub_zone.add(outingbox_subzone_61)
    outingbox_address_14.metro_station.add(outingbox_metrostation_122)

    outingbox_address_15 = Address()
    outingbox_address_15.title = 'The Yoga Studio'
    outingbox_address_15.address_line1 = ' # D-43,Hauz Khas, New Delhi, Delhi '
    outingbox_address_15.address_line2 = ''
    outingbox_address_15.zone = outingbox_zone_2
    outingbox_address_15.pin_code = 110016
    outingbox_address_15.map_address = ''
    outingbox_address_15.location = '28.550435,77.206611'
    outingbox_address_15.save()

    outingbox_address_15.sub_zone.add(outingbox_subzone_9)
    outingbox_address_15.sub_zone.add(outingbox_subzone_47)
    outingbox_address_15.sub_zone.add(outingbox_subzone_81)
    outingbox_address_15.metro_station.add(outingbox_metrostation_35)
    outingbox_address_15.metro_station.add(outingbox_metrostation_112)

    outingbox_address_16 = Address()
    outingbox_address_16.title = 'Yogakshema - Iyengar Yoga Centre'
    outingbox_address_16.address_line1 = 'Plot No.65,66,67, Deendayal Upadhyay Marg, Rouse Avenue, New Delhi '
    outingbox_address_16.address_line2 = ''
    outingbox_address_16.zone = outingbox_zone_2
    outingbox_address_16.pin_code = 110002
    outingbox_address_16.map_address = ''
    outingbox_address_16.location = '28.629935,77.236802'
    outingbox_address_16.save()

    outingbox_address_16.sub_zone.add(outingbox_subzone_52)
    outingbox_address_16.sub_zone.add(outingbox_subzone_53)
    outingbox_address_16.sub_zone.add(outingbox_subzone_54)
    outingbox_address_16.sub_zone.add(outingbox_subzone_55)
    outingbox_address_16.sub_zone.add(outingbox_subzone_81)
    outingbox_address_16.metro_station.add(outingbox_metrostation_10)
    outingbox_address_16.metro_station.add(outingbox_metrostation_66)
    outingbox_address_16.metro_station.add(outingbox_metrostation_105)

    outingbox_address_17 = Address()
    outingbox_address_17.title = 'Every Other Day (Appu Ghar Express)'
    outingbox_address_17.address_line1 = 'Building No. 105, Plot No. 2A'
    outingbox_address_17.address_line2 = 'Sector 38 A, Noida'
    outingbox_address_17.zone = outingbox_zone_1
    outingbox_address_17.pin_code = 201301
    outingbox_address_17.map_address = ' sector 38 noida'
    outingbox_address_17.location = '28.562308,77.329571'
    outingbox_address_17.save()

    outingbox_address_17.sub_zone.add(outingbox_subzone_21)
    outingbox_address_17.sub_zone.add(outingbox_subzone_22)
    outingbox_address_17.sub_zone.add(outingbox_subzone_40)
    outingbox_address_17.metro_station.add(outingbox_metrostation_88)

    outingbox_address_18 = Address()
    outingbox_address_18.title = 'The Mind Cafe'
    outingbox_address_18.address_line1 = '2nd Floor, Cross Point,  Opp. Galleria Market, DLF Phase 4, Gurgaon (HR)'
    outingbox_address_18.address_line2 = ''
    outingbox_address_18.zone = outingbox_zone_2
    outingbox_address_18.pin_code = 122002
    outingbox_address_18.map_address = ''
    outingbox_address_18.location = '28.468281,77.083210'
    outingbox_address_18.save()

    outingbox_address_18.sub_zone.add(outingbox_subzone_8)
    outingbox_address_18.sub_zone.add(outingbox_subzone_51)
    outingbox_address_18.metro_station.add(outingbox_metrostation_36)

    outingbox_address_19 = Address()
    outingbox_address_19.title = 'Arnos Den'
    outingbox_address_19.address_line1 = 'Pacific Mall, Subhash Nagar     '
    outingbox_address_19.address_line2 = ''
    outingbox_address_19.zone = outingbox_zone_2
    outingbox_address_19.pin_code = 110027
    outingbox_address_19.map_address = ''
    outingbox_address_19.location = '18.501079,73.872429'
    outingbox_address_19.save()

    outingbox_address_19.sub_zone.add(outingbox_subzone_38)
    outingbox_address_19.sub_zone.add(outingbox_subzone_81)
    outingbox_address_19.metro_station.add(outingbox_metrostation_123)

    outingbox_address_20 = Address()
    outingbox_address_20.title = 'Fun Zone'
    outingbox_address_20.address_line1 = 'City Mall, Sector 12 Faridabad  '
    outingbox_address_20.address_line2 = ''
    outingbox_address_20.zone = outingbox_zone_2
    outingbox_address_20.pin_code = 121101
    outingbox_address_20.map_address = ''
    outingbox_address_20.location = '28.570434,77.337280'
    outingbox_address_20.save()

    outingbox_address_20.sub_zone.add(outingbox_subzone_36)
    outingbox_address_20.sub_zone.add(outingbox_subzone_49)
    outingbox_address_20.metro_station.add(outingbox_metrostation_9)

    outingbox_address_21 = Address()
    outingbox_address_21.title = 'Big Dance Center'
    outingbox_address_21.address_line1 = ' 505, Ring Road Mall, Sector 3, Rohini, New Delhi'
    outingbox_address_21.address_line2 = ''
    outingbox_address_21.zone = outingbox_zone_2
    outingbox_address_21.pin_code = 110085
    outingbox_address_21.map_address = ''
    outingbox_address_21.location = '28.698277,77.116007'
    outingbox_address_21.save()

    outingbox_address_21.sub_zone.add(outingbox_subzone_14)
    outingbox_address_21.sub_zone.add(outingbox_subzone_16)
    outingbox_address_21.sub_zone.add(outingbox_subzone_24)
    outingbox_address_21.sub_zone.add(outingbox_subzone_81)
    outingbox_address_21.metro_station.add(outingbox_metrostation_111)

    outingbox_address_22 = Address()
    outingbox_address_22.title = 'Flyboy'
    outingbox_address_22.address_line1 = 'Po – Daula, Karanki, Vatika Complex, next to the Westin Sohna Resort & Spa, Sohna, Gurgaon'
    outingbox_address_22.address_line2 = ''
    outingbox_address_22.zone = outingbox_zone_2
    outingbox_address_22.pin_code = 122001
    outingbox_address_22.map_address = ''
    outingbox_address_22.location = '28.237296,77.149235'
    outingbox_address_22.save()

    outingbox_address_22.sub_zone.add(outingbox_subzone_8)
    outingbox_address_22.sub_zone.add(outingbox_subzone_50)
    outingbox_address_22.metro_station.add(outingbox_metrostation_36)

    outingbox_address_23 = Address()
    outingbox_address_23.title = 'Glued Entertainment'
    outingbox_address_23.address_line1 = 'Dynamic House, Opp Petrol Bunk, Dadri Main Road, Sector-41, Noida, Uttar Pradesh '
    outingbox_address_23.address_line2 = ''
    outingbox_address_23.zone = outingbox_zone_2
    outingbox_address_23.pin_code = 201301
    outingbox_address_23.map_address = ''
    outingbox_address_23.location = '28.561075,77.363055'
    outingbox_address_23.save()

    outingbox_address_23.sub_zone.add(outingbox_subzone_22)
    outingbox_address_23.metro_station.add(outingbox_metrostation_88)

    outingbox_address_24 = Address()
    outingbox_address_24.title = 'Planet Bowling'
    outingbox_address_24.address_line1 = 'A-38, Mohan Co-Operative Industrial Estate, Mathura Road, Badarpur,Delhi'
    outingbox_address_24.address_line2 = ''
    outingbox_address_24.zone = outingbox_zone_2
    outingbox_address_24.pin_code = 110044
    outingbox_address_24.map_address = ''
    outingbox_address_24.location = '28.469887,77.305907'
    outingbox_address_24.save()

    outingbox_address_24.sub_zone.add(outingbox_subzone_48)
    outingbox_address_24.sub_zone.add(outingbox_subzone_49)
    outingbox_address_24.metro_station.add(outingbox_metrostation_113)
    outingbox_address_24.metro_station.add(outingbox_metrostation_129)

    outingbox_address_25 = Address()
    outingbox_address_25.title = 'Fun N Fair'
    outingbox_address_25.address_line1 = 'A-38, Mohan Cooperative Industrial Estate,, Near Pind Balluchi Restaurant, Main Mathura Road,, New Delhi, Delhi '
    outingbox_address_25.address_line2 = ''
    outingbox_address_25.zone = outingbox_zone_2
    outingbox_address_25.pin_code = 110044
    outingbox_address_25.map_address = ''
    outingbox_address_25.location = '28.611238,77.240114'
    outingbox_address_25.save()

    outingbox_address_25.sub_zone.add(outingbox_subzone_48)
    outingbox_address_25.sub_zone.add(outingbox_subzone_49)
    outingbox_address_25.metro_station.add(outingbox_metrostation_113)
    outingbox_address_25.metro_station.add(outingbox_metrostation_129)

    outingbox_address_26 = Address()
    outingbox_address_26.title = 'Anandyogam'
    outingbox_address_26.address_line1 = 'House No. 1, Block- J & K Ext- 1, Lakshmi Nagar, New Delhi'
    outingbox_address_26.address_line2 = ''
    outingbox_address_26.zone = outingbox_zone_2
    outingbox_address_26.pin_code = 110092
    outingbox_address_26.map_address = ''
    outingbox_address_26.location = ''
    outingbox_address_26.save()

    outingbox_address_26.sub_zone.add(outingbox_subzone_5)
    outingbox_address_26.sub_zone.add(outingbox_subzone_57)
    outingbox_address_26.sub_zone.add(outingbox_subzone_81)
    outingbox_address_26.metro_station.add(outingbox_metrostation_63)

    outingbox_address_27 = Address()
    outingbox_address_27.title = 'Delhi Dance Academy'
    outingbox_address_27.address_line1 = 'E-238, Amar Colony, Lajpat Nagar 4, New Delhi'
    outingbox_address_27.address_line2 = ''
    outingbox_address_27.zone = outingbox_zone_2
    outingbox_address_27.pin_code = 0
    outingbox_address_27.map_address = ''
    outingbox_address_27.location = '28.561197,77.241680'
    outingbox_address_27.save()

    outingbox_address_27.sub_zone.add(outingbox_subzone_9)
    outingbox_address_27.sub_zone.add(outingbox_subzone_46)
    outingbox_address_27.sub_zone.add(outingbox_subzone_81)
    outingbox_address_27.metro_station.add(outingbox_metrostation_62)

    outingbox_address_28 = Address()
    outingbox_address_28.title = 'F.o.G - Federation of Gamers'
    outingbox_address_28.address_line1 = 'Shop No. 239&240, 1st Floor, DLF Place Mall, Saket, New Delhi'
    outingbox_address_28.address_line2 = ''
    outingbox_address_28.zone = outingbox_zone_2
    outingbox_address_28.pin_code = 110017
    outingbox_address_28.map_address = ''
    outingbox_address_28.location = '28.524579,77.206615'
    outingbox_address_28.save()

    outingbox_address_28.sub_zone.add(outingbox_subzone_9)
    outingbox_address_28.sub_zone.add(outingbox_subzone_37)
    outingbox_address_28.sub_zone.add(outingbox_subzone_81)
    outingbox_address_28.metro_station.add(outingbox_metrostation_65)

    outingbox_address_29 = Address()
    outingbox_address_29.title = 'AtreYoga Studio'
    outingbox_address_29.address_line1 = '252-A, Second floor, Nanak Bhavan, Shahpur Jat, New Delhi '
    outingbox_address_29.address_line2 = ''
    outingbox_address_29.zone = outingbox_zone_2
    outingbox_address_29.pin_code = 110049
    outingbox_address_29.map_address = ''
    outingbox_address_29.location = '28.548121,77.211445'
    outingbox_address_29.save()

    outingbox_address_29.sub_zone.add(outingbox_subzone_9)
    outingbox_address_29.sub_zone.add(outingbox_subzone_47)
    outingbox_address_29.sub_zone.add(outingbox_subzone_81)
    outingbox_address_29.metro_station.add(outingbox_metrostation_35)

    outingbox_address_30 = Address()
    outingbox_address_30.title = 'Lock n Load Paintball'
    outingbox_address_30.address_line1 = 'Pacific Mall'
    outingbox_address_30.address_line2 = 'Subhash Nagar, New Delhi'
    outingbox_address_30.zone = outingbox_zone_1
    outingbox_address_30.pin_code = 110018
    outingbox_address_30.map_address = 'rajouri garden'
    outingbox_address_30.location = '28.642207,77.106280'
    outingbox_address_30.save()

    outingbox_address_30.sub_zone.add(outingbox_subzone_1)
    outingbox_address_30.sub_zone.add(outingbox_subzone_2)
    outingbox_address_30.sub_zone.add(outingbox_subzone_38)
    outingbox_address_30.sub_zone.add(outingbox_subzone_81)
    outingbox_address_30.metro_station.add(outingbox_metrostation_123)
    outingbox_address_30.metro_station.add(outingbox_metrostation_126)
    outingbox_address_30.metro_station.add(outingbox_metrostation_127)

    outingbox_address_31 = Address()
    outingbox_address_31.title = 'Versus Gaming Zone'
    outingbox_address_31.address_line1 = '2nd Floor, Pacific Mall, Tagore Garden, New Delhi'
    outingbox_address_31.address_line2 = ''
    outingbox_address_31.zone = outingbox_zone_2
    outingbox_address_31.pin_code = 110027
    outingbox_address_31.map_address = ''
    outingbox_address_31.location = '28.643895,77.112830'
    outingbox_address_31.save()

    outingbox_address_31.sub_zone.add(outingbox_subzone_38)
    outingbox_address_31.sub_zone.add(outingbox_subzone_81)
    outingbox_address_31.metro_station.add(outingbox_metrostation_123)

    outingbox_address_32 = Address()
    outingbox_address_32.title = 'F9 Go Karting'
    outingbox_address_32.address_line1 = 'Sector 17-18 Link Road, 1.8 Kms. from IFFCO Chowk,Gurgaon'
    outingbox_address_32.address_line2 = ''
    outingbox_address_32.zone = outingbox_zone_2
    outingbox_address_32.pin_code = 122001
    outingbox_address_32.map_address = ''
    outingbox_address_32.location = '28.465067,77.507711'
    outingbox_address_32.save()

    outingbox_address_32.sub_zone.add(outingbox_subzone_8)
    outingbox_address_32.sub_zone.add(outingbox_subzone_43)
    outingbox_address_32.sub_zone.add(outingbox_subzone_44)
    outingbox_address_32.metro_station.add(outingbox_metrostation_70)

    outingbox_address_33 = Address()
    outingbox_address_33.title = 'Essex Farms Future Bowl'
    outingbox_address_33.address_line1 = '4, Aurobindo Marg, New Delhi'
    outingbox_address_33.address_line2 = ''
    outingbox_address_33.zone = outingbox_zone_2
    outingbox_address_33.pin_code = 110016
    outingbox_address_33.map_address = ''
    outingbox_address_33.location = '28.546344,77.202296'
    outingbox_address_33.save()

    outingbox_address_33.sub_zone.add(outingbox_subzone_9)
    outingbox_address_33.sub_zone.add(outingbox_subzone_47)
    outingbox_address_33.sub_zone.add(outingbox_subzone_81)
    outingbox_address_33.metro_station.add(outingbox_metrostation_65)

    outingbox_address_34 = Address()
    outingbox_address_34.title = 'Shootout Zone'
    outingbox_address_34.address_line1 = 'A- 265, Andheria Modh,Near Kishan Haat,New Delhi'
    outingbox_address_34.address_line2 = ''
    outingbox_address_34.zone = outingbox_zone_2
    outingbox_address_34.pin_code = 110074
    outingbox_address_34.map_address = ''
    outingbox_address_34.location = '28.613939,77.209021'
    outingbox_address_34.save()

    outingbox_address_34.sub_zone.add(outingbox_subzone_9)
    outingbox_address_34.sub_zone.add(outingbox_subzone_18)
    outingbox_address_34.sub_zone.add(outingbox_subzone_39)
    outingbox_address_34.sub_zone.add(outingbox_subzone_81)
    outingbox_address_34.metro_station.add(outingbox_metrostation_14)

    outingbox_address_35 = Address()
    outingbox_address_35.title = 'Wonder Speedway'
    outingbox_address_35.address_line1 = 'Worlds of Wonder, A-2, Sector-38, Noida, Uttar Pradesh '
    outingbox_address_35.address_line2 = ''
    outingbox_address_35.zone = outingbox_zone_2
    outingbox_address_35.pin_code = 201301
    outingbox_address_35.map_address = ''
    outingbox_address_35.location = '28.564066,77.325414'
    outingbox_address_35.save()

    outingbox_address_35.sub_zone.add(outingbox_subzone_21)
    outingbox_address_35.sub_zone.add(outingbox_subzone_22)
    outingbox_address_35.sub_zone.add(outingbox_subzone_40)
    outingbox_address_35.sub_zone.add(outingbox_subzone_41)
    outingbox_address_35.sub_zone.add(outingbox_subzone_42)
    outingbox_address_35.metro_station.add(outingbox_metrostation_11)
    outingbox_address_35.metro_station.add(outingbox_metrostation_88)

    outingbox_address_36 = Address()
    outingbox_address_36.title = '32nd Milestone'
    outingbox_address_36.address_line1 = 'NH. 8, Behind Sector 15, Gurgaon, Haryana 122001, India'
    outingbox_address_36.address_line2 = ''
    outingbox_address_36.zone = outingbox_zone_2
    outingbox_address_36.pin_code = 122001
    outingbox_address_36.map_address = ''
    outingbox_address_36.location = '28.458089,77.041191'
    outingbox_address_36.save()

    outingbox_address_36.sub_zone.add(outingbox_subzone_8)
    outingbox_address_36.sub_zone.add(outingbox_subzone_35)
    outingbox_address_36.sub_zone.add(outingbox_subzone_45)
    outingbox_address_36.metro_station.add(outingbox_metrostation_36)
    outingbox_address_36.metro_station.add(outingbox_metrostation_37)
    outingbox_address_36.metro_station.add(outingbox_metrostation_70)

    outingbox_address_37 = Address()
    outingbox_address_37.title = 'Adventure Island'
    outingbox_address_37.address_line1 = 'Unitech Amusement Parks Ltd. Opposite Rithala Metro Station,Sector-10, Rohini, New Delhi'
    outingbox_address_37.address_line2 = ''
    outingbox_address_37.zone = outingbox_zone_2
    outingbox_address_37.pin_code = 110085
    outingbox_address_37.map_address = ''
    outingbox_address_37.location = '28.723728,77.113592'
    outingbox_address_37.save()

    outingbox_address_37.sub_zone.add(outingbox_subzone_23)
    outingbox_address_37.sub_zone.add(outingbox_subzone_24)
    outingbox_address_37.sub_zone.add(outingbox_subzone_25)
    outingbox_address_37.sub_zone.add(outingbox_subzone_81)
    outingbox_address_37.metro_station.add(outingbox_metrostation_109)

    outingbox_address_38 = Address()
    outingbox_address_38.title = 'OYSTERS Beach Park-Appu Ghar'
    outingbox_address_38.address_line1 = 'Sector 29, Adjacent to Huda City Metro Station, Gurgaon'
    outingbox_address_38.address_line2 = ''
    outingbox_address_38.zone = outingbox_zone_2
    outingbox_address_38.pin_code = 122001
    outingbox_address_38.map_address = ''
    outingbox_address_38.location = '28.462200,77.071474'
    outingbox_address_38.save()

    outingbox_address_38.sub_zone.add(outingbox_subzone_8)
    outingbox_address_38.sub_zone.add(outingbox_subzone_17)
    outingbox_address_38.sub_zone.add(outingbox_subzone_18)
    outingbox_address_38.metro_station.add(outingbox_metrostation_36)

    outingbox_address_39 = Address()
    outingbox_address_39.title = 'Amoeba - Gurgaon'
    outingbox_address_39.address_line1 = 'M.G.F Metropolitan Mall, 2nd floor, Mehrauli Gurgaon Road'
    outingbox_address_39.address_line2 = ''
    outingbox_address_39.zone = outingbox_zone_2
    outingbox_address_39.pin_code = 122001
    outingbox_address_39.map_address = ''
    outingbox_address_39.location = '28.529568,77.220172'
    outingbox_address_39.save()

    outingbox_address_39.sub_zone.add(outingbox_subzone_8)
    outingbox_address_39.sub_zone.add(outingbox_subzone_9)
    outingbox_address_39.metro_station.add(outingbox_metrostation_37)
    outingbox_address_39.metro_station.add(outingbox_metrostation_70)

    outingbox_address_40 = Address()
    outingbox_address_40.title = 'Drizzling Land'
    outingbox_address_40.address_line1 = '8th Mile Stone, Delhi-Meerut Highway(NH-58), Duhai,Ghaziabad'
    outingbox_address_40.address_line2 = ''
    outingbox_address_40.zone = outingbox_zone_2
    outingbox_address_40.pin_code = 201206
    outingbox_address_40.map_address = ''
    outingbox_address_40.location = ''
    outingbox_address_40.save()

    outingbox_address_40.sub_zone.add(outingbox_subzone_30)
    outingbox_address_40.sub_zone.add(outingbox_subzone_31)
    outingbox_address_40.sub_zone.add(outingbox_subzone_32)
    outingbox_address_40.metro_station.add(outingbox_metrostation_134)

    outingbox_address_41 = Address()
    outingbox_address_41.title = 'Fun N Food Village'
    outingbox_address_41.address_line1 = 'Kapashera Estate, Old Delhi Gurgaon Road'
    outingbox_address_41.address_line2 = 'Opp. Kapshera Bus Stand'
    outingbox_address_41.zone = outingbox_zone_1
    outingbox_address_41.pin_code = 110037
    outingbox_address_41.map_address = 'fun and food village'
    outingbox_address_41.location = '28.527434,77.080704'
    outingbox_address_41.save()

    outingbox_address_41.sub_zone.add(outingbox_subzone_3)
    outingbox_address_41.sub_zone.add(outingbox_subzone_8)
    outingbox_address_41.sub_zone.add(outingbox_subzone_9)
    outingbox_address_41.sub_zone.add(outingbox_subzone_81)
    outingbox_address_41.metro_station.add(outingbox_metrostation_36)

    outingbox_address_42 = Address()
    outingbox_address_42.title = 'BluO'
    outingbox_address_42.address_line1 = 'Level 1, Ambience Mall, Nelson Mandela Marg, Vasant Kunj'
    outingbox_address_42.address_line2 = ''
    outingbox_address_42.zone = outingbox_zone_2
    outingbox_address_42.pin_code = 0
    outingbox_address_42.map_address = ''
    outingbox_address_42.location = '28.502705,77.097512'
    outingbox_address_42.save()

    outingbox_address_42.sub_zone.add(outingbox_subzone_9)
    outingbox_address_42.sub_zone.add(outingbox_subzone_81)
    outingbox_address_42.metro_station.add(outingbox_metrostation_14)

    outingbox_address_43 = Address()
    outingbox_address_43.title = 'Skittle Bowling Arena'
    outingbox_address_43.address_line1 = 'Ug-17, Ansal Plaza, Greater Noida'
    outingbox_address_43.address_line2 = ''
    outingbox_address_43.zone = outingbox_zone_2
    outingbox_address_43.pin_code = 201308
    outingbox_address_43.map_address = ''
    outingbox_address_43.location = '28.535902,77.392013'
    outingbox_address_43.save()

    outingbox_address_43.sub_zone.add(outingbox_subzone_22)
    outingbox_address_43.metro_station.add(outingbox_metrostation_88)

    outingbox_address_44 = Address()
    outingbox_address_44.title = 'Just Chill Water Park'
    outingbox_address_44.address_line1 = 'Main GT Karnal Road near GTB, Memorial Delhi - 110040 (India)'
    outingbox_address_44.address_line2 = ''
    outingbox_address_44.zone = outingbox_zone_2
    outingbox_address_44.pin_code = 110040
    outingbox_address_44.map_address = ''
    outingbox_address_44.location = '28.850358,77.128133'
    outingbox_address_44.save()

    outingbox_address_44.sub_zone.add(outingbox_subzone_11)
    outingbox_address_44.sub_zone.add(outingbox_subzone_12)
    outingbox_address_44.sub_zone.add(outingbox_subzone_13)
    outingbox_address_44.sub_zone.add(outingbox_subzone_14)
    outingbox_address_44.sub_zone.add(outingbox_subzone_81)
    outingbox_address_44.metro_station.add(outingbox_metrostation_42)

    outingbox_address_45 = Address()
    outingbox_address_45.title = 'Gallery Espace'
    outingbox_address_45.address_line1 = '16 Community Centre New Friends Colony New Delhi '
    outingbox_address_45.address_line2 = ''
    outingbox_address_45.zone = outingbox_zone_2
    outingbox_address_45.pin_code = 110025
    outingbox_address_45.map_address = ''
    outingbox_address_45.location = '28.561436,77.267981'
    outingbox_address_45.save()

    outingbox_address_45.sub_zone.add(outingbox_subzone_69)
    outingbox_address_45.sub_zone.add(outingbox_subzone_70)
    outingbox_address_45.sub_zone.add(outingbox_subzone_81)
    outingbox_address_45.metro_station.add(outingbox_metrostation_46)
    outingbox_address_45.metro_station.add(outingbox_metrostation_79)

    outingbox_address_46 = Address()
    outingbox_address_46.title = 'SPLASH-The Water Park'
    outingbox_address_46.address_line1 = 'Main GT Karnal Road Near Palla Moad ,Alipur,Delhi'
    outingbox_address_46.address_line2 = ''
    outingbox_address_46.zone = outingbox_zone_2
    outingbox_address_46.pin_code = 110036
    outingbox_address_46.map_address = ''
    outingbox_address_46.location = ''
    outingbox_address_46.save()

    outingbox_address_46.sub_zone.add(outingbox_subzone_11)
    outingbox_address_46.sub_zone.add(outingbox_subzone_15)
    outingbox_address_46.sub_zone.add(outingbox_subzone_16)
    outingbox_address_46.sub_zone.add(outingbox_subzone_81)
    outingbox_address_46.metro_station.add(outingbox_metrostation_42)

    outingbox_address_47 = Address()
    outingbox_address_47.title = 'Jurasik Park Inn'
    outingbox_address_47.address_line1 = 'GT Karnal Road, National Highway 1, Sonepat, Haryana  '
    outingbox_address_47.address_line2 = ''
    outingbox_address_47.zone = outingbox_zone_2
    outingbox_address_47.pin_code = 131021
    outingbox_address_47.map_address = ''
    outingbox_address_47.location = '29.008682,77.081989'
    outingbox_address_47.save()

    outingbox_address_47.sub_zone.add(outingbox_subzone_11)
    outingbox_address_47.sub_zone.add(outingbox_subzone_26)
    outingbox_address_47.sub_zone.add(outingbox_subzone_27)
    outingbox_address_47.sub_zone.add(outingbox_subzone_28)
    outingbox_address_47.sub_zone.add(outingbox_subzone_29)
    outingbox_address_47.metro_station.add(outingbox_metrostation_42)

    outingbox_address_48 = Address()
    outingbox_address_48.title = 'Bikram Yoga '
    outingbox_address_48.address_line1 = 'A 24 ,Vishal enclave, Rajouri Garden,New Delhi'
    outingbox_address_48.address_line2 = ''
    outingbox_address_48.zone = outingbox_zone_2
    outingbox_address_48.pin_code = 110027
    outingbox_address_48.map_address = ''
    outingbox_address_48.location = ''
    outingbox_address_48.save()

    outingbox_address_48.sub_zone.add(outingbox_subzone_1)
    outingbox_address_48.sub_zone.add(outingbox_subzone_10)
    outingbox_address_48.sub_zone.add(outingbox_subzone_81)
    outingbox_address_48.metro_station.add(outingbox_metrostation_106)

    outingbox_address_49 = Address()
    outingbox_address_49.title = 'Amoeba - Noida'
    outingbox_address_49.address_line1 = 'Shop No-309, Spice World, 2nd Floor'
    outingbox_address_49.address_line2 = 'Sector 25 A, Noida'
    outingbox_address_49.zone = outingbox_zone_1
    outingbox_address_49.pin_code = 201301
    outingbox_address_49.map_address = 'spice noida'
    outingbox_address_49.location = '28.586345,77.341250'
    outingbox_address_49.save()

    outingbox_address_49.sub_zone.add(outingbox_subzone_4)
    outingbox_address_49.sub_zone.add(outingbox_subzone_22)
    outingbox_address_49.metro_station.add(outingbox_metrostation_84)
    outingbox_address_49.metro_station.add(outingbox_metrostation_88)

    outingbox_address_50 = Address()
    outingbox_address_50.title = 'Aapno Ghar Amusement & Water Park'
    outingbox_address_50.address_line1 = '43rd Milestone, Main Delhi Jaipur Expressway, Nh-8, Sector-77,Gurgaon'
    outingbox_address_50.address_line2 = ''
    outingbox_address_50.zone = outingbox_zone_2
    outingbox_address_50.pin_code = 122001
    outingbox_address_50.map_address = ''
    outingbox_address_50.location = '28.386775,76.974399'
    outingbox_address_50.save()

    outingbox_address_50.sub_zone.add(outingbox_subzone_8)
    outingbox_address_50.sub_zone.add(outingbox_subzone_26)
    outingbox_address_50.sub_zone.add(outingbox_subzone_34)
    outingbox_address_50.sub_zone.add(outingbox_subzone_35)
    outingbox_address_50.metro_station.add(outingbox_metrostation_36)
    outingbox_address_50.metro_station.add(outingbox_metrostation_37)

    outingbox_address_51 = Address()
    outingbox_address_51.title = 'Pool World'
    outingbox_address_51.address_line1 = 'M-22, Greater Kailash 1, Delhi'
    outingbox_address_51.address_line2 = ''
    outingbox_address_51.zone = outingbox_zone_2
    outingbox_address_51.pin_code = 0
    outingbox_address_51.map_address = ''
    outingbox_address_51.location = '28.552320,77.235405'
    outingbox_address_51.save()

    outingbox_address_51.sub_zone.add(outingbox_subzone_9)
    outingbox_address_51.sub_zone.add(outingbox_subzone_81)
    outingbox_address_51.metro_station.add(outingbox_metrostation_51)

    outingbox_address_52 = Address()
    outingbox_address_52.title = 'Rockshot Paintball Sports'
    outingbox_address_52.address_line1 = 'Green View Resedency C-254, Sector-44 Near - Challera Market, Noida'
    outingbox_address_52.address_line2 = ''
    outingbox_address_52.zone = outingbox_zone_2
    outingbox_address_52.pin_code = 0
    outingbox_address_52.map_address = ''
    outingbox_address_52.location = '28.535516,77.391026'
    outingbox_address_52.save()

    outingbox_address_52.sub_zone.add(outingbox_subzone_22)
    outingbox_address_52.sub_zone.add(outingbox_subzone_75)
    outingbox_address_52.sub_zone.add(outingbox_subzone_76)
    outingbox_address_52.metro_station.add(outingbox_metrostation_84)
    outingbox_address_52.metro_station.add(outingbox_metrostation_85)

    outingbox_address_53 = Address()
    outingbox_address_53.title = 'National Science Centre'
    outingbox_address_53.address_line1 = 'Near Gate No.1, Bhairon Road, '
    outingbox_address_53.address_line2 = 'Pragati Maidan, New Delhi - 110001'
    outingbox_address_53.zone = outingbox_zone_1
    outingbox_address_53.pin_code = 110001
    outingbox_address_53.map_address = 'National Science Centre, Delhi'
    outingbox_address_53.location = '28.612983,77.245724'
    outingbox_address_53.save()

    outingbox_address_53.sub_zone.add(outingbox_subzone_77)
    outingbox_address_53.sub_zone.add(outingbox_subzone_81)
    outingbox_address_53.metro_station.add(outingbox_metrostation_96)

    outingbox_address_54 = Address()
    outingbox_address_54.title = 'Nehru Planetarium'
    outingbox_address_54.address_line1 = 'Teen Murti House,  '
    outingbox_address_54.address_line2 = 'New Delhi - 110011,  India'
    outingbox_address_54.zone = outingbox_zone_1
    outingbox_address_54.pin_code = 2
    outingbox_address_54.map_address = '28.603843, 77.198134'
    outingbox_address_54.location = '28.603835,77.198145'
    outingbox_address_54.save()

    outingbox_address_54.sub_zone.add(outingbox_subzone_78)
    outingbox_address_54.sub_zone.add(outingbox_subzone_79)
    outingbox_address_54.sub_zone.add(outingbox_subzone_80)
    outingbox_address_54.sub_zone.add(outingbox_subzone_81)
    outingbox_address_54.metro_station.add(outingbox_metrostation_102)

    outingbox_address_55 = Address()
    outingbox_address_55.title = 'Rockshot Paintball Sports'
    outingbox_address_55.address_line1 = 'S11/C3, Pandav Nagar Ext, New Delhi'
    outingbox_address_55.address_line2 = ''
    outingbox_address_55.zone = outingbox_zone_2
    outingbox_address_55.pin_code = 110092
    outingbox_address_55.map_address = ''
    outingbox_address_55.location = '28.620798,77.283030'
    outingbox_address_55.save()

    outingbox_address_55.sub_zone.add(outingbox_subzone_5)
    outingbox_address_55.sub_zone.add(outingbox_subzone_81)
    outingbox_address_55.sub_zone.add(outingbox_subzone_82)
    outingbox_address_55.metro_station.add(outingbox_metrostation_4)
    outingbox_address_55.metro_station.add(outingbox_metrostation_68)

    outingbox_address_56 = Address()
    outingbox_address_56.title = 'Visual Arts Gallery'
    outingbox_address_56.address_line1 = 'Habitat World at India Habitat Centre  Lodhi Road  New Delhi '
    outingbox_address_56.address_line2 = ''
    outingbox_address_56.zone = outingbox_zone_2
    outingbox_address_56.pin_code = 110003
    outingbox_address_56.map_address = ''
    outingbox_address_56.location = '28.589890,77.225225'
    outingbox_address_56.save()

    outingbox_address_56.sub_zone.add(outingbox_subzone_72)
    outingbox_address_56.sub_zone.add(outingbox_subzone_73)
    outingbox_address_56.sub_zone.add(outingbox_subzone_74)
    outingbox_address_56.sub_zone.add(outingbox_subzone_81)
    outingbox_address_56.metro_station.add(outingbox_metrostation_47)
    outingbox_address_56.metro_station.add(outingbox_metrostation_50)

    outingbox_address_57 = Address()
    outingbox_address_57.title = 'Vadhera Art Gallery'
    outingbox_address_57.address_line1 = 'D-53 Defence Colony New Delhi '
    outingbox_address_57.address_line2 = ''
    outingbox_address_57.zone = outingbox_zone_2
    outingbox_address_57.pin_code = 110024
    outingbox_address_57.map_address = ''
    outingbox_address_57.location = '28.568649,77.234525'
    outingbox_address_57.save()

    outingbox_address_57.sub_zone.add(outingbox_subzone_9)
    outingbox_address_57.sub_zone.add(outingbox_subzone_71)
    outingbox_address_57.sub_zone.add(outingbox_subzone_81)
    outingbox_address_57.metro_station.add(outingbox_metrostation_62)

    outingbox_address_58 = Address()
    outingbox_address_58.title = 'Vadhera Art Gallery'
    outingbox_address_58.address_line1 = 'D-40 Defence Colony New Delhi '
    outingbox_address_58.address_line2 = ''
    outingbox_address_58.zone = outingbox_zone_2
    outingbox_address_58.pin_code = 110024
    outingbox_address_58.map_address = ''
    outingbox_address_58.location = '28.570746,77.235820'
    outingbox_address_58.save()

    outingbox_address_58.sub_zone.add(outingbox_subzone_9)
    outingbox_address_58.sub_zone.add(outingbox_subzone_71)
    outingbox_address_58.sub_zone.add(outingbox_subzone_81)
    outingbox_address_58.metro_station.add(outingbox_metrostation_62)

    outingbox_address_59 = Address()
    outingbox_address_59.title = 'Studio Prana'
    outingbox_address_59.address_line1 = '#37, Second Floor, Pratap Nagar, Main Acharya Niketan Market, Mayur Vihar, Phase - I, New Delhi '
    outingbox_address_59.address_line2 = ''
    outingbox_address_59.zone = outingbox_zone_2
    outingbox_address_59.pin_code = 110091
    outingbox_address_59.map_address = ''
    outingbox_address_59.location = '28.606984,77.294454'
    outingbox_address_59.save()

    outingbox_address_59.sub_zone.add(outingbox_subzone_5)
    outingbox_address_59.sub_zone.add(outingbox_subzone_6)
    outingbox_address_59.sub_zone.add(outingbox_subzone_7)
    outingbox_address_59.sub_zone.add(outingbox_subzone_81)
    outingbox_address_59.metro_station.add(outingbox_metrostation_68)

    outingbox_address_60 = Address()
    outingbox_address_60.title = 'Delhi Heritage Walks'
    outingbox_address_60.address_line1 = 'Delhi'
    outingbox_address_60.address_line2 = ''
    outingbox_address_60.zone = outingbox_zone_1
    outingbox_address_60.pin_code = 0
    outingbox_address_60.map_address = ''
    outingbox_address_60.location = ''
    outingbox_address_60.save()

    outingbox_address_60.sub_zone.add(outingbox_subzone_81)

    outingbox_address_61 = Address()
    outingbox_address_61.title = '1100 Walks'
    outingbox_address_61.address_line1 = 'Delhi'
    outingbox_address_61.address_line2 = ''
    outingbox_address_61.zone = outingbox_zone_1
    outingbox_address_61.pin_code = 0
    outingbox_address_61.map_address = ''
    outingbox_address_61.location = ''
    outingbox_address_61.save()

    outingbox_address_61.sub_zone.add(outingbox_subzone_81)

    outingbox_address_62 = Address()
    outingbox_address_62.title = 'DelhiByFoot'
    outingbox_address_62.address_line1 = 'Delhi'
    outingbox_address_62.address_line2 = ''
    outingbox_address_62.zone = outingbox_zone_1
    outingbox_address_62.pin_code = 0
    outingbox_address_62.map_address = ''
    outingbox_address_62.location = ''
    outingbox_address_62.save()

    outingbox_address_62.sub_zone.add(outingbox_subzone_81)

    outingbox_address_63 = Address()
    outingbox_address_63.title = 'Delhi Walks'
    outingbox_address_63.address_line1 = 'Delhi'
    outingbox_address_63.address_line2 = ''
    outingbox_address_63.zone = outingbox_zone_1
    outingbox_address_63.pin_code = 0
    outingbox_address_63.map_address = ''
    outingbox_address_63.location = ''
    outingbox_address_63.save()

    outingbox_address_63.sub_zone.add(outingbox_subzone_81)

    outingbox_address_64 = Address()
    outingbox_address_64.title = 'MKH Tourism'
    outingbox_address_64.address_line1 = 'Delhi'
    outingbox_address_64.address_line2 = ''
    outingbox_address_64.zone = outingbox_zone_1
    outingbox_address_64.pin_code = 0
    outingbox_address_64.map_address = ''
    outingbox_address_64.location = ''
    outingbox_address_64.save()

    outingbox_address_64.sub_zone.add(outingbox_subzone_81)

    outingbox_address_65 = Address()
    outingbox_address_65.title = 'Delhi By Cycle'
    outingbox_address_65.address_line1 = 'Delhi'
    outingbox_address_65.address_line2 = ''
    outingbox_address_65.zone = outingbox_zone_1
    outingbox_address_65.pin_code = 0
    outingbox_address_65.map_address = ''
    outingbox_address_65.location = ''
    outingbox_address_65.save()

    outingbox_address_65.sub_zone.add(outingbox_subzone_81)

    outingbox_address_66 = Address()
    outingbox_address_66.title = 'Intach Heritage Walks'
    outingbox_address_66.address_line1 = 'Delhi'
    outingbox_address_66.address_line2 = ''
    outingbox_address_66.zone = outingbox_zone_1
    outingbox_address_66.pin_code = 0
    outingbox_address_66.map_address = ''
    outingbox_address_66.location = ''
    outingbox_address_66.save()

    outingbox_address_66.sub_zone.add(outingbox_subzone_81)

    outingbox_address_67 = Address()
    outingbox_address_67.title = 'Camp Wild Dhauj'
    outingbox_address_67.address_line1 = 'Near Mangar Village, Dhauj, Faridabad,'
    outingbox_address_67.address_line2 = ' Haryana 121004'
    outingbox_address_67.zone = outingbox_zone_1
    outingbox_address_67.pin_code = 121004
    outingbox_address_67.map_address = ''
    outingbox_address_67.location = '28.361108,77.188064'
    outingbox_address_67.save()

    outingbox_address_67.sub_zone.add(outingbox_subzone_26)
    outingbox_address_67.sub_zone.add(outingbox_subzone_36)
    outingbox_address_67.metro_station.add(outingbox_metrostation_1)
    outingbox_address_67.metro_station.add(outingbox_metrostation_9)

    outingbox_address_68 = Address()
    outingbox_address_68.title = 'Golden Dunes Retreat'
    outingbox_address_68.address_line1 = 'Village Chandu near Sultanpur Bird sanctuary, 44 Kms from Delhi,'
    outingbox_address_68.address_line2 = '12 Kms from Rajiv Gandhi Chowk, Pataudi Road, Gurgaon  '
    outingbox_address_68.zone = outingbox_zone_1
    outingbox_address_68.pin_code = 122506
    outingbox_address_68.map_address = ''
    outingbox_address_68.location = '28.428191,76.952049'
    outingbox_address_68.save()

    outingbox_address_68.sub_zone.add(outingbox_subzone_8)
    outingbox_address_68.sub_zone.add(outingbox_subzone_81)
    outingbox_address_68.metro_station.add(outingbox_metrostation_36)

    outingbox_address_69 = Address()
    outingbox_address_69.title = 'Camp Tikkling'
    outingbox_address_69.address_line1 = 'Village Gairatpur Baas, Badshahpur, '
    outingbox_address_69.address_line2 = 'District Gurgaon, Haryana'
    outingbox_address_69.zone = outingbox_zone_1
    outingbox_address_69.pin_code = 122103
    outingbox_address_69.map_address = ''
    outingbox_address_69.location = '28.338168,77.008362'
    outingbox_address_69.save()

    outingbox_address_69.sub_zone.add(outingbox_subzone_8)
    outingbox_address_69.sub_zone.add(outingbox_subzone_26)
    outingbox_address_69.metro_station.add(outingbox_metrostation_36)

    outingbox_address_70 = Address()
    outingbox_address_70.title = 'Camp Mustang'
    outingbox_address_70.address_line1 = 'Sohna Road, Gurgaon'
    outingbox_address_70.address_line2 = ''
    outingbox_address_70.zone = outingbox_zone_1
    outingbox_address_70.pin_code = 122103
    outingbox_address_70.map_address = ''
    outingbox_address_70.location = '28.340107,77.010366'
    outingbox_address_70.save()

    outingbox_address_70.sub_zone.add(outingbox_subzone_8)
    outingbox_address_70.metro_station.add(outingbox_metrostation_36)
    outingbox_address_70.metro_station.add(outingbox_metrostation_37)

    # Processing model: Place

    from outingbox.models import Place

    outingbox_place_1 = Place()
    outingbox_place_1.address = 'aapno ghar'
    outingbox_place_1.location = '28.386775,76.974399'
    outingbox_place_1.save()

    outingbox_place_2 = Place()
    outingbox_place_2.address = 'bluo vasant kunj'
    outingbox_place_2.location = '28.502705,77.097512'
    outingbox_place_2.save()

    outingbox_place_3 = Place()
    outingbox_place_3.address = 'Kapashera Estate, Old Delhi Gurgaon Road, Opp. Kapshera Bus Stand'
    outingbox_place_3.location = '28.525481,77.084136'
    outingbox_place_3.save()

    outingbox_place_4 = Place()
    outingbox_place_4.address = 'Fun N Food Village,Kapashera Estate, Old Delhi Gurgaon Road, Opp. Kapshera Bus Stand'
    outingbox_place_4.location = '28.525481,77.084136'
    outingbox_place_4.save()

    outingbox_place_5 = Place()
    outingbox_place_5.address = 'Fun and Food Village'
    outingbox_place_5.location = '28.524374,77.083415'
    outingbox_place_5.save()

    outingbox_place_6 = Place()
    outingbox_place_6.address = 'Fun N Food Village'
    outingbox_place_6.location = '28.523910,77.084727'
    outingbox_place_6.save()

    outingbox_place_7 = Place()
    outingbox_place_7.address = 'appu ghar,Gurgaon'
    outingbox_place_7.location = '28.462200,77.071474'
    outingbox_place_7.save()

    outingbox_place_8 = Place()
    outingbox_place_8.address = 'delhirides'
    outingbox_place_8.location = '28.545555,77.309635'
    outingbox_place_8.save()

    outingbox_place_9 = Place()
    outingbox_place_9.address = 'A- 265, Andheria Modh,Near Kishan Haat,New Delhi'
    outingbox_place_9.location = '28.613939,77.209021'
    outingbox_place_9.save()

    outingbox_place_10 = Place()
    outingbox_place_10.address = 'A- 265, Andheria Modh,Near Kishan Haat,New Delhi'
    outingbox_place_10.location = '28.613939,77.209021'
    outingbox_place_10.save()

    outingbox_place_11 = Place()
    outingbox_place_11.address = 'A- 265, Andheria Modh,Near Kishan Haat,New Delhi'
    outingbox_place_11.location = '28.613939,77.209021'
    outingbox_place_11.save()

    outingbox_place_12 = Place()
    outingbox_place_12.address = 'Shop No. 239&240, 1st Floor, DLF Place Mall, Saket, New Delhi'
    outingbox_place_12.location = '28.524579,77.206615'
    outingbox_place_12.save()

    outingbox_place_13 = Place()
    outingbox_place_13.address = 'NH. 8, Behind Sector 15, Gurgaon, Haryana 122001, India'
    outingbox_place_13.location = '28.458089,77.041191'
    outingbox_place_13.save()

    outingbox_place_14 = Place()
    outingbox_place_14.address = 'E-238, Amar Colony, Lajpat Nagar 4, New Delhi'
    outingbox_place_14.location = '28.561197,77.241680'
    outingbox_place_14.save()

    outingbox_place_15 = Place()
    outingbox_place_15.address = ' 505, Ring Road Mall, Sector 3, Rohini, New Delhi'
    outingbox_place_15.location = '28.698277,77.116007'
    outingbox_place_15.save()

    outingbox_place_16 = Place()
    outingbox_place_16.address = 'just chill water park,new delhi'
    outingbox_place_16.location = '28.850358,77.128133'
    outingbox_place_16.save()

    outingbox_place_17 = Place()
    outingbox_place_17.address = 'adventure island,rohini'
    outingbox_place_17.location = '28.723728,77.113592'
    outingbox_place_17.save()

    outingbox_place_18 = Place()
    outingbox_place_18.address = 'jurassic park inn,sonepat'
    outingbox_place_18.location = '29.008682,77.081989'
    outingbox_place_18.save()

    outingbox_place_19 = Place()
    outingbox_place_19.address = 'club platinum resort,'
    outingbox_place_19.location = '28.670857,77.085852'
    outingbox_place_19.save()

    outingbox_place_20 = Place()
    outingbox_place_20.address = 'Shop No-309, Spice World, 2nd Flr, Sector 25 A, Noida'
    outingbox_place_20.location = '28.535516,77.391026'
    outingbox_place_20.save()

    outingbox_place_21 = Place()
    outingbox_place_21.address = 'Shop No-309, Spice World, 2nd Flr, Sector 25 A, Noida'
    outingbox_place_21.location = '28.535516,77.391026'
    outingbox_place_21.save()

    outingbox_place_22 = Place()
    outingbox_place_22.address = 'M.G.F Metropolitan Mall, Mehrauli'
    outingbox_place_22.location = '28.529568,77.220172'
    outingbox_place_22.save()

    outingbox_place_23 = Place()
    outingbox_place_23.address = '4, Aurobindo Marg, New Delhi'
    outingbox_place_23.location = '28.546344,77.202296'
    outingbox_place_23.save()

    outingbox_place_24 = Place()
    outingbox_place_24.address = 'Building No. 105, Plot No. 2A, Sector 38 A, Noida'
    outingbox_place_24.location = '28.562308,77.329571'
    outingbox_place_24.save()

    outingbox_place_25 = Place()
    outingbox_place_25.address = '2nd Floor, Pacific Mall, Tagore Garden, New Delhi'
    outingbox_place_25.location = '28.643895,77.112830'
    outingbox_place_25.save()

    outingbox_place_26 = Place()
    outingbox_place_26.address = 'Ug-17, Ansal Plaza, Greater Noida'
    outingbox_place_26.location = '28.535902,77.392013'
    outingbox_place_26.save()

    outingbox_place_27 = Place()
    outingbox_place_27.address = 'A-38, Mohan Cooperative Industrial Estate,, Near Pind Balluchi Restaurant, Main Mathura Road, New Delhi'
    outingbox_place_27.location = '28.611238,77.240114'
    outingbox_place_27.save()

    outingbox_place_28 = Place()
    outingbox_place_28.address = 'A-38, Mohan Co-Operative Industrial Estate, Mathura Road, Badarpur,Delhi'
    outingbox_place_28.location = '28.469887,77.305907'
    outingbox_place_28.save()

    outingbox_place_29 = Place()
    outingbox_place_29.address = 'Dynamic House, Opp Petrol Bunk, Dadri Main Road, Sector-41, Noida'
    outingbox_place_29.location = '28.561075,77.363055'
    outingbox_place_29.save()

    outingbox_place_30 = Place()
    outingbox_place_30.address = 'wonder speedways,noida'
    outingbox_place_30.location = '28.564066,77.325414'
    outingbox_place_30.save()

    outingbox_place_31 = Place()
    outingbox_place_31.address = 'Westin Resort, Sohna, Gurgaon'
    outingbox_place_31.location = '28.248699,77.063512'
    outingbox_place_31.save()

    outingbox_place_32 = Place()
    outingbox_place_32.address = 'F9 Go-Karting, Sector 17-18 Link Road, Gurgaon'
    outingbox_place_32.location = '28.423184,77.188572'
    outingbox_place_32.save()

    outingbox_place_33 = Place()
    outingbox_place_33.address = 'F9 Go Karting Gurgaon'
    outingbox_place_33.location = '28.459497,77.026638'
    outingbox_place_33.save()

    outingbox_place_34 = Place()
    outingbox_place_34.address = 'F9 Go Karting Gurgaon'
    outingbox_place_34.location = '28.459497,77.026638'
    outingbox_place_34.save()

    outingbox_place_35 = Place()
    outingbox_place_35.address = 'luxmi plaza gurgaon'
    outingbox_place_35.location = '28.465048,77.507700'
    outingbox_place_35.save()

    outingbox_place_36 = Place()
    outingbox_place_36.address = 'F9 Go Karting Gurgaon'
    outingbox_place_36.location = '28.465067,77.507711'
    outingbox_place_36.save()

    outingbox_place_37 = Place()
    outingbox_place_37.address = 'Sohna Gugaon'
    outingbox_place_37.location = '28.237296, 77.149235'
    outingbox_place_37.save()

    outingbox_place_38 = Place()
    outingbox_place_38.address = 'Pacific Mall, Subhash Nagar, 110027'
    outingbox_place_38.location = '18.501079,73.872429'
    outingbox_place_38.save()

    outingbox_place_39 = Place()
    outingbox_place_39.address = 'City Mall, Sector 12 Faridabad'
    outingbox_place_39.location = '28.570434,77.337280'
    outingbox_place_39.save()

    outingbox_place_40 = Place()
    outingbox_place_40.address = 'City Mall, Sector 12 Faridabad'
    outingbox_place_40.location = '28.570434,77.337280'
    outingbox_place_40.save()

    outingbox_place_41 = Place()
    outingbox_place_41.address = 'M-22, Greater Kailash 1, Delhi'
    outingbox_place_41.location = '28.552320,77.235405'
    outingbox_place_41.save()

    outingbox_place_42 = Place()
    outingbox_place_42.address = 'Mind Cafe'
    outingbox_place_42.location = '28.468281,77.083210'
    outingbox_place_42.save()

    outingbox_place_43 = Place()
    outingbox_place_43.address = 'Iyengar Yoga Centre, new delhi'
    outingbox_place_43.location = '28.629935, 77.236802'
    outingbox_place_43.save()

    outingbox_place_44 = Place()
    outingbox_place_44.address = 'Sivanand'
    outingbox_place_44.location = '28.553610, 77.242764'
    outingbox_place_44.save()

    outingbox_place_45 = Place()
    outingbox_place_45.address = 'the yoga studio,'
    outingbox_place_45.location = '28.550435,77.206611'
    outingbox_place_45.save()

    outingbox_place_46 = Place()
    outingbox_place_46.address = 'Kedarnath Yoga'
    outingbox_place_46.location = '28.465526, 77.079122'
    outingbox_place_46.save()

    outingbox_place_47 = Place()
    outingbox_place_47.address = 'Universal Yoga Group'
    outingbox_place_47.location = '28.475262, 77.025490'
    outingbox_place_47.save()

    outingbox_place_48 = Place()
    outingbox_place_48.address = 'Universal Yoga Group'
    outingbox_place_48.location = '28.613939,77.209021'
    outingbox_place_48.save()

    outingbox_place_49 = Place()
    outingbox_place_49.address = 'Yogakul'
    outingbox_place_49.location = '28.548664, 77.214060'
    outingbox_place_49.save()

    outingbox_place_50 = Place()
    outingbox_place_50.address = 'AtreYoga'
    outingbox_place_50.location = '28.548121, 77.211445'
    outingbox_place_50.save()

    outingbox_place_51 = Place()
    outingbox_place_51.address = 'Studio Prana'
    outingbox_place_51.location = '28.606984, 77.294454'
    outingbox_place_51.save()

    outingbox_place_52 = Place()
    outingbox_place_52.address = 'Studio Prana'
    outingbox_place_52.location = '28.606984, 77.294454'
    outingbox_place_52.save()

    outingbox_place_53 = Place()
    outingbox_place_53.address = 'Navadha Yoga Centre'
    outingbox_place_53.location = '28.531865, 77.208166'
    outingbox_place_53.save()

    outingbox_place_54 = Place()
    outingbox_place_54.address = 'iSkate'
    outingbox_place_54.location = '28.503812,77.097349'
    outingbox_place_54.save()

    outingbox_place_55 = Place()
    outingbox_place_55.address = 'Art alive gallery'
    outingbox_place_55.location = '28.542863, 77.215889'
    outingbox_place_55.save()

    outingbox_place_56 = Place()
    outingbox_place_56.address = 'Dhoomimal art gallery'
    outingbox_place_56.location = '28.632732, 77.217847'
    outingbox_place_56.save()

    outingbox_place_57 = Place()
    outingbox_place_57.address = 'Gallery Espace'
    outingbox_place_57.location = '28.561436, 77.267981'
    outingbox_place_57.save()

    outingbox_place_58 = Place()
    outingbox_place_58.address = 'Vadhera Art '
    outingbox_place_58.location = '28.570746, 77.235820'
    outingbox_place_58.save()

    outingbox_place_59 = Place()
    outingbox_place_59.address = 'Vadhera Art '
    outingbox_place_59.location = '28.568649, 77.234525'
    outingbox_place_59.save()

    outingbox_place_60 = Place()
    outingbox_place_60.address = 'Visual Art Gallery'
    outingbox_place_60.location = '28.589890, 77.225225'
    outingbox_place_60.save()

    outingbox_place_61 = Place()
    outingbox_place_61.address = 'S11/C3, Pandav Nagar Ext, New Delhi 110092'
    outingbox_place_61.location = '28.620798,77.283030'
    outingbox_place_61.save()

    outingbox_place_62 = Place()
    outingbox_place_62.address = 'Green View Resedency C-254, Sector-44 Near - Challera Market, Noida'
    outingbox_place_62.location = '28.535516,77.391026'
    outingbox_place_62.save()

    # Processing model: Box

    from outingbox.models import Box

    outingbox_box_1 = Box()
    outingbox_box_1.title = 'Science, Art, and History'
    outingbox_box_1.url_name = 'science-art-and-history'
    outingbox_box_1.featured_image = 'photos/box/science-art-and-history'
    outingbox_box_1.save()

    outingbox_box_2 = Box()
    outingbox_box_2.title = 'Nature'
    outingbox_box_2.url_name = 'nature'
    outingbox_box_2.featured_image = 'photos/box/nature'
    outingbox_box_2.save()

    outingbox_box_3 = Box()
    outingbox_box_3.title = 'Entertainment'
    outingbox_box_3.url_name = 'entertainment'
    outingbox_box_3.featured_image = 'photos/box/entertainment'
    outingbox_box_3.save()

    outingbox_box_4 = Box()
    outingbox_box_4.title = 'Games and Sports'
    outingbox_box_4.url_name = 'games-and-sports'
    outingbox_box_4.featured_image = 'photos/box/games-and-sports'
    outingbox_box_4.save()

    outingbox_box_5 = Box()
    outingbox_box_5.title = 'Hobbies'
    outingbox_box_5.url_name = 'hobbies'
    outingbox_box_5.featured_image = 'photos/box/hobbies'
    outingbox_box_5.save()

    outingbox_box_6 = Box()
    outingbox_box_6.title = 'Health and Wellness'
    outingbox_box_6.url_name = 'health-and-wellness'
    outingbox_box_6.featured_image = 'photos/box/health-and-wellness'
    outingbox_box_6.save()

    # Processing model: Category

    from outingbox.models import Category

    outingbox_category_1 = Category()
    outingbox_category_1.title = 'Science Center'
    outingbox_category_1.save()

    outingbox_category_1.box.add(outingbox_box_1)

    outingbox_category_2 = Category()
    outingbox_category_2.title = 'Para Gliding'
    outingbox_category_2.save()

    outingbox_category_2.box.add(outingbox_box_4)
    outingbox_category_2.box.add(outingbox_box_2)

    outingbox_category_3 = Category()
    outingbox_category_3.title = 'Para Motoring'
    outingbox_category_3.save()

    outingbox_category_3.box.add(outingbox_box_4)
    outingbox_category_3.box.add(outingbox_box_2)

    outingbox_category_4 = Category()
    outingbox_category_4.title = 'Paintball'
    outingbox_category_4.save()

    outingbox_category_4.box.add(outingbox_box_4)

    outingbox_category_5 = Category()
    outingbox_category_5.title = 'Arcade'
    outingbox_category_5.save()

    outingbox_category_5.box.add(outingbox_box_4)

    outingbox_category_6 = Category()
    outingbox_category_6.title = 'Art Galleries'
    outingbox_category_6.save()

    outingbox_category_6.box.add(outingbox_box_1)

    outingbox_category_7 = Category()
    outingbox_category_7.title = 'Bowling'
    outingbox_category_7.save()

    outingbox_category_7.box.add(outingbox_box_4)

    outingbox_category_8 = Category()
    outingbox_category_8.title = 'Pool'
    outingbox_category_8.save()

    outingbox_category_8.box.add(outingbox_box_4)

    outingbox_category_9 = Category()
    outingbox_category_9.title = 'Camping'
    outingbox_category_9.save()

    outingbox_category_9.box.add(outingbox_box_2)

    outingbox_category_10 = Category()
    outingbox_category_10.title = 'Ice Skating'
    outingbox_category_10.save()

    outingbox_category_10.box.add(outingbox_box_4)

    outingbox_category_11 = Category()
    outingbox_category_11.title = 'Pilates'
    outingbox_category_11.save()

    outingbox_category_11.box.add(outingbox_box_6)

    outingbox_category_12 = Category()
    outingbox_category_12.title = 'Naturopathy'
    outingbox_category_12.save()

    outingbox_category_12.box.add(outingbox_box_6)

    outingbox_category_13 = Category()
    outingbox_category_13.title = 'Yoga'
    outingbox_category_13.save()

    outingbox_category_13.box.add(outingbox_box_6)

    outingbox_category_14 = Category()
    outingbox_category_14.title = 'Board Game'
    outingbox_category_14.save()

    outingbox_category_14.box.add(outingbox_box_4)

    outingbox_category_15 = Category()
    outingbox_category_15.title = 'Zumba'
    outingbox_category_15.save()

    outingbox_category_15.box.add(outingbox_box_5)

    outingbox_category_16 = Category()
    outingbox_category_16.title = 'Bollywood Dance'
    outingbox_category_16.save()

    outingbox_category_16.box.add(outingbox_box_5)

    outingbox_category_17 = Category()
    outingbox_category_17.title = 'Contemporary Dance'
    outingbox_category_17.save()

    outingbox_category_17.box.add(outingbox_box_5)

    outingbox_category_18 = Category()
    outingbox_category_18.title = 'Hip Hop Dance'
    outingbox_category_18.save()

    outingbox_category_18.box.add(outingbox_box_5)

    outingbox_category_19 = Category()
    outingbox_category_19.title = 'Salsa'
    outingbox_category_19.save()

    outingbox_category_19.box.add(outingbox_box_5)

    outingbox_category_20 = Category()
    outingbox_category_20.title = 'Wedding Choreography'
    outingbox_category_20.save()

    outingbox_category_20.box.add(outingbox_box_5)

    outingbox_category_21 = Category()
    outingbox_category_21.title = 'Belly Dance'
    outingbox_category_21.save()

    outingbox_category_21.box.add(outingbox_box_5)

    outingbox_category_22 = Category()
    outingbox_category_22.title = 'Martial Arts'
    outingbox_category_22.save()

    outingbox_category_22.box.add(outingbox_box_5)
    outingbox_category_22.box.add(outingbox_box_6)

    outingbox_category_23 = Category()
    outingbox_category_23.title = 'Self Defence'
    outingbox_category_23.save()

    outingbox_category_23.box.add(outingbox_box_5)
    outingbox_category_23.box.add(outingbox_box_6)

    outingbox_category_24 = Category()
    outingbox_category_24.title = 'Aerobics'
    outingbox_category_24.save()

    outingbox_category_24.box.add(outingbox_box_5)
    outingbox_category_24.box.add(outingbox_box_6)

    outingbox_category_25 = Category()
    outingbox_category_25.title = 'B Boying and Break Dance'
    outingbox_category_25.save()

    outingbox_category_25.box.add(outingbox_box_5)

    outingbox_category_26 = Category()
    outingbox_category_26.title = 'Jazz Dance'
    outingbox_category_26.save()

    outingbox_category_26.box.add(outingbox_box_5)

    outingbox_category_27 = Category()
    outingbox_category_27.title = 'Gymnastics'
    outingbox_category_27.save()

    outingbox_category_27.box.add(outingbox_box_5)
    outingbox_category_27.box.add(outingbox_box_6)

    outingbox_category_28 = Category()
    outingbox_category_28.title = 'Go Karting'
    outingbox_category_28.save()

    outingbox_category_28.box.add(outingbox_box_4)

    outingbox_category_29 = Category()
    outingbox_category_29.title = 'Amusement Park'
    outingbox_category_29.save()

    outingbox_category_29.box.add(outingbox_box_3)
    outingbox_category_29.box.add(outingbox_box_4)

    outingbox_category_30 = Category()
    outingbox_category_30.title = 'Water Park'
    outingbox_category_30.save()

    outingbox_category_30.box.add(outingbox_box_3)
    outingbox_category_30.box.add(outingbox_box_4)

    outingbox_category_31 = Category()
    outingbox_category_31.title = 'Museum'
    outingbox_category_31.save()

    outingbox_category_31.box.add(outingbox_box_1)

    outingbox_category_32 = Category()
    outingbox_category_32.title = 'Planetarium'
    outingbox_category_32.save()

    outingbox_category_32.box.add(outingbox_box_1)

    outingbox_category_33 = Category()
    outingbox_category_33.title = 'History Walk'
    outingbox_category_33.save()

    outingbox_category_33.box.add(outingbox_box_1)

    # Processing model: Activity

    from outingbox.models import Activity

    outingbox_activity_1 = Activity()
    outingbox_activity_1.title = 'Delhi Rides'
    outingbox_activity_1.url_name = 'delhi-rides'
    outingbox_activity_1.address = outingbox_address_11
    outingbox_activity_1.description = 'Delhi Rides is situated in Delhi. Offering double dose of thrill and delights. Delhi Rides has everything to take you to the next level of entertainment.'
    outingbox_activity_1.rating = Decimal('2.3')
    outingbox_activity_1.votes = 1
    outingbox_activity_1.cost = 3
    outingbox_activity_1.person_of_contact = ''
    outingbox_activity_1.contact_numbers = ['011-64659291', '09873715909', '09540231938']
    outingbox_activity_1.email = 'delhirides@gmail.com'
    outingbox_activity_1.website = 'http://www.delhirides.in'
    outingbox_activity_1.facebook = 'https://www.facebook.com/delhirides.in?fref=ts'
    outingbox_activity_1.twitter = ''
    outingbox_activity_1.linkedin = ''
    outingbox_activity_1.featured_image = 'photos/activity/featured/img-1_p2BmAKf.jpg'
    outingbox_activity_1.save()

    outingbox_activity_1.category.add(outingbox_category_29)
    outingbox_activity_1.category.add(outingbox_category_30)

    outingbox_activity_2 = Activity()
    outingbox_activity_2.title = 'Lock n Load Paintball'
    outingbox_activity_2.url_name = 'lock-n-load-paintball'
    outingbox_activity_2.address = outingbox_address_30
    outingbox_activity_2.description = ''
    outingbox_activity_2.rating = Decimal('1.6')
    outingbox_activity_2.votes = 1
    outingbox_activity_2.cost = 3
    outingbox_activity_2.person_of_contact = 'Mr. Karamjit Bawa'
    outingbox_activity_2.contact_numbers = ['+91-9873444019']
    outingbox_activity_2.email = 'karamjitbawa@kaarma.in'
    outingbox_activity_2.website = ''
    outingbox_activity_2.facebook = 'https://www.facebook.com/pages/LocknLoad-Paintball/298881570184537'
    outingbox_activity_2.twitter = ''
    outingbox_activity_2.linkedin = ''
    outingbox_activity_2.featured_image = 'photos/activity/featured/img-1_zwDZQ7u.jpg'
    outingbox_activity_2.save()

    outingbox_activity_2.category.add(outingbox_category_4)

    outingbox_activity_3 = Activity()
    outingbox_activity_3.title = 'Every Other Day (Appu Ghar Express)'
    outingbox_activity_3.url_name = 'every-other-day-appu-ghar-express'
    outingbox_activity_3.address = outingbox_address_17
    outingbox_activity_3.description = ''
    outingbox_activity_3.rating = Decimal('4.3')
    outingbox_activity_3.votes = 2
    outingbox_activity_3.cost = 4
    outingbox_activity_3.person_of_contact = 'Mr. Ashish Bhardwaj'
    outingbox_activity_3.contact_numbers = ['0120-4247560', ' +91-8527991150']
    outingbox_activity_3.email = 'ashish@appughar.com'
    outingbox_activity_3.website = 'http://www.appugharexpress.com/bowling_bonanza.html'
    outingbox_activity_3.facebook = ''
    outingbox_activity_3.twitter = ''
    outingbox_activity_3.linkedin = ''
    outingbox_activity_3.featured_image = 'photos/activity/featured/img-1.JPG'
    outingbox_activity_3.save()

    outingbox_activity_3.category.add(outingbox_category_7)
    outingbox_activity_3.category.add(outingbox_category_8)

    outingbox_activity_4 = Activity()
    outingbox_activity_4.title = 'Jurasik Park Inn'
    outingbox_activity_4.url_name = 'jurasik-park-inn'
    outingbox_activity_4.address = outingbox_address_47
    outingbox_activity_4.description = ''
    outingbox_activity_4.rating = Decimal('4.6')
    outingbox_activity_4.votes = 1
    outingbox_activity_4.cost = 1
    outingbox_activity_4.person_of_contact = ''
    outingbox_activity_4.contact_numbers = ['08882388843', '01147082702', '01147082703 ']
    outingbox_activity_4.email = 'info@jurasikparkinn.com'
    outingbox_activity_4.website = 'http://www.jurasikparkinn.com'
    outingbox_activity_4.facebook = 'https://www.facebook.com/JurasikParkInn.Official'
    outingbox_activity_4.twitter = ''
    outingbox_activity_4.linkedin = ''
    outingbox_activity_4.featured_image = 'photos/activity/featured/img-5_wXJW06r.jpg'
    outingbox_activity_4.save()

    outingbox_activity_4.category.add(outingbox_category_28)
    outingbox_activity_4.category.add(outingbox_category_29)
    outingbox_activity_4.category.add(outingbox_category_30)

    outingbox_activity_5 = Activity()
    outingbox_activity_5.title = 'Essex Farms Future Bowl'
    outingbox_activity_5.url_name = 'essex-farms-future-bowl'
    outingbox_activity_5.address = outingbox_address_33
    outingbox_activity_5.description = ''
    outingbox_activity_5.rating = Decimal('3.2')
    outingbox_activity_5.votes = 1
    outingbox_activity_5.cost = 4
    outingbox_activity_5.person_of_contact = ''
    outingbox_activity_5.contact_numbers = ['9899003311', ' 01126528080']
    outingbox_activity_5.email = 'futurebowl@essexfarms.com'
    outingbox_activity_5.website = 'http://www.essexfarms.com/bowl.html'
    outingbox_activity_5.facebook = ''
    outingbox_activity_5.twitter = ''
    outingbox_activity_5.linkedin = ''
    outingbox_activity_5.featured_image = 'photos/activity/featured/img-2.png'
    outingbox_activity_5.save()

    outingbox_activity_5.category.add(outingbox_category_5)
    outingbox_activity_5.category.add(outingbox_category_7)
    outingbox_activity_5.category.add(outingbox_category_8)

    outingbox_activity_6 = Activity()
    outingbox_activity_6.title = 'Amoeba - Noida'
    outingbox_activity_6.url_name = 'amoeba-noida'
    outingbox_activity_6.address = outingbox_address_49
    outingbox_activity_6.description = ''
    outingbox_activity_6.rating = Decimal('3.7')
    outingbox_activity_6.votes = 1
    outingbox_activity_6.cost = 5
    outingbox_activity_6.person_of_contact = ''
    outingbox_activity_6.contact_numbers = ['0120-3128733', ' 0120-4366400']
    outingbox_activity_6.email = ''
    outingbox_activity_6.website = 'http://www.hmleisure.com/centre/details/amoeba-noida-spice-world'
    outingbox_activity_6.facebook = ''
    outingbox_activity_6.twitter = ''
    outingbox_activity_6.linkedin = ''
    outingbox_activity_6.featured_image = 'photos/activity/featured/img-1_u9KlBna.jpg'
    outingbox_activity_6.save()

    outingbox_activity_6.category.add(outingbox_category_5)
    outingbox_activity_6.category.add(outingbox_category_7)
    outingbox_activity_6.category.add(outingbox_category_8)

    outingbox_activity_7 = Activity()
    outingbox_activity_7.title = 'Worlds of Wonder'
    outingbox_activity_7.url_name = 'worlds-of-wonder'
    outingbox_activity_7.address = outingbox_address_1
    outingbox_activity_7.description = ''
    outingbox_activity_7.rating = Decimal('4.6')
    outingbox_activity_7.votes = 1
    outingbox_activity_7.cost = 3
    outingbox_activity_7.person_of_contact = ''
    outingbox_activity_7.contact_numbers = ['0120-4015011', '1800-103-1415']
    outingbox_activity_7.email = 'info@worldsofwonder.in'
    outingbox_activity_7.website = 'http://www.worldsofwonder.in'
    outingbox_activity_7.facebook = 'https://www.facebook.com/worldsofwonder'
    outingbox_activity_7.twitter = ''
    outingbox_activity_7.linkedin = ''
    outingbox_activity_7.featured_image = 'photos/activity/featured/img-8.png'
    outingbox_activity_7.save()

    outingbox_activity_7.category.add(outingbox_category_29)
    outingbox_activity_7.category.add(outingbox_category_30)

    outingbox_activity_8 = Activity()
    outingbox_activity_8.title = 'Wonder Speedway'
    outingbox_activity_8.url_name = 'wonder-speedway'
    outingbox_activity_8.address = outingbox_address_35
    outingbox_activity_8.description = ''
    outingbox_activity_8.rating = Decimal('1.8')
    outingbox_activity_8.votes = 1
    outingbox_activity_8.cost = 5
    outingbox_activity_8.person_of_contact = ''
    outingbox_activity_8.contact_numbers = ['9968146687', '0120-4650451']
    outingbox_activity_8.email = 'meher@wonderspeedway.com'
    outingbox_activity_8.website = 'http://wonderspeedway.com/'
    outingbox_activity_8.facebook = 'https://www.facebook.com/pages/Wonder-Speedway/1411637735732912'
    outingbox_activity_8.twitter = ''
    outingbox_activity_8.linkedin = ''
    outingbox_activity_8.featured_image = 'photos/activity/featured/img-1_hNL60oI.jpg'
    outingbox_activity_8.save()

    outingbox_activity_8.category.add(outingbox_category_28)

    outingbox_activity_9 = Activity()
    outingbox_activity_9.title = 'SPLASH-The Water Park'
    outingbox_activity_9.url_name = 'splash-the-water-park'
    outingbox_activity_9.address = outingbox_address_46
    outingbox_activity_9.description = ''
    outingbox_activity_9.rating = Decimal('2.7')
    outingbox_activity_9.votes = 1
    outingbox_activity_9.cost = 1
    outingbox_activity_9.person_of_contact = ''
    outingbox_activity_9.contact_numbers = ['01127708503', '9250055222']
    outingbox_activity_9.email = 'enquiry@splashwaterpark.co.in'
    outingbox_activity_9.website = 'http://www.splashwaterpark.co.in'
    outingbox_activity_9.facebook = ''
    outingbox_activity_9.twitter = ''
    outingbox_activity_9.linkedin = ''
    outingbox_activity_9.featured_image = 'photos/activity/featured/img-1.png'
    outingbox_activity_9.save()

    outingbox_activity_9.category.add(outingbox_category_29)
    outingbox_activity_9.category.add(outingbox_category_30)

    outingbox_activity_10 = Activity()
    outingbox_activity_10.title = 'BluO'
    outingbox_activity_10.url_name = 'bluo'
    outingbox_activity_10.address = outingbox_address_42
    outingbox_activity_10.description = ''
    outingbox_activity_10.rating = Decimal('2.0')
    outingbox_activity_10.votes = 1
    outingbox_activity_10.cost = 1
    outingbox_activity_10.person_of_contact = ''
    outingbox_activity_10.contact_numbers = ['9810270160']
    outingbox_activity_10.email = 'bluo.ambi@pvrbluo.com'
    outingbox_activity_10.website = 'http://www.pvrbluo.com/'
    outingbox_activity_10.facebook = ''
    outingbox_activity_10.twitter = ''
    outingbox_activity_10.linkedin = ''
    outingbox_activity_10.featured_image = 'photos/activity/featured/img-3_7Q3Y0ZH.jpg'
    outingbox_activity_10.save()

    outingbox_activity_10.category.add(outingbox_category_7)
    outingbox_activity_10.category.add(outingbox_category_8)

    outingbox_activity_11 = Activity()
    outingbox_activity_11.title = 'Drizzling Land'
    outingbox_activity_11.url_name = 'drizzling-land'
    outingbox_activity_11.address = outingbox_address_40
    outingbox_activity_11.description = ''
    outingbox_activity_11.rating = Decimal('0.5')
    outingbox_activity_11.votes = 1
    outingbox_activity_11.cost = 5
    outingbox_activity_11.person_of_contact = 'Mr. Manish Sharma'
    outingbox_activity_11.contact_numbers = ['0120-2675513', '0120-2675514', '09650597345', '09650597341 ']
    outingbox_activity_11.email = 'manish.trufill@gmail.com'
    outingbox_activity_11.website = 'http://www.drizzlingland.com/'
    outingbox_activity_11.facebook = ''
    outingbox_activity_11.twitter = ''
    outingbox_activity_11.linkedin = ''
    outingbox_activity_11.featured_image = 'photos/activity/featured/img-3.gif'
    outingbox_activity_11.save()

    outingbox_activity_11.category.add(outingbox_category_29)
    outingbox_activity_11.category.add(outingbox_category_30)

    outingbox_activity_12 = Activity()
    outingbox_activity_12.title = 'Amoeba - Gurgaon'
    outingbox_activity_12.url_name = 'amoeba-gurgaon'
    outingbox_activity_12.address = outingbox_address_39
    outingbox_activity_12.description = 'Amoeba is a complete family entertainer, providing bowling, a playground, and an arcade'
    outingbox_activity_12.rating = Decimal('4.9')
    outingbox_activity_12.votes = 1
    outingbox_activity_12.cost = 3
    outingbox_activity_12.person_of_contact = 'Surender'
    outingbox_activity_12.contact_numbers = ['08742983884', '01244265892']
    outingbox_activity_12.email = 'joy.amoeba@gmail.com'
    outingbox_activity_12.website = 'http://www.hmleisure.com/'
    outingbox_activity_12.facebook = ''
    outingbox_activity_12.twitter = ''
    outingbox_activity_12.linkedin = ''
    outingbox_activity_12.featured_image = 'photos/activity/featured/img-1_ed8AFsk.JPG'
    outingbox_activity_12.save()

    outingbox_activity_12.category.add(outingbox_category_5)
    outingbox_activity_12.category.add(outingbox_category_7)

    outingbox_activity_13 = Activity()
    outingbox_activity_13.title = 'OYSTERS Beach Park-Appu Ghar'
    outingbox_activity_13.url_name = 'oysters-beach-park-appu-ghar'
    outingbox_activity_13.address = outingbox_address_38
    outingbox_activity_13.description = ''
    outingbox_activity_13.rating = Decimal('3.7')
    outingbox_activity_13.votes = 1
    outingbox_activity_13.cost = 1
    outingbox_activity_13.person_of_contact = ''
    outingbox_activity_13.contact_numbers = ['01244891000 ']
    outingbox_activity_13.email = 'branding@appughar.com'
    outingbox_activity_13.website = 'http://www.oystersbeach.com'
    outingbox_activity_13.facebook = 'https://www.facebook.com/oystersappughar'
    outingbox_activity_13.twitter = ''
    outingbox_activity_13.linkedin = ''
    outingbox_activity_13.featured_image = 'photos/activity/featured/img-1_6lAXl0N.jpg'
    outingbox_activity_13.save()

    outingbox_activity_13.category.add(outingbox_category_30)

    outingbox_activity_14 = Activity()
    outingbox_activity_14.title = '32nd Milestone'
    outingbox_activity_14.url_name = '32nd-milestone'
    outingbox_activity_14.address = outingbox_address_36
    outingbox_activity_14.description = ''
    outingbox_activity_14.rating = Decimal('2.4')
    outingbox_activity_14.votes = 1
    outingbox_activity_14.cost = 5
    outingbox_activity_14.person_of_contact = 'Mr. Ayush Tiwari'
    outingbox_activity_14.contact_numbers = ['07838294041', '01244870400']
    outingbox_activity_14.email = 'ayush.tiwari@32ndmilestone.com'
    outingbox_activity_14.website = 'http://www.32ndmilestone.com/'
    outingbox_activity_14.facebook = ''
    outingbox_activity_14.twitter = ''
    outingbox_activity_14.linkedin = ''
    outingbox_activity_14.featured_image = 'photos/activity/featured/img-11.jpg'
    outingbox_activity_14.save()

    outingbox_activity_14.category.add(outingbox_category_7)
    outingbox_activity_14.category.add(outingbox_category_28)

    outingbox_activity_15 = Activity()
    outingbox_activity_15.title = 'City Bowl'
    outingbox_activity_15.url_name = 'city-bowl'
    outingbox_activity_15.address = outingbox_address_2
    outingbox_activity_15.description = ''
    outingbox_activity_15.rating = Decimal('3.0')
    outingbox_activity_15.votes = 1
    outingbox_activity_15.cost = 3
    outingbox_activity_15.person_of_contact = 'Raanti Dev Gupta'
    outingbox_activity_15.contact_numbers = ['01294315317', '09810002980']
    outingbox_activity_15.email = 'raanti@citybowlindia.com'
    outingbox_activity_15.website = 'http://www.citybowlindia.com'
    outingbox_activity_15.facebook = ''
    outingbox_activity_15.twitter = ''
    outingbox_activity_15.linkedin = ''
    outingbox_activity_15.featured_image = 'photos/activity/featured/img-1_px4WhgU.jpg'
    outingbox_activity_15.save()

    outingbox_activity_15.category.add(outingbox_category_7)
    outingbox_activity_15.category.add(outingbox_category_8)

    outingbox_activity_16 = Activity()
    outingbox_activity_16.title = 'Aapno Ghar Amusement & Water Park'
    outingbox_activity_16.url_name = 'aapno-ghar-amusement-water-park'
    outingbox_activity_16.address = outingbox_address_50
    outingbox_activity_16.description = ''
    outingbox_activity_16.rating = Decimal('2.6')
    outingbox_activity_16.votes = 1
    outingbox_activity_16.cost = 1
    outingbox_activity_16.person_of_contact = 'Mr. Ravi'
    outingbox_activity_16.contact_numbers = ['01242371281', '9717283535', '9650687778']
    outingbox_activity_16.email = 'info@aapnoghar.com'
    outingbox_activity_16.website = 'http://www.aapnoghar.com'
    outingbox_activity_16.facebook = ''
    outingbox_activity_16.twitter = ''
    outingbox_activity_16.linkedin = ''
    outingbox_activity_16.featured_image = 'photos/activity/featured/img-2.jpg'
    outingbox_activity_16.save()

    outingbox_activity_16.category.add(outingbox_category_29)
    outingbox_activity_16.category.add(outingbox_category_30)

    outingbox_activity_17 = Activity()
    outingbox_activity_17.title = 'Shootout Zone'
    outingbox_activity_17.url_name = 'shootout-zone'
    outingbox_activity_17.address = outingbox_address_34
    outingbox_activity_17.description = ''
    outingbox_activity_17.rating = Decimal('0.6')
    outingbox_activity_17.votes = 1
    outingbox_activity_17.cost = 5
    outingbox_activity_17.person_of_contact = 'Sanjeet Dagar'
    outingbox_activity_17.contact_numbers = ['09810012506', '09811007094']
    outingbox_activity_17.email = 'dagarsanjeet6@gmail.com'
    outingbox_activity_17.website = 'http://www.shootoutzone.com'
    outingbox_activity_17.facebook = ''
    outingbox_activity_17.twitter = ''
    outingbox_activity_17.linkedin = ''
    outingbox_activity_17.featured_image = 'photos/activity/featured/img-1_WhoQIMQ.jpg'
    outingbox_activity_17.save()

    outingbox_activity_17.category.add(outingbox_category_4)

    outingbox_activity_18 = Activity()
    outingbox_activity_18.title = 'Club Platinum Resort'
    outingbox_activity_18.url_name = 'club-platinum-resort'
    outingbox_activity_18.address = outingbox_address_6
    outingbox_activity_18.description = ''
    outingbox_activity_18.rating = Decimal('1.6')
    outingbox_activity_18.votes = 1
    outingbox_activity_18.cost = 2
    outingbox_activity_18.person_of_contact = 'Mr. Udit Chadha'
    outingbox_activity_18.contact_numbers = ['8447693142']
    outingbox_activity_18.email = 'clubplatinumresort@gmail.com'
    outingbox_activity_18.website = 'http://www.clubplatinumresorts.com'
    outingbox_activity_18.facebook = ''
    outingbox_activity_18.twitter = ''
    outingbox_activity_18.linkedin = ''
    outingbox_activity_18.featured_image = 'photos/activity/featured/img-4_0dFGJTQ.jpg'
    outingbox_activity_18.save()

    outingbox_activity_18.category.add(outingbox_category_29)
    outingbox_activity_18.category.add(outingbox_category_30)

    outingbox_activity_19 = Activity()
    outingbox_activity_19.title = 'Fun N Food Village'
    outingbox_activity_19.url_name = 'fun-n-food-village'
    outingbox_activity_19.address = outingbox_address_41
    outingbox_activity_19.description = ''
    outingbox_activity_19.rating = Decimal('4.5')
    outingbox_activity_19.votes = 1
    outingbox_activity_19.cost = 3
    outingbox_activity_19.person_of_contact = 'Vijay Gupta'
    outingbox_activity_19.contact_numbers = ['011-43260099', ' +91-9990006521', ' +91-9990006522']
    outingbox_activity_19.email = 'info.delhi@funnfood.com'
    outingbox_activity_19.website = 'http://www.funnfood.com'
    outingbox_activity_19.facebook = 'https://www.facebook.com/FunNFoodVillage'
    outingbox_activity_19.twitter = ''
    outingbox_activity_19.linkedin = ''
    outingbox_activity_19.featured_image = 'photos/activity/featured/img-6.jpg'
    outingbox_activity_19.save()

    outingbox_activity_19.category.add(outingbox_category_29)
    outingbox_activity_19.category.add(outingbox_category_30)

    outingbox_activity_20 = Activity()
    outingbox_activity_20.title = 'Just Chill Water Park'
    outingbox_activity_20.url_name = 'just-chill-water-park'
    outingbox_activity_20.address = outingbox_address_44
    outingbox_activity_20.description = ''
    outingbox_activity_20.rating = Decimal('2.0')
    outingbox_activity_20.votes = 1
    outingbox_activity_20.cost = 3
    outingbox_activity_20.person_of_contact = 'Mr. Amit'
    outingbox_activity_20.contact_numbers = ['09910499774 ']
    outingbox_activity_20.email = 'justchillwp@gmail.com'
    outingbox_activity_20.website = 'http://www.justchillwaterpark.com'
    outingbox_activity_20.facebook = 'https://www.facebook.com/justchillwaterpark?rf=154117894729340'
    outingbox_activity_20.twitter = ''
    outingbox_activity_20.linkedin = ''
    outingbox_activity_20.featured_image = 'photos/activity/featured/img-5.jpg'
    outingbox_activity_20.save()

    outingbox_activity_20.category.add(outingbox_category_29)
    outingbox_activity_20.category.add(outingbox_category_30)

    outingbox_activity_21 = Activity()
    outingbox_activity_21.title = 'Adventure Island'
    outingbox_activity_21.url_name = 'adventure-island'
    outingbox_activity_21.address = outingbox_address_37
    outingbox_activity_21.description = "Spread over 62 acres of sprawling land. Adventure Island is India's 1st world-class amusement park. Adventure Island has features that attract people from far and wide with amazing rides, a picturesque lake , rain dance , magic show and lot more!"
    outingbox_activity_21.rating = Decimal('2.8')
    outingbox_activity_21.votes = 1
    outingbox_activity_21.cost = 1
    outingbox_activity_21.person_of_contact = ''
    outingbox_activity_21.contact_numbers = ['01147041111']
    outingbox_activity_21.email = 'frontoffice@uaplindia.com'
    outingbox_activity_21.website = ''
    outingbox_activity_21.facebook = 'https://www.facebook.com/funatadventureisland/info?tab=overview'
    outingbox_activity_21.twitter = ''
    outingbox_activity_21.linkedin = ''
    outingbox_activity_21.featured_image = 'photos/activity/featured/img-2_hjcJT62.jpg'
    outingbox_activity_21.save()

    outingbox_activity_21.category.add(outingbox_category_29)

    outingbox_activity_22 = Activity()
    outingbox_activity_22.title = 'Skittle Bowling Arena'
    outingbox_activity_22.url_name = 'skittle-bowling-arena'
    outingbox_activity_22.address = outingbox_address_43
    outingbox_activity_22.description = ''
    outingbox_activity_22.rating = Decimal('0.9')
    outingbox_activity_22.votes = 1
    outingbox_activity_22.cost = 5
    outingbox_activity_22.person_of_contact = ''
    outingbox_activity_22.contact_numbers = ['09711615321', '01204291729']
    outingbox_activity_22.email = 'play@skittlebowling.com'
    outingbox_activity_22.website = 'http://www.skittlebowling.com'
    outingbox_activity_22.facebook = ''
    outingbox_activity_22.twitter = ''
    outingbox_activity_22.linkedin = ''
    outingbox_activity_22.featured_image = 'photos/activity/featured/img-4_2jwipw0.jpg'
    outingbox_activity_22.save()

    outingbox_activity_22.category.add(outingbox_category_5)
    outingbox_activity_22.category.add(outingbox_category_7)
    outingbox_activity_22.category.add(outingbox_category_8)

    outingbox_activity_23 = Activity()
    outingbox_activity_23.title = 'F.o.G - Federation of Gamers'
    outingbox_activity_23.url_name = 'fog-federation-of-gamers'
    outingbox_activity_23.address = outingbox_address_28
    outingbox_activity_23.description = "F.o.G (Federation of Gamers) is a gaming lounge where casual gamers can come to play the latest games on the newest consoles hooked upto big HD TV's. Along with gaming we have a small café where we serve French Fries, Chicken Nuggets, Pasta, Sandwiches etc. \r\n\r\nF.o.G has been the destination of choice for many birthday parties, for which we have tailor-made food and gaming packages. \r\n\r\nAs a gaming destination our aim has been to promote gaming amongst the youth and thus host gaming tournaments every month at F.o.G. Participants can compete with other avid gamers to stand a chance to take home a sizable prize. \r\n\r\nStandard Pricing: Rs.60/per 10mins/ per person \r\n\r\nFood and Gaming Combos (starting at): Rs. 440/per person \r\n\r\nBirthday Packages (gaming + food): Rs.700/per person"
    outingbox_activity_23.rating = Decimal('0.0')
    outingbox_activity_23.votes = 1
    outingbox_activity_23.cost = 5
    outingbox_activity_23.person_of_contact = 'Ganesh Tripathi'
    outingbox_activity_23.contact_numbers = ['0114632360']
    outingbox_activity_23.email = 'info@thefog.in'
    outingbox_activity_23.website = 'http://thefog.in/'
    outingbox_activity_23.facebook = 'https://www.facebook.com/fedgamers?ref=settings'
    outingbox_activity_23.twitter = ''
    outingbox_activity_23.linkedin = ''
    outingbox_activity_23.featured_image = 'photos/activity/featured/featured.png'
    outingbox_activity_23.save()

    outingbox_activity_23.category.add(outingbox_category_5)

    outingbox_activity_24 = Activity()
    outingbox_activity_24.title = 'Kedarnath Centre for Yoga and Naturopathy'
    outingbox_activity_24.url_name = 'kedarnath-centre-for-yoga-and-naturopathy'
    outingbox_activity_24.address = outingbox_address_13
    outingbox_activity_24.description = ''
    outingbox_activity_24.rating = Decimal('4.7')
    outingbox_activity_24.votes = 1
    outingbox_activity_24.cost = 5
    outingbox_activity_24.person_of_contact = ''
    outingbox_activity_24.contact_numbers = ['09810281808', '09971848805']
    outingbox_activity_24.email = 'contact@kedarnathyoga.com'
    outingbox_activity_24.website = 'http://www.kedarnathyoga.com'
    outingbox_activity_24.facebook = 'https://www.facebook.com/pages/Kedarnath-yoga-centre/466565750123432'
    outingbox_activity_24.twitter = 'https://twitter.com/yogaathomeindia'
    outingbox_activity_24.linkedin = ''
    outingbox_activity_24.featured_image = 'photos/activity/featured/img-4_oUIaZRj.jpg'
    outingbox_activity_24.save()

    outingbox_activity_24.category.add(outingbox_category_12)
    outingbox_activity_24.category.add(outingbox_category_13)

    outingbox_activity_25 = Activity()
    outingbox_activity_25.title = 'Fun N Fair'
    outingbox_activity_25.url_name = 'fun-n-fair'
    outingbox_activity_25.address = outingbox_address_25
    outingbox_activity_25.description = ''
    outingbox_activity_25.rating = Decimal('1.2')
    outingbox_activity_25.votes = 1
    outingbox_activity_25.cost = 5
    outingbox_activity_25.person_of_contact = ''
    outingbox_activity_25.contact_numbers = ['01126959563', '01126959591', '09555673242']
    outingbox_activity_25.email = 'funnfair11@gmail.com'
    outingbox_activity_25.website = 'http://www.fun-fair.qapacity.com/'
    outingbox_activity_25.facebook = 'https://www.facebook.com/funnfair'
    outingbox_activity_25.twitter = ''
    outingbox_activity_25.linkedin = ''
    outingbox_activity_25.featured_image = 'photos/activity/featured/img-3_mn5h1CP.jpg'
    outingbox_activity_25.save()

    outingbox_activity_25.category.add(outingbox_category_5)
    outingbox_activity_25.category.add(outingbox_category_7)
    outingbox_activity_25.category.add(outingbox_category_8)

    outingbox_activity_26 = Activity()
    outingbox_activity_26.title = 'Arnos Den'
    outingbox_activity_26.url_name = 'arnos-den'
    outingbox_activity_26.address = outingbox_address_19
    outingbox_activity_26.description = ''
    outingbox_activity_26.rating = Decimal('3.1')
    outingbox_activity_26.votes = 1
    outingbox_activity_26.cost = 5
    outingbox_activity_26.person_of_contact = ''
    outingbox_activity_26.contact_numbers = ['09910994870']
    outingbox_activity_26.email = 'anjali@arnosden.com'
    outingbox_activity_26.website = ''
    outingbox_activity_26.facebook = ''
    outingbox_activity_26.twitter = ''
    outingbox_activity_26.linkedin = ''
    outingbox_activity_26.featured_image = 'photos/activity/featured/img-1_mUoQyM6.jpg'
    outingbox_activity_26.save()

    outingbox_activity_26.category.add(outingbox_category_8)

    outingbox_activity_27 = Activity()
    outingbox_activity_27.title = 'F9 Go Karting'
    outingbox_activity_27.url_name = 'f9-go-karting'
    outingbox_activity_27.address = outingbox_address_32
    outingbox_activity_27.description = ''
    outingbox_activity_27.rating = Decimal('4.3')
    outingbox_activity_27.votes = 1
    outingbox_activity_27.cost = 5
    outingbox_activity_27.person_of_contact = 'S.K. Tyagi '
    outingbox_activity_27.contact_numbers = ['09818048655', '08826738655']
    outingbox_activity_27.email = 'f9gokarting@gmail.com'
    outingbox_activity_27.website = 'http://www.f9gokarting.com/'
    outingbox_activity_27.facebook = 'https://www.facebook.com/pages/F9-Go-Karting/644569965648721?fref=ts'
    outingbox_activity_27.twitter = ''
    outingbox_activity_27.linkedin = ''
    outingbox_activity_27.featured_image = 'photos/activity/featured/img-3.JPG'
    outingbox_activity_27.save()

    outingbox_activity_27.category.add(outingbox_category_28)

    outingbox_activity_28 = Activity()
    outingbox_activity_28.title = 'Glued Entertainment'
    outingbox_activity_28.url_name = 'glued-entertainment'
    outingbox_activity_28.address = outingbox_address_23
    outingbox_activity_28.description = 'Glued, Gaming and Sports Lounge, is an unusual combination of gaming ,sports & entertainment offering its customer’s a break, TO LIVE FOR !!'
    outingbox_activity_28.rating = Decimal('1.3')
    outingbox_activity_28.votes = 1
    outingbox_activity_28.cost = 4
    outingbox_activity_28.person_of_contact = ''
    outingbox_activity_28.contact_numbers = ['09891339974']
    outingbox_activity_28.email = ''
    outingbox_activity_28.website = ''
    outingbox_activity_28.facebook = 'https://www.facebook.com/gluednoida'
    outingbox_activity_28.twitter = ''
    outingbox_activity_28.linkedin = ''
    outingbox_activity_28.featured_image = 'photos/activity/featured/img-8.jpeg'
    outingbox_activity_28.save()

    outingbox_activity_28.category.add(outingbox_category_5)
    outingbox_activity_28.category.add(outingbox_category_7)
    outingbox_activity_28.category.add(outingbox_category_8)

    outingbox_activity_29 = Activity()
    outingbox_activity_29.title = 'AtreYoga Studio'
    outingbox_activity_29.url_name = 'atreyoga-studio'
    outingbox_activity_29.address = outingbox_address_29
    outingbox_activity_29.description = ''
    outingbox_activity_29.rating = Decimal('2.0')
    outingbox_activity_29.votes = 1
    outingbox_activity_29.cost = 4
    outingbox_activity_29.person_of_contact = ''
    outingbox_activity_29.contact_numbers = ['09958937036']
    outingbox_activity_29.email = 'info@atreyogastudio.com'
    outingbox_activity_29.website = 'http://www.atreyogastudio.com'
    outingbox_activity_29.facebook = 'https://www.facebook.com/atreyogastudio?ref=br_rs'
    outingbox_activity_29.twitter = ''
    outingbox_activity_29.linkedin = ''
    outingbox_activity_29.featured_image = 'photos/activity/featured/img-1_7FY9X9g.jpg'
    outingbox_activity_29.save()

    outingbox_activity_29.category.add(outingbox_category_13)

    outingbox_activity_30 = Activity()
    outingbox_activity_30.title = 'Bikram Yoga '
    outingbox_activity_30.url_name = 'bikram-yoga'
    outingbox_activity_30.address = outingbox_address_48
    outingbox_activity_30.description = ''
    outingbox_activity_30.rating = Decimal('2.0')
    outingbox_activity_30.votes = 1
    outingbox_activity_30.cost = 3
    outingbox_activity_30.person_of_contact = ''
    outingbox_activity_30.contact_numbers = ['09650020333']
    outingbox_activity_30.email = ''
    outingbox_activity_30.website = 'http://www.bikramyoga.com'
    outingbox_activity_30.facebook = 'https://www.facebook.com/bikramyogadelhi?ref=br_rs'
    outingbox_activity_30.twitter = ''
    outingbox_activity_30.linkedin = ''
    outingbox_activity_30.featured_image = 'photos/activity/featured/bikramyoga2.jpg'
    outingbox_activity_30.save()

    outingbox_activity_30.category.add(outingbox_category_13)

    outingbox_activity_31 = Activity()
    outingbox_activity_31.title = 'Fun Zone'
    outingbox_activity_31.url_name = 'fun-zone'
    outingbox_activity_31.address = outingbox_address_20
    outingbox_activity_31.description = ''
    outingbox_activity_31.rating = Decimal('4.0')
    outingbox_activity_31.votes = 1
    outingbox_activity_31.cost = 1
    outingbox_activity_31.person_of_contact = 'Mr. Raj'
    outingbox_activity_31.contact_numbers = ['09211699658']
    outingbox_activity_31.email = 'melodieskidszone25@yahoo.com'
    outingbox_activity_31.website = ''
    outingbox_activity_31.facebook = ''
    outingbox_activity_31.twitter = ''
    outingbox_activity_31.linkedin = ''
    outingbox_activity_31.featured_image = 'photos/activity/featured/featured.png'
    outingbox_activity_31.save()

    outingbox_activity_31.category.add(outingbox_category_5)

    outingbox_activity_32 = Activity()
    outingbox_activity_32.title = 'Rockshot Paintball Sports'
    outingbox_activity_32.url_name = 'rockshot-paintball-sports'
    outingbox_activity_32.address = outingbox_address_52
    outingbox_activity_32.description = ''
    outingbox_activity_32.rating = Decimal('4.2')
    outingbox_activity_32.votes = 1
    outingbox_activity_32.cost = 3
    outingbox_activity_32.person_of_contact = 'Akash Thapa'
    outingbox_activity_32.contact_numbers = ['9818215877']
    outingbox_activity_32.email = 'rockshotpaintballsportsco@gmail.com'
    outingbox_activity_32.website = 'http://www.rockshotpaintballsports.com'
    outingbox_activity_32.facebook = 'https://www.facebook.com/pages/Rockshot-Paintball-Sports/502558346441184'
    outingbox_activity_32.twitter = ''
    outingbox_activity_32.linkedin = ''
    outingbox_activity_32.featured_image = 'photos/activity/featured/img-5_rpvWFc9.jpg'
    outingbox_activity_32.save()

    outingbox_activity_32.category.add(outingbox_category_4)

    outingbox_activity_33 = Activity()
    outingbox_activity_33.title = 'Planet Bowling'
    outingbox_activity_33.url_name = 'planet-bowling'
    outingbox_activity_33.address = outingbox_address_24
    outingbox_activity_33.description = ''
    outingbox_activity_33.rating = Decimal('4.0')
    outingbox_activity_33.votes = 2
    outingbox_activity_33.cost = 1
    outingbox_activity_33.person_of_contact = ''
    outingbox_activity_33.contact_numbers = ['01126959563', '01126959665']
    outingbox_activity_33.email = ''
    outingbox_activity_33.website = ''
    outingbox_activity_33.facebook = ''
    outingbox_activity_33.twitter = ''
    outingbox_activity_33.linkedin = ''
    outingbox_activity_33.featured_image = 'photos/activity/featured/featured.png'
    outingbox_activity_33.save()

    outingbox_activity_33.category.add(outingbox_category_7)
    outingbox_activity_33.category.add(outingbox_category_8)

    outingbox_activity_34 = Activity()
    outingbox_activity_34.title = 'Big Dance Center'
    outingbox_activity_34.url_name = 'big-dance-center'
    outingbox_activity_34.address = outingbox_address_21
    outingbox_activity_34.description = ''
    outingbox_activity_34.rating = Decimal('2.8')
    outingbox_activity_34.votes = 2
    outingbox_activity_34.cost = 4
    outingbox_activity_34.person_of_contact = ''
    outingbox_activity_34.contact_numbers = ['01147090148', '01147090149', '01147090150']
    outingbox_activity_34.email = 'info@bigdancecentre.com'
    outingbox_activity_34.website = 'http://www.bigdancecentre.com'
    outingbox_activity_34.facebook = 'http://www.facebook.com/bigdancecentreindia'
    outingbox_activity_34.twitter = 'https://twitter.com/bigdancecentre'
    outingbox_activity_34.linkedin = ''
    outingbox_activity_34.featured_image = 'photos/activity/featured/Screen_Shot_2016-02-20_at_6.32.55_PM.png'
    outingbox_activity_34.save()

    outingbox_activity_34.category.add(outingbox_category_26)
    outingbox_activity_34.category.add(outingbox_category_16)
    outingbox_activity_34.category.add(outingbox_category_17)
    outingbox_activity_34.category.add(outingbox_category_18)
    outingbox_activity_34.category.add(outingbox_category_19)
    outingbox_activity_34.category.add(outingbox_category_25)

    outingbox_activity_35 = Activity()
    outingbox_activity_35.title = 'Sivananda Yoga '
    outingbox_activity_35.url_name = 'sivananda-yoga'
    outingbox_activity_35.address = outingbox_address_12
    outingbox_activity_35.description = ''
    outingbox_activity_35.rating = Decimal('0.8')
    outingbox_activity_35.votes = 1
    outingbox_activity_35.cost = 4
    outingbox_activity_35.person_of_contact = ''
    outingbox_activity_35.contact_numbers = ['011–32069070', '011-29230962', '08860954455']
    outingbox_activity_35.email = 'delhi@sivananda.org'
    outingbox_activity_35.website = 'http://www.sivananda.org.in/delhi/'
    outingbox_activity_35.facebook = 'http://www.facebook.com/sivanandayoga.9.newdelhi'
    outingbox_activity_35.twitter = ''
    outingbox_activity_35.linkedin = ''
    outingbox_activity_35.featured_image = 'photos/activity/featured/img-6_XngWzU9.jpg'
    outingbox_activity_35.save()

    outingbox_activity_35.category.add(outingbox_category_13)

    outingbox_activity_36 = Activity()
    outingbox_activity_36.title = 'Flyboy'
    outingbox_activity_36.url_name = 'flyboy'
    outingbox_activity_36.address = outingbox_address_22
    outingbox_activity_36.description = ''
    outingbox_activity_36.rating = Decimal('1.8')
    outingbox_activity_36.votes = 1
    outingbox_activity_36.cost = 1
    outingbox_activity_36.person_of_contact = 'Mr. Shantanu'
    outingbox_activity_36.contact_numbers = ['09871510510']
    outingbox_activity_36.email = 'info@flyboy.in'
    outingbox_activity_36.website = 'http://www.flyboy.in/'
    outingbox_activity_36.facebook = 'https://www.facebook.com/pages/Flyboy-Aviation/263546580354464'
    outingbox_activity_36.twitter = 'https://twitter.com/flyboyaviation'
    outingbox_activity_36.linkedin = ''
    outingbox_activity_36.featured_image = 'photos/activity/featured/dscn4087.jpg'
    outingbox_activity_36.save()

    outingbox_activity_36.category.add(outingbox_category_2)
    outingbox_activity_36.category.add(outingbox_category_3)

    outingbox_activity_37 = Activity()
    outingbox_activity_37.title = 'Pool World'
    outingbox_activity_37.url_name = 'pool-world'
    outingbox_activity_37.address = outingbox_address_51
    outingbox_activity_37.description = 'Pool World is based in M Block market of Greater Kailash, 2 of Delhi. They conduct classes for Pool & Snooker both. However, the cost of coaching is on per hour basis and it is open 7 days a week.'
    outingbox_activity_37.rating = Decimal('0.3')
    outingbox_activity_37.votes = 1
    outingbox_activity_37.cost = 2
    outingbox_activity_37.person_of_contact = ''
    outingbox_activity_37.contact_numbers = ['09891545424']
    outingbox_activity_37.email = ''
    outingbox_activity_37.website = ''
    outingbox_activity_37.facebook = ''
    outingbox_activity_37.twitter = ''
    outingbox_activity_37.linkedin = ''
    outingbox_activity_37.featured_image = 'photos/activity/featured/glued-pool.jpg'
    outingbox_activity_37.save()

    outingbox_activity_37.category.add(outingbox_category_8)

    outingbox_activity_38 = Activity()
    outingbox_activity_38.title = 'Universal Yoga Group'
    outingbox_activity_38.url_name = 'universal-yoga-group'
    outingbox_activity_38.address = outingbox_address_10
    outingbox_activity_38.description = ''
    outingbox_activity_38.rating = Decimal('3.2')
    outingbox_activity_38.votes = 1
    outingbox_activity_38.cost = 4
    outingbox_activity_38.person_of_contact = ''
    outingbox_activity_38.contact_numbers = ['09350070549']
    outingbox_activity_38.email = 'info@universalyoga.in'
    outingbox_activity_38.website = 'http://www.universalyoga.in'
    outingbox_activity_38.facebook = 'https://www.facebook.com/UniversalYogaGroup'
    outingbox_activity_38.twitter = ''
    outingbox_activity_38.linkedin = ''
    outingbox_activity_38.featured_image = 'photos/activity/featured/img-3_mxYJvWv.jpg'
    outingbox_activity_38.save()

    outingbox_activity_38.category.add(outingbox_category_13)

    outingbox_activity_39 = Activity()
    outingbox_activity_39.title = 'Dhoomimal Art Centre'
    outingbox_activity_39.url_name = 'dhoomimal-art-centre'
    outingbox_activity_39.address = outingbox_address_4
    outingbox_activity_39.description = ''
    outingbox_activity_39.rating = Decimal('4.3')
    outingbox_activity_39.votes = 1
    outingbox_activity_39.cost = 4
    outingbox_activity_39.person_of_contact = ''
    outingbox_activity_39.contact_numbers = ['011-23324492', '011-23713025', '011-4151617']
    outingbox_activity_39.email = 'info@dhoomimalartcentre.com'
    outingbox_activity_39.website = 'http://www.dhoomimalartcentre.com'
    outingbox_activity_39.facebook = 'http://www.facebook.com/DhoomimalGallery'
    outingbox_activity_39.twitter = ''
    outingbox_activity_39.linkedin = ''
    outingbox_activity_39.featured_image = 'photos/activity/featured/slide-four.jpg'
    outingbox_activity_39.save()

    outingbox_activity_39.category.add(outingbox_category_6)

    outingbox_activity_40 = Activity()
    outingbox_activity_40.title = 'Universal Yoga Group'
    outingbox_activity_40.url_name = 'universal-yoga-group'
    outingbox_activity_40.address = outingbox_address_14
    outingbox_activity_40.description = ''
    outingbox_activity_40.rating = Decimal('3.9')
    outingbox_activity_40.votes = 1
    outingbox_activity_40.cost = 5
    outingbox_activity_40.person_of_contact = ''
    outingbox_activity_40.contact_numbers = ['09350070549']
    outingbox_activity_40.email = 'info@universalyoga.in'
    outingbox_activity_40.website = 'http://www.universalyoga.in/'
    outingbox_activity_40.facebook = 'https://www.facebook.com/UniversalYogaGroup'
    outingbox_activity_40.twitter = ''
    outingbox_activity_40.linkedin = ''
    outingbox_activity_40.featured_image = 'photos/activity/featured/283048_256487204378000_4704371_n.jpg'
    outingbox_activity_40.save()

    outingbox_activity_40.category.add(outingbox_category_13)

    outingbox_activity_41 = Activity()
    outingbox_activity_41.title = 'The Pilates Studio'
    outingbox_activity_41.url_name = 'the-pilates-studio'
    outingbox_activity_41.address = outingbox_address_9
    outingbox_activity_41.description = ''
    outingbox_activity_41.rating = Decimal('4.5')
    outingbox_activity_41.votes = 1
    outingbox_activity_41.cost = 4
    outingbox_activity_41.person_of_contact = ''
    outingbox_activity_41.contact_numbers = ['09811202480']
    outingbox_activity_41.email = ''
    outingbox_activity_41.website = ''
    outingbox_activity_41.facebook = 'https://www.facebook.com/pages/The-Pilates-StudioNew-Delhi/221975111200344?ref=br_rs'
    outingbox_activity_41.twitter = ''
    outingbox_activity_41.linkedin = ''
    outingbox_activity_41.featured_image = 'photos/activity/featured/10645310_980910568640124_8347948851935456579_n.jpg'
    outingbox_activity_41.save()

    outingbox_activity_41.category.add(outingbox_category_11)
    outingbox_activity_41.category.add(outingbox_category_13)

    outingbox_activity_42 = Activity()
    outingbox_activity_42.title = 'The Yoga Studio'
    outingbox_activity_42.url_name = 'the-yoga-studio'
    outingbox_activity_42.address = outingbox_address_15
    outingbox_activity_42.description = ''
    outingbox_activity_42.rating = Decimal('0.1')
    outingbox_activity_42.votes = 1
    outingbox_activity_42.cost = 3
    outingbox_activity_42.person_of_contact = ''
    outingbox_activity_42.contact_numbers = ['09811131368', '09899950200']
    outingbox_activity_42.email = 'contact@theyogastudio.info'
    outingbox_activity_42.website = 'http://www.theyogastudio.info/'
    outingbox_activity_42.facebook = 'https://www.facebook.com/seemasondhiyogastudio'
    outingbox_activity_42.twitter = ''
    outingbox_activity_42.linkedin = ''
    outingbox_activity_42.featured_image = 'photos/activity/featured/img-4_cjPDMAU.jpg'
    outingbox_activity_42.save()

    outingbox_activity_42.category.add(outingbox_category_13)

    outingbox_activity_43 = Activity()
    outingbox_activity_43.title = 'Vadhera Art Gallery'
    outingbox_activity_43.url_name = 'vadhera-art-gallery'
    outingbox_activity_43.address = outingbox_address_58
    outingbox_activity_43.description = ''
    outingbox_activity_43.rating = Decimal('4.5')
    outingbox_activity_43.votes = 1
    outingbox_activity_43.cost = 2
    outingbox_activity_43.person_of_contact = ''
    outingbox_activity_43.contact_numbers = ['011-24622545', '011-24615368']
    outingbox_activity_43.email = 'art@vadehraart.com'
    outingbox_activity_43.website = 'http://www.vadehraart.com/'
    outingbox_activity_43.facebook = 'https://www.facebook.com/vadehraart'
    outingbox_activity_43.twitter = ''
    outingbox_activity_43.linkedin = ''
    outingbox_activity_43.featured_image = 'photos/activity/featured/featured.png'
    outingbox_activity_43.save()

    outingbox_activity_43.category.add(outingbox_category_6)

    outingbox_activity_44 = Activity()
    outingbox_activity_44.title = 'Visual Arts Gallery'
    outingbox_activity_44.url_name = 'visual-arts-gallery'
    outingbox_activity_44.address = outingbox_address_56
    outingbox_activity_44.description = ''
    outingbox_activity_44.rating = Decimal('0.4')
    outingbox_activity_44.votes = 1
    outingbox_activity_44.cost = 5
    outingbox_activity_44.person_of_contact = ''
    outingbox_activity_44.contact_numbers = ['011-43662024']
    outingbox_activity_44.email = 'habitatworld@oldworldhospitality.com'
    outingbox_activity_44.website = 'http://www.indiahabitat.org/vag'
    outingbox_activity_44.facebook = 'https://www.facebook.com/pages/Visual-Arts-Gallery/526772930797596'
    outingbox_activity_44.twitter = ''
    outingbox_activity_44.linkedin = ''
    outingbox_activity_44.featured_image = 'photos/activity/featured/art-gallery.jpg'
    outingbox_activity_44.save()

    outingbox_activity_44.category.add(outingbox_category_6)

    outingbox_activity_45 = Activity()
    outingbox_activity_45.title = 'Versus Gaming Zone'
    outingbox_activity_45.url_name = 'versus-gaming-zone'
    outingbox_activity_45.address = outingbox_address_31
    outingbox_activity_45.description = 'The finest 8-lane bowling alley with hi-end graphic games, third person shooting games, imported heavy duty pool tables, dynamic air hockey and much more. The bowling alley offers the best engineered & highest performing bowling alley in India from the latest model of Brunswick worldwide GS® Series for the fanatic gaming junkies. An ideal hangout area, it comprises of no less than 40 arcade games, air hockey, pool table & a golf simulator, not to mention a bowling alley with 8-state of the art bowling lanes & to further up-size your excitement, you can even create your own private VIP bowling zone for special occasions.'
    outingbox_activity_45.rating = Decimal('0.7')
    outingbox_activity_45.votes = 1
    outingbox_activity_45.cost = 3
    outingbox_activity_45.person_of_contact = 'Devender Shah'
    outingbox_activity_45.contact_numbers = ['01145719207', '09650078976']
    outingbox_activity_45.email = 'versusdelhi@cinemax.co.in'
    outingbox_activity_45.website = 'http://www.facebook.com/versusgamingzone'
    outingbox_activity_45.facebook = ''
    outingbox_activity_45.twitter = ''
    outingbox_activity_45.linkedin = ''
    outingbox_activity_45.featured_image = 'photos/activity/featured/img-3_myHZSmZ.jpg'
    outingbox_activity_45.save()

    outingbox_activity_45.category.add(outingbox_category_5)
    outingbox_activity_45.category.add(outingbox_category_7)
    outingbox_activity_45.category.add(outingbox_category_8)

    outingbox_activity_46 = Activity()
    outingbox_activity_46.title = 'Yogakshema - Iyengar Yoga Centre'
    outingbox_activity_46.url_name = 'yogakshema-iyengar-yoga-centre'
    outingbox_activity_46.address = outingbox_address_16
    outingbox_activity_46.description = ''
    outingbox_activity_46.rating = Decimal('5.0')
    outingbox_activity_46.votes = 1
    outingbox_activity_46.cost = 2
    outingbox_activity_46.person_of_contact = ''
    outingbox_activity_46.contact_numbers = ['011-23234356', '011-2323', '4357']
    outingbox_activity_46.email = 'info@iyengaryogakshema.org'
    outingbox_activity_46.website = 'http://www.iyengaryogakshema.org/'
    outingbox_activity_46.facebook = 'https://www.facebook.com/yogakshemadelhi?fref=nf'
    outingbox_activity_46.twitter = ''
    outingbox_activity_46.linkedin = ''
    outingbox_activity_46.featured_image = 'photos/activity/featured/10733797_928762400518291_3656194764249358557_o.jpg'
    outingbox_activity_46.save()

    outingbox_activity_46.category.add(outingbox_category_13)

    outingbox_activity_47 = Activity()
    outingbox_activity_47.title = 'Navdha Yoga Center'
    outingbox_activity_47.url_name = 'navdha-yoga-center'
    outingbox_activity_47.address = outingbox_address_7
    outingbox_activity_47.description = ''
    outingbox_activity_47.rating = Decimal('0.0')
    outingbox_activity_47.votes = 1
    outingbox_activity_47.cost = 1
    outingbox_activity_47.person_of_contact = ''
    outingbox_activity_47.contact_numbers = ['09654231889', '09711801895']
    outingbox_activity_47.email = ''
    outingbox_activity_47.website = 'http://navadhayoga.com/'
    outingbox_activity_47.facebook = 'https://www.facebook.com/pages/Navadha-Yoga/217244035112068?ref=br_rs'
    outingbox_activity_47.twitter = ''
    outingbox_activity_47.linkedin = ''
    outingbox_activity_47.featured_image = 'photos/activity/featured/img-4_RLyUZCP.jpg'
    outingbox_activity_47.save()

    outingbox_activity_47.category.add(outingbox_category_11)
    outingbox_activity_47.category.add(outingbox_category_13)

    outingbox_activity_48 = Activity()
    outingbox_activity_48.title = 'Gallery Espace'
    outingbox_activity_48.url_name = 'gallery-espace'
    outingbox_activity_48.address = outingbox_address_45
    outingbox_activity_48.description = ''
    outingbox_activity_48.rating = Decimal('2.6')
    outingbox_activity_48.votes = 1
    outingbox_activity_48.cost = 5
    outingbox_activity_48.person_of_contact = 'Ms. Neerah'
    outingbox_activity_48.contact_numbers = ['011-26923287', '011-26326267', '011-26922947']
    outingbox_activity_48.email = 'art@galleryespace.com'
    outingbox_activity_48.website = 'http://www.galleryespace.com'
    outingbox_activity_48.facebook = 'http://www.facebook.com/GalleryEspace'
    outingbox_activity_48.twitter = ''
    outingbox_activity_48.linkedin = ''
    outingbox_activity_48.featured_image = 'photos/activity/featured/12747416_1123096257722969_5032867245218531870_o.jpg'
    outingbox_activity_48.save()

    outingbox_activity_48.category.add(outingbox_category_6)

    outingbox_activity_49 = Activity()
    outingbox_activity_49.title = 'Studio Prana'
    outingbox_activity_49.url_name = 'studio-prana'
    outingbox_activity_49.address = outingbox_address_59
    outingbox_activity_49.description = ''
    outingbox_activity_49.rating = Decimal('3.6')
    outingbox_activity_49.votes = 1
    outingbox_activity_49.cost = 5
    outingbox_activity_49.person_of_contact = ''
    outingbox_activity_49.contact_numbers = ['09810172485', '09716308893']
    outingbox_activity_49.email = 'voyageabsolute@gmail.com'
    outingbox_activity_49.website = 'http://www.studioprana.in/'
    outingbox_activity_49.facebook = 'https://www.facebook.com/studiopran'
    outingbox_activity_49.twitter = ''
    outingbox_activity_49.linkedin = ''
    outingbox_activity_49.featured_image = 'photos/activity/featured/img-1_UqcKTZC.jpg'
    outingbox_activity_49.save()

    outingbox_activity_49.category.add(outingbox_category_11)
    outingbox_activity_49.category.add(outingbox_category_13)

    outingbox_activity_50 = Activity()
    outingbox_activity_50.title = 'Anandyogam'
    outingbox_activity_50.url_name = 'anandyogam'
    outingbox_activity_50.address = outingbox_address_26
    outingbox_activity_50.description = ''
    outingbox_activity_50.rating = Decimal('4.0')
    outingbox_activity_50.votes = 1
    outingbox_activity_50.cost = 2
    outingbox_activity_50.person_of_contact = ''
    outingbox_activity_50.contact_numbers = ['09899183279']
    outingbox_activity_50.email = 'anandashramballia@rediffmail.com'
    outingbox_activity_50.website = ''
    outingbox_activity_50.facebook = 'https://www.facebook.com/Anandyogam'
    outingbox_activity_50.twitter = ''
    outingbox_activity_50.linkedin = ''
    outingbox_activity_50.featured_image = 'photos/activity/featured/img-3_nDUtmml.jpg'
    outingbox_activity_50.save()

    outingbox_activity_50.category.add(outingbox_category_13)

    outingbox_activity_51 = Activity()
    outingbox_activity_51.title = 'Rockshot Paintball Sports'
    outingbox_activity_51.url_name = 'rockshot-paintball-sports'
    outingbox_activity_51.address = outingbox_address_55
    outingbox_activity_51.description = ''
    outingbox_activity_51.rating = Decimal('0.3')
    outingbox_activity_51.votes = 1
    outingbox_activity_51.cost = 3
    outingbox_activity_51.person_of_contact = 'Akash Thapa'
    outingbox_activity_51.contact_numbers = ['9818215877']
    outingbox_activity_51.email = 'rockshotpaintballsportsco@gmail.com'
    outingbox_activity_51.website = 'http://www.rockshotpaintballsports.com'
    outingbox_activity_51.facebook = 'https://www.facebook.com/pages/Rockshot-Paintball-Sports/502558346441184?fref=ts'
    outingbox_activity_51.twitter = ''
    outingbox_activity_51.linkedin = ''
    outingbox_activity_51.featured_image = 'photos/activity/featured/featured.png'
    outingbox_activity_51.save()

    outingbox_activity_51.category.add(outingbox_category_4)

    outingbox_activity_52 = Activity()
    outingbox_activity_52.title = 'Yogakul'
    outingbox_activity_52.url_name = 'yogakul'
    outingbox_activity_52.address = outingbox_address_5
    outingbox_activity_52.description = ''
    outingbox_activity_52.rating = Decimal('1.3')
    outingbox_activity_52.votes = 1
    outingbox_activity_52.cost = 1
    outingbox_activity_52.person_of_contact = ''
    outingbox_activity_52.contact_numbers = ['09711825994']
    outingbox_activity_52.email = ''
    outingbox_activity_52.website = 'http://www.yogakul.com'
    outingbox_activity_52.facebook = 'https://www.facebook.com/yogakulstudio?ref=br_rs'
    outingbox_activity_52.twitter = ''
    outingbox_activity_52.linkedin = ''
    outingbox_activity_52.featured_image = 'photos/activity/featured/img-3_hCxjj8Y.jpg'
    outingbox_activity_52.save()

    outingbox_activity_52.category.add(outingbox_category_13)

    outingbox_activity_53 = Activity()
    outingbox_activity_53.title = 'Art Alive Gallery'
    outingbox_activity_53.url_name = 'art-alive-gallery'
    outingbox_activity_53.address = outingbox_address_3
    outingbox_activity_53.description = ''
    outingbox_activity_53.rating = Decimal('2.0')
    outingbox_activity_53.votes = 1
    outingbox_activity_53.cost = 5
    outingbox_activity_53.person_of_contact = ''
    outingbox_activity_53.contact_numbers = ['011-41639000', '011-41638050']
    outingbox_activity_53.email = 'info@artalivegallery.com'
    outingbox_activity_53.website = 'http://www.artalivegallery.com/'
    outingbox_activity_53.facebook = 'https://www.facebook.com/pages/Art-Alive-Gallery/1458750674340639'
    outingbox_activity_53.twitter = ''
    outingbox_activity_53.linkedin = ''
    outingbox_activity_53.featured_image = 'photos/activity/featured/Howard_Tran.jpg'
    outingbox_activity_53.save()

    outingbox_activity_53.category.add(outingbox_category_6)

    outingbox_activity_54 = Activity()
    outingbox_activity_54.title = 'Vadhera Art Gallery'
    outingbox_activity_54.url_name = 'vadhera-art-gallery'
    outingbox_activity_54.address = outingbox_address_57
    outingbox_activity_54.description = ''
    outingbox_activity_54.rating = Decimal('0.8')
    outingbox_activity_54.votes = 1
    outingbox_activity_54.cost = 2
    outingbox_activity_54.person_of_contact = ''
    outingbox_activity_54.contact_numbers = ['011-65474005', '011-65474006']
    outingbox_activity_54.email = 'art@vadehraart.com'
    outingbox_activity_54.website = 'http://www.vadehraart.com/'
    outingbox_activity_54.facebook = 'https://www.facebook.com/vadehraart'
    outingbox_activity_54.twitter = ''
    outingbox_activity_54.linkedin = ''
    outingbox_activity_54.featured_image = 'photos/activity/featured/12651027_989168394455491_1964824886806369645_n.jpg'
    outingbox_activity_54.save()

    outingbox_activity_54.category.add(outingbox_category_6)

    outingbox_activity_55 = Activity()
    outingbox_activity_55.title = 'iSkate'
    outingbox_activity_55.url_name = 'iskate'
    outingbox_activity_55.address = outingbox_address_8
    outingbox_activity_55.description = ''
    outingbox_activity_55.rating = Decimal('4.1')
    outingbox_activity_55.votes = 2
    outingbox_activity_55.cost = 1
    outingbox_activity_55.person_of_contact = 'Mr. Nibin'
    outingbox_activity_55.contact_numbers = ['0124-4610606', '09958436009']
    outingbox_activity_55.email = 'info@iskate.co.in'
    outingbox_activity_55.website = 'http://www.iskate.co.in/'
    outingbox_activity_55.facebook = 'http://www.facebook.com/iskateIndia'
    outingbox_activity_55.twitter = ''
    outingbox_activity_55.linkedin = ''
    outingbox_activity_55.featured_image = 'photos/activity/featured/skaters-enjoy-at-iskate.jpg'
    outingbox_activity_55.save()

    outingbox_activity_55.category.add(outingbox_category_10)

    outingbox_activity_56 = Activity()
    outingbox_activity_56.title = 'Delhi Dance Academy'
    outingbox_activity_56.url_name = 'delhi-dance-academy'
    outingbox_activity_56.address = outingbox_address_27
    outingbox_activity_56.description = 'Delhi Dance Academy is one of the better known names for high quality dance education, has been featured on almost every lifestyle TV channel and newspaper as the best in its field and has been awarded “The Best Dance Academy in Delhi” in Jan 2014 at the Brands Academy Business and Service Excellence Awards. \r\nIt stands as Delhi’s most visible dance institute on the Internet with 84,588 visits in all of 2013, of which 46,981 were from Delhi and also one with the highest social appeal/interaction and with excellent user reviews on Facebook and on Trip Advisor. \r\n\r\n'
    outingbox_activity_56.rating = Decimal('3.8')
    outingbox_activity_56.votes = 1
    outingbox_activity_56.cost = 3
    outingbox_activity_56.person_of_contact = 'Anant'
    outingbox_activity_56.contact_numbers = ['01141012909', '09953835088']
    outingbox_activity_56.email = ''
    outingbox_activity_56.website = 'http://www.delhidanceacademy.in'
    outingbox_activity_56.facebook = 'http://www.Facebook.com/DelhiDanceAcademy'
    outingbox_activity_56.twitter = 'https://twitter.com/dancedelhi'
    outingbox_activity_56.linkedin = ''
    outingbox_activity_56.featured_image = 'photos/activity/featured/793908_590843794264014_1393347949_o.jpg'
    outingbox_activity_56.save()

    outingbox_activity_56.category.add(outingbox_category_13)
    outingbox_activity_56.category.add(outingbox_category_26)
    outingbox_activity_56.category.add(outingbox_category_27)
    outingbox_activity_56.category.add(outingbox_category_15)
    outingbox_activity_56.category.add(outingbox_category_16)
    outingbox_activity_56.category.add(outingbox_category_17)
    outingbox_activity_56.category.add(outingbox_category_18)
    outingbox_activity_56.category.add(outingbox_category_24)
    outingbox_activity_56.category.add(outingbox_category_19)
    outingbox_activity_56.category.add(outingbox_category_20)
    outingbox_activity_56.category.add(outingbox_category_21)
    outingbox_activity_56.category.add(outingbox_category_22)
    outingbox_activity_56.category.add(outingbox_category_23)
    outingbox_activity_56.category.add(outingbox_category_25)

    outingbox_activity_57 = Activity()
    outingbox_activity_57.title = 'Delhi Walks'
    outingbox_activity_57.url_name = 'delhi-walks'
    outingbox_activity_57.address = outingbox_address_63
    outingbox_activity_57.description = 'Delhi Walks™, specialises in organising walking tours. It is conceived by Sachin Bansal to showcase historical and contemporary facets of Delhi. Whatsoever is the chosen subject of interest, age group, the level of participation preferred.'
    outingbox_activity_57.rating = Decimal('4.5')
    outingbox_activity_57.votes = 1
    outingbox_activity_57.cost = 5
    outingbox_activity_57.person_of_contact = ''
    outingbox_activity_57.contact_numbers = ['9899692790', '9711190192']
    outingbox_activity_57.email = 'share@delhiwalks.in'
    outingbox_activity_57.website = 'http://www.delhiwalks.in/'
    outingbox_activity_57.facebook = 'https://www.facebook.com/delhiwalks'
    outingbox_activity_57.twitter = 'https://twitter.com/delhiwalks'
    outingbox_activity_57.linkedin = 'https://www.linkedin.com/company/delhi-walks'
    outingbox_activity_57.featured_image = 'photos/activity/featured/The-Artifacts-Inside-Picture.jpg'
    outingbox_activity_57.save()

    outingbox_activity_57.category.add(outingbox_category_33)

    outingbox_activity_58 = Activity()
    outingbox_activity_58.title = 'The Mind Cafe'
    outingbox_activity_58.url_name = 'the-mind-cafe'
    outingbox_activity_58.address = outingbox_address_18
    outingbox_activity_58.description = "The Mind Cafe is Singapore's award winning board games cafe which has been awarded by Singapore Book of Records for widest collection of board games. The Mind Cafe is the first and the only of its kind in India and the outlet amenities include a well-stocked library of international board games, the largest collection in India, along with a range of dining options. The Mind Cafe is an ideal meeting place where families, colleagues and friends meet up for board games over good food, snacks and drinks. The Mind Cafe has delectable multi-cuisine menu with large variety of food and beverages on offer."
    outingbox_activity_58.rating = Decimal('5.0')
    outingbox_activity_58.votes = 1
    outingbox_activity_58.cost = 3
    outingbox_activity_58.person_of_contact = ''
    outingbox_activity_58.contact_numbers = ['0124-4088830', '09873441161']
    outingbox_activity_58.email = ''
    outingbox_activity_58.website = 'http://www.themindcafe.co.in/index.php'
    outingbox_activity_58.facebook = 'https://www.facebook.com/MindCafeIndia'
    outingbox_activity_58.twitter = ''
    outingbox_activity_58.linkedin = ''
    outingbox_activity_58.featured_image = 'photos/activity/featured/themindcafe.jpg'
    outingbox_activity_58.save()

    outingbox_activity_58.category.add(outingbox_category_14)

    outingbox_activity_59 = Activity()
    outingbox_activity_59.title = 'Delhi By Cycle'
    outingbox_activity_59.url_name = 'delhi-by-cycle'
    outingbox_activity_59.address = outingbox_address_65
    outingbox_activity_59.description = 'DelhiByCycle (DBC) is an initiative taken by a Dutchman Jack Leenaars in 2009. While working as a South Asia correspondent for De Telegraaf, one fine morning Jack started  to discover the back lanes of Delhi on his cycle. From a couple of participants on his first expeditions, the cycling tours have become a full hit in Delhi’s streets. Unique and green but most important, it’s a project with a soul. '
    outingbox_activity_59.rating = Decimal('0.0')
    outingbox_activity_59.votes = 0
    outingbox_activity_59.cost = 0
    outingbox_activity_59.person_of_contact = ''
    outingbox_activity_59.contact_numbers = ['9811723720', '011-64645906']
    outingbox_activity_59.email = 'info@delhibycycle.com'
    outingbox_activity_59.website = 'http://www.delhibycycle.com'
    outingbox_activity_59.facebook = 'https://www.facebook.com/delhibycycle'
    outingbox_activity_59.twitter = ''
    outingbox_activity_59.linkedin = ''
    outingbox_activity_59.featured_image = 'photos/activity/featured/421736_3566404129903_396932093_n.jpg'
    outingbox_activity_59.save()

    outingbox_activity_59.category.add(outingbox_category_33)

    outingbox_activity_60 = Activity()
    outingbox_activity_60.title = 'MKH Tourism'
    outingbox_activity_60.url_name = 'mkh-tourism'
    outingbox_activity_60.address = outingbox_address_64
    outingbox_activity_60.description = 'Experience the culture, heritage, traditions and culinary experience of Delhi'
    outingbox_activity_60.rating = Decimal('4.7')
    outingbox_activity_60.votes = 1
    outingbox_activity_60.cost = 1
    outingbox_activity_60.person_of_contact = ''
    outingbox_activity_60.contact_numbers = ['9810750217']
    outingbox_activity_60.email = 'friendsindelhi6@gmail.com'
    outingbox_activity_60.website = 'http://www.masterjikeehaveli.com/'
    outingbox_activity_60.facebook = 'https://www.facebook.com/olddelhiheritagewalk/'
    outingbox_activity_60.twitter = ''
    outingbox_activity_60.linkedin = ''
    outingbox_activity_60.featured_image = 'photos/activity/featured/featured.png'
    outingbox_activity_60.save()

    outingbox_activity_60.category.add(outingbox_category_33)

    outingbox_activity_61 = Activity()
    outingbox_activity_61.title = 'Delhi Heritage Walks'
    outingbox_activity_61.url_name = 'delhi-heritage-walks'
    outingbox_activity_61.address = outingbox_address_60
    outingbox_activity_61.description = 'Delhi Heritage Walks (DHW) explores the city of Delhi, its neighbourhoods, as never before. We are a team of young people which organises heritage walks to lesser known areas in the city of Delhi.'
    outingbox_activity_61.rating = Decimal('4.7')
    outingbox_activity_61.votes = 1
    outingbox_activity_61.cost = 4
    outingbox_activity_61.person_of_contact = ''
    outingbox_activity_61.contact_numbers = ['9212534868']
    outingbox_activity_61.email = 'info@delhiheritagewalks.com'
    outingbox_activity_61.website = 'http://delhiheritagewalks.com/'
    outingbox_activity_61.facebook = 'https://www.facebook.com/HeritageWalks/'
    outingbox_activity_61.twitter = 'https://twitter.com/HeritageWalks'
    outingbox_activity_61.linkedin = ''
    outingbox_activity_61.featured_image = 'photos/activity/featured/551649_411411975564239_1567849126_n.jpg'
    outingbox_activity_61.save()

    outingbox_activity_61.category.add(outingbox_category_33)

    outingbox_activity_62 = Activity()
    outingbox_activity_62.title = 'Intach Heritage Walks'
    outingbox_activity_62.url_name = 'intach-heritage-walks'
    outingbox_activity_62.address = outingbox_address_66
    outingbox_activity_62.description = 'The Delhi Chapter, started in 1984, has been involved in a variety of programmes and activities that have helped promote the cause of INTACH and heritage conservation.'
    outingbox_activity_62.rating = Decimal('0.0')
    outingbox_activity_62.votes = 0
    outingbox_activity_62.cost = 0
    outingbox_activity_62.person_of_contact = ''
    outingbox_activity_62.contact_numbers = ['011-24632267', '011-24641304']
    outingbox_activity_62.email = 'walks@intachdelhichapter.org'
    outingbox_activity_62.website = 'http://www.intachdelhichapter.org/'
    outingbox_activity_62.facebook = 'https://www.facebook.com/Intach-Heritage-Walks-199442496810218/'
    outingbox_activity_62.twitter = ''
    outingbox_activity_62.linkedin = ''
    outingbox_activity_62.featured_image = 'photos/activity/featured/10357636_989233181164475_4194660819674661375_o.jpg'
    outingbox_activity_62.save()

    outingbox_activity_62.category.add(outingbox_category_33)

    outingbox_activity_63 = Activity()
    outingbox_activity_63.title = 'Nehru Planetarium'
    outingbox_activity_63.url_name = 'nehru-planetarium'
    outingbox_activity_63.address = outingbox_address_54
    outingbox_activity_63.description = "The Nehru Planetarium in New Delhi is situated in the green surroundings of the Teen Murti House, earlier the official residence of India's first Prime Minister, Jawaharlal Nehru and now a museum in his memory. Conscious of the fact that an understanding of the spirit and method of science was crucial for children to become responsible citizens, Nehru liked every opportunity to be provided to them in this endeavor. In 1964, the Jawaharlal Nehru Memorial Fund was set up to promote his ideas and subsequently it undertook to build the Nehru Planetarium with its primary aim being the promotion of astronomy education. Nehru Planetarium is now a wing of the Nehru Memorial Museum and Library.    "
    outingbox_activity_63.rating = Decimal('4.3')
    outingbox_activity_63.votes = 1
    outingbox_activity_63.cost = 2
    outingbox_activity_63.person_of_contact = ''
    outingbox_activity_63.contact_numbers = ['011-23014504', '011-23012994']
    outingbox_activity_63.email = 'nehruplanetarium@gmail.com'
    outingbox_activity_63.website = 'http://nehruplanetarium.org/'
    outingbox_activity_63.facebook = 'https://www.facebook.com/nehruplanetarium.newdelhi?ref=br_rs'
    outingbox_activity_63.twitter = ''
    outingbox_activity_63.linkedin = ''
    outingbox_activity_63.featured_image = 'photos/activity/featured/12672015_1532031713761867_1513809538782779832_o.jpg'
    outingbox_activity_63.save()

    outingbox_activity_63.category.add(outingbox_category_32)

    outingbox_activity_64 = Activity()
    outingbox_activity_64.title = 'Delhi By Foot'
    outingbox_activity_64.url_name = 'delhi-by-foot'
    outingbox_activity_64.address = outingbox_address_62
    outingbox_activity_64.description = 'Experience Delhi, the way a city should be...Walk. See. Hear. Stop. Feel. Touch. Taste. Know and Love Dilli Again!'
    outingbox_activity_64.rating = Decimal('4.8')
    outingbox_activity_64.votes = 1
    outingbox_activity_64.cost = 3
    outingbox_activity_64.person_of_contact = 'Ramit'
    outingbox_activity_64.contact_numbers = ['9871181775']
    outingbox_activity_64.email = 'explore@delhibyfoot.in'
    outingbox_activity_64.website = 'http://delhibyfoot.in/'
    outingbox_activity_64.facebook = 'https://www.facebook.com/DelhiByFootAdventures/'
    outingbox_activity_64.twitter = 'https://twitter.com/DelhibyFoot'
    outingbox_activity_64.linkedin = ''
    outingbox_activity_64.featured_image = 'photos/activity/featured/1005943_10201460665538058_263412653_n.jpg'
    outingbox_activity_64.save()

    outingbox_activity_64.category.add(outingbox_category_33)

    outingbox_activity_65 = Activity()
    outingbox_activity_65.title = 'Camp Wild Dhauj'
    outingbox_activity_65.url_name = 'camp-wild-dhauj'
    outingbox_activity_65.address = outingbox_address_67
    outingbox_activity_65.description = 'Dhauj is a location at a distance of 55 kms from Gurgaon, found in the town of Faridabad within the state Haryana. The Camp Dhauj is found in the area of Mangar Village at Dhauj. The Camp Wild Dhauj has attained great attractiveness because of its place near Delhi and Gurgaon. The area is certainly reachable and something should to get time from the hectic lifestyle so take part in Camp Wild Dhauj. It provides stunning scenic landscapes, which is encompassed by the Aravali Hills on every side making the area look breathtaking.'
    outingbox_activity_65.rating = Decimal('0.0')
    outingbox_activity_65.votes = 0
    outingbox_activity_65.cost = 0
    outingbox_activity_65.person_of_contact = ''
    outingbox_activity_65.contact_numbers = ['011-65100333', '9999273336']
    outingbox_activity_65.email = 'campwild.aravali@gmail.com'
    outingbox_activity_65.website = 'http://www.campwilddhauj.in/'
    outingbox_activity_65.facebook = 'https://www.facebook.com/Campwild.Dhauj?ref=hl'
    outingbox_activity_65.twitter = ''
    outingbox_activity_65.linkedin = ''
    outingbox_activity_65.featured_image = 'photos/activity/featured/featured.png'
    outingbox_activity_65.save()

    outingbox_activity_65.category.add(outingbox_category_9)

    outingbox_activity_66 = Activity()
    outingbox_activity_66.title = '1100 Walks'
    outingbox_activity_66.url_name = '1100-walks'
    outingbox_activity_66.address = outingbox_address_61
    outingbox_activity_66.description = '1100 Walks is an exploration and celebration of Delhi, one of the most historic living cities of the world. Many cities, centuries and cultures come together to create the dynamic city of contemporary Delhi, and 1100 Walks takes you on a discovery of this multi-layered fabric. Our walks are conceptual, experiential and take you to the heart of Delhi; Innovatively, Intimately, Passionately…'
    outingbox_activity_66.rating = Decimal('4.3')
    outingbox_activity_66.votes = 1
    outingbox_activity_66.cost = 4
    outingbox_activity_66.person_of_contact = 'Himanshu Verma'
    outingbox_activity_66.contact_numbers = ['011‐41671100']
    outingbox_activity_66.email = 'himanshu@redearthindia.com'
    outingbox_activity_66.website = 'http://1100walks.com/'
    outingbox_activity_66.facebook = 'https://www.facebook.com/1100walks/'
    outingbox_activity_66.twitter = ''
    outingbox_activity_66.linkedin = ''
    outingbox_activity_66.featured_image = 'photos/activity/featured/11745482_947026338673327_8473836414331798034_n.jpg'
    outingbox_activity_66.save()

    outingbox_activity_66.category.add(outingbox_category_33)

    outingbox_activity_67 = Activity()
    outingbox_activity_67.title = 'National Science Centre'
    outingbox_activity_67.url_name = 'national-science-centre'
    outingbox_activity_67.address = outingbox_address_53
    outingbox_activity_67.description = 'The National Science Center in Delhi is a science museum located in Bhairon Road between Gate No. 1 and 2 of the Pragati Maidan exhibition grounds, across Purana Qila. The center functions under the National Council of Science Museums (NCSM), which is an autonomous body under the Ministry of Culture, Government of India. This pioneering center, which popularises science among the people in general and among the students in particular, was inaugurated on 9 January 1992 by the then Prime Minister of India, Mr. P.V.Narasimha Rao. And since its inception, the National Science Center has been rendering services towards popularising the cause of science and sceintific works.'
    outingbox_activity_67.rating = Decimal('0.2')
    outingbox_activity_67.votes = 1
    outingbox_activity_67.cost = 5
    outingbox_activity_67.person_of_contact = ''
    outingbox_activity_67.contact_numbers = ['011-23371945', ' 011-23371893', '011-23371297']
    outingbox_activity_67.email = 'nscdl01@gmail.com'
    outingbox_activity_67.website = 'http://www.nscdelhi.org'
    outingbox_activity_67.facebook = 'https://www.facebook.com/pages/National-Science-Centre-Delhi/147880188618183?fref=ts'
    outingbox_activity_67.twitter = ''
    outingbox_activity_67.linkedin = ''
    outingbox_activity_67.featured_image = 'photos/activity/featured/922957_206099403064781_4524394341635628337_n.jpg'
    outingbox_activity_67.save()

    outingbox_activity_67.category.add(outingbox_category_1)
    outingbox_activity_67.category.add(outingbox_category_31)

    outingbox_activity_68 = Activity()
    outingbox_activity_68.title = 'Golden Dunes Retreat'
    outingbox_activity_68.url_name = 'golden-dunes-retreat'
    outingbox_activity_68.address = outingbox_address_68
    outingbox_activity_68.description = 'Located near Sultanpur Bird Sanctuary in an expanse of natural valley, Golden Dunes offers natures bounties in pure tranquility. Spread over 45 acres of lush green fields, unspoilt terrain smattered with flowers & chirping melody of birds provides a perfect blend to experience nature so close. Besides being an idyllic location for an easy getaway the place provides a unique setting for conferences, workshops & training programs. Activities:- Croquet & Golf, Splash pools, Cow milking, Archery, Kite flying, Rides: Tractor/ Bullock cart/ camel /horse ride, Games with ( vegetable findings, flower finding, adventure sports sand volley ball, hurdle clearance, treasure hunts )'
    outingbox_activity_68.rating = Decimal('0.0')
    outingbox_activity_68.votes = 0
    outingbox_activity_68.cost = 3
    outingbox_activity_68.person_of_contact = ''
    outingbox_activity_68.contact_numbers = ['011-41612107', '09810002772', '09910002772']
    outingbox_activity_68.email = 'reservations@ashextourism.com'
    outingbox_activity_68.website = 'http://www.ashextourism.com/village/haryana/golden_dunes_retreat.htm'
    outingbox_activity_68.facebook = ''
    outingbox_activity_68.twitter = ''
    outingbox_activity_68.linkedin = ''
    outingbox_activity_68.featured_image = 'photos/activity/featured/featured.png'
    outingbox_activity_68.save()

    outingbox_activity_68.category.add(outingbox_category_9)

    outingbox_activity_69 = Activity()
    outingbox_activity_69.title = 'Camp Tikkling'
    outingbox_activity_69.url_name = 'camp-tikkling'
    outingbox_activity_69.address = outingbox_address_69
    outingbox_activity_69.description = 'Claim your own patch of wilderness. Find a clear space and pitch the camping tent. Scramble up the highest hill around. Check out the villages in the vicinity, with buffaloes, wells, ponds, and green fields. Survive in the wild by learning how to draw water and build fire. Enjoy a tractor or a camel cart ride. Milk a cow. Spend some time at the Potters hut, moulding chunks of clay into creative shapes. And when tired, simply hang the boots in shade, sip a cool drink and watch the clouds sweep across the sky.'
    outingbox_activity_69.rating = Decimal('0.0')
    outingbox_activity_69.votes = 0
    outingbox_activity_69.cost = 2
    outingbox_activity_69.person_of_contact = ''
    outingbox_activity_69.contact_numbers = ['011-25847000', ' 8826603636']
    outingbox_activity_69.email = 'info@camptikkling.com'
    outingbox_activity_69.website = 'http://www.camptikkling.com/'
    outingbox_activity_69.facebook = 'https://www.facebook.com/pages/Camp-Tikkling/261318423899387'
    outingbox_activity_69.twitter = ''
    outingbox_activity_69.linkedin = ''
    outingbox_activity_69.featured_image = 'photos/activity/featured/featured.png'
    outingbox_activity_69.save()

    outingbox_activity_69.category.add(outingbox_category_9)

    outingbox_activity_70 = Activity()
    outingbox_activity_70.title = 'Camp Mustang'
    outingbox_activity_70.url_name = 'camp-mustang'
    outingbox_activity_70.address = outingbox_address_70
    outingbox_activity_70.description = "Camp Mustang is located near Delhi and is easily accessible with just an hour's drive from Delhi. Surrounded by the wilderness of the Aravalli Hills range and countryside farms in the backdrop, Camp Mustang provides an ideal destination for Day adventure picnics, Day outing, One day picnic spot, Corporate and family events, Team Building Programs, Friends and Family outing and various other activities to enjoy."
    outingbox_activity_70.rating = Decimal('0.0')
    outingbox_activity_70.votes = 0
    outingbox_activity_70.cost = 3
    outingbox_activity_70.person_of_contact = ''
    outingbox_activity_70.contact_numbers = ['9911039423', '9910644233']
    outingbox_activity_70.email = 'info@zlifeeducation.com'
    outingbox_activity_70.website = 'http://www.campmustang.com/'
    outingbox_activity_70.facebook = 'https://www.facebook.com/pages/Camp-Mustang/108396852618743'
    outingbox_activity_70.twitter = ''
    outingbox_activity_70.linkedin = ''
    outingbox_activity_70.featured_image = 'photos/activity/featured/featured.png'
    outingbox_activity_70.save()

    outingbox_activity_70.category.add(outingbox_category_9)

    from outingbox.models import FeaturedActivity

    outingbox_featuredactivity_1 = FeaturedActivity()
    outingbox_featuredactivity_1.featured_1 = outingbox_activity_2
    outingbox_featuredactivity_1.featured_2 = outingbox_activity_19
    outingbox_featuredactivity_1.featured_3 = outingbox_activity_3
    outingbox_featuredactivity_1.featured_4 = outingbox_activity_6
    outingbox_featuredactivity_1.save()

import_data()
