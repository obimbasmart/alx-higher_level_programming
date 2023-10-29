-- display student with names (skip names with NULL)

SELECT score, name FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score DESC;
