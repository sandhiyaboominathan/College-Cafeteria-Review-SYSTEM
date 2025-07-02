-- Step 1: Create the database
CREATE DATABASE IF NOT EXISTS cafeteria;
USE cafeteria;

-- Step 2: Create 'users' table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Step 3: Create 'reviews' table
CREATE TABLE IF NOT EXISTS reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    food_item VARCHAR(100) NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    date DATE,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

ALTER TABLE reviews MODIFY rating FLOAT CHECK (rating >= 1.0 AND rating <= 5.0);
