''' Testing Code for (without UI) '''

# Libraries
from datetime import datetime
from plyer import gps

# Classes
import Evaluation
import Course
import QRSticker
import Admin
import Camera
import ErrorFile
import Note
import Comment
import Academy
import Map
import Marker

#-----------------------------------------------------------------------------------------------------------------------

# Testing Note (Use Case 6)

# User's inputs
name = "Data_Mining-sos"
description = "This file contains sos for Data Mining course"
file = "Data_Mining-sos.zip"

# System data (from previous menus)
user = 'andrew97'
timestamp = datetime.now().strftime('%d-%m-%Y')
course = "Data Mining"

aNote = Note.Note(name, course, timestamp, description, user)
aNote.StoreNote(1)
notes = aNote.RetrieveNote()

notes_list = []  # List with all note objects

for x in range(len(notes)):

    filename = notes[x]['filename']
    course = notes[x]['course']
    timestamp = notes[x]['timestamp']
    description = notes[x]['description']
    author = notes[x]['author']

    notes_list.append(Note.Note(filename, course, timestamp, description, author))

for x in notes_list:
    print(x.filename)

#-----------------------------------------------------------------------------------------------------------------------

# Testing Comment (Use Case 9)

text = None
score = 5
userC = 'michellehunt'
isCreated = False

aComment = Comment.Comment('','','','','','')
isCreated = aComment.StoreComment(text, notes_list[0].course, timestamp, score, notes_list[0].filename, userC)
print(isCreated)

#-----------------------------------------------------------------------------------------------------------------------

# Testing Course and Evaluation (Use Case 5)

# User's inputs
rate = 5
comments = 'Nice one!'

# System data (from previous menus)
user = 'andrew97'
timestamp = datetime.now().strftime('%d-%m-%Y')

aCourse = Course.Course()
course = "Data Mining"

aEvaluation = Evaluation.Evaluation(user, course, rate, comments, timestamp)
isValid = aEvaluation.MakeEvaluation(rate, comments)
if isValid is True:
    aEvaluation.StoreEvaluation()
else:
    print(f'Evaluation is invalid!')

evaluations = aEvaluation.RetrieveEvaluations()

evaluations_list = []  # List with all evaluation objects

for x in range(len(evaluations)):

    course = notes[x]['filename']
    evaluator = notes[x]['course']
    rate = notes[x]['timestamp']
    comments = notes[x]['description']
    timestamp = evaluations[x]['timestamp']

    evaluations_list.append(Evaluation.Evaluation(course, evaluator, rate, comments, timestamp))

for x in evaluations_list:
    print(x.filename)

#-----------------------------------------------------------------------------------------------------------------------

# Testing Camera, QRSticker, ErrorFile and Admin (Use Case 10)

aCamera = Camera.Camera(False)
camera_input = aCamera.EnableCamera()
code_input = 100

aQRSticker = QRSticker.QRSticker('', '', '')

# User choose input
# Camera or code
# If there is no camera input then the code is taken as input
aQRSticker.ReadQR(camera_input, code_input)

# System data (from previous menus)
qrcode = 100
id = datetime.now().strftime('%d%m%Y') + str(qrcode)
text = f'Error on QR-sticker with code {qrcode}!'

aErrorFile = ErrorFile.ErrorFile(id, 1, text)
error_file = aErrorFile.CreateErrorLog(camera_input)

if error_file is not None:
    aAdmin = Admin.Admin('panagiotis_tslk', 107)
    aAdmin.SendErrorLog(error_file)

#-----------------------------------------------------------------------------------------------------------------------

# Testing Marker and Map (Use Case 1)

# Attribute name is taken from Class Universities
uni_name = 'University of Patras'
lat = 2000012120
lon = 2000902120
category_markers_list = []

aMap = Map.Map(uni_name, [])
aMap.RetrieveCategAndMap()

# User choose find by category
category = 'academy'
aMarker = Marker.Marker('', '', category, '', '', '')
category_markers = aMarker.RetrieveCoord()

for x in range(len(category_markers)):

    name = category_markers[x]['name']
    coordinates = category_markers[x]['coordinates']
    kind = category_markers[x]['kind']
    color = category_markers[x]['color']
    data = category_markers[x]['data']
    timetable = category_markers[x]['timetable']

    category_markers_list.append(Marker.Marker(name, coordinates, kind, color, data, timetable))

# Keep only open points
for m in category_markers_list:
    m.CheckOpenMarks()
    m.RemoveClosedMarks()

# For every marker in markers list take the name of marker and check if it's category = academy
for m in category_markers_list:
    mar_name = m.name
    aAcademy = Academy.Academy(mar_name, '', '', '', '')
    isFound_acad = aAcademy.CheckIfAcademyBuild()
    if isFound_acad:
        aAcademy.RetrievePdfInnerMap()
        aAcademy.DownloadPdf()
    else:
        print(f"There is no {mar_name}_inner_map.png!")

#-----------------------------------------------------------------------------------------------------------------------

# Testing Academy and Map (Use Case 4)

# User choose find by search
name = 'ceid'
aMarker = Marker.Marker(name, '', '', '', '', '')
isFound = aMarker.RetrieveMarker()

# Run RetrieveMarker another one time with lowercase name
if not isFound:
    aMarker.LocAnalysis()
    aMarker.RetrieveMarker()

# Choosing GPS
gps.configure(on_location=aMap.EnGps())
# Taking user's coordinates
gps.start(minTime=1000)
gps.stop()
