-- creates the MySQL server user user_0d_1. with
-- all privileges and do nothig if it exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* to 'user_0d_1'@'localhost' WITH GRANT OPTION;
