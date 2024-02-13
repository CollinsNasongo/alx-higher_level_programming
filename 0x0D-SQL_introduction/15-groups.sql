-- List the number of records with same score in second table.
SELECT `score`, COUNT(`id`) as `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
