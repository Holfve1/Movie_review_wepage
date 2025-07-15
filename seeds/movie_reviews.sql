DROP TABLE IF EXISTS movies;
DROP SEQUENCE IF EXISTS movies_id_seq;

CREATE SEQUENCE IF NOT EXISTS movies_id_seq;
CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INT,
    genre VARCHAR(255)
);


INSERT INTO movies (title, release_year, genre) VALUES ('Inception', 2010,'Sci-fi');
INSERT INTO movies (title, release_year, genre) VALUES ('The Dark Knight', 2008, 'Action');
INSERT INTO movies (title, release_year, genre) VALUES ('Pulp Fiction', 1994,'Drama');
INSERT INTO movies (title, release_year, genre) VALUES ('The Shawshank Redemption', 1994, 'Drama');
INSERT INTO movies (title, release_year, genre) VALUES ('Forrest Gump', 1994, 'Drama');
INSERT INTO movies (title, release_year, genre) VALUES ('Fight Club', 1999, 'Drama');
INSERT INTO movies (title, release_year, genre) VALUES ('The Matrix', 1999, 'Sci-fi');
INSERT INTO movies (title, release_year, genre) VALUES ('The Lord of the Rings: The Fellowship of the Ring', 2001, 'Fantasy');
INSERT INTO movies (title, release_year, genre) VALUES ('Spirited Away', 2001, 'Animation');
INSERT INTO movies (title, release_year, genre) VALUES ('The Lord of the Rings: The Return of the King', 2003, 'Fantasy');


