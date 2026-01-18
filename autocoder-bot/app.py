from flask import Flask, request, jsonify
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.serialize() for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if 'title' not in data or 'author' not in data or 'isbn' not in data:
        return jsonify({'error': 'Missing data'}), 400
    book = Book(title=data['title'], author=data['author'], isbn=data['isbn'])
    db.session.add(book)
    db.session.commit()
    return jsonify(book.serialize()), 201
