from .Data_base import get_connection


def add_professor(professor):
    connection = get_connection()

    connection.execute("""
        INSERT INTO Professors
        (professor_id, user_id, department_id, specialization)
        VALUES (?, ?, ?, ?)
    """, (
        professor.professor_id,
        professor.user_id,
        professor.department.department_id,
        professor.specialization
    ))

    connection.commit()
    connection.close()


def delete_professor(professor_id):
    connection = get_connection()

    connection.execute(
        "DELETE FROM Professors WHERE professor_id = ?",
        (professor_id,)
    )

    connection.commit()
    connection.close()