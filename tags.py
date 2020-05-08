# -*- coding: utf-8 -*-

""" 
+ -----------------------------------------------------------------------------------+
Author : 
L.Ferhi (derived from the Udacity code sample in Project 2 - lesson 13)

Description :
Function returning a dictionnary containing the number of "k" value types based
on the following regular expressions:
  "lower", for tags that contain only lowercase letters and are valid,
  "lower_colon", for otherwise valid tags with a colon in their names,
  "problemchars", for tags with problematic characters, and
  "other", for other tags that do not fall into the other three categories.
+ -----------------------------------------------------------------------------------+
"""

import xml.etree.cElementTree as ET
import pprint
import re

filename = 'glasgow.osm'

# Definition of the patterns to be recognized
lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

# Increases the value of 'keys' dictionnary with the pattern that has been recognized
def key_type(element, keys):
    if element.tag == "tag":
        key = element.attrib['k']
        # re.match compares the key to the pattern (returns None if no match)
        if re.match(lower, key) != None:  
            keys['lower'] += 1
        elif re.match(lower_colon, key) != None:
            keys['lower_colon'] += 1
        elif re.match(problemchars, key) != None:
            keys['problemchars'] += 1
        else:
            keys['other'] += 1
    return keys

# Returns the number of each pattern recognized in the osm file 
def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)
    return keys
