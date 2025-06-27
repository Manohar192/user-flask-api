from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User created", "user": data}), 201

@app.route('/users/<int:index>', methods=['PUT'])
def update_user(index):
    if index < 0 or index >= len(users):
        return jsonify({"error": "User not found"}), 404
    users[index] = request.json
    return jsonify({"message": "User updated", "user": users[index]}), 200

@app.route('/users/<int:index>', methods=['DELETE'])
def delete_user(index):
    if index < 0 or index >= len(users):
        return jsonify({"error": "User not found"}), 404
    deleted = users.pop(index)
    return jsonify({"message": "User deleted", "user": deleted}), 200

if __name__ == '__main__':
    app.run(debug=True)
