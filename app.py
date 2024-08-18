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
        return jsonify({"error": "Tip sadržaja mora biti: application/json"}), 415

    data = request.json
    
    print("Received data:", data)

    movie_title = data.get('title')
    movie_resolution = data.get('resolution') or "N/A"
    movie_season = data.get('season') or "N/A"

    message = f"""Primljen naslov: {movie_title}
    Rezolucija: {movie_resolution}
    Sezona: {movie_season}"""

    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)