# These my notes specifically for my FastAPI Learning

To install FastAPI

- pip install fastapi

To run FastAPI

- fastapi dev main.py

To set up your first FastAPI app:

from fastapi import FastAPI
app = FastAPI()

# Make classes to make the crud apps

Example:

@app.get - gets the data
@app.post - makes new data into the database
@app.patch - update the data
@app.delete - deletes the data from the data base


Status codes

# Don't forget to pip freeze > requirements.txt to ensure that the correct files and versions are up to date.