from flask import Flask, request, jsonify
from database import connect_db, create_table

app = Flask(__name__)

create_table()

# Home Route
@app.route("/")
def home():
    return "Student Management Backend Running 🚀"

#1.create student route(post)
@app.route("/add_student", methods=["POST"])
def add_student():
    data = request.json
    
    name = data["name"]
    age = data["age"]
    course = data["course"]

    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", 
                   (name, age, course))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Student added successfully"})

#2.read all students routes(get)
@app.route("/students", methods=["GET"])
def get_students():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    
    conn.close()

    return jsonify(students)

#3.update student route(put)
@app.route("/update_student/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.json
    
    name = data["name"]
    age = data["age"]
    course = data["course"]

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?",
                   (name, age, course, id))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Student updated successfully"})
#4.delete student route (delete)
@app.route("/delete_student/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Student deleted successfully"})
if __name__ == "__main__":
    app.run(debug=True)