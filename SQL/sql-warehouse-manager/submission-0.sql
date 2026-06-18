-- Write your query below

SELECT  wh.name as warehouse_name, 
        SUM(wh.units * p.width * p.length * p.height) as volume
FROM    warehouse wh JOIN products p USING (product_id)
GROUP BY wh.name
