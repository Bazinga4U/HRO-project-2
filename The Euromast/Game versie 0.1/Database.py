"""
@copyright 2017 Created by De Vijf Musketiers
@content this class
"""

import psycopg2

class Connect:
    # Use the database
    def __init__(self):
        # Connect and set up cursor
        self.connection = psycopg2.connect("dbname=TheEuromast user=postgres  password=admin host=127.0.0.1 port=5432")
        self.cursor = self.connection.cursor()
    def interact_with_database(self,command):
        # Execute the command
        self.cursor.execute(command)
        self.connection.commit()

        # Save results
        results = None
        try:
            results = self.cursor.fetchall()
        except psycopg2.ProgrammingError:
            # Nothing to fetch (maak error statement later?)
            return False
        return results
    def close_connection(self):
        self.cursor.close()
        self.connection.close()
    # Uploads a score into the hiscore table
    def update_playerscore_table(self,name):
        playerExists = self.interact_with_database("SELECT count(*) FROM playerscorelist WHERE playername = '{}'"
                               .format(name))
        if playerExists != 0:
            self.interact_with_database("UPDATE playerscorelist SET playerscore = playerscore + 1 WHERE playername = '{}'"
                               .format(name))
        else:
            self.interact_with_database("INSERT INTO playerscorelist VALUES ('{}',1) "
                               .format(name))
    # Downloads score data
    def download_scores(self):
        return self.interact_with_database("SELECT * FROM playerscorelist ORDER BY playerscore DESC LIMIT 10")
        print(download_scores())
    #delete alle games, zodat de id altijd 1 kan blijven (misschien later kan dit meerdere savegames worden)
    def deleteSaveGame(self):
        self.interact_with_database("DELETE FROM save_game")
        self.interact_with_database("DELETE FROM save_game_turn")
        self.interact_with_database("DELETE FROM save_game_players")
    #insert de save game tabel (naam + id)
    def insertSaveGame(self, sg_id, sg_name):
        self.interact_with_database("INSERT INTO save_game VALUES ({}, '{}')".format(sg_id, sg_name))
    #ginsert de save_game_turn tabel (geeft aan welke speler aan de beurt is)
    def insertSaveGameTurn(self, sg_id, playerID):
        self.interact_with_database("INSERT INTO save_game_turn VALUES ({}, '{}')".format(sg_id, playerID))
    #insert de posities, namen, etc. van de spelers
    def insertSaveGamePlayers(self, player_id, sg_id, sgp_x_position, sgp_y_position, sgp_position_name, sgp_name, sgp_is_computer_player):
        sgp_position_name =  sgp_position_name.replace("'","*")
        self.interact_with_database("INSERT INTO save_game_players VALUES ({}, {}, {}, {}, '{}', '{}', {})".format(player_id, sg_id, sgp_x_position, sgp_y_position, sgp_position_name, sgp_name, sgp_is_computer_player))
    def SelectLoadGame(self):
        return self.interact_with_database("SELECT sgt.player_id FROM save_game AS sg INNER JOIN save_game_turn AS sgt ON sg.sg_id = sgt.sgt_id WHERE sg.sg_id = 1")
    def SelectLoadGamePlayers(self):
        return self.interact_with_database("SELECT * FROM save_game_players WHERE sg_id = 1 ORDER BY player_id ASC")
