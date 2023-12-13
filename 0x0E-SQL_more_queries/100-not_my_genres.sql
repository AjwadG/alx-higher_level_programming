-- uses the hbtn_0d_tvshows database to lists
-- all genres thatare not of the show Dexter.
SELECT tv_genres.name 
from tv_genres
WHERE tv_genres.name NOT IN (
		SELECT g.name FROM tv_genres AS g 
			INNER JOIN tv_show_genres AS sg 
			ON g.id = sg.genre_id 
			INNER JOIN tv_shows AS s 
			ON sg.show_id = s.id 
		WHERE s.title = 'Dexter')
ORDER BY tv_genres.name ASC;
