-- Write your query below
WITH RECURSIVE subtask_numbers AS (
    SELECT task_id, 1 AS subtask_id, subtasks_count
    FROM tasks
    UNION ALL
    SELECT task_id, subtask_id + 1, subtasks_count
    FROM subtask_numbers
    WHERE subtask_id < subtasks_count
)

SELECT  task_id, subtask_id
FROM    subtask_numbers sn
WHERE   NOT EXISTS (
    SELECT  1
    FROM    executed e
    WHERE   sn.task_id = e.task_id 
            AND sn.subtask_id = e.subtask_id
)

