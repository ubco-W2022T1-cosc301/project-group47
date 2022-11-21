import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):


    df = (
        pd.read_csv(url_or_path_to_csv_file))

    df_cleaned = (df[df.Region != '-'])

    df_cleaned2 = ( df_cleaned.copy().drop(['Generosity'], axis=1)
         .copy().drop(df_cleaned.columns[0], axis=1)
         .dropna(axis=0))
    
    df_cleaned_3 = (df_cleaned2[df_cleaned2.Year != 2022])
    
    
 
    
    # Make sure to return the latest dataframe
    return df_cleaned_3
    
