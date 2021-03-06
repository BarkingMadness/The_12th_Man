#!/usr/local/bin/python2.7

import sqlite3

# open the database and print message when it works. create a cursor object & table if it doesnt exist.

con = sqlite3.connect('The_12th_Man.db')
print ("Opened database successfully")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Fixtures (id INTEGER PRIMARY KEY AUTOINCREMENT, game_date TEXT, opposition TEXT, venue TEXT, formats TEXT);")

# create a class called database to handle inputting, outputting and display of database information.

class Database():

    # init class variables used to crreate fixture information.

    def __init__(self):

        self.game_date = ""
        self.opposition = ""
        self.venue = ""
        self.formats = ""

    # allows the user to make a choice from the menu

    def menu(self):
        print "\n------------------------"
        print "1. Enter Fixtures"
        print "2. View Fixtures"
        print "--------------------------"
        option = raw_input("Make a selection: ")

        if option == "1":
            self.input_fixtures()
        elif option == "2":
            self.view_fixtures()
        else:
            print "That is not an option"
            self.menu()

    # asks the user to input fixture details and return values

    def input_fixtures(self):
        self.game_date = raw_input("Date of game: ")
        self.opposition = raw_input("Opposition: ")
        self.venue = raw_input("Venue: ")
        self.formats = raw_input("Format: ")
        return self.game_date, self.opposition, self.venue, self.formats

    # take the user entered fixtures details and add them to the table 'Fixtures'. If one doesn't already exist, create it.

    def update_db(self):
        with con:
            cur = con.cursor()
            cur.execute('''INSERT INTO Fixtures (game_date, opposition, venue, formats) VALUES(?,?,?,?)''', (self.game_date, self.opposition, self.venue, self.formats))
            con.commit()

    # displays all the fixtures currently in the database.

    def view_fixtures(self):
        print "\nList of Fixtures:\n-----------------\n"
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Fixtures ORDER BY game_date ASC")
            rows = cur.fetchall()
            for row in rows:
                print row

        print "\nView match details? \n-------------------\n"
        self.view_date = raw_input("Enter date: ")
        with con:
            cur = con.cursor()
            cur.execute("select * from Fixtures where game_date = '%s'" % self.view_date)   #insecure?
            for row in cur:
                print row
                con.commit()



    # main loop to run the methods in the Database class.

    def main_loop(self):
        self.menu()
        self.update_db()
        self.menu()


if __name__ == '__main__':
    input = Database()
    input.main_loop()
    con.close()
