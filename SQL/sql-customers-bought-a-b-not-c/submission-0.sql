-- Write your query below
WITH ab_product as (
    (
        SELECT customer_id from orders
        WHERE product_name = 'A'
    )
    INTERSECT
    (
        SELECT customer_id from orders
        WHERE product_name = 'B'
    )
)

SELECT
    c.customer_id AS customer_id,
    c.customer_name AS customer_name
FROM customers c JOIN ab_product abp USING (customer_id)
WHERE c.customer_id NOT IN (SELECT customer_id from orders WHERE product_name = 'C')
ORDER BY c.customer_name
