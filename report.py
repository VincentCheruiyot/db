from collections import OrderedDict
import datetime

from peewee import *
db = MySQLDatabase("report", user="root",password="",host="localhost")

class Entry(Model):
    #content and timestamp
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """Create the database and the table if they don't exist"""
    db.connect()
    db.create_tables([Entry],safe=True)

def menu_loop():
    """Show the menu."""

def add_entry():
    """Add an entry."""

def view_entries():
    """View previous entries"""

def delete_entry(entry):
    """Delete an entry."""

if __name__=="__main__":
    initialize()
    menu_loop()

