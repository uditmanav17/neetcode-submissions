-- Write your query below

SELECT  DISTINCT p.product_name, p.product_id, o.order_id, o.order_date
FROM    orders o JOIN products p USING (product_id)
        JOIN (
            SELECT  product_id, MAX(order_date) AS latest_order
            FROM    orders
            GROUP BY product_id
        ) t ON o.order_date = t.latest_order
ORDER BY product_name, product_id, order_id
