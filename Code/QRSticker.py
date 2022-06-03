#!/usr/bin/python
# -*- coding:utf-8 -*-

''' Script for Class QRSticker '''

# Libraries
import qrcode

# Class for QR-Stickers
class QRSticker:

  # Constructor
  def __init__(self, code, room, capacity):
    self.code = code
    self.room = room
    self.capacity = capacity

  # Reading QR and displaying data to user depending input
  def ReadQR(self, camera_input, code_input):

    # Taking scan for input
    if camera_input is not None:
      print(f'\nRoom: {self.room}\nCapacity: {self.capacity}\nCode: {self.code}')

    # Taking code for input
    elif camera_input is None:

      # Connecting with database
      dbname = get_database()
      # Choosing collection
      col = dbname["QRStickers"]

      for q in col.find():

        if q['code'] == code_input:
          self.room = q['room']
          self.capacity = q['capacity']
          self.code = q['code']

    # No input
    else:
      print('QR sticker is damaged!')

# Connection with database
def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://****:************@cluster0.jnvsh.mongodb.net/StudentUp"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]
