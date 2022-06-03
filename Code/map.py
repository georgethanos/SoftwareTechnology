# Connection with database
def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://****:************@cluster0.jnvsh.mongodb.net/StudentUp"
    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]


# Class for maps
class Map:
    # Constructor
    def __init__(self, name, tiles):
        self.name = name
        self.tiles = tiles

    # Create the map by adding tiles
    def RetrieveCategAndMap(self):
        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["tiles"]

        # Taking tiles from web
        for c in col.find():
            self.tiles = c['data']

        print("The categories are: Academies, Estia, Atms, Coffee shops, Deanery")

    def EnGps(self, **kwargs):
        kwargs['lat'] = 10.0
        kwargs['lon'] = 10.0
        print(kwargs)
