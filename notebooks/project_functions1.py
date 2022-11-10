import pandas as pd
import numpy as np 

def load_and_process(url_or_path_to_csv_file):


    dfa = (
        pd.read_csv(url_or_path_to_csv_file))

    dfb = ( dfa.transform(pd.to_numeric, errors='coerce')
         .drop(columns=['Country', 'Region']))
    dfc = dfb[dfb.Freedom.notnull()]
    dfd = dfc.drop(columns=dfc.columns[0])
    
    # Make sure to return the latest dataframe
    return dfd
