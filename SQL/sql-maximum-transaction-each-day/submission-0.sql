-- Write your query below

SELECT  transaction_id 
FROM    (
    SELECT  transaction_id, day::date, amount, 
            DENSE_RANK() OVER (partition by day::date order by amount DESC) as rnk
    FROM    transactions
)
WHERE   rnk = 1
ORDER BY transaction_id
