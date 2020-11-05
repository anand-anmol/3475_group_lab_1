from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="p",
    database="lamp",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()


@app.route("/", methods=["GET"])
def home():
	cursor.execute('SELECT * FROM lamp.student;')
	student_list = cursor.fetchall()
	return render_template('index.html', student=student_list)


if __name__ == '__main__':
    app.run()
