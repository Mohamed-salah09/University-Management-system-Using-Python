import sqlite3
def get_connection(): 
   return sqlite3.connect("DataBase/management.db")

def create_database():
   connection=get_connection() 
   with open ("DataBase/schema.sql","r") as file:
    sql_script= file.read()

    connection.executescript(sql_script)

    connection.commit()
    connection.close()

# Here i tell the compiler if i run the main then make the db 
if __name__=="__main__":
    create_database()
    

