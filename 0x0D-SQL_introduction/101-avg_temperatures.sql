-- display student with names (skip names with NULL)

SELECT city, AVG(value) AS avg_temp 
	FROM temperatures
	GROUP BY city 
	ORDER BY avg_temp DESC;
