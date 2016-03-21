#!/usr/local/bin/python2.7

import sqlite3

# open the database and print message when it works. create a cursor object & table if it doesnt exist.

con = sqlite3.connect('test5.db')
print ("Opened database successfully")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Fixtures (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                game_date TEXT, opposition TEXT, venue TEXT, formats TEXT,
                                                runs INTEGER, not_out TEXT, fours INTEGER, sixes INTEGER, dismissal TEXT, bat_av INTEGER,
                                                overs REAL, mdns INTEGER, runs_con INTEGER, wickets INTEGER, econ REAL);""")



# Create a class called Data to handle all inputing of data

class Data():

    # init class variables used to create fixture information.

    def __init__(self):

    # fixture variables
        self.game_date = ""
        self.opposition = ""
        self.venue = ""
        self.formats = ""


    # Allows the user to input fixtures details

    def add_fixtures(self):
        self.game_date = raw_input("Date of game: ")
        self.opposition = raw_input("Opposition: ")
        self.venue = raw_input("Venue: ")
        self.formats = raw_input("Format: ")
        return self.game_date, self.opposition, self.venue, self.formats

        with con:
            cur = con.cursor()
            cur.execute('''INSERT INTO Fixtures (game_date, opposition, venue, formats) VALUES(?,?,?,?)''', (self.game_date, self.opposition, self.venue, self.formats))
            # cur.execute("INSERT INTO Fixtures VALUES (?, ?, ?, ?);", (self.game_date, self.opposition, self.venue, self.formats))
            con.commit()




class Stats():

    def __init__(self):

        pass


# create a class called Data_menu to show user options re: entering fixtures and runs/wickets etc...

class Data_menu():

    print "Make a choice \n-----------------\n"
    print "1. Add Fixtures"
    print "2. Add Stats"
    print "3. Main Menu"
    while True:
        cmd = raw_input("Make a Selection: ")
        if cmd == "1":
            action = Data()
            action.add_fixtures()
        elif cmd == "2":
            action = Stats()
            action.menu()
        else:
            print("Command not recognized. Exiting.")
            break




# Calls and runs program

if __name__ == '__main__':
    print "12th Man - Main Menu \n-----------------\n"
    print "1. Enter Data"
    print "2. View Stats"
    while True:
        cmd = raw_input("Make a Selection: ")
        if cmd == "1":
            action = Fixtures()
            action.view_fixtures()
        elif cmd == "2":
            action = Datainput()
            action.menu()
        else:
            print("Command not recognized. Exiting.")
            break



