-- Write your query below
SELECT
    sale_date, 
    SUM(CASE 
        WHEN fruit = 'apples' THEN sold_num
        WHEN fruit = 'oranges' THEN -sold_num
    END) as diff
FROM    sales
GROUP BY sale_date
ORDER BY sale_date
