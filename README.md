# URLShortener

- Sorry I do not have time to come up with a better version especially the frontend because I am in the last few weeks of school (dated 02/08/2021)
- This URL shortener allows users to enter a full URL to obtain a shortened URL, vice versa.
  - In retrieving the full URL from the shortened URL, the full URL will first be displayed, which can be clicked by the user after the user has verified the full URL.
- The shortener works by mapping the full URL to a string of alphanumeric characters (A-Z, a-z, 0-9 for a total of 62 characters) of length 6.
- If a full URL has already been shortened before, the program will retrieve the existing shortened URL.
- This means that a total of 62^6 unique full URLs can be shortened.

## Frontend
- Created with ReactJS
### Running frontend
- Only on first run, navigate into folder `frontend` and run command (NodeJS has to be installed)
```
npm install
```
- If not already, navigate into folder `frontend` and run command
```
npm start
```

## Backend
- Created with Python
- Created using FastAPI
- v0.2 uses sqlite3 to store the table of full URLs and shortened URLs
  - SQLite was used over MySQL for ease of setting up (all written in code, no additional step required to run)
- v0.1 (old) uses pandas to store the table of full URLs and shortened URLs, i.e., no database
  - Commented out in code for reference
### Running backend
- Only on first run, navgiate into folder `backend` and run command to install Python libraries (ideally in a virtual environment (venv))
```
pip install -r requirements.txt
```
- Navigate into subfolder `app` and run command
```
uvicorn main:app --reload
```
