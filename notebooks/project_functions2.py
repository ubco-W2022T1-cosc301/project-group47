import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    
    def normalize_with_percent(df):
        
        df["Happiness Score"]=df["Happiness Score"].astype(float)
        df["Economy (GDP per Capita)"]=df["Economy (GDP per Capita)"].astype(float)
        df["Family (Social Support)"]=df["Family (Social Support)"].astype(float)
        df["Health (Life Expectancy)"]=df["Health (Life Expectancy)"].astype(float)
        df["Freedom"]=df["Freedom"].astype(float)
        df["Trust (Government Corruption)"]=df["Trust (Government Corruption)"].astype(float)
        
        result = df.copy()
        
        for feature_name in df.columns:
            if df[feature_name].dtype==float:
                # if dtype is float then normalize it
                max_value = df[feature_name].max()
                min_value = df[feature_name].min()
                result[feature_name] = ((df[feature_name] - min_value) / (max_value - min_value))*100
        return result
    
    dfa = (
        pd.read_csv(url_or_path_to_csv_file))
    dfb = (dfa[dfa.Year != 2022]
          .drop(columns = ['Unnamed: 0', 'Year', 'Generosity'], axis=1))

    dfc = (normalize_with_percent(dfb).groupby(['Country'], as_index = False, sort = False)['Happiness Score', 'Economy (GDP per Capita)',
                                           'Family (Social Support)', 'Health (Life Expectancy)', 
                                           'Freedom', 'Trust (Government Corruption)'].mean())
    


    # Make sure to return the latest dataframe
    return dfc
    
