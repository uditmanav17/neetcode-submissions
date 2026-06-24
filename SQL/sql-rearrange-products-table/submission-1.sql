-- Write your query below

SELECT p.product_id, v.store, 
       CASE v.store
           WHEN 'store1' THEN p.store1
           WHEN 'store2' THEN p.store2
           WHEN 'store3' THEN p.store3
       END AS price
FROM products p
CROSS JOIN (VALUES ('store1'), ('store2'), ('store3')) AS v(store)
WHERE 
    CASE v.store
        WHEN 'store1' THEN p.store1
        WHEN 'store2' THEN p.store2
        WHEN 'store3' THEN p.store3
    END IS NOT NULL;
