CREATE DATABASE test;
DROP DATABASE test;
CREATE DATABASE record_company;
USE record_company;
CREATE TABLE test(
	test_col INT
);
ALTER TABLE test
ADD another_col VARCHAR(20);

DROP TABLE test;

CREATE TABLE bands(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE albums(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
    release_year INT,
    band_id INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(band_id) REFERENCES bands(id)
);

INSERT INTO bands(name)
VALUES ('DurannameDuran'), ('ABBA'), ('Eagles'), ('Kaveret'), ('MoneSkin');

SELECT * FROM bands LIMIT 2;
SELECT name FROM bands;
SELECT name FROM bands LIMIT 3;

SELECT id AS 'bandID', name AS 'bandName' FROM bands;
SELECT * FROM bands ORDER BY name;
SELECT * FROM bands ORDER BY name DESC;

INSERT INTO albums (name, release_year, band_id)
VALUES ('GIMMIE!', 1979, 2), ('A View To A Kill', 1982, 1), ('MY TEST', NULL, 3);

SELECT * FROM albums;
SELECT DISTINCT name FROM albums;

UPDATE albums
SET release_year = 1976
WHERE id = 1;

UPDATE albums
SET release_year = 1972
WHERE id > 1;

SELECT * FROM albums
WHERE release_year < 1976;

SELECT * FROM albums
WHERE name LIKE '%!%' OR id = 4;

SELECT * FROM albums
WHERE name LIKE '%!%' AND id = 4;

SELECT * FROM albums
WHERE release_year BETWEEN 1971 AND 1974;

SELECT * FROM albums
WHERE release_year IS NULL;

DELETE FROM albums WHERE name = 'MY TEST';
DELETE FROM albums WHERE id = 7;

SELECT * FROM  bands
JOIN albums ON bands.id = albums.band_id;

SELECT * FROM albums
JOIN bands ON bands.id = albums.band_id;

SELECT * FROM  bands
LEFT JOIN albums ON bands.id = albums.band_id;

SELECT * FROM  albums
RIGHT JOIN bands ON bands.id = albums.band_id;

SELECT AVG(release_year) FROM albums;
SELECT MAX(release_year) FROM albums;
SELECT MIN(release_year) FROM albums;
SELECT SUM(release_year) FROM albums;
SELECT COUNT(release_year) FROM albums;

SELECT band_id, COUNT(band_id) FROM albums
GROUP BY band_id;

# BELOW, we return a table with the names of the bands, along with the number of albums each band released.
SELECT b.name AS band_name, COUNT(a.id) AS num_albums # Here, we give our columns meaningful names.
FROM bands AS b
LEFT JOIN albums AS a ON b.id = a.band_id # We're doing LEFT JOIN, so all bands, even those without albums, appear in the query.
GROUP BY b.id;  # Here we count.

# BELOW, we return a table with the names of the bands, along with the number of albums each band released. BUT we filter out those who didn't released albums.
SELECT b.name AS band_name, COUNT(a.id) AS num_albums # Here, we give our columns meaningful names.
FROM bands AS b
LEFT JOIN albums AS a ON b.id = a.band_id # We're doing LEFT JOIN, so all bands, even those without albums, appear in the query.
GROUP BY b.id  # Here we count.
HAVING num_albums > 0;  # We can't use WHERE after merging. we can use HAVING instead.