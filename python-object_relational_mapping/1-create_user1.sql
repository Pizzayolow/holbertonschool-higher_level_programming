-- Write a script that creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'pizza'@'localhost' IDENTIFIED BY 'cheese';
GRANT ALL PRIVILEGES ON * . * TO 'pizza'@'localhost';
FLUSH PRIVILEGES;