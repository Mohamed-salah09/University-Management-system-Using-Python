from .Data_base import get_connection


def add_department(department):
    connection = get_connection()

    connection.execute("""
        INSERT INTO Departments
        (department_id, department_name, description)
        VALUES (?, ?, ?)
    """, (
        department.department_id,
        department.department_name,
        department.description
    ))

    connection.commit()
    connection.close()


def delete_department(department_id):
    connection = get_connection()

    connection.execute(
        "DELETE FROM Departments WHERE department_id = ?",
        (department_id,)
    )

    connection.commit()
    connection.close()