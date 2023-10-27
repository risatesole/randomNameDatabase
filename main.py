# random person data generator
import requests
import sqlite3 as sql
import time

def createDatabaseFile():
    conn = sql.connect("randomNames.db")
    conn.commit()
    conn.close()

def createTables():
    conn = sql.connect("randomNames.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS PEOPLE(
            title text,
            firstName text,
            lastName text,
            gender text,
            city text,
            country text
        )"""
    )
    conn.commit()
    conn.close()

# insert one row into database 
def insertDataDatabase():

    response = requests.get("https://randomuser.me/api")
    title = response.json()['results'][0]['name']['title']
    gender = response.json()['results'][0]['gender']
    firstName = response.json()['results'][0]['name']['first']
    lastName = response.json()['results'][0]['name']['last']
    locationCity = response.json()['results'][0]['location']['city']
    locationCountry = response.json()['results'][0]['location']['country']

    conn = sql.connect("randomNames.db")
    cur = conn.cursor()
    cur.execute("insert into PEOPLE (title, firstName, lastName, gender, city, country) values (?, ?, ?,?, ?, ?)",(title , firstName, lastName, gender,locationCity, locationCountry))
    conn.commit()
    conn.close()

createDatabaseFile()
createTables()
insertDataDatabase()