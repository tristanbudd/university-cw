-- Question #1
SELECT
    actor.actor_id AS "Actor ID",
    actor.first_name AS "First Name",
    actor.last_name AS "Last Name"
FROM
    actor
WHERE
    actor.first_name ILIKE 'Scar%';

-- Question #2
SELECT
    COUNT(DISTINCT last_name) AS "Unique Last Names"
FROM
    actor;

-- Question #3
SELECT
    actor.last_name AS "Last Name"
FROM
    actor
GROUP BY
    last_name
HAVING
    COUNT(*) = 1
ORDER BY
    last_name;

-- Question #4
SELECT
    first_name AS "First Name",
    last_name AS "Last Name",
    COUNT(*) AS movie_count
FROM
    actor
JOIN
    movie_actor USING (actor_id)
GROUP BY
    actor_id, first_name, last_name
ORDER BY
    movie_count DESC
LIMIT 1;

-- Question #5
-- Listing Inventory ID's
SELECT
    i.inventory_id AS "Inventory ID"
FROM
    inventory i
JOIN
    movie m ON i.movie_id = m.movie_id
LEFT JOIN
    rental r ON i.inventory_id = r.inventory_id AND r.return_date IS NULL
WHERE
    m.title ILIKE 'Purple%'
    AND i.store_id = 1;
    AND r.rental_id IS NULL;

-- Counting Available Copies
SELECT
    COUNT(*) AS "Available Copies"
FROM
    inventory i
JOIN
    movie m ON i.movie_id = m.movie_id
LEFT JOIN
    rental r ON i.inventory_id = r.inventory_id AND r.return_date IS NULL
WHERE
    m.title ILIKE 'Purple%'
    AND i.store_id = 1
    AND r.rental_id IS NULL;

-- Question #6
SELECT
    CONCAT_WS(' ', staff.first_name, staff.last_name) AS "Staff Name",
    address.address AS "Staff Address",
    city.city AS "Staff City",
    lower(staff.email) AS "Staff Email"
FROM
    staff
JOIN
    address ON staff.address_id = address.address_id
JOIN
    city ON address.city_id = city.city_id;

-- Question #7
SELECT
    CONCAT_WS(' ', a.first_name, a.last_name) AS "Actor Name"
FROM
    actor a
JOIN
    movie_actor ma ON a.actor_id = ma.actor_id
JOIN
    movie m ON ma.movie_id = m.movie_id
WHERE
    m.title ILIKE 'Agent Tru%'
ORDER BY
    a.last_name, a.first_name;

-- Challenge Question
SELECT
    INITCAP(m.title) AS "Movie Title",
    STRING_AGG(INITCAP(CONCAT_WS(' ', a.first_name, a.last_name)), ', ' ORDER BY a.last_name, a.first_name) AS "Actors in the movie"
FROM
    movie m
JOIN
    movie_actor ma ON m.movie_id = ma.movie_id
JOIN
    actor a ON ma.actor_id = a.actor_id
WHERE
    m.title ILIKE 'Agent Tru%'
GROUP BY
    m.title;