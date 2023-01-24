from flask import Blueprint, render_template

booksCtrlr = Blueprint('books', __name__)

@booksCtrlr.route('/')
def list():
    return render_template("books/list.html")

# @booksCtrlr.route('/<int:id>')
# def getItem(id: int):
#     return render_template("books/detail.html", id=id)