import extract
import transform
import config
import data_quality_test
import mysql.connector
import sqlalchemy
import pandas as pd


# Importing the songs_df from the extract.py and run data quality tests on data retrieved:
df_extract = extract.song_df
if(data_quality_test.tests(df_extract) == False):
    raise ("Failed at Data Validation")

df_transform = transform.transformed_df

# Making connection to MySQL with defined connection credentials
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}?auth_plugin=mysql_native_password'.
                                        format(config.database_username, 
                                               config.database_password, 
                                               config.database_ip, 
                                               config.database_name))
# auth_plugin issue: https://stackoverflow.com/questions/50557234/authentication-plugin-caching-sha2-password-is-not-supported

# Writing to MySQL db
try:
    df_extract.to_sql(con=database_connection, name='raw_spotify_top_50', if_exists='append')
except:
    print("Data already exists in the database")

try:
    df_transform.to_sql(con=database_connection, name='daily_top_artists', if_exists='append')
except:
    print("Data already exists in the database")