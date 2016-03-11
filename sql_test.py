#!/usr/local/bin/python2.7

import sqlite3

conn = sqlite3.connect('twelth_man.db')
print ("Opened database successfully")


def create_db():
	print("Creating fields")
	with conn:
		cursor = conn.cursor()
		cursor.execute("DROP IF TABLE EXISTS Contacts")
		cursor.execute("""CREATE TABLE Contacts (Match INTEGER, Date TEXT, Opposition TEXT, Venue TEXT, Format TEXT""")
		cursor.commit()

def fixtures():
	date = user_input("Date: ")
	opp = user_input("Opposition: ")
	venue = user_input("Venue: ")
	format = user_input("Format: ")
