#!/usr/bin/python
# -*- coding:utf-8 -*-

''' Script for Class Note '''

# Class for students
class Student:

  # Constructor
  def __init__(self, username, password, name, surname, AM, import_year, email, kind):
    self.username = username
    self.password = password
    self.name = name
    self.surname = surname
    self.AM = AM
    self.import_year = import_year
    self.email = email
    self.kind = kind

  def FindStudent(self):
    # Connecting with database
    dbname = get_database()
    # Choosing collection
    col = dbname["Students"]

    for n in col.find():
        # Check only for user
        if n['AM'] == self.AM:
            username = n['username']

    return username


# Connection with database
def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://****:************@cluster0.jnvsh.mongodb.net/StudentUp"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]
