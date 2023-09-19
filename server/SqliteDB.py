import sqlite3
import os
import pandas as pd
import re

class SqliteDB:
    # Constructor
    def __init__(self):
        self.sqliteConnection = None
        self.dbname = ""

    # Destructor
    def __del__(self):
        print("Destructor Sqlite")
        if self.sqliteConnection:
            self.sqliteConnection.close()
            os.remove(self.dbname)

    # Create a SQLite database
    def connect(self, dbname):
        try:
            self.dbname = dbname
            self.sqliteConnection = sqlite3.connect(dbname, check_same_thread=False)
            cur = self.sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")
            query = "SELECT sqlite_version();"
            cur.execute(query)
            rec = cur.fetchall()
            print("SQLite Database Version is: ", rec)
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

    # Build a query for creating a table
    def _build_create_query(self, cols):
        query = """CREATE TABLE Database ("""
        query += cols[0][0] + " " + cols[0][1] + " PRIMARY KEY,"
        for i in range(1, len(cols)):
            query += " [" + cols[i][0] + "] " + cols[i][1] + " NOT NULL,"
        query = query[:-1] + ")"
        print(query)
        return(query)

    # Create a table for the database
    def createTable(self, cols):
        try:
            cur = self.sqliteConnection.cursor()
            query = self._build_create_query(cols)
            cur.execute(query)
            self.sqliteConnection.commit()
            print("SQLite table created")
        except sqlite3.Error as error:
            print("Table exists: ", error)

    # Get all the records of a table
    def readTable(self):
        rec = None
        try:
            cur = self.sqliteConnection.cursor()
            query = """SELECT * from Database"""
            cur.execute(query)
            rec = cur.fetchall()
            print("Total rows are:  ", len(rec))
        except sqlite3.Error as error:
            print("Failed to read data from table", error)
        finally:
            return rec

    def readTableToDf(self):
        df = None
        try:
            query = """SELECT * from Database"""
            df = pd.read_sql_query(query, self.sqliteConnection)
            print("Total rows are:  ", len(df.index))
        except sqlite3.Error as error:
            print("Failed to read data from table", error)
        finally:
            return df

    # Build a query for inserting a record
    def _build_insert_query(self):
        # Get all column names from the table
        cur = self.sqliteConnection.cursor()
        query = """SELECT name from PRAGMA_TABLE_INFO('Database')"""
        cur.execute(query)
        rec = cur.fetchall()
        cols = "[" + "], [".join([r[0] for r in rec]) + "]"
        vals = ", ".join("?" * len(rec))
        query = 'INSERT into Database ({}) VALUES ({})'.format(cols, vals)
        print(query)
        return query

    def insert(self, tup):
        try:
            query = self._build_insert_query()
            cur = self.sqliteConnection.cursor()
            cur.execute(query, tup)
            self.sqliteConnection.commit()
            print("Inserted successfully into table")
        except sqlite3.Error as error:
            print("Failed to insert: ", error)

    # Search records by the name and return a list of tuples (id, name, html)
    def search(self, year, col_name):
        rec = None
        try:
            cursor = self.sqliteConnection.cursor()
            sel = 'SELECT [{}] FROM Database WHERE Year == "{}"'.format(col_name, year)
            cursor.execute(sel)
            rec = cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to search:", error)
        finally:
            return rec

    def get_column_names(self):
        # Get all column names from the table
        cur = self.sqliteConnection.cursor()
        query = """SELECT name from PRAGMA_TABLE_INFO('Database')"""
        cur.execute(query)
        rec = cur.fetchall()
        columns = [r[0] for r in rec]
        print(columns)
        return columns

    def search_row(self, name, start_year, end_year):
        rec = None
        try:
            cursor = self.sqliteConnection.cursor()
            sel = 'SELECT * FROM Database WHERE Country == "{}" AND Year >= {} AND Year <= {}'.format(name, start_year, end_year)
            cursor.execute(sel)
            rec = cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to search:", error)
        finally:
            return rec

    def search_column(self, col_name):
        rec = None
        try:
            cursor = self.sqliteConnection.cursor()
            sel = 'SELECT [{}] FROM Database'.format(col_name)
            cursor.execute(sel)
            rec = cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to search:", error)
        finally:
            return rec