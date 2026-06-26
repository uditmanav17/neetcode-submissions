-- Write your query below
SELECT DISTINCT l.page_id AS recommended_page
FROM likes l
WHERE l.user_id IN (
    SELECT user2_id FROM friendship WHERE user1_id = 1
    UNION
    SELECT user1_id FROM friendship WHERE user2_id = 1
)
AND NOT EXISTS (
    SELECT 1 FROM likes u1 WHERE u1.user_id = 1 AND u1.page_id = l.page_id
)
