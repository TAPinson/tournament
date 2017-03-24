-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.



CREATE TABLE players(
  player_id serial PRIMARY KEY,
  player_name text
);


CREATE TABLE matches(
  match_id serial PRIMARY KEY,
  winner INTEGER,
  loser INTEGER,
  FOREIGN KEY(winner) REFERENCES players(player_id),
  FOREIGN KEY(loser) REFERENCES players(player_id)
);


CREATE VIEW standings AS
SELECT p.player_id as player_id, p.player_name,
(SELECT count(*) FROM matches WHERE matches.winner = p.player_id) as won,
(SELECT count(*) FROM matches WHERE p.player_id in (winner, loser)) as played
FROM players p
GROUP BY p.player_id
ORDER BY won DESC;

-- view explanation:
-- new view named standings
-- select players id and the players name
-- using the matches tree, count instances where the player has won as "won"
-- using the matches tree, count instances where the player has won or lost as "played"
-- p is from players tree
-- group the by player id
-- tell me who has the most! 
