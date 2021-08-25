SELECT * FROM rater_api_game;

SELECT AVG(r.rating) AS average_rating, g.title
FROM rater_api_game AS g, rater_api_gamerating AS r
WHERE g.id = r.game_id
GROUP BY g.id
ORDER BY average_rating DESC
LIMIT 5;