from .Data_base import get_connection
def add_course(course):
    connection = get_connection()

    connection.execute("""
        INSERT INTO Courses
        (course_id, course_name, course_code, credits, description, department_id, professor_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        course.course_id,
        course.course_name,
        course.course_code,
        course.credits,
        course.description,
        course.department.department_id,
        course.professor.professor_id if course.professor else None
    ))

    connection.commit()
    connection.close()


def delete_course(course_id):
    connection = get_connection()

    connection.execute(
        "DELETE FROM Courses WHERE course_id = ?",
        (course_id,)
    )

    connection.commit()
    connection.close()


def update_professor(course_id, professor_id):
    connection = get_connection()

    connection.execute("""
        UPDATE Courses
        SET professor_id = ?
        WHERE course_id = ?
    """, (
        professor_id,
        course_id
    ))

    connection.commit()
    connection.close()


def remove_professor(course_id):
    connection = get_connection()

    connection.execute("""
        UPDATE Courses
        SET professor_id = NULL
        WHERE course_id = ?
    """, (course_id,))

    connection.commit()
    connection.close()