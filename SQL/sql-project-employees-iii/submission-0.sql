-- Write your query below
SELECT  project_id, employee_id
FROM    (
    SELECT  p.project_id, e.employee_id, e.experience_years,
            DENSE_RANK() OVER (PARTITION BY project_id ORDER BY e.experience_years DESC) rnk
    FROM    project p JOIN employee e USING (employee_id)
)
WHERE rnk = 1
