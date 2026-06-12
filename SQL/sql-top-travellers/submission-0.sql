-- Write your query below

SELECT  u.name, COALESCE(SUM(r.distance), 0) as travelled_distance
FROM    users u LEFT JOIN rides r ON u.id = r.user_id
GROUP BY name
ORDER BY travelled_distance DESC
