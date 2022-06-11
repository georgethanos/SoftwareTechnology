#!/usr/bin/python
# -*- coding:utf-8 -*-

''' Script for Class Comment '''

# Class for comments
class Comment:

  # Constructor
  def __init__(self, subject, text, timestamp, score, note_name, comment_writer):
    self.subject = subject
    self.text = text
    self.timestamp = timestamp
    self.score = score
    self.note_name = note_name
    self.comment_writer = comment_writer

  def RetrieveComment(self):
    # List with comments to be returned
    comment_list = []

    # Connecting with database
    dbname = get_database()
    # Choosing Comments collection
    col = dbname["Comments"]

    for n in col.find():
      # Check only comments from the selected course and note
      if n['course'] == self.subject and n['note_name'] == self.note_name:

        comment = {
          "text": n['text'],
          "score": n['score'],
          "comment_writer": n['comment_writer']
        }
        comment_list.append(comment)

    if len(comment_list) == 0:
      return False
    else:
      return comment_list

  # SAKIS

  def CheckForm(self, text, score):
    isRight = False

    if text is None or score is None:
      isRight = False

    else:
      isRight = True

    return isRight



  def StoreComment(self, text, subject, timestamp, score, note_name, comment_writer):

    hasCreated = False

    self.subject = subject
    self.text = text
    self.timestamp = timestamp
    self.score = score
    self.note_name = note_name
    self.comment_writer = comment_writer


    hasCreated = self.CheckForm(self.text, self.score)

    if hasCreated is True:

      # Connecting with database
      dbname = get_database()
      # Choosing collection

      col = dbname["Comments"]

      comment = {
        "subject": self.subject,
        "text": self.text,
        "timestamp": self.timestamp,
        "score": self.score,
        "note_name": self.note_name,
        "comment_writer": self.comment_writer
      }

      col.insert_one(comment)
      print("Comment added successfully!")

    return hasCreated


# Connection with database
def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://****:************@cluster0.jnvsh.mongodb.net/StudentUp"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]
