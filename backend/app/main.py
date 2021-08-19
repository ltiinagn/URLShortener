import uvicorn
from fastapi import FastAPI, Request, Response, APIRouter
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
import pandas as pd
import os

from custom_errors import URLNotFoundError
from models import URLData

import sys
sys.path.append("./../..")
from database.app.main import connect, findEntry, addEntry, getLastIndex, updateEntryCount

CHARACTERS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM_CHARACTERS = 6
VALID_TIMES = 5
# # CSV way
# COLUMNS = ["index", "shortenedURL", "fullURL"]
# DTYPES = {"index": "int64", "shortenedURL": "str", "fullURL": "str"}
# CSV_FOLDER_PATH = "../data"
# CSV_PATH = "../data/urls.csv"

# SQLite way
DATABASE_FOLDER_PATH = "../../database/data"
DATABASE_PATH = "../../database/data/URLShortener.db"

app = FastAPI()

con = connect(DATABASE_FOLDER_PATH, DATABASE_PATH)
cur = con.cursor()

def computeShortenedURL(x):
	shortenedURL = ""
	for power in range(5, -1, -1):
		index = x // len(CHARACTERS) ** power
		shortenedURL += CHARACTERS[index]
		x = x % len(CHARACTERS) ** power
	return shortenedURL

# SQLite way
@app.get("/go/{url}")
def getFullURL(url: str):
	res = findEntry(cur, "shortenedURL", url)
	if res:
		times = res[3] + 1
		# if resUpdate.rowcount == 1:
		if times <= VALID_TIMES:
			resUpdate = updateEntryCount(con, cur, "times", times, "shortenedURL", url)
			return JSONResponse(content={"fullURL": res[2]})
	else:
		return JSONResponse(content={"fullURL": ""})

@app.post("/shorten/")
def getShortenedURL(urlData: URLData):
	res = findEntry(cur, "fullURL", urlData.url)
	if res is None:
		idx = getLastIndex(cur)
		if idx is None:
			idx = 0
		else:
			idx += 1
		shortenedURL = computeShortenedURL(idx)
		addEntry(con, cur, idx, shortenedURL, urlData.url)
		res = findEntry(cur, "fullURL", urlData.url)
	return JSONResponse(content={"shortenedURL": res[1]})

# # CSV way
# @app.get("/go/{url}")
# def getFullURL(url: str):
# 	try:
# 		df = pd.read_csv(CSV_PATH, dtype = DTYPES)
# 		result = df.loc[df['shortenedURL'] == url]
# 		if result.empty:
# 			raise URLNotFoundError
# 		else:
# 			fullURL = result.iloc[0]["fullURL"]
# 			return JSONResponse(content={"fullURL": fullURL})
# 	except (FileNotFoundError, URLNotFoundError):
# 		return JSONResponse(content={"fullURL": ""})

# @app.post("/shorten/")
# def getShortenedURL(urlData: URLData):
# 	try:
# 		df = pd.read_csv(CSV_PATH, dtype = DTYPES)
# 		lastLine = df.tail(1)
# 		x = int(lastLine["index"]) + 1
# 	except FileNotFoundError:
# 		if not os.path.exists(CSV_FOLDER_PATH):
# 			os.makedirs(CSV_FOLDER_PATH)
# 		df = pd.DataFrame(columns = COLUMNS)
# 		df.astype(DTYPES).dtypes
# 		x = 0
# 	result = df.loc[df['fullURL'] == urlData.url]
# 	if result.empty:
# 		shortenedURL = computeShortenedURL(x)
# 		df.loc[x] = [x, shortenedURL, urlData.url]
# 		df.to_csv(CSV_PATH, index = False)
# 	else:
# 		shortenedURL = result.iloc[0]["shortenedURL"]

# 	return JSONResponse(content={"shortenedURL": shortenedURL})

origins=["*"]
app = CORSMiddleware(
    app=app,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)