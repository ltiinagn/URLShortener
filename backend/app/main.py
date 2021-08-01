import uvicorn
from fastapi import FastAPI, Request, Response, APIRouter
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
import pandas as pd

from custom_errors import URLNotFoundError
from models import URLData

import time

CHARACTERS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM_CHARACTERS = 6
COLUMNS = ["index", "shortenedURL", "fullURL"]
DTYPES = {"index": "int64", "shortenedURL": "str", "fullURL": "str"}
CSV_PATH = "../data/urls.csv"

app = FastAPI()

def computeShortenedURL(x):
	shortenedURL = ""
	for power in range(5, -1, -1):
		index = x // len(CHARACTERS) ** power
		shortenedURL += CHARACTERS[index]
		x = x % len(CHARACTERS) ** power
	return shortenedURL

@app.get("/go/{url}")
def getFullURL(url: str):
	try:
		df = pd.read_csv(CSV_PATH, dtype = DTYPES)
		result = df.loc[df['shortenedURL'] == url]
		if result.empty:
			raise URLNotFoundError
		else:
			fullURL = result.iloc[0]["fullURL"]
			return JSONResponse(content={"fullURL": fullURL})
	except (FileNotFoundError, URLNotFoundError):
		return JSONResponse(content={"fullURL": ""})

@app.post("/shorten/")
def getShortenedURL(urlData: URLData):
	try:
		df = pd.read_csv(CSV_PATH, dtype = DTYPES)
		lastLine = df.tail(1)
		x = int(lastLine["index"]) + 1
	except FileNotFoundError:
		df = pd.DataFrame(columns = COLUMNS)
		df.astype(DTYPES).dtypes
		x = 0
	result = df.loc[df['fullURL'] == urlData.url]
	if result.empty:
		shortenedURL = computeShortenedURL(x)
		df.loc[x] = [x, shortenedURL, urlData.url]
		df.to_csv(CSV_PATH, index = False)
	else:
		shortenedURL = result.iloc[0]["shortenedURL"]

	return JSONResponse(content={"shortenedURL": shortenedURL})

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