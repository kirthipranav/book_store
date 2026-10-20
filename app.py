from flask import Flask, render_template, request, redirect, session
from database_connection import DatabaseConnection
from book_repository import BookRepository
from book import Book
from user import User
from user_repository import UserRepository
from login_required import *

app = Flask(__name__)
app.secret_key = "some_really_secret_key"

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello to you too"

@app.route("/books", methods=["GET"])
def books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books=books)

@app.route("/authors", methods=["GET"])
def authors():
    author_list = [{"name": "Julia Donaldson", "dob": "1948-09-16"}, {"name": "Andrea Beaty", "dob": "1961-10-08"}, {"name": "Kelly Barnhill", "dob": "1973-01-01"}, {"name": "Zetta Elliott", "dob": "1979-11-11"}]
    return author_list

def is_authenticated(session):
    return "user_id" in session

@app.route('/books', methods=['POST'])
@login_required
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"])
    book_repository.create(book)
    return redirect("/books")

@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("/books")

@app.route('/users/new', methods=['GET'])
def get_signup_form():
    return render_template("signup_form.html")

@app.route('/sessions/new', methods=['GET'])
def get_login_form():
    return render_template("login_form.html")

@app.route('/sessions', methods=['POST'])
def create_session():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    username = request.form["username"]
    password = request.form["password"]
    user = user_repository.find_by_username(username)
    if user and user.password == password:
        session["user_id"] = user.id
        session["username"] = user.username
        return redirect("/books")
    else:
        return redirect("/sessions/new")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
