import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

# Routes
#http://127.0.0.1:5000/
@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# A route to return all of the available entries in our catalog.
# http://127.0.0.1:5000/api/v1/resources/books/all
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

# Filtering ID
# 127.0.0.1:5000/api/v1/resources/books?id=0
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if ID came with the URL
    # If it was provided, save in a variable
    # If it was not, display an error
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: There is not ID calling the method"

    results = []

    # Reading all books and adding only with the ID
    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)

app.run()