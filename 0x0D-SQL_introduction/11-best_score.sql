-- lists records > 10 of the table second_table
-- only socre and name actulay in DESC order by score
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC
