SELECT c.customer_id, c.customer_name
FROM customers c
WHERE EXISTS (SELECT 1 FROM orders WHERE customer_id = c.customer_id AND product_name = 'A')
  AND EXISTS (SELECT 1 FROM orders WHERE customer_id = c.customer_id AND product_name = 'B')
  AND NOT EXISTS (SELECT 1 FROM orders WHERE customer_id = c.customer_id AND product_name = 'C')
ORDER BY c.customer_name;
