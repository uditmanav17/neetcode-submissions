-- Write your query below
SELECT  COALESCE(e.employee_id, s.employee_id) as employee_id
FROM    employees e FULL OUTER JOIN salaries s USING (employee_id)
WHERE   e.name IS NULL OR s.salary IS NULL
ORDER BY employee_id
