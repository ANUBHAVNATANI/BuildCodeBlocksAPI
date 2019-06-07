import pyrebase

config = {
    "apiKey": "API key of the firebase database",
    "authDomain": "AuthDomain of the firebase database",
    "databaseURL": "Database Url of the firebase database",
    "storageBucket": "Stroage Bucket Url of the firebase database",
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
