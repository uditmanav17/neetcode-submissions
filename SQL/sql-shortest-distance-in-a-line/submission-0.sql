-- Write your query below

SELECT MIN(ABS(x - nxt)) AS shortest
FROM(
    SELECT  x, LAG(x, 1) OVER (ORDER BY x) AS nxt
    FROM    point
)
