CREATE TABLE reviews
(
    id INT NOT NULL
    AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR
    (100),
    movie_id VARCHAR
    (100),
    review VARCHAR
    (100),  
    rating INT
    );
