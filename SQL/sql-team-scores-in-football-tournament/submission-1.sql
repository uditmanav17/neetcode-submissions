-- Write your query below
WITH scores AS (
    SELECT
        host_team, guest_team,
        CASE 
            WHEN host_goals > guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END AS host_score, 
        CASE 
            WHEN host_goals < guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END AS guest_score
    FROM    matches
),
aggregated_scores AS (
    (
        SELECT  host_team AS team_id, host_score AS team_score
        FROM    scores
    )
    UNION ALL
    (
        SELECT  guest_team AS team_id, guest_score AS team_score
        FROM    scores
    )
)

-- SELECT * FROM aggregated_scores

SELECT  t.team_id, t.team_name, COALESCE(SUM(ag_s.team_score), 0) AS num_points
FROM    teams t LEFT JOIN aggregated_scores ag_s USING (team_id)
GROUP BY t.team_id, t.team_name
ORDER BY num_points DESC, team_id
