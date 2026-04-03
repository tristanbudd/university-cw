-- Question #1
\c movie_rental (To connect to the database)
\df (To list all of the functions available)

-- Question #2
SELECT
    p_movie_count AS "Movies in Stock"
FROM
    movie_in_stock(25, 1);

SELECT
    p_movie_count AS "Movies in Stock"
FROM
    movie_in_stock((SELECT movie_id FROM movie WHERE movie.title ILIKE 'Angels Life'), 1);

-- Question #3
CREATE OR REPLACE PROCEDURE sp_add_new_actor(first_name VARCHAR(30), last_name VARCHAR(30))
    LANGUAGE SQL
AS $$
    INSERT INTO actor(first_name, last_name) VALUES (first_name, last_name);
$$;

CALL sp_add_new_actor('Val', 'Adamescu');

-- Question #4
ALTER TABLE country
    ADD COLUMN country_code VARCHAR(2);

-- Question #5
ALTER TABLE country
    ALTER COLUMN country_code TYPE CHAR(2),
    ADD CONSTRAINT country_code UNIQUE (country_code);

-- Question #6
UPDATE
    country
SET
    country_code = 'UK'
WHERE
    country ILIKE 'United Kingdom';

SELECT
    country_id AS "Country ID",
    country AS "Country Name",
    country_Code AS "Country Code"
FROM
    country
WHERE
    country_code = 'UK';

-- Question #7
CREATE TABLE new_staff AS
SELECT
    staff_id,
    first_name,
    last_name,
    email
FROM
    staff;

-- Question #8
SELECT
    movie.title AS "Movie Title",
    (SELECT
        COUNT(*)
     FROM
        inventory
     WHERE
        inventory.movie_id = movie.movie_id) AS "Number of Copies"
FROM
    movie
ORDER BY
    "Number of Copies" DESC,
    "Movie Title" ASC;

-- Question #9
SELECT
    c.name AS "Category",
    ROUND(AVG(m.length), 2) AS "Average movie length in Minutes"
FROM
    category c
JOIN
    movie_category mc ON c.category_id = mc.category_id
JOIN
    movie m ON mc.movie_id = m.movie_id
GROUP BY
    c.name
ORDER BY
    "Average movie length in Minutes" DESC;

-- Question #10
SELECT
    c.name AS "Category",
    ROUND(AVG(m.length), 2) AS "Average movie length in Minutes"
FROM
    category c
JOIN
    movie_category mc ON c.category_id = mc.category_id
JOIN
    movie m ON mc.movie_id = m.movie_id
GROUP BY
    c.name
HAVING
    AVG(m.length) > 115.27
ORDER BY
    "Average movie length in Minutes" DESC;