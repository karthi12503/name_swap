from flask import Flask, render_template,url_for,redirect,request
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql connection
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='karthi'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql = MySQL(app)

@app.route('/')
def home():
        con = mysql.connection.cursor()
        sql = "select * from users"
        con.execute(sql)
        res = con.fetchall()
        return render_template("index.html",datas = res)

#add user
@app.route('/addUser',methods=['POST','GET'])
def adduser():
	if request.method == "POST":
		fname = request.form['fname']
		mname = request.form['mname']
		lname = request.form['lname']
		con = mysql.connection.cursor()
		sql = "insert into users(NAME,MIDDLE_NAME,LAST_NAME) values(%s,%s,%s)"
		con.execute(sql,[fname,mname,lname])
		mysql.connection.commit()
		con.close()
		return redirect(url_for('home'))

	return render_template("Adduser.html")


if __name__ == "__main__":
	app.run(debug=True)
