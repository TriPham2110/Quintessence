from flask import Flask, render_template, request, jsonify, g, session, redirect, url_for
import os.path
import json
import hashlib

from userMethods import addUser, checkCredentials, userExists


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
        return "False"


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
        return "False"


@app.route('/profile', methods=['GET'])
def profile():
    if g.user:
        return render_template('profile.html', user = g.user)
    else:
        return redirect(url_for('login'))

@app.route('/gallery', methods=['GET'])
def gallery():
    return render_template('gallery.html')


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