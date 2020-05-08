#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
+ -----------------------------------------------------------------------------------+
Author : 
L.Ferhi (derived from the Udacity code sample in Project 2 - lesson 13)

Description :
Script returning a set of unique user ids 
+ -----------------------------------------------------------------------------------+
"""

import xml.etree.cElementTree as ET
import pprint
import re

filename = 'glasgow.osm'

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if 'uid' in element.attrib.keys():
            user_id = element.attrib['uid']
            if user_id not in users:
                users.add(user_id)
    return len(users)
