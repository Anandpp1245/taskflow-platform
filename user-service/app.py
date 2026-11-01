from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/health')
def health():
    return jsonify(status='healthy', service='user-service')


@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(list(users.values()))


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    uid = len(users) + 1
    users[uid] = {'id': uid, 'name': data.get('name'), 'email': data.get('email')}
    return jsonify(users[uid]), 201


@app.route('/users/<int:uid>', methods=['GET'])
def get_user(uid):
    user = users.get(uid)
    if not user:
        return jsonify(error='not found'), 404
    return jsonify(user)
