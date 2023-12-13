-- creates the database hbtn_0d_usa and the table states
-- if exists do nothing
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
		id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
		name VARCHAR(256)
		);
