-- Write your query below
SELECT  DISTINCT title
FROM    (   SELECT content_id 
            FROM tv_program 
            WHERE   EXTRACT(YEAR FROM CAST(program_date AS TIMESTAMP)) = 2020
                    AND EXTRACT(MONTH FROM CAST(program_date AS TIMESTAMP)) = 6
) t1 LEFT JOIN content t2 USING (content_id)
WHERE kids_content = 'Y' AND content_type = 'Movies'