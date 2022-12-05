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
    
    def normalize_with_percent(df):
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
            .drop(dfa.columns[0], axis=1)
              .apply(convert_dict))

    
#     df = (pd.read_csv(url_or_path_to_csv_file))
#     df_cleaned = (df[df.Region != '-'])
#     df_cleaned_2 = (df_cleaned.copy().drop(['Generosity'], axis=1)
#                      .copy().drop(df_cleaned.columns[0], axis=1)
#                      .dropna(axis=0))
#     df_cleaned_3 = (df_cleaned_2[df_cleaned_2.Year != 2022])
#     df_cleaned_4 = (df_cleaned_3.copy().drop(['Year'], axis=1)
                    
#     df_cleaned_4["Happiness Score"]=df_cleaned_4["Happiness Score"].astype(float)
#     df_cleaned_4["Economy (GDP per Capita)"]=df_cleaned_4["Economy (GDP per Capita)"].astype(float)
#     df_cleaned_4["Family (Social Support)"]=df_cleaned_4["Family (Social Support)"].astype(float)
#     df_cleaned_4["Health (Life Expectancy)"]=df_cleaned_4["Health (Life Expectancy)"].astype(float)
#     df_cleaned_4["Freedom"]=df_cleaned_4["Freedom"].astype(float)
#     df_cleaned_4["Trust (Government Corruption)"]=df_cleaned_4["Trust (Government Corruption)"].astype(float)

    # Make sure to return the latest dataframe
    return dfb
    
