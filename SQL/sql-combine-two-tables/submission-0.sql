-- Write your query below
SELECT 
    first_name, last_name, city, state
FROM
    person p LEFT JOIN address a USING (person_id)
