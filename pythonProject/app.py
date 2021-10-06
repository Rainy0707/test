import sqlite3

from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def registartion():
    return render_template('student.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            add = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("pythonsqlite.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO registration (name, addr, city, pin) VALUES (?,?,?,?)",(nm, add, city, pin))
                msg = "Record successful"

        except:
            con.rollback()
            msg = "error"

        finally:
            return render_template("result.html", msg = msg)
            con.close()



@app.route('/addlogin', methods=['POST', 'GET'])
def addlogin():
    if request.method == 'POST':
        try:
            usr = request.form['usr']
            password = request.form['password']

            with sql.connect("pythonsqlite.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO login (username, password) VALUES (?,?)",(usr, password))
                msg = "Record successful"

        except:
            con.rollback()
            msg = "error"

        finally:
            return render_template("result.html", msg = msg)
            con.close()



@app.route('/list')
def list():
    con = sqlite3.connect('pythonsqlite.db')
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("select * from registration")




    rows = cur.fetchall()

    return render_template("list.html", rows=rows)


if __name__ =='__main__':
    app.run(debug=True)
    print("hello")
