#!/usr/local/bin/python2.7

import sqlite3

# open the database and print message when it works. create a cursor object & table if it doesnt exist.

con = sqlite3.connect('test5.db')
print ("Opened database successfully")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Fixtures (game_date TEXT, opposition TEXT, venue TEXT, formats TEXT,
                                                runs INTEGER, not_out TEXT, fours INTEGER, sixes INTEGER, dismissal TEXT, bat_av INTEGER,
                                                overs REAL, mdns INTEGER, runs_con INTEGER, wickets INTEGER, econ REAL);""")


# Create a class called Data to handle all inputing of data

class DataInput():

    # init class variables used to create fixture information.

    def __init__(self):

    # Fixture variables
        self.game_date = ""
        self.opposition = ""
        self.venue = ""
        self.formats = ""

    # Batting variables
        self.runs = 0
        self.not_out = ""
        self.fours = 0
        self.sixes = 0
        self.dismissal = ""

    # Bowling variables
        self.overs = 0
        self.mdns = 0
        self.runs_con = 0
        self.wickets = 0
        self.econ = 0

    # Fielding variables
        self.catches = 0
        self.drops = 0
        self.run_outs = 0
        self.stumpings = 0


    def fixtures_submenu(self):
        print "\n--------------------\nFixtures & Data Input:\n---------------------\n"
        print "1. Enter Fixtures"
        print "2. View Fixtures"
        print "3. Enter Data"
        print "4. Return to Main Menu"
        cmd = raw_input("\nMake a Selection: ")
        if cmd == "1":
            action = DataInput()
            action.add_fixtures()
        elif cmd == "2":
            action = DataInput()
            action.view_fixtures()
        elif cmd == "3":
            action = DataInput()
            action.input_scores()
        elif cmd == "4":
            return
        else:
            print("Command not recognized. Exiting.")
            con.close()

    # Allows the user to input fixtures details

    def add_fixtures(self):
        print "\n--------------------\nEnter a Fixture:\n---------------------\n"
        self.game_date = raw_input("Date of game: ")
        self.opposition = raw_input("Opposition: ")
        self.venue = raw_input("Venue: ")
        self.formats = raw_input("Format: ")

        with con:
            cur = con.cursor()
            cur.execute('''INSERT INTO Fixtures (game_date, opposition, venue, formats) VALUES(?,?,?,?)''', (self.game_date, self.opposition, self.venue, self.formats))
            # cur.execute("INSERT INTO Fixtures VALUES (?, ?, ?, ?);", (self.game_date, self.opposition, self.venue, self.formats))
            con.commit()
        DataInput.fixtures_submenu(self)


    #Allows the user to display all fixture details currently in the database.

    def view_fixtures(self):
        print "\n------------\nFixture List:\n------------\n"
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Fixtures ORDER BY game_date ASC")
            rows = cur.fetchall()
            for row in rows:
                print row
        DataInput.fixtures_submenu(self)


    # Allows user to input game data.

    def input_scores(self):
        print "\nInput Match Data \n---------------\n"
        self.view_date = raw_input("Enter Date: ")
        with con:
            cur = con.cursor()
            cur.execute("SELECT EXISTS(SELECT 1 FROM Fixtures WHERE game_date='self.view_date')")
            if cur.fetchone():
                print("Record Found:")
            else:
                print("Not found...")

            cur.execute("SELECT * from Fixtures WHERE game_date = '%s'" % self.view_date)
            for row in cur:
                print row
                con.commit()
        self.runs = raw_input("Runs Scored: ")
        #self.not_out = raw_input("Not out?: ")
        #self.fours = raw_input("Fours Scored: ")
        #self.sixes = raw_input("Sixes scored: ")
        #self.dismissal = raw_input("Method of dismissal: ")

        cur.execute("UPDATE Fixtures SET runs=? WHERE game_date=?", (self.runs, self.view_date))
        con.commit()


class Stats():

    def __init__(self):

        pass



# Calls and runs program

if __name__ == '__main__':
    while True:
        print "\n\n--------------------\n12th Man - Main Menu \n--------------------\n"
        print "1. Enter Data"
        print "2. View Stats"
        print "3. Exit Program"

        choice = raw_input("\nMake a Selection: ")
        while choice != '1' and choice != '2' and choice != '3':
            choice = raw_input("\nInvalid Input: Make a Selection: ")
        if choice== "1":
            action = DataInput()
            action.fixtures_submenu()
        elif choice == "2":
            action = DataInput()
            action.menu()
        elif choice == "3":
            print("Goodbye!")
            con.close()
