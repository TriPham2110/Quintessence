from flask import Flask, render_template, request, jsonify, g, session, redirect, url_for, flash, send_from_directory
import os.path
import json
import hashlib

from userMethods import addUser, checkCredentials, userExists

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/api/login',methods=['POST'])
def loginApi():

    # s = request.form.to_dict()['json_string']
    # json_acceptable_string = s.replace("'","\"")
    # d = json.loads(json_acceptable_string)
    #
    # h = hashlib.md5(d['password'].encode())
    # hashed_password = h.hexdigest()

    h = hashlib.md5(request.form['password'].encode())
    hashed_password = h.hexdigest()

    if checkCredentials(request.form['username'],hashed_password):
        session['user'] = request.form['username']
        return redirect(url_for('profile'))
    else:
        flash("Invalid credentials. Try again!")
        return render_template('login.html')

@app.route('/create', methods=['GET'])
def create():
    return render_template('create_account.html')


@app.route('/api/create', methods=['POST'])
def createApi():
    if not userExists(request.form['username']):
        h = hashlib.md5(request.form['password'].encode())
        hashed_password = h.hexdigest()

        addUser(request.form['username'],hashed_password)
        return redirect(url_for('login'))
    else:
        flash("User already exists. Try again!")
        return render_template('create_account.html')


@app.route('/profile', methods=['GET'])
def profile():
    if g.user:
        return render_template('profile.html', user = g.user)
    else:
        return redirect(url_for('login'))

@app.route('/profile', methods=['POST'])
def upload():
    #target = os.path.join(APP_ROOT, 'images/')
    target = os.path.join(APP_ROOT, 'static/images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    #return send_from_directory("images", filename, as_attachment=True)
    return render_template('complete.html', image_name=filename)

@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory('./static/images', filename)

#@app.route('/api/complete', methods=['POST'])
#def complete():
#    session.pop('user', None)
#    return redirect(url_for('login'))

@app.route('/gallery')
def gallery():
    image_names = os.listdir('./static/images')
    print(image_names)
    return render_template('gallery.html', image_names=image_names)

@app.route('/api/dropsession', methods=['GET'])
def dropsession():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)