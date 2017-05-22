/*
-- Query used to create the database

CREATE DATABASE TheEuromast

*/

-- Query's used to test the database.

/*
CREATE TABLE test (
	username varchar(25),
    score int,
    PRIMARY KEY(username)
);

*/

/*

INSERT INTO playerscorelist (playername,playerscore) VALUES ('Tester',1000)
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Tester2',900)
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Tester4',888)
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Tester3',850)
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Tester5',770)
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Tester6',720)
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Tester7',640)
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Tester8',550)
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Tester9',490)
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Tester10',430)
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Tester11',320)
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Tester12',250)


-- FInals query's used for the correct database.

/*
-- Query used to create the table.

CREATE TABLE playerscorelist (
    playername varchar(25),
    playerscore int,
    PRIMARY KEY (playername)
);

*/

/*
-- Query's used to test out the new table in the game

INSERT INTO playerscorelist (playername,playerscore) VALUES ('Test',8)
DELETE FROM playerscorelist

*/

/*
-- Query's used to insert the new scores for show.

INSERT INTO playerscorelist (playername,playerscore) VALUES ('EIbert',8);
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Redouan',16);
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Roos',32);
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Jürgen',64);
INSERT INTO playerscorelist (playername,playerscore) VALUES ('Wessel',128);

*/
-- CREATE TABLE IF NOT EXISTS playerscorelist (
--     playername varchar(25),
--     playerscore int,
--     PRIMARY KEY (playername)
-- );

-- CREATE TABLE IF NOT EXISTS save_game(
--     sg_id integer, 
--     sg_name varchar(20),
--     PRIMARY KEY(sg_id));

-- CREATE TABLE IF NOT EXISTS save_game_turn(
-- 	sgt_id integer, 
-- 	player_id integer,
-- 	PRIMARY KEY(sgt_id));
    
-- CREATE TABLE IF NOT EXISTS save_game_players(
-- 	player_id integer,
--     sg_id integer,
-- 	sgp_x_position integer,
-- 	sgp_y_position integer, 
-- 	sgp_position_name varchar(15),
-- 	sgp_name varchar(15),
-- 	sgp_is_computer_player boolean,
-- 	PRIMARY KEY(player_id)); 
   
-- SELECT * FROM save_game_turn

/*
-- Query's used in python code.

SELECT * FROM test ORDER BY score DESC LIMIT 10
UPDATE score SET score = {} WHERE name = '{}' 

*/

