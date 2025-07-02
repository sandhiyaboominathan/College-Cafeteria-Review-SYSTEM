from db.db_config import get_connection
from models.user import User

class UserDAO:
    def register(self, user):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Check if username already exists
            cursor.execute("SELECT * FROM users WHERE username = %s", (user.username,))
            if cursor.fetchone():
                print("⚠️ Username already exists. Please login instead.")
                return False

            # Insert new user
            query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (user.username, user.email, user.password))
            conn.commit()

            print("✅ Registered successfully!")
            return True

        except Exception as e:
            print("❌ Registration failed:", e)
            return False

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def login(self, username, password):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()

            if user:
                print(f"✅ Login successful! Welcome, {username}")
                return True
            else:
                print("❌ Invalid username or password.")
                return False

        except Exception as e:
            print("❌ Login failed:", e)
            return False

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
