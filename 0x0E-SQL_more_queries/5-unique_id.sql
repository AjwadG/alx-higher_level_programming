-- creates the table unique_id on your MySQL server.
-- if exists do nothing
CREATE TABLE IF NOT EXISTS unique_id (
		id INT DEFAULT 1 UNIQUE,
		name VARCHAR(256)
		);
