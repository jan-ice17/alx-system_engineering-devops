#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/home_page/home', methods=['GET'])
def home():
    response = {
        "name": "Webserver",
        "id": "22deftrshju3456"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=8000)


