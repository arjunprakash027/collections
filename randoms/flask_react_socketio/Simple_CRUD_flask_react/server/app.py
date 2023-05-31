from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/greetings', methods=['GET'])
def greetings():
    print("client tried to ping")
    return jsonify({'message': 'Hello from server!'})


if __name__ == '__main__':
    app.run(debug=True)