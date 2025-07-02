from db.db_config import get_connection
from models.review import Review

class ReviewDAO:
    def add_review(self, review):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO reviews (food_item, rating, comment, date, user_id)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (review.food_item, review.rating, review.comment, review.date, review.user_id)
            cursor.execute(query, values)
            conn.commit()

            print("✅ Review added successfully!")

        except Exception as e:
            print("❌ Failed to add review:", e)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_all_reviews(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
            SELECT r.food_item, r.rating, r.comment, r.date, u.username
            FROM reviews r
            JOIN users u ON r.user_id = u.id
            ORDER BY r.date DESC
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            reviews = []
            for row in rows:
                food_item, rating, comment, date, username = row
                reviews.append(
                    f"👤 User: {username} | 🍽️ Food: {food_item} | ⭐ Rating: {rating} | 💬 Comment: {comment} | 📅 Date: {date}"
                )

            return reviews

        except Exception as e:
            print("❌ Error fetching reviews:", e)
            return []

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_average_rating(self, food_item):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = "SELECT AVG(rating) FROM reviews WHERE food_item = %s"
            cursor.execute(query, (food_item,))
            avg = cursor.fetchone()[0]

            return avg

        except Exception as e:
            print("❌ Error calculating average rating:", e)
            return None

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
