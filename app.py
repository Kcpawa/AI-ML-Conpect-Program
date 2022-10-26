from flask import Flask,redirect,url_for,render_template,request
import sqlite3
app=Flask(__name__)
app.secret_key="123"

#con=sqlite3.connect("Database.db")
#con.execute("create table detail(name varchar(20),email varchar(40) UNIQUE,Password varchar(40),Re_typr_Password varchar(40))")
@app.route('/')
@app.route('/Register')
def Route1():
	return render_template("indexx.html")
@app.route('/add')
def Add():
	return render_template("add.html")
@app.route("/savedetail",methods=["POST","GET"])		
def Save():
	msg="msg"
	if request.method =="POST":
		
		try:
			name = request.form["name"]
			email = request.form["email"]
			Password = request.form["Password"]		
			Re_type_Password= request.form["Re_type_Password"]
			with sqlite3.connect("Database.db") as con:
				cur= con.cursor()
				cur.execute("insert into detail(name,email,Password,Re_typr_Password)values(?,?,?,?)",(name,email,Password,Re_type_Password))
				con.commit()
				msg="Successful!!"
		except:
			con.rollback()
			msg="sorry we failed"
		finally:
			return render_template("success.html",msg=msg)
		
			
if __name__==("__main__"):
	app.run(debug=True)