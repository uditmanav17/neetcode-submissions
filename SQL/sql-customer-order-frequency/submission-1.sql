-- Write your query below
SELECT
    o.customer_id,
    c.name
FROM orders o
JOIN customers c USING (customer_id)
JOIN product p USING (product_id)
WHERE order_date >= DATE '2020-06-01'
  AND order_date < DATE '2020-08-01'
GROUP BY o.customer_id, c.name
HAVING
    SUM(
        CASE
            WHEN EXTRACT(MONTH FROM order_date) = 6
            THEN o.quantity * p.price
            ELSE 0
        END
    ) >= 100
    AND
    SUM(
        CASE
            WHEN EXTRACT(MONTH FROM order_date) = 7
            THEN o.quantity * p.price
            ELSE 0
        END
    ) >= 100