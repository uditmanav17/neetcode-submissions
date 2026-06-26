-- Write your query below
SELECT  DISTINCT node as id, 
        CASE
            WHEN parent IS NULL THEN 'Root'
            WHEN child IS NULL THEN 'Leaf'
            ELSE 'Inner'
        END as type
FROM    (
    SELECT  t1.id as node, t1.p_id as parent, t2.id as child
    FROM    tree t1 LEFT JOIN tree t2 ON t1.id = t2.p_id
) t
