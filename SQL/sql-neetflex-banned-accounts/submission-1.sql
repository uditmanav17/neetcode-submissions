-- Write your query below
SELECT  DISTINCT a1.account_id
FROM    log_info a1 JOIN log_info a2 USING (account_id)
WHERE   1 = 1 
        AND a1.login <= a2.logout
        AND a2.login <= a1.logout 
        AND a1.ip_address != a2.ip_address
