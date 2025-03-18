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




# Databases with SQL Model

In real-world applications it is essential to use a persistent database solution

PostgreSQL is a database management system, open source and free.

An Object-Relational Mapper (ORM) translates between a programming language, such as Python, and a database, like PostgreSQL.

SQLAlchemy is the most popular ORM for Python mapping objects to database tables and providing a high-level SQL language.

# When is the right time to connect to a database?

It is when the application starts running

# Connecting the database to the application

async def init_db()