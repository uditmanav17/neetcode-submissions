-- Write your query below

SELECT  employee_id, COUNT(*) OVER (PARTITION BY team_id) as team_size
FROM    employee
