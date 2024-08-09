from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/submit', methods=['POST'])
def submit():
    # checks if type is json
    if request.content_type != 'aplication/json':
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.json
    movie_title = data.get('title')
    return jsonify({"message": f"Received title: {movie_title}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)