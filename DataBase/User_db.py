from .Data_base import get_connection
from User import User
connection=get_connection()
def add_user(user):
    

    connection.execute("""
        INSERT INTO Users
        (user_id, name, date_birth, email, password)
        VALUES (?, ?, ?, ?, ?)
    """, (
        user.user_id,
        user.name,
        user.date_birth,
        user.email,
        user.password
    ))

    connection.commit()
    connection.close()


def delete_user(user_id):
    

    connection.execute(
        "DELETE FROM Users WHERE user_id = ?",
        (user_id,)
    )

    connection.commit()
    connection.close()


def get_all_users():
    

    cursor = connection.execute("SELECT * FROM Users")
    rows = cursor.fetchall()

    connection.close()

    users = []

    for row in rows:
        users.append(
            User(
                row[0],  
                row[1],  
                row[2],  
                row[3],  
                row[4]   
            )
        )

    return users