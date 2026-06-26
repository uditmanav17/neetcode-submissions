-- Write your query below
SELECT  DISTINCT page_id AS recommended_page
FROM    likes
WHERE   user_id IN (
    SELECT
        CASE 
            WHEN user1_id = 1 THEN user2_id
            WHEN user2_id = 1 THEN user1_id
        END AS user1_friends
    FROM    friendship
) AND page_id not in (SELECT page_id from likes where user_id = 1)
