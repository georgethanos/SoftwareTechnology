# Connection with database
def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://****:************@cluster0.jnvsh.mongodb.net/StudentUp"
    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]


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

    # Retrieve markers for categories
    def RetrieveCoord(self):

        # List with markers to be returned
        markers_list = []

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Markers"]

        for m in col.find():

            if ['kind'] == self.kind:
                marker = {
                    "name": m['name'],
                    "coordinates": m['coordinates'],
                    "kind": self.kind,
                    "color": 'white',
                    "data": m['data'],
                    "timetable": m['timetable']
                }
                markers_list.append(marker)

        return markers_list

    # Check marker's color
    def CheckOpenMarks(self):
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M")  # 22:30

        time = self.timetable.split("-")                          # 09:00-21:00
        time1 = time[0] + time[1] + time[2] + time[3] + time[4]   # 09:00
        time2 = time[6] + time[7] + time[8] + time[9] + time[10]  # 21:00
        if current_time > time2 or current_time < time1:
            # Closed point
            self.color = 'red'
        else:
            # Open point
            self.color = 'green'

    def RemoveClosedMarks(self):
        if self.color == 'green':
            print(self.name)

    def RetrieveMarkerInfo(self, marker_touch):
        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Markers"]

        for c in col.find():
            if c['name'] == marker_touch:
                self.data = c['data']

        return self.data
        # print(self.data)

    def CheckLoc(self):

        isFound1 = False

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Markers"]

        for c in col.find():
            if c['name'] == self.name:
                isFound1 = True

        return isFound1

    def LocAnalysis(self):
        print("Maybe yoy should search for: (ceid), (estia), ....")
        self.name = self.name.lower()

    # Retrieve markers for search
    def RetrieveMarker(self):

        isloc = self.CheckLoc()

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Markers"]

        if isloc:
            for c in col.find():
                if c['name'] == self.name:
                    self.name = c['name']
                    self.coordinates = c['coordinates']
                    self.kind = c['kind']
                    self.data = c['data']
                    self.timetable = c['timetable']
        else:
            print("Location don't found")
            # self.LocAnalysis()

        return isloc

