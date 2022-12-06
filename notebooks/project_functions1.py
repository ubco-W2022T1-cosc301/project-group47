import pandas as pd
import numpy as np 



def load_and_process(url_or_path_to_csv_file):

    convert_dict = {'Happiness Score': float,
                'Economy (GDP per Capita)': float, 
               'Family (Social Support)': float,
               'Health (Life Expectancy)':float,
               'Freedom':float, 
               'Country':str, 
               'Region':str, 
               'Year':float, 
               'Happiness Rank':float, 
               'Trust (Government Corruption)':float,
                'Generosity':float
               }

    dfa = (
        pd.read_csv(url_or_path_to_csv_file))
    dfb = (dfa[dfa.Year != 2022]
            .drop(dfa.columns[0], axis=1)
              .apply(convert_dict))
    
    return dfb
