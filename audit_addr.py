# -*- coding: utf-8 -*-

""" 
+ -----------------------------------------------------------------------------------+
Author : 
L.Ferhi (derived from the Udacity code sample in Project 2 - lesson 13)

Description :
Script auditing the postal codes according to a regular expression.
The unexpected names can be updated with the 'update_street_name' function according
to a mapping giving, for each non-conform name, the conform one.
+ -----------------------------------------------------------------------------------+
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import re

osmfile = 'glasgow.osm'

mapping_city = {
    ' GLASGOW ' : 'Glasgow',
    'glasgow' : 'Glasgow',
    'Anniesland, Glasgow' : 'Glasgow',
    'Baillieston, Glasgow' : 'Glasgow',
    'Bearsden, Glasgow' : 'Bearsden',
    'Bishopb' : 'Bishopbriggs',
    'Bishopbriggs Glasgow' : 'Bishopbriggs',
    'Bishopbriggs, Glasgow' : 'Bishopbriggs',
    'Braehead' : 'Glasgow',
    'Cambuslang' : 'Cambulsang',
    'Clarkston, Glasgow' : 'Clarkston',
    'Drumchapel' : 'Glasgow',
    'Drumchapel Glasgow' : 'Glasgow',
    'Drumpchapel Glasgow' : 'Glasgow',
    'Finnieston' : 'Glasgow',
    'GLASGOW' : 'Glasgow',
    'Glasgow    ' : 'Glasgow',
    'Glasgw' : 'Glasgow',
    'Gorbals' : 'Glasgow',
    'Griffnock' : 'Giffnock',
    'RUTHERGLEN' : 'Rutherglen',
    'Rutherglen, Glasgow' : 'Rutherglen',
    'South Lanarkshire' : 'Hamilton',
    'Tannochside' : 'Uddingston',
    'Thornliebank, Glasgow' : 'Thornliebank',
    'clydebank': 'Clydebank'
}


# Regular expression for Glasgow city postal codes
""" Type of postal codes : G31 1HB, G3 6LL, 
G : "[G]"
1 or 2 digits : "\d{1,2}"
1 blank : " "
\b to search for beginning of the next word
1 digits followed by 2 letters : "\d[A-Z]{2,2}"
"""
post_code_re = re.compile(r'[G]\d{1,2} \b\d[A-Z]{2,2}', re.IGNORECASE)

def is_post_code(elem):
    return (elem.attrib['k'] == "addr:postcode")

def is_city(elem):
    return (elem.attrib['k'] == "addr:city")

# Returns a tuple with city and postal code if postal code does not match reg. exp.
def audit_postal(osmfile):
    osm_file = open(osmfile, "rb")
    post_codes = set()
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        postal, city = '', ''
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                # Search for City in the adress
                if is_city(tag):
                    city = tag.attrib['v']
                # Search for postal code in the adress
                if is_post_code(tag):
                    postal = tag.attrib['v']
                    m = post_code_re.match(postal)
                    if not m:
                        post_codes.add((city , postal))
    osm_file.close()
    return post_codes

# Returns a set of the cities
def audit_city(osmfile):
    osm_file = open(osmfile, "rb")
    cities = set()
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_city(tag):
                    cities.add(tag.attrib['v'])
    osm_file.close()
    return cities               

# Change a non-confrom city name to a conform one
def update_city_name(name, mapping_city):
    for old_name, new_name in mapping_city.items():
        if name == old_name:
            name = name.replace(old_name, new_name)
            break
    return name

# Returns a set of old street name => corrected street name (only checking function)
def check_fixed_city(osmfile, mapping_city):
    osm_file = open(osmfile, "rb")
    city_name_change = set()
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        city = ''
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                # Search for City in the adress
                if is_city(tag):
                    city = tag.attrib['v']
                    if city in mapping_city:
                        better_city = update_city_name(city, mapping_city)
                        city_name_change.add((city, better_city))   
    for couple in city_name_change:
        print (couple[0], "=>", couple[1])
    osm_file.close()
