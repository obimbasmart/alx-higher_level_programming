-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked

SELECT name, COUNT(show_id) AS number_of_shows
FROM 
	(SELECT tv_genres.name, tv_show_genres.show_id 
	 FROM tv_genres
	 JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id) AS deriv 
GROUP BY name ORDER BY number_of_shows DESC;
