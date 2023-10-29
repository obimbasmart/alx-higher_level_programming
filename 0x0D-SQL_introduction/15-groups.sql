-- compute the average of student's score

SELECT score, COUNT(*) AS number
	FROM second_table
	GROUP BY score
	ORDER BY number;
