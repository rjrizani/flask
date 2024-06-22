from flask import Flask, render_template
app = Flask(__name__)                    # Create a new instance of the Flask class called "app"
title = 'Book List'
books = [
    {
        'id': 0,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'year': 1992,
        'description': 'A novel attributed to C.S. Lewis'
    },
    {
        'id': 1,
        'title': 'The Salmon of Doubt',
        'author': 'Ahmad rizani',
        'year': 1999,
        'description': 'A novel attributed to C.S. Lewis'
    }
]

#route for homepage book_list.html

@app.route('/')
def book_list():
    return render_template('book_list.html', Title=title, books=books)

@app.route('/books/<int:book_id>')
def book_detail(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return render_template('book_detail.html', book=book)
    else:
        return 'Book not found'


if __name__ == '__main__':
    app.run(debug=True)