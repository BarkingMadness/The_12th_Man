#!/usr/local/bin/python2.7

import sqlite3

con = sqlite3.connect('twelth_man.db')
print ("Opened database successfully")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Fixtures (date TEXT, opposition TEXT, venue TEXT, formats TEXT);")


class Database():

    def __init__(self):

        self.date = ""
        self.opposition = ""
        self.venue = ""
        self.formats = ""


    def input_fixtures(self):
        self.date = raw_input("Date of game: ")
        self.opposition = raw_input("Opposition: ")
        self.venue = raw_input("Venue: ")
        self.formats = raw_input("Format: ")
        return self.date, self.opposition, self.venue, self.formats


    def update_db(self):
        with con:
            cur = con.cursor()
            # cur.execute("DROP TABLE IF EXISTS Fixtures")
            cur.execute("CREATE TABLE IF NOT EXISTS Fixtures (date TEXT, opposition TEXT, venue TEXT, formats TEXT);")
            cur.execute("INSERT INTO Fixtures VALUES (?, ?, ?, ?);", (self.date, self.opposition, self.venue, self.formats))
            cur.execute("SELECT * FROM Fixtures ORDER BY date ASC")
            con.commit()


    def display_db(self):
        print "\nList of Fixtures:\n"
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Fixtures")

            rows = cur.fetchall()
            for row in rows:
                print row


    def main_loop(self):
        fixture_input = self.input_fixtures()
        update_db = self.update_db()
        view_db = self.display_db()


if __name__ == '__main__':
    input = Database()
    input.main_loop()
    con.close()
