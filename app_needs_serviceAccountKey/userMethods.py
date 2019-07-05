import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Fetch the service account key JSON file contents
cred = credentials.Certificate("path/to/serviceAccountKey.json")

#Initialize the app with a service account
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://databaseName.firebaseio.com"
})

root = db.reference()
users_ref = root.child('users')

def addUser(username, password):
    print (username,password)
    users_ref.child(username).set({'password': password})
    return True

def checkCredentials(username, password):
    if userExists(username):
        credentials = users_ref.child(username).get()
        if password == credentials['password']:
            return True
        else:
            return False
    else:
        return False


def userExists(username):
    if users_ref.child(username).get() != None:
        return True
    else:
        return False