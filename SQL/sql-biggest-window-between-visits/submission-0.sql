-- Write your query below
SELECT  user_id, MAX(ABS(visit_date - prev)) AS biggest_window
FROM    (
    SELECT  user_id, visit_date, 
            COALESCE(
                LEAD(visit_Date, 1) OVER (partition by user_id order by visit_date),
                '2021-1-1'
            ) as prev
    FROM    user_visits
) t
GROUP BY user_id
ORDER BY user_id
