#!/usr/local/bin/python2.7

#import sqlite3 library to enable use of database

import sqlite3

# open the database and print message when it works. create a cursor object & table if it doesnt exist.

con = sqlite3.connect('12thman_test.db')
print ("Opened database successfully")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Fixtures (game_date TEXT, opposition TEXT, venue TEXT, formats TEXT);")

# create a class called database to handle inputting, outputting and display of database information.

class Database():

    # init class variables used to crreate fixture information.

    def __init__(self):

        self.game_date = ""
        self.opposition = ""
        self.venue = ""
        self.formats = ""

    # allows the user to make a choice from the menu

    def menu():
        print "\n------------------------"
        print "1. Enter Fixtures"
        print "2. View Fixtures"
        print "--------------------------"
        option = raw_input("Make a selection: ")

        if option == "1":
            input_fixtures()
        elif option == "2":
            show_fixtures()
        else:
            print "That is not an option"
            menu()

    # asks the user to input fixture details and return values

    def input_fixtures(self):
        self.game_date = raw_input("Date of game: ")
        self.opposition = raw_input("Opposition: ")
        self.venue = raw_input("Venue: ")
        self.formats = raw_input("Format: ")
        return self.game_date, self.opposition, self.venue, self.formats

    # take the user entered fixtures details and add them to the database. sort them by date

    def update_db(self):
        with con:
            cur = con.cursor()
            # cur.execute("DROP TABLE IF EXISTS Fixtures")
            cur.execute("CREATE TABLE IF NOT EXISTS Fixtures (date TEXT, opposition TEXT, venue TEXT, formats TEXT);")
            cur.execute("INSERT INTO Fixtures VALUES (?, ?, ?, ?);", (self.game_date, self.opposition, self.venue, self.formats))
            con.commit()

    # displays all the fixtures currently in the database.

    def show_fixtures(self):
        print "\nList of Fixtures:\n"
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Fixtures")
            cur.execute("SELECT * FROM Fixtures ORDER BY game_date ASC")
            rows = cur.fetchall()
            for row in rows:
                print row

    # main loop to run the methods in the Database class.

    def main_loop(self):
        fixture_input = self.input_fixtures()
        update_db = self.update_db()
        view_db = self.show_fixtures()


if __name__ == '__main__':
    input = Database()
    input.main_loop()
    con.close()
