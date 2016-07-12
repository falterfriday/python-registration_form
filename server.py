from flask import Flask, render_template, redirect, request, session, flash

import re, datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')


app = Flask(__name__)

app.secret_key = "ihuvlbln;kq3ijop34ty89ergiohdfbm"

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
	if len(request.form['email']) < 1:
		flash("email required")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("invalid email address!")
	else:
		flash("email success!")
	if len(request.form['f_name']) < 1:
		flash("first name required")
	elif not NAME_REGEX.match(request.form['f_name']):
		flash("invalid first name")
	else:
		flash("first name success!")
	if len(request.form['l_name']) < 1:
		flash("last name required")
	elif not NAME_REGEX.match(request.form['l_name']):
		flash("invalid last name")
	else:
		flash("last name success!")
	if len(request.form['password']) < 8:
		flash("longer password required")
	elif not PASSWORD_REGEX.match(request.form['password']):
		flash("invalid password")
	else:
		flash("password success!")
	if request.form['password'] != request.form['conf_password']:
		flash("passwords dont match")
	else:
		flash("passwords match!")
	mydate = []
	today = datetime.date.today()
	mydate.append(today)
	if str(request.form['birthday']) != str(mydate[0]):
		flash("birthday success!")
	return redirect('/')



app.run(debug=True)