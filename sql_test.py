#!/usr/local/bin/python2.7

import sqlite3

con = sqlite3.connect('twelth_man.db')
print ("Opened database successfully")


class Database():

    def __init__(self):

        self.date = ""
        self.opposition = ""
        self.venue = ""
        self.format = ""


    def input(self):
        self.date = raw_input("Date of game: ")
        self.opposition = raw_input("Opposition: ")
        self.venue = raw_input("Venue: ")
        self.format = raw_input("Format: ")
        return self.date, self.opposition, self.venue, self.format


    def create_db(self):
        with con:
            cur = con.cursor()
            # cur.execute("DROP TABLE IF EXISTS Fixtures")
            # cur.execute("CREATE TABLE Fixtures (First Name TEXT, Last Name TEXT, Phone TEXT, Email TEXT);")
            cur.execute("INSERT INTO Fixtures VALUES (?, ?, ?, ?);", (self.date, self.opposition, self.venue, self.format))
            con.commit()

    def display_db(self):
        print "\nHere's a listing of all the records in the table:\n"
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Fixtures")
            rows = cur.fetchall()
            for row in rows:
                print row


    def main_loop(self):
        fixture_input = self.input()
        update_db = self.create_db()
        view_db = self.display_db()


if __name__ == '__main__':
    input = Database()
    input.main_loop()
    con.close()
