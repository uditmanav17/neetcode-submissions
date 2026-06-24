-- Write your query below
SELECT seat_id
FROM    (
    SELECT  seat_id, free, 
            LEAD(free, 1) OVER () AS prev,
            LAG(free, 1) OVER () AS nxt
    FROM cinema
) t
WHERE (free = prev OR free = nxt) AND free = 1
ORDER BY seat_id
