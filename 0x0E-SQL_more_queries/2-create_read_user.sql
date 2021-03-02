-- Creates a user
-- with only read permissions
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT PRIVILEGES ON 'hbtn_0d_2' TO 'user_0d_2'@'localhost';