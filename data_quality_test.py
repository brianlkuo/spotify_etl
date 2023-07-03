import extract
import pandas as pd 

# Set of Data Quality Checks Needed to Perform Before Loading
def tests(load_df):
    # Empty test: whether the DataFrame is empty
    if load_df.empty:
        print('No song information extracted')
        return False

    # Null test: checking for null values
    if load_df.isnull().values.any():
        raise Exception("Null values found")    
    
    # Unique test: checking all loaded data is unique
    if pd.Series(load_df['track_id'].map(str) + load_df['timestamp'].map(str)).is_unique:
        pass
    else:
        raise Exception('Exception: possible duplications in loaded data')


load_df=extract.song_df

if(tests(load_df) == False):
    raise ("Failed at Data Validation")
else:
    print('Passed all data quality checks!')