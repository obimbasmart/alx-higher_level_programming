--  lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT DISTINCT title 
FROM tv_shows AS ts 
WHERE NOT EXISTS ( SELECT 1 
	FROM tv_show_genres AS tsg 
	INNER JOIN tv_genres AS tg ON tsg.genre_id = tg.id 
	WHERE tsg.show_id = ts.id AND tg.name = 'Comedy' )
ORDER BY title;
