-- Run this SQL in your MySQL environment
CREATE DATABASE blog_db;

USE blog_db;

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) UNIQUE NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE tags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE post_tags (
    post_id INT,
    tag_id INT,
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

USE blog_db;

-- Insert Posts
INSERT INTO posts (title, content) VALUES 
('Python Basics', 'This post introduces Python basics including syntax and variables.'),
('MySQL for Beginners', 'An introduction to relational databases and MySQL queries.'),
('Web Development with Flask', 'Learn how to build web apps using Flask and Python.'),
('Data Analysis in Pandas', 'Explore how to clean and analyze data using Pandas.'),
('Machine Learning 101', 'Basic concepts and workflows in machine learning.'),
('Docker for Developers', 'A beginner guide to using Docker in development.'),
('Deploying Apps with Heroku', 'Steps to deploy Python apps using Heroku.'),
('Understanding REST APIs', 'Designing and consuming REST APIs.'),
('Advanced SQL Tricks', 'Using advanced SQL for data manipulation and queries.'),
('Building a Portfolio Website', 'Guide to create your own portfolio using HTML, CSS, and JS.');

-- Insert Tags
INSERT INTO tags (name) VALUES 
('Python'), ('MySQL'), ('Flask'), ('Pandas'), 
('Machine Learning'), ('Docker'), ('Heroku'), 
('REST'), ('SQL'), ('WebDev');

-- Manually link tags to posts in post_tags
-- Format: (post_id, tag_id)

INSERT INTO post_tags (post_id, tag_id) VALUES
(1, 1),  -- Python Basics -> Python
(2, 2),  -- MySQL for Beginners -> MySQL
(3, 1), (3, 3), -- Flask & Python
(4, 1), (4, 4), -- Pandas & Python
(5, 1), (5, 5), -- ML & Python
(6, 6), -- Docker
(7, 1), (7, 7), -- Heroku & Python
(8, 8), -- REST
(9, 2), (9, 9), -- SQL
(10, 10); -- WebDev
