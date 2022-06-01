# Connection with database
def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://****:************@cluster0.jnvsh.mongodb.net/StudentUp"
    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]


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
        isFound2 = False

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Academies"]

        for c in col.find():
            if c['name'] == self.name:
                print(f"{self.name}_inner_map.png found")
                isFound2 = True

        return isFound2

    def RetrievePdfInnerMap(self):
        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Academies"]

        for c in col.find():
            if c['name'] == self.name:
                self.name = c['name']
                self.address = c['address']
                self.num_of_students = c['num_of_students']
                self.num_of_professors = c['num_of_professors']
                self.inner_map = c['inner_map']

    def DownloadPdf(self):
        # download to phone
        # imported the requests library
        import requests
        image_url = self.inner_map
        # URL of the image to be downloaded is defined as image_url
        # create HTTP response object
        r = requests.get(image_url)
        # send a HTTP request to the server and save
        # the HTTP response in a response object called r
        with open("inner_map.png", 'wb') as f:
            # Saving received content as a png file in
            # binary format
            # write the contents of the response (r.content)
            # to a new file in binary mode.
            f.write(r.content)
