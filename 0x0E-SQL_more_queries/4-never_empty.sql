-- creates the table id_not_null on your MySQL server.
-- if exists do nothing
CREATE TABLE IF NOT EXISTS id_not_null (
		id INT DEFAULT 1,
		name VARCHAR(256)
		);
