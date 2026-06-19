-- Write your query below

SELECT customer_number
FROM (
    SELECT customer_number, COUNT(*) AS cnt,
           RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
    FROM orders
    GROUP BY customer_number
) t
WHERE rnk = 1
