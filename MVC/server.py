from flask import Flask, render_template
from src.controllers.books import booksCtrlr
# from src.controllers.authors import authorsCtrlr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

app.register_blueprint(booksCtrlr, url_prefix="/src/controllers/books")
# app.register_blueprint(authorsCtrlr, url_prefix="/authors")

app.run(host="0.0.0.0", port=50100, debug=True)