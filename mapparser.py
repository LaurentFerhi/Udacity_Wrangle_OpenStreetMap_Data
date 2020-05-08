# -*- coding: utf-8 -*-

""" 
+ -----------------------------------------------------------------------------------+
Author : 
L.Ferhi (derived from the Udacity code sample in Project 2 - lesson 13)

Description :
Map parsing function that returns a dictionnary with the tag name as the key 
and number of times this tag can be encountered in the map as value.
+ -----------------------------------------------------------------------------------+
"""

filename = 'glasgow.osm'

import xml.etree.cElementTree as ET
import pprint

# Returns a dictionnary like {'tag_name' : quantity, ...}
def count_tags(filename):
    result = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag not in result:
            result[elem.tag] = 1 # Creating the key with value = 1 
        else:
            result[elem.tag] += 1 # Adding 1 to the value of the corresponding key
    return result