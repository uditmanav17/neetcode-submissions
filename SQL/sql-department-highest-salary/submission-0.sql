-- Write your query below
SELECT  department, employee, salary
FROM    (
    SELECT  e.name as employee, e.salary, d.name as department,
            DENSE_RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS rnk
    FROM    employee e JOIN department d ON e.department_id = d.id
) tmp
WHERE rnk = 1

