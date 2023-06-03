from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'sect'
jwt = JWTManager(app)

@app.route('/api/login',methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username == 'admin' and password == 'admin':
        access_token = create_access_token(identity=username)
        return jsonify({"token":access_token}), 200
    

    return jsonify({"error":"Invalid username or password"}), 401


@app.route('/api/protected',methods=['GET'])
@jwt_required()
def protected():
    try:
        return jsonify({"message":"access granted"}), 200
    except:
        return jsonify({"error":"access denied"}), 401

if __name__ == '__main__':
    app.run(debug=True)


