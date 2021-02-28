from flask import flask, jsonify

# Create an app, being sure to pass __name__
app = Flask(__name__)


movies = [{'Genre': 'Romance', 'Duration': '74', 'Budget': '25000000'}, {'Genre': 'Horror', 'Duration': '85', 'Budget': '60000'}, {'Genre': 'Action, Adventure, Comedy', 'Duration': '68', 'Budget': '5000000'}]

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)

if __name__ == "__main__":
    app.run(debug=True)
