import sqlite3 
from sqlite3 import Error

sql_create_predictions_history_table = """ CREATE TABLE IF NOT EXISTS predictions_history (
                                        id integer PRIMARY KEY,
                                        prediction_date text,
                                        user_group text,
                                        track_id text,
                                        name text,
                                        popularity real,
                                        duration_ms integer,
                                        explicit integer,
                                        id_artist text,
                                        release_date text,
                                        danceability real,
                                        key real,
                                        energy real,
                                        loudness real,
                                        speechiness real,
                                        acousticness real,
                                        instrumentalness real,
                                        liveness real,
                                        valence real,
                                        tempo real,
                                        genre text
                                    );"""

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_prediction(conn, prediction):
    """
    Insert prediction log into the predictions_history table
    :param conn:
    :param prediction:
    :return: prediction id
    """
    sql = ''' INSERT INTO predictions_history(prediction_date,user_group,track_id,name,popularity,duration_ms,explicit,id_artist,release_date,danceability,key,energy,loudness,speechiness,acousticness,instrumentalness, liveness,valence,tempo,genre)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, prediction)
    conn.commit()
    return cur.lastrowid

if __name__ == '__main__':
    conn = create_connection(r"database\saved_data.db")
    if conn is not None:
        create_table(conn, sql_create_predictions_history_table)
    else:
        print("Error! cannot create the database connection.")
    
    

    