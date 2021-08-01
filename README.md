# URLShortener

## Sorry I do not have time to come up with a better version especially the frontend because I am in the last few weeks of schools (dated 02/08/2021)

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
