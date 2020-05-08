# -*- coding: utf-8 -*-

""" 
+ -----------------------------------------------------------------------------------+
Author : 
L.Ferhi (derived from the Udacity code sample in Project 2 - lesson 13)

Description :
Script auditing the street names according to a list of expected names.
The unexpected names can be updated with the 'update_street_name' function according
to a mapping giving, for each non-conform name, the conform one.
+ -----------------------------------------------------------------------------------+
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

osmfile = 'glasgow.osm'

expected_street = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", 
            "Lane", "Road", "Trail", "Parkway", "Commons", "Terrace", "Gardens", "Crescent",
           "Quadrant", "Way", "Gate", "Path", "Circus", "Park"]

mapping_street = {
    "road" : "Road",
    "Rd" : "Road",
    "street" : "Street",
    "St": "Street",
    "St.": "Street",
    "Ave" : "Avenue",
    "Rd." : "Road",
    "St." : "Street",
    "Sreet" : "Street",
    "bank" : "Bank",
    "Strret" : "Street",
    "Road," : "Road"
            }

# Street type pattern
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

def audit_street_type(street_types, street_name, expected):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

# Returns a dictionnary {'last street name word' : {'Full street name 1', 'Full street name 2',...},...}
def audit_steet_names(osmfile, expected):
    osm_file = open(osmfile, "rb")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'], expected)
    osm_file.close()
    return street_types

# Change a non-confrom street name to a conform one
def update_street_name(name, mapping_street):
    for old_name, new_name in mapping_street.items():
        if name.endswith(old_name):
            name = name.replace(old_name, new_name)
            break
    return name

# Print old street name => corrected street name (only checking function)
def check_fixed_street(osmfile, expected, mapping_street):
    st_types = audit_steet_names(osmfile, expected)
    for st_type, ways in st_types.items(): # in python3 iteritems() becomes items()
        for name in ways:
            better_name = update_street_name(name, mapping_street)
            if better_name != name:
                print (name, "=>", better_name)
