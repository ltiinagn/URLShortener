# URLShortener

- Sorry I do not have time to come up with a better version especially the frontend because I am in the last few weeks of school (dated 02/08/2021)
- This URL shortener works by mapping the full URL to a string of alphanumeric characters (A-Z, a-z, 0-9 for a total of 62 characters) of length 6.
- If a full URL has already been shortened before, the program will retrieve the existing shortened URL.
- This means that a total of 62^6 unique full URLs can be shortened.

## Frontend
- Created with ReactJS
### Running frontend
- Navigate into folder `frontend` and run command (NodeJS has to be installed)
```
npm start
```

## Backend
- Created with Python
- Created using FastAPI
- v0.1 uses pandas to store the map of full URLs and shortened URLs, i.e., no database
### Running backend
- Navgiate into folder `backend` and run command to install Python libraries (ideally in a virtual environment (venv))
```
pip install -r requirements.txt
```
- Navigate into subfolder `app` and run command
```
uvicorn main:app --reload
```
