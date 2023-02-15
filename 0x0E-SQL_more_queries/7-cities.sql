-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.cities (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
