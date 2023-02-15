-- creates the table unique_id
-- with values id and name
-- id should have default value 1 and must be unique
CREATE TABLE IF NOT EXISTS unique_iD (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
