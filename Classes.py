''' Script with classes '''

    
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

''' USE CASE 6, 7 & 8 '''

# Class for notes
class Note:

  # Constructor
  def __init__(self, file, course, timestamp, description, author):
    self.file = file
    self.course = course
    self.timestamp = timestamp
    self.description = description
    self.author = author

  def SearchNote(self):
    pass

  def RetrieveNoteNames(self):
    pass

  def DownloadNote(self):
    pass

  def MakeNote(self):
    pass

  def CheckFileSize(self):
    pass

  def StoreNote(self):
    pass

  def RetrieveNote(self):
    pass

  def UpdateNote(self):
    pass

  def SaveNote(self):
    pass

  def DeleteNote(self):
    pass
  
  def CheckDownloadedNotes(self):
    pass


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

  def SearchComment(self):
    pass

  def RetrieveComment(self):
    pass
  
   def CreateDownloadedNotes(self):
    pass

  def CheckForm(self):
    pass

  def StoreComments(self):
    pass


# Class for students
class Student:

  # Constructor
  def __init__(self, name, surname, AM, import_year, email):
    self.name = name
    self.surname = surname
    self.AM = AM
    self.import_year = import_year
    self.email = email

  def FindStudent(self):
    pass
  

''' USE CASE 9 & 11 '''

# Class for announcements
class Announcement:

  # Constructor
  def __init__(self, timestamp, author, text, website, kind):
    self.timestamp = timestamp
    self.author = author
    self.text = text
    self.website = website
    self.kind = kind

  def StoreAnnouncements(self):
    pass

  def ReclassifyAnnouncements(self):
    pass

  def CheckSourceAnnouncements(self):
    pass

  def RetrieveAnnouncement(self):
    pass

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

  def ActivateCrawler(self):
    pass
  
