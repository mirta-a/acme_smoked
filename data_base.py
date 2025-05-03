from pymongo import MongoClient

def get_database():


#  conectar a la base de datos
    acme_smoked_fish = "mongodb://localhost:27017"
    client = MongoClient(acme_smoked_fish)

    return client["acme_smoked_fish"]










