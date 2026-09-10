from .Data_base import get_connection
def add_admin(admin):
    connection = get_connection()

    connection.execute("""
        INSERT INTO Admins
        (admin_id, user_id)
        VALUES (?, ?)
    """, (
        admin.admin_id,
        admin.user_id
    ))

    connection.commit()
    connection.close()


def delete_admin(admin_id):
    connection = get_connection()

    connection.execute(
        "DELETE FROM Admins WHERE admin_id = ?",
        (admin_id,)
    )

    connection.commit()
    connection.close()