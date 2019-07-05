# quintessence
A personal gallery project for testing and getting familiar with HTML, CSS, JavaScript, Windows PowerShell, Python, Flask, and Firebase API

# instructions
1. Install Flask (Python's microframework) (check out this link for an easy to install Flask https://www.youtube.com/watch?v=zPMr0lEMqpo)
2. Install Python 3 (3.6.5 recommended)
3. Download the files from this repository
4. Register on Firebase to create a new project and retrieve the service account key (or json file)
5. Copy and paste the json file inside the folder "app_need_serviceAccountKey"
6. Open userMethods.py and update the service account key and databaseURL
7. Open Windows PowerShell
8. Navigate and change directory to where the file "server.py" is
9. Use command "pip install firebase-admin" for Firebase API purpose
10. Type in command "py server.py" to run the program
11. Once the program runs, open a browser and enter "localhost:8000"
13. The link will lead the user to the main page to interact with other webpages using a local server
14. The user can also go to the Realtime Database in the Firebase console to see the changes made for authentication feature

# to-do things
Expand the applications of this project such as including music, calendar, etc.
Photo gallery needs tranferred to Firebase for realtime database purposes
Update the look of some features
 
# demonstration

![testFirebase](https://user-images.githubusercontent.com/44308446/60702239-f3f14f00-9ec3-11e9-8ef0-509594296d86.png)
Fig1. Firebase realtime database

![testFirebase3](https://user-images.githubusercontent.com/44308446/60640592-78bd6980-9ded-11e9-9d77-6b47fdd1453c.png)
Fig2. Login page using the credentials from the database

![testFirebase4](https://user-images.githubusercontent.com/44308446/60640594-7fe47780-9ded-11e9-8d74-dd514249d056.png)
Fig3. Profile page after the successful login

![testFirebase5](https://user-images.githubusercontent.com/44308446/60702402-8e519280-9ec4-11e9-80e9-67a1bb76404f.png)
Fig4. User's gallery (still need realtime interaction with the database)
