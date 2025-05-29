from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)

# mă asigur că fișierul există
if not os.path.exists(os.path.join(app.root_path, 'static')):
    os.makedirs(os.path.join(app.root_path, 'static'))

DATA_FILE = os.path.join(app.root_path, 'students.json')

# load la studenții din json
def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

# salvăm datele
def save_students(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# generare id
def get_next_id(data):
    max_id = 0
    for student in data.values():
        if isinstance(student.get("id"), int):
            max_id = max(max_id, student["id"])
    return max_id + 1

# ruta pentru pagina principala
@app.route('/')
def home():
    return render_template('studenti.html')

# rută pentru get
@app.route('/api/students', methods=['GET'])
def get_students():
    students = load_students()
    return jsonify(students)

# rută pentru post
@app.route('/api/students', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({"error": "Name is required"}), 400

    students = load_students()
    if name in students:
        return jsonify({"error": "Student already exists"}), 400

    students[name] = {"id": get_next_id(students)}
    save_students(students)
    return jsonify({"message": f"Student '{name}' added."}), 201

# rută pentru update
@app.route('/api/students/<old_name>', methods=['PATCH'])
def update_student(old_name):
    data = request.get_json()
    new_name = data.get('new_name')

    students = load_students()
    if old_name not in students:
        return jsonify({"error": "Student not found"}), 404

    if new_name in students:
        return jsonify({"error": "New name already taken"}), 400

    students[new_name] = students.pop(old_name)
    save_students(students)
    return jsonify({"message": f"Student name updated from '{old_name}' to '{new_name}'."})

# rută pentru ștergere
@app.route('/api/students/<name>', methods=['DELETE'])
def delete_student(name):
    students = load_students()
    if name not in students:
        return jsonify({"error": "Student not found"}), 404

    del students[name]
    save_students(students)
    return jsonify({"message": f"Student '{name}' deleted."})

if __name__ == '__main__':
    app.run(debug=True)