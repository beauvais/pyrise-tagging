This is a basic Python script used to tag people stored in Highrise based on results from a CSV file. I needed to be familiar with the pyrise module in order to write the script.

## modules needed:

*pyrise*
pyrise is a Python module for Highrise created by [jasford](https://github.com/feedmagnet/pyrise).

*csv*
the csv module is used to open and read rows from the csv file

*re*
regular expressions module is used for searching strings in the csv

## Tags

I created variables based on the csv index (columns) with which to add tags. There were a few different kinds of items within my csv:

* email address
* Yes/No
* Multiple Choice
* Free text

I needed to count the columns in my csv to identify the index that matched each variable I required. I then tested this simply by printing that field:

print row[0]

**email address**

This script relies on the email address to perform the lookup in highrise.

**Yes/No**

The logic is that if a person is categorised as a "Yes", they would be tagged.

**Multiple Choice**

There were some fields which contained a predictable selection of strings, and the tags I was after were based on one of them. I used regex to search for the string. An example would be that I wanted to tag all the "green people":

red, green, blue, white

So the re module is called to search for "green"

**Free Text**

Some fields in the CSV would make good notes instead of tags, and this is handled by the pyrise module using:

i.add_note(tag4)

## General Comments

The script (pyrise-tagging.py) is commented inline, to explain the steps needed. A few things to point out:

* You will need your Highrise server (the address of your Highrise account)
* You will need a 37Signals API Key
