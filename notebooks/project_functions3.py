import pandas as pd
import numpy as np 

def load_and_process(url_or_path_to_csv_file):


    df1 = (
        pd.read_csv(url_or_path_to_csv_file))

    df2 = ( df1.transform(pd.to_numeric, errors='coerce')
         .copy().drop(['Happiness Rank', 'Country', 'Region', 'Freedom', 'Trust (Government Corruption)', 'Generosity'], axis=1)
         .copy().drop(df1.columns[0], axis=1)
         .dropna(axis=0))
    
    df3 = (df2[df2.Year != 2022])
    
    # Make sure to return the latest dataframe
    return df3
