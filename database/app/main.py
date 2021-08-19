import sqlite3
import os

def connect(database_folder_path, database_path):
	if not os.path.exists(database_folder_path):
		os.makedirs(database_folder_path)
		con = sqlite3.connect(database_path, check_same_thread=False)
		cur = con.cursor()
		cur.execute('''CREATE TABLE urlShortener
			(idx int, shortenedURL text, fullURL text, times int)''')
	else:
		con = sqlite3.connect(database_path, check_same_thread=False)
	return con

def findEntry(cur, column, value):
	return cur.execute("SELECT * FROM urlShortener WHERE {} == '{}'".format(column, value)).fetchone()

def findEntryNull(cur, column, value):
	return cur.execute("SELECT * FROM urlShortener WHERE {} {}".format(column, value)).fetchall()

def addEntry(con, cur, idx, shortenedURL, fullURL):
	cur.execute("INSERT INTO urlShortener VALUES ({},'{}','{}', {})".format(idx, shortenedURL, fullURL, 0))
	con.commit()

def updateEntryCount(con, cur, column, columnNewValue, columnToCheck, columnToCheckValue):
	cur.execute("UPDATE urlShortener SET {} = {} WHERE {} == '{}'".format(column, columnNewValue, columnToCheck, columnToCheckValue))
	con.commit()

def getLastIndex(cur):
	return cur.execute("SELECT MAX(idx) from urlShortener").fetchone()[0]