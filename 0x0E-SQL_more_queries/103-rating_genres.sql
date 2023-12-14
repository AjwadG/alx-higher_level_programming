-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT name, sum(rate) AS rating 
FROM tv_genres 
	INNER JOIN tv_show_genres AS sg 
	ON id = sg.genre_id 
		INNER JOIN tv_show_ratings AS sr 
		ON sr.show_id = sg.show_id
 GROUP BY name 
 ORDER BY rating DESC;
