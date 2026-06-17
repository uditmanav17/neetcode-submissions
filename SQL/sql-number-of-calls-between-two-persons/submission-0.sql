-- Write your query below

SELECT
    person1, person2,
    Count(*) AS call_count,
    SUM(duration) AS total_duration
FROM (
    SELECT
        CASE
            WHEN from_id < to_id THEN from_id
            WHEN from_id > to_id THEN to_id
        END AS person1,
        CASE
            WHEN from_id < to_id THEN to_id
            WHEN from_id > to_id THEN from_id
        END AS person2,
        duration
    FROM calls
) tmp
GROUP BY person1, person2

