-- Write your query below

SELECT * 
FROM (
    SELECT product_id, 'store1' AS store, store1 as price FROM products
    UNION ALL
    SELECT product_id, 'store2' AS store, store2 as price FROM products
    UNION ALL
    SELECT product_id, 'store3' AS store, store3 as price FROM products
) t
WHERE price is NOT NULL
