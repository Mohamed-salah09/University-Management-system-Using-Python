class User:

    def __init__(self, user_id, name, date_birth, email, password):
        self.user_id = user_id
        self.name = name
        self.date_birth = date_birth
        self.email = email
        self.password = password

    def login(self):
        from DataBase.Data_base import get_connection

        connection = get_connection()

        cursor = connection.execute("""
            SELECT user_id, name, date_birth, email, password
            FROM Users
            WHERE email = ? AND password = ?
        """, (self.email, self.password))

        user = cursor.fetchone()

        connection.close()

        if user:
            print("Login successful.")
            return True

        print("Invalid email or password.")
        return False

    def logout(self):
        print("Logout successful.")

    def view_profile(self):
      return {
        "user_id": self.user_id,
        "name": self.name,
        "date_birth": self.date_birth,
        "email": self.email
    }