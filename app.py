from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # checks if type is json
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.json
    movie_title = data.get('title')
    return jsonify({"message": f"Received title: {movie_title}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)