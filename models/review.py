class Review:
    def __init__(self, food_item, rating, comment, date, user_id):
        self.food_item = food_item
        self.rating = rating
        self.comment = comment
        self.date = date
        self.user_id = user_id

    def __str__(self):
        return f"🍽️ Food: {self.food_item} | ⭐ Rating: {self.rating} | 💬 Comment: {self.comment} | 📅 Date: {self.date}"
