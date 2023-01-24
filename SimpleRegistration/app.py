from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', user=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Registered Successfully")
        fname = request.form['fname']
        lname = request.form['lname']
        sex = request.form['sex']
        address = request.form['address']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (fname, lname, sex, address) VALUES (%s, %s, %s, %s)", (fname, lname, sex, address))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM user WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))



@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        fname = request.form['fname']
        lname = request.form['lname']
        sex = request.form['sex']
        address = request.form['address']

        cur = mysql.connection.cursor()
        cur.execute(
        "UPDATE user SET fname=%s, lname=%s, sex=%s, address=%s WHERE id=%s"
        , (fname, lname, sex, address, id_data))
        mysql.connection.commit()
        flash("Data Updated Successfully")
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)