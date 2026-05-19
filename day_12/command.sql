-- Create a new database
CREATE DATABASE mydatabase;

-- Use a database
USE mydatabase;

-- Delete a database
DROP DATABASE mydatabase;

-- Create a table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- Integer with auto-increment
    name VARCHAR(100) NOT NULL,               -- Variable-length string
    email VARCHAR(100) UNIQUE,                -- Email must be unique
    password CHAR(64),                        -- Fixed-length string (e.g., hashed password)
    age TINYINT,                              -- Small integer (0–255)
    dob DATE,                                 -- Date only (YYYY-MM-DD)
    gender ENUM('Male', 'Female', 'Other'),   -- One value from predefined options
    is_active BOOLEAN DEFAULT TRUE,           -- True or false flag
    bio TEXT,                                 -- Long text (for user bio/about)
    signup_time DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date & time of signup
    profile_pic BLOB                          -- Binary data (e.g., image)
);


-- View table structure
DESCRIBE users;

-- Delete a table
DROP TABLE users;

INSERT INTO users (name, email)
VALUES ('Antick', 'antick@example.com');

-- Select all rows
SELECT * FROM users;

-- Select specific columns
SELECT name, email FROM users;

-- With conditions
SELECT * FROM users WHERE id = 1;
SELECT * FROM users WHERE name = 'Antick';

-- Update user's name and email
UPDATE users
SET name = 'Anshu Updated', email = 'anshu_updated@example.com'
WHERE id = 1;

-- Delete a specific user
DELETE FROM users WHERE id = 1;

-- Delete all users (⚠️ dangerous!)
DELETE FROM users;

-- WHERE with conditions
SELECT * FROM users WHERE name LIKE 'A%';  -- names starting with 'A'

-- ORDER BY
SELECT * FROM users ORDER BY name ASC;

-- LIMIT
SELECT * FROM users LIMIT 5;

-- Add a column
ALTER TABLE users ADD age INT;

-- Drop a column
ALTER TABLE users DROP COLUMN age;

-- Change column type
ALTER TABLE users MODIFY email VARCHAR(150);

