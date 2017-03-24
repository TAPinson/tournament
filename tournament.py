import psycopg2


def connect():
    return psycopg2.connect("dbname=tournament")

# Connect to database, establish a cursor,
# send command to delete contents from the "matches" table.


def deleteMatches():
    DB = psycopg2.connect("dbname=tournament")
    cursor = DB.cursor()
    cursor.execute("delete FROM matches;")
    DB.commit()
    DB.close()

# Connect to database, establish a cursor, send command to delete contents
# from the "players" table.


def deletePlayers():
    DB = psycopg2.connect("dbname=tournament")
    cursor = DB.cursor()
    cursor.execute("delete FROM players;")
    DB.commit()
    DB.close()

# Connect to database, establish a cursor, count columns in "players_name"
# and return table as num


def countPlayers():
    DB = psycopg2.connect("dbname=tournament")
    cursor = DB.cursor()
    cursor.execute("SELECT player_name as num FROM players")
    results = cursor.fetchall()
    DB.close()
    return len(results)

# Connect to database, establish a cursor, insert a player into players table
# securely w/ python name variable


def registerPlayer(name):
    DB = psycopg2.connect("dbname=tournament")
    cursor = DB.cursor()
    cursor.execute("INSERT INTO players (player_name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()

# Connect to database, establish a cursor, use the "standings" view created in
# our tournament sql file. More about this view in the tournament sql file


def playerStandings():
    DB = psycopg2.connect("dbname=tournament")
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM standings;")
    results = cursor.fetchall()
    return results

# Connect to database, establish a cursor, inserts entry into "matches" table
# with values from the python variables winner" and "loser"


def reportMatch(winner, loser):
    DB = connect()
    cursor = DB.cursor()
    cursor.execute('INSERT INTO matches'
                   ' (winner, loser) VALUES (%s, %s)', (winner, loser,))
    DB.commit()
    DB.close()


# Define standings as the results of the playerStandings function. Define num
# as the number of players. List "pairings" needed for function pairings
# If pairings are set, tournament should run
def swissPairings():
    standings = playerStandings()
    num = int(countPlayers())
    pairings = []
    if (num > 0):
        for i in range(num):
            if (i % 2 == 0):
                id1 = standings[i][0]
                name1 = standings[i][1]
                id2 = standings[i + 1][0]
                name2 = standings[i + 1][1]
                pair = (id1, name1, id2, name2)
                pairings.append(pair)
    return pairings

# Given the existing set of registered players and the matches they have played,
# generates and returns a list of pairings according to the Swiss system.
# Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the
# paired players. For instance, if there are eight registered players,
# this function should return four pairings. This function should use
# playerStandings to find the ranking of players. This comment with explanation
# provided by Udacity.

