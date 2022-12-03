import pandas as pd
import numpy as np 

def load_and_process(url_or_path_to_csv_file):


    df1 = (
        pd.read_csv(url_or_path_to_csv_file))

    df2 = ( df1.transform(pd.to_numeric, errors='coerce')
         .drop(['Happiness Rank', 'Country', 'Region', 'Freedom', 'Trust (Government Corruption)', 'Generosity'], axis=1)
         .drop(df1.columns[0], axis=1)
         .dropna(axis=0)
         [df1["Year"]!=2022]
           .apply(normalize1)
          )
    
    
 
    
    # Make sure to return the latest dataframe
    return df2
    
