import os
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="banco-api",
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )
    return conn

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM users ORDER BY id;')
    users_data = cur.fetchall()
    cur.close()
    conn.close()

    users = [{"id": row[0], "name": row[1]} for row in users_data]
    return jsonify(users)


@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    name = new_user['name']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name) VALUES (%s) RETURNING id', (name,))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "success", "id": new_id, "message": f"Usuário '{name}' adicionado."}), 201