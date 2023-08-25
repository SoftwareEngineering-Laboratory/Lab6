import os

import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
conn = psycopg2.connect(
    f"dbname='{DB_NAME}' user='{DB_USER}' password='{DB_PASSWORD}' host='{DB_HOST}' port={DB_PORT}")


@app.route('/add', methods=['POST'])
def add_to_db():
    name = request.json['name']
    email = request.json['email']

    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()

    return jsonify({'message': 'User added successfully'})


@app.route('/get')
def get_from_db():
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    users = []
    for row in rows:
        user = {'name': row[0], 'email': row[1]}
        users.append(user)

    return jsonify({'users': users})


if __name__ == '__main__':
    app.run(debug=True)
