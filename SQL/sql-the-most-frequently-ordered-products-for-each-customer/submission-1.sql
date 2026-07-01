-- Write your query below

SELECT  customer_id, product_id, product_name
FROM    (
    SELECT  o.customer_id, o.product_id, p.product_name,
            DENSE_RANK() OVER (PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) as rnk
    FROM    orders o JOIN products p USING (product_id)
            JOIN customers c USING (customer_id)
    GROUP BY o.customer_id, o.product_id, p.product_name
)
WHERE rnk = 1
