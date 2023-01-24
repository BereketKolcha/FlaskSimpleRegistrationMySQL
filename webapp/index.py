from flask import Flask , render_template ,request
import mysql.connector

app = Flask(__name__)

# configure a route handler
@app.route("/", methods=["GET", "POST"])
def index():
    errors = {}
    if request.method == "POST":
        uname = request.form["uName"]
        uphone = request.form["uPhone"]
        Uemail = request.form["uEmail"]
        if len(uname)<36:

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="test"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO officers (username, password, area) VALUES (%s, %s, %s)"
            val = (uname, uname, uname)
            mycursor.execute(sql, val)

            # mycursor.execute("SELECT * FROM officers")
            # myresult = mycursor.fetchall()
            # print(myresult)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
        else:
            errors["uName"] = ["username should not corrects"]
            print("record not inserted.")

        # check if the username starts with an alphabet
        # if not uname[0].isalpha():
        #     errors["uName"] = ["username should start with alphabets"]
    return render_template("home.html.j2", errors=errors)

# run the server
app.run(host="0.0.0.0", port=50100, debug=True)