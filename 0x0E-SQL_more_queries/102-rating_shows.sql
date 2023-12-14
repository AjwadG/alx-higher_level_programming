-- lists all shows from hbtn_0d_tvshows_rate by their sum of rating.
-- sorted in descending order by the rating
SELECT title, SUM(rate) AS rating
FROM tv_shows
	INNER JOIN tv_show_ratings
	ON id = show_id
GROUP BY title
ORDER BY rating DESC;
