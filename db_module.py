from sqlalchemy import create_engine
import pandas as pd


def load_db():

    # Load the engine and get the connection, write to beer.db
    print(">> Creating sqlalchemy engine and connection")
    engine = create_engine("sqlite:///Resources/beer.db", echo=False)
    conn = engine.connect()

    # If database exists then drop the table first, reload the data
    print(">> Dropping beer_reviews table if needed")
    try:
        conn.execute("""DROP TABLE beer_reviews""")
    except:
        print(">> skipped droping beer_reviews table, doesn't exist yet")

    # Create the table - note that if we use automap_base, the table must have primary key!
    print(">> Creating beer_reviews table")
    conn.execute("""CREATE TABLE IF NOT EXISTS beer_reviews ( 
        beer_reviews_id INTEGER PRIMARY KEY AUTOINCREMENT ,
        beer_id         INTEGER NOT NULL , 
        username        TEXT NOT NULL ,
        date            TEXT NOT NULL , 
        look            REAL NOT NULL ,
        smell           REAL NOT NULL ,
        taste           REAL NOT NULL ,
        feel            REAL NOT NULL ,
        overall         REAL NOT NULL ,
        score           REAL NOT NULL ,
        beer_name       TEXT NOT NULL ,
        review_state    TEXT NOT NULL ,
        style           TEXT NOT NULL ,
        availability    TEXT NOT NULL , 
        abv             REAL NOT NULL ,
        brewery_id      INTEGER NOT NULL ,
        brewery_name    TEXT NOT NULL ,
        brewery_city    TEXT NOT NULL ,
        brewery_state   TEXT NOT NULL ,
        brewery_types   TEXT NOT NULL 
    )
    """)

    # Read in target dataframe
    print(">> Reading in beer reviews data from csv")
    review_df = pd.read_csv("Resources/reviews_beer_brewery.zip")

    # Insert into table
    print(">> Inserting data into the beer_reviews table")
    review_df.to_sql("beer_reviews", conn, if_exists="append", index=False)

    # Clean up
    print(">> clean up database resources")
    conn.close()
    engine.dispose()
