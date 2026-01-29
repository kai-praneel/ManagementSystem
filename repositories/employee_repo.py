from db_pool.connection import connect, cursor

class EmployeeDB:

    def user_exists_by_name(self, name):
        cursor.execute(
            "SELECT 1 FROM user WHERE user_name = %s",
            (name,)
        )
        return cursor.fetchone() is not None

    def user_exists_by_email(self, email):
        cursor.execute(
            "SELECT 1 FROM user WHERE user_email = %s",
            (email,)
        )
        return cursor.fetchone() is not None

    def createEMP(self, name, email, password):
        query = """
            INSERT INTO user (user_name, user_email, password, is_employee)
            VALUES (%s, %s, %s, 1)
        """
        cursor.execute(query, (name, email, password))
        connect.commit()

    def searchEMP(self, email):
        cursor.execute(
            "SELECT password FROM user WHERE user_email = %s",
            (email,)
        )
        row = cursor.fetchone()
        return row["password"] if row else None
