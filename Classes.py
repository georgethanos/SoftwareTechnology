''' Script with classes '''


# Class for students
class Student:

  # Constructor
  def __init__(self, name, surname, AM, import_year, email):
    self.name = name
    self.surname = surname
    self.AM = AM
    self.import_year = import_year
    self.email = email


# Class for courses
class Course:

  # Constructor
  def __init__(self, name, semester, academy, professor, ECTS, points):
    self.name = name
    self.semester = semester
    self.academy = academy
    self.professor = professor
    self.ECTS = ECTS
    self.points = points


# Class for notes
class Note:

  # Constructor
  def __init__(self, file, course, timestamp, description, author):
    self.file = file
    self.course = course
    self.timestamp = timestamp
    self.description = description
    self.author = author


# Class for comments
class Comment:

  # Constructor
  def __init__(self, subject, text, timestamp):
    self.subject = subject
    self.text = text
    self.timestamp = timestamp


# Class for evaluations
class Evaluation:

  # Constructor
  def __init__(self, evaluator, rate, timestamp):
    self.evaluator = evaluator
    self.rate = rate
    self.timestamp = timestamp


# Class for announcements
class Announcement:

  # Constructor
  def __init__(self, timestamp, author, text, website, kind):
    self.timestamp = timestamp
    self.author = author
    self.text = text
    self.website = website
    self.kind = kind


# Class for maps
class Map:

  # Constructor
  def __init__(self, name, kind):
    self.name = name
    self.kind = kind


# Class for inner maps
class InnerMap:

  # Constructor
  def __init__(self, name, building, rooms):
    self.name = name
    self.building = building
    self.rooms = rooms


# Class for academies
class Academy:

  # Constructor
  def __init__(self, name, address, num_of_students, num_of_professors):
    self.name = name
    self.address = address
    self.num_of_students = num_of_students
    self.num_of_professors = num_of_professors


# Class for QR-Stickers
class QRSticker:

  # Constructor
  def __init__(self, code, room):
    self.code = code
    self.room = room


# Class for Rooms
class Room:

  # Constructor
  def __init__(self, name, capacity, kind, schedule):
    self.name = name
    self.capacity = capacity
    self.kind = kind
    self.schedule = schedule


# Class for Markers
class Marker:

  # Constructor
  def __init__(self, name, coordinates, kind, color, data):
    self.name = name
    self.coordinates = coordinates
    self.kind = kind
    self.color = color
    self.data = data


# Class for Crawlers
class Crawler:

  # Constructor
  def __init__(self, websites, kind):
    self.websites = websites
    self.kind = kind

