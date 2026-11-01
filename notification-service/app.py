from flask import Flask, jsonify, request

app = Flask(__name__)
notifications = []


@app.route('/health')
def health():
    return jsonify(status='healthy', service='notification-service')


@app.route('/notifications', methods=['GET'])
def list_notifications():
    return jsonify(notifications)


@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.get_json() or {}
    note = {'id': len(notifications) + 1, 'message': data.get('message'), 'user_id': data.get('user_id')}
    notifications.append(note)
    return jsonify(note), 201
