#!/usr/local/bin/python2.7

"""Test program using SQLite3 to allow user to enter a fixture then display all fixtures in the database."""

#import sqlite3 library to enable use of database

import sqlite3

# open the database and print message when it works. create a cursor object & table if it doesnt exist.

con = sqlite3.connect('twelth_man.db')
print ("Opened database successfully")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Fixtures (date TEXT, opposition TEXT, venue TEXT, formats TEXT);")

# create a class called database to handle inputting, outputting and display of database information.

class Database():
    
    # init class variables used to crreate fixture information.

    def __init__(self):

        self.date = ""
        self.opposition = ""
        self.venue = ""
        self.formats = ""

    # asks user to input fixture details and return values

    def input_fixtures(self):
        self.date = raw_input("Date of game: ")
        self.opposition = raw_input("Opposition: ")
        self.venue = raw_input("Venue: ")
        self.formats = raw_input("Format: ")
        return self.date, self.opposition, self.venue, self.formats

    # take the user entered fixtures details and add them to the database. sort them by date (NOT WORKING!)

    def update_db(self):
        with con:
            cur = con.cursor()
            # cur.execute("DROP TABLE IF EXISTS Fixtures")
            cur.execute("CREATE TABLE IF NOT EXISTS Fixtures (date TEXT, opposition TEXT, venue TEXT, formats TEXT);")
            cur.execute("INSERT INTO Fixtures VALUES (?, ?, ?, ?);", (self.date, self.opposition, self.venue, self.formats))
            cur.execute("SELECT * FROM Fixtures ORDER BY date ASC")
            con.commit()

    # display all fixtures entered into the database.

    def display_db(self):
        print "\nList of Fixtures:\n"
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Fixtures")

            rows = cur.fetchall()
            for row in rows:
                print row

    # main loop to run the methods in the Database class.

    def main_loop(self):
        fixture_input = self.input_fixtures()
        update_db = self.update_db()
        view_db = self.display_db()

# runs the programme.

if __name__ == '__main__':
    input = Database()
    input.main_loop()
    con.close()
