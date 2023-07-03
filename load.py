import extract
import config
import data_quality_test
import mysql.connector
import sqlalchemy
import pandas as pd


# Importing the songs_df from the extract.py and run data quality tests on data retrieved:
df = extract.song_df
if(data_quality_test.tests(df) == False):
    raise ("Failed at Data Validation")

# Making connection to MySQL with defined connection credentials
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}?auth_plugin=mysql_native_password'.
                                        format(config.database_username, 
                                               config.database_password, 
                                               config.database_ip, 
                                               config.database_name))
# auth_plugin issue: https://stackoverflow.com/questions/50557234/authentication-plugin-caching-sha2-password-is-not-supported

# Writing to MySQL db
try:
    df.to_sql(con=database_connection, name='spotify_top_50', if_exists='append')
except:
    print("Data already exists in the database")
