-- Write your query below
SELECT customer_id, name
FROM (
    SELECT
        o.customer_id,
        c.name,
        date_trunc('month', order_date) AS month_,
        SUM(o.quantity * p.price) AS spent
    FROM orders o
    JOIN customers c USING (customer_id)
    JOIN product p USING (product_id)
    WHERE order_date >= DATE '2020-06-01'
      AND order_date < DATE '2020-08-01'
    GROUP BY o.customer_id, c.name, month_
) t
WHERE spent >= 100
GROUP BY customer_id, name
HAVING COUNT(*) = 2
