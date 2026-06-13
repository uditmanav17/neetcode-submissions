-- Write your query below
SELECT  sp.name
FROM    sales_person sp
WHERE   sp.sales_id NOT IN (
    SELECT  o.sales_id
    FROM    orders o
    WHERE   o.com_id IN (
        SELECT  c.com_id 
        FROM    company c
        WHERE   c.name = 'CRIMSON'
    )

)
