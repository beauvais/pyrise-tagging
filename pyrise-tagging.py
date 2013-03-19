#! /usr/bin/python

import csv
import re
from pyrise import Highrise, Person
# import Highrise Python Library which can be found at https://github.com/feedmagnet/pyrise

# connect to Highrise
Highrise.set_server('your_project.highrisehq.com')
Highrise.auth('your_api_key')

# open csv using reader, and set the delimiter
csvFile = csv.reader(open('/survey.csv', 'rb'), delimiter=',')

# identify header row
header = next(csvFile)

# loop rows in csv file, and identify variables for fields, you will need to know which index contains the tag you want.
for row in csvFile:
    if len(row) < 21:  # use if final column can be blank
        continue
    tag1 = row[0]  # Yes or No
    tag2 = row[1]
    address = row[2]  # Email address (required to lookup)
    tag3 = row[10]  # multiple choice
    tag4 = row[20]  # final column, free-text so might be empty

# if a column contains multiple choice, use regex to search for the choice you want to tag on (e.g. I like: red, white, green; search for green to tag: 'likes green')
    green = re.search("green", tag3)

# if a person has an email address, use the Person.filter to identify the addresses, and add tags to accounts mapped to the address.
    if address:
        people = Person.filter(email=address)

    for i in people:
        if tag1 == "Yes":
            i.add_tag("tag one")
            i.save()
            i.add_tag("text " + tag2)
            i.add_note(tag4)

        if green:
            i.add_tag("likes green")
