#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    return jsonify([user for user in users.values()])

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_users(username):
    if username not in users:
        return "User not found", 404

    return jsonify(users[username]) 

@app.route("/add_user", methods = ['POST'])
def add_user():
    user_data = request.get_json()
    username = user_data["name"].lower()
    users[username] = user_data 

    return jsonify(user_data), 201

if __name__ == "__main__":
    app.run()





