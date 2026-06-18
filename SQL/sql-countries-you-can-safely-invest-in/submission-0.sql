-- Write your query below

-- SELECT  c.name as country
-- FROM    country c 

SELECT  country
FROM    (
    SELECT  cn.name as country,
            c.duration
    FROM    person p JOIN (
        SELECT caller_id, duration from calls
        UNION ALL
        SELECT callee_id, duration from calls
    ) c ON c.caller_id = p.id 
        JOIN country cn 
        ON cn.country_code = SUBSTRING(p.phone_number, 0, 4)
) ca
GROUP BY country
HAVING AVG(duration) > (SELECT AVG(duration) FROM calls)
