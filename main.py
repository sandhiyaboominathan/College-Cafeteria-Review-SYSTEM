from models.user import User
from models.review import Review
from dao.user_dao import UserDAO
from dao.review_dao import ReviewDAO
from db.db_config import get_connection
import getpass

class CafeteriaSystem:
    def __init__(self):
        self.user_dao = UserDAO()
        self.review_dao = ReviewDAO()
        self.current_user_id = None
        self.current_username = None

    def start(self):
        while True:
            print("\n🍽️ College Cafeteria Review System")
            print("1. 📝 Register")
            print("2. 🔐 Login")
            print("3. 🚪 Exit")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                if self.login_user():
                    self.main_menu()
            elif choice == "3":
                print("👋 Exiting. Have a great day!")
                break
            else:
                print("⚠️ Invalid choice.")

    def register_user(self):
        print("\n📝 Register New User")
        username = input("Username: ")
        email = input("Email: ")
        password = getpass.getpass("Password (hidden): ")

        user = User(username, email, password)
        self.user_dao.register(user)

    def login_user(self):
        print("\n🔐 Login")
        username = input("Username: ")
        password = getpass.getpass("Password (hidden): ")

        if self.user_dao.login(username, password):
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                result = cursor.fetchone()
                if result:
                    self.current_user_id = result[0]
                    self.current_username = username
                    return True
                else:
                    print("❌ Unable to fetch user ID.")
                    return False
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
        else:
            print("\n🚨 Wrong password or username. Please try again.\n")
            return False

    def main_menu(self):
        while True:
            print(f"\n🎉 Welcome, {self.current_username}!")
            print("1. ➕ Add Review")
            print("2. 📄 View All Reviews")
            print("3. 📊 Check Average Rating")
            print("4. 🔓 Logout")

            choice = input("Enter your choice (1–4): ")

            if choice == "1":
                self.add_review()
            elif choice == "2":
                self.view_reviews()
            elif choice == "3":
                self.check_avg_rating()
            elif choice == "4":
                print(f"👋 Logged out, {self.current_username}")
                self.current_user_id = None
                self.current_username = None
                break
            else:
                print("⚠️ Invalid choice.")

    def add_review(self):
        print("\n➕ Add a New Review")
        food_item = input("Enter food item: ")
        try:
            rating = float(input("Enter rating (1.0–5.0): "))
            if not 1.0 <= rating <= 5.0:
                print("⚠️ Rating must be between 1.0 and 5.0.")
                return
        except ValueError:
            print("⚠️ Please enter a valid number for rating.")
            return

        comment = input("Enter comment: ")
        date = input("Enter date (YYYY-MM-DD): ")

        review = Review(food_item, rating, comment, date, self.current_user_id)
        self.review_dao.add_review(review)

    def view_reviews(self):
        print("\n📄 All Reviews")
        reviews = self.review_dao.get_all_reviews()
        if reviews:
            for r in reviews:
                print(r)
        else:
            print("No reviews yet.")

    def check_avg_rating(self):
        food_item = input("\nEnter food item name to check rating: ")
        avg = self.review_dao.get_average_rating(food_item)
        if avg:
            print(f"⭐ Average Rating for '{food_item}': {round(avg, 2)}")
        else:
            print(f"No reviews found for '{food_item}'.")

if __name__ == "__main__":
    app = CafeteriaSystem()
    app.start()
