import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("service_account_key.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL' : "path_to_project.firebaseio.com",
    'storageBucket': 'path_to_project.appspot.com'
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