from .Data_base import get_connection


def add_student(student):
    connection = get_connection()

    connection.execute("""
        INSERT INTO Students
        (student_id, user_id, department_id, level)
        VALUES (?, ?, ?, ?)
    """, (
        student.student_id,
        student.user_id,
        student.department.department_id,
        student.level
    ))

    connection.commit()
    connection.close()


def delete_student(student_id):
    connection = get_connection()

    connection.execute(
        "DELETE FROM Students WHERE student_id = ?",
        (student_id,)
    )

    connection.commit()
    connection.close()