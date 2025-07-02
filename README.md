# 🍽️ College Cafeteria Review System

A **console-based Python project** that allows students to give reviews and ratings for cafeteria food items. This system helps the college administration collect structured feedback and analyze trends to improve food quality and service.

---

## 📌 Features

- 📝 Students can submit text reviews and rate food items (1–5 stars)
- 📊 View average ratings for each dish
- 🧾 Display all reviews submitted for a food item
- 🗃️ Data stored using **MySQL** or **CSV files**
- 🔐 Admin functionality (optional): View reports, identify poor-performing items

---

## 🛠️ Tech Stack

| Tech | Purpose |
|------|---------|
| **Python** | Main programming language |
| **MySQL / CSV** | Data storage backend |
| **OOP (Classes)** | Structure: User, FoodItem, Review, Admin, etc. |
| **DAO Pattern** | Data Access Layer (if implemented) |

---

## 📂 Project Structure

COLLEGE_CAFF_REV_SYS/
│
├── main.py # Main program (menu-based UI)
├── food_item.py # Class definition for food items
├── review.py # Review class
├── database.py # MySQL or CSV handling
├── utils.py # Helper functions (e.g., validation)
├── requirements.txt # Required Python packages (if any)
└── README.md

---

## 🚀 How to Run

### ✅ If using Python + CSV:
```bash
python main.py
====== Welcome to College Cafeteria Review System ======

1. Add Review
2. View Average Rating
3. View All Reviews
4. Exit

Enter your choice: 1

Enter food item name: Veg Biryani
Rate (1-5): 4
Write your review: Tasty but a bit spicy!

✅ Thank you for your feedback!
