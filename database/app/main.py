import sqlite3
import os

def connect(database_folder_path, database_path):
	if not os.path.exists(database_folder_path):
		os.makedirs(database_folder_path)
		con = sqlite3.connect(database_path, check_same_thread=False)
		cur = con.cursor()
		cur.execute('''CREATE TABLE urlShortener
			(idx int, shortenedURL text, fullURL text)''')
	else:
		con = sqlite3.connect(database_path, check_same_thread=False)
	return con

def findEntry(cur, column, value):
	return cur.execute("SELECT * FROM urlShortener WHERE {} == '{}'".format(column, value)).fetchone()

def addEntry(con, cur, idx, shortenedURL, fullURL):
	cur.execute("INSERT INTO urlShortener VALUES ({},'{}','{}')".format(idx, shortenedURL, fullURL))
	con.commit()

def getLastIndex(cur):
	return cur.execute("SELECT MAX(idx) from urlShortener").fetchone()[0]

# cur = con.cursor()

# cur.execute('''CREATE TABLE urlShortener
#   (idx text, shortenedURL text, fullURL text)''')

# cur.execute("INSERT INTO urlShortener VALUES (1,'000000','www.google.com')")

# # Save (commit) the changes
# con.commit()

# for row in cur.execute("SELECT * FROM urlShortener WHERE shortenedURL == '000000'"):
#   print(row)

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# con.close()