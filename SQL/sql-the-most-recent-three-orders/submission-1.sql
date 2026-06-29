-- Write your query below

SELECT  customer_name, customer_id, order_id, order_date
FROM    (
    SELECT  c.name as customer_name, c.customer_id, o.order_id, o.order_date,
            DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY o.order_date DESC) as rnk
    FROM    orders o JOIN customers c USING (customer_id)
)
WHERE rnk <= 3
ORDER BY customer_name, customer_id, order_date DESC
