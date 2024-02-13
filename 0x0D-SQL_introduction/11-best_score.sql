-- List all records with score >= 10 from second_table starting with the highest score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
