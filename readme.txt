OpenStreetMap position : 
https://www.openstreetmap.org/#map=12/55.8553/-4.2632

Files related to the project submission:

Wrangle_OpenStreetMap_Data_final.html  - Report on the data wrangling project
Wrangle_OpenStreetMap_Data_final.ipynb - Jupyter notebook used to make the report

glasgow_sample.osm                     - Sample of the full osm file

udacity_sample.py                      - Script to generate sample from the full osm file
mapparser.py                           - Script returning the names and number of tags
user.py                                - Script returning the number of distinct users
tags.py                                - Script returning the number of tag types (lower, colon, problematic characters and other)
audit_streets.py                       - Script used to audit the street names with function to clean them
audit_addr.py                          - Script used to audit the postale codes and city names with function to clean the city names
schema.py                              - Script defining the schema of csv tables to be created
data_clean.py                          - Script generated the csv files according to the schema with cleaned data and table dependencies

data-wrangling-schema.sql              - SQL database schema
