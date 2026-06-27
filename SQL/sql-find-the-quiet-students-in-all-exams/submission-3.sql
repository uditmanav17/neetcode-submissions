-- Write your query below
WITH ranked_exams AS (
    SELECT  student_id, exam_id, score,
            DENSE_RANK() OVER (PARTITION BY exam_id ORDER BY score) as lowest,
            DENSE_RANK() OVER (PARTITION BY exam_id ORDER BY score DESC) as highest
    FROM    exam
)

SELECT  DISTINCT s.student_id, s.student_name
FROM    student s JOIN ranked_exams re USING (student_id)
WHERE   s.student_id NOT IN (
    SELECT  student_id
    FROM    ranked_exams
    WHERE   highest = 1 OR lowest = 1
)
ORDER BY student_id

