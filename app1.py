
from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)

@app.route('/')
def home():
	return render_template("indexx.html")
@app.route('/Contact')
def Route():
	return render_template("cont.html")
@app.route('/Register')
def Route1():
	return render_template("indexx.html")
@app.route('/home')
def summa():
	return "<h2>YEAH YOU RETURN TO THE HOME PAGE</h2>"
@app.route('/<name>')
def admin(name):
	return render_template("index.html")
@app.route('/home/<name>')
def variya(name):
	return f"<h2>YEAH YOU RETURN TO THE HOME PAGE {name} </h2>"
@app.route('/Admin')
def user():
	return redirect(url_for("summa"))



if __name__==("__main__"):
	app.run(debug=True)