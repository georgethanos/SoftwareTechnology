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


# Class for announcements
class Announcement:

  # Constructor
  def __init__(self, timestamp, author, text, website, kind):
    self.timestamp = timestamp
    self.author = author
    self.text = text
    self.website = website
    self.kind = kind


# Class for Rooms
class Room:

  # Constructor
  def __init__(self, name, capacity, kind, schedule):
    self.name = name
    self.capacity = capacity
    self.kind = kind
    self.schedule = schedule


# Class for Crawlers
class Crawler:

  # Constructor
  def __init__(self, websites, kind):
    self.websites = websites
    self.kind = kind

    
    ''' USE CASE 5 & 10 '''

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

  def RetrieveCourseInfo(self):
    pass


# Class for evaluations
class Evaluation:

  # Constructor
  def __init__(self, evaluator, rate, timestamp):
    self.evaluator = evaluator
    self.rate = rate
    self.timestamp = timestamp

  def MakeEvaluation(self):
    pass

  def CheckGrade(self):
    pass

  def StoreEvaluation(self):
    pass

  def RetrieveEvaluations(self):
    pass


# Class for QR-Stickers
class QRSticker:

  # Constructor
  def __init__(self, code, room):
    self.code = code
    self.room = room

  def ReadQR(self):
    pass

# Class for Admins
class Admin:

  # Constructor
  def __init__(self, name, log):
    self.name = name
    self.log = log

  def SendErrorLog(self):
    pass


# Class for Cameras
class Camera:

  # Constructor
  def __init__(self, trigger):
    self.trigger = trigger

  def EnableCamera(self):
    pass

  def CheckCamera(self):
    pass


# Class for ErrorFiles
class ErrorFile:

  # Constructor
  def __init__(self, id, code, text):
    self.id = id
    self.code = code
    self.text = text

  def CreateErrorLog(self):
    pass
  
  
  ''' USE CASE 1 & 4 '''

# Class for maps
class Map:

  # Constructor
  def __init__(self, name, kind):
    self.name = name
    self.kind = kind

  def RetrieveCategAndMap(self):
    pass

  def EndGps(self):
    pass


# Class for Markers
class Marker:

  # Constructor
  def __init__(self, name, coordinates, kind, color, data, timetable):
    self.name = name
    self.coordinates = coordinates
    self.kind = kind
    self.color = color
    self.data = data
    self.timetable = timetable

  def RetrieveCoord(self):
    pass

  def CheckOpenMarks(self):
    pass

  def RemoveClosedMarks(self):
    pass

  def RetrieveMarkerInfo(self):
    pass

  def CheckLoc(self):
    pass

  def LocAnalysis(self):
    pass

  def RetrieveMarker(self):
    pass


# Class for academies
class Academy:

  # Constructor
  def __init__(self, name, address, num_of_students, num_of_professors, inner_map):
    self.name = name
    self.address = address
    self.num_of_students = num_of_students
    self.num_of_professors = num_of_professors
    self.inner_map = inner_map

  def CheckIfAcademyBuild(self):
    pass

  def RetrievePdfInnerMap(self):
    pass

  def DownloadPdf(self):
    pass


