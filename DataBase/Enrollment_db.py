from .Data_base import get_connection
def add_enrollment(enrollment):
    connection = get_connection()

    connection.execute("""
        INSERT INTO Enrollments
        (enrollment_id, student_id, course_id, semester, grade, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        enrollment.enrollment_id,
        enrollment.student.student_id,
        enrollment.course.course_id,
        enrollment.semester,
        enrollment.grade,
        enrollment.status.value
    ))

    connection.commit()
    connection.close()


def delete_enrollment(enrollment_id):
    connection = get_connection()

    connection.execute(
        "DELETE FROM Enrollments WHERE enrollment_id = ?",
        (enrollment_id,)
    )

    connection.commit()
    connection.close()


def update_status(enrollment_id, status):
    connection = get_connection()

    connection.execute("""
        UPDATE Enrollments
        SET status = ?
        WHERE enrollment_id = ?
    """, (
        status.value,
        enrollment_id
    ))

    connection.commit()
    connection.close()


def update_grade(enrollment_id, grade):
    connection = get_connection()

    connection.execute("""
        UPDATE Enrollments
        SET grade = ?
        WHERE enrollment_id = ?
    """, (
        grade,
        enrollment_id
    ))

    connection.commit()
    connection.close()