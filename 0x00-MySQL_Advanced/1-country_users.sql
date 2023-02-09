--creates a table users
--field includes name, email id, country

CREATE TABLE IF NOT EXISTS user(
  id int NOT NULL AUTO_INCREMENT,
  email varchar(255) NOT NULL UNIQUE,
  name varchar(255),
  country enum('US', 'CO', 'TN') DEFAULT 'US',
  PRIMARY KEY(id)
);
