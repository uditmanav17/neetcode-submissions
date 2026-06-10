-- Write your query below
SELECT student_id, exam_id, score
FROM    (
    SELECT 
        student_id, 
        exam_id, 
        score, 
        DENSE_RANK() OVER (
            PARTITION BY student_id 
            ORDER BY score DESC, exam_id ASC
        ) as rnk
    FROM exam_results
)
WHERE rnk = 1
ORDER BY student_id
