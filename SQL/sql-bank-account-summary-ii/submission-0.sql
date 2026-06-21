-- Write your query below

SELECT  u.name, 
        SUM(t.amount) as balance
FROM    users u JOIN transactions t USING (account)
GROUP BY u.name
HAVING SUM(t.amount) > 10000
