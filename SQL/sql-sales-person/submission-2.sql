-- Write your query below
SELECT sp.name
FROM sales_person sp
WHERE NOT EXISTS (
    SELECT o.sales_id
    FROM orders o
    JOIN company c ON o.com_id = c.com_id
    WHERE c.name = 'CRIMSON'
      AND o.sales_id = sp.sales_id
);
