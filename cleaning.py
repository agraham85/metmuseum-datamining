#!/usr/bin/env python
# coding: utf-8



#Import Modulea
import pandas as pd
import os
from cleaning_utils import *
import numpy as np


#Load Met DataFrame

cwd = os.getcwd()
df = pd.read_csv(os.path.join(cwd, "MetObjects.txt"))


#Create Artist Dataframe and split rows
artist_col_list = list(range(16, 28)) # making list of column index from Q->AB
artist_col_list.insert(0, 0) # Adding the first column as index
artist_df = df.iloc[: , artist_col_list] #subsets originas dataframe 'df'
artist_df = split_rows(artist_df)




#Split Data Fram into sections by group member

andrew_col_list = [i for i in range(2, df.shape[1], 3)]
andrew_col_list.insert(0, 0)
andrew_df = df.iloc[:, andrew_col_list]
andrew_df = andrew_df.astype(str, errors="ignore")
andrew_artist_cols = [i for i in range(2, artist_df.shape[1], 3)]
andrew_artist_df = artist_df.iloc[:, andrew_artist_cols]




# Andrew Cleaning

#Is Timeline Work
andrew_df['Is Timeline Work'] = andrew_df['Is Timeline Work'].astype(bool)

#Period
andrew_df["Period"] = andrew_df["Period"].replace(to_replace = '\(\?\)|\?', value = '', regex = True)
andrew_df["Period"] = andrew_df["Period"].replace(to_replace = '\(.*', value = '', regex = True)
andrew_df["Period"] = andrew_df["Period"].replace(to_replace = 'late|early|probably', value = '', regex = True)
andrew_df["Period"] = andrew_df["Period"].replace(to_replace = '\sor.*', value = '', regex = True)
andrew_df["Period"] = andrew_df["Period"].replace(to_replace = ',.*', value = '', regex = True)
andrew_df["Period"] = andrew_df["Period"].str.strip()

#Portfolio
andrew_df["Portfolio"] = andrew_df["Portfolio"].replace(to_replace = '\\r\\n', value = '', regex = True)
andrew_df = andrew_df.replace(r'^\s*$', np.nan, regex=True)

#Object Begin Date
andrew_df['Object Begin Date']= pd.to_numeric(andrew_df['Object Begin Date'].copy())
andrew_df['Object Begin Date'].mask(andrew_df['Object Begin Date'] == 5000, -5000, inplace = True)

#Dimensions
andrew_df["Dimensions"] = andrew_df["Dimensions"].replace(to_replace = '\\r|\\n|\\t', value = '', regex = True)

#City
andrew_df["City"] = andrew_df["City"].replace(to_replace = '\(\?\)|\?', value = '', regex = True)
andrew_df["City"] = andrew_df["City"].replace(to_replace = '\(.*', value = '', regex = True)
andrew_df["City"] = andrew_df["City"].replace(to_replace = 'maybe|probably|possibly', value = '', regex = True)
andrew_df["City"] = andrew_df["City"].replace(to_replace = '\sor\s.*', value = '|', regex = True)
andrew_df["City"] = andrew_df["City"].replace(to_replace = '\sor.*', value = '|', regex = True)
# andrew_df["Period"] = andrew_df["Period"].replace(to_replace = ',.*', value = '', regex = True)
andrew_df["City"] = andrew_df["City"].str.strip()

#Country
andrew_df["Country"] = andrew_df["Country"].replace(to_replace = '\(\?\)|\?', value = '', regex = True)
andrew_df["Country"] = andrew_df["Country"].replace(to_replace = '\(.*', value = '', regex = True)
andrew_df["Country"] = andrew_df["Country"].replace(to_replace = 'maybe|probably|possibly', value = '', regex = True)
andrew_df["Country"] = andrew_df["Country"].replace(to_replace = '\sor\s.*', value = '|', regex = True)
andrew_df["Country"] = andrew_df["Country"].replace(to_replace = '\sor.*', value = '|', regex = True)
andrew_df["Country"] = andrew_df["Country"].str.replace(r'([\w\s]+)(\|(\1))+', r'\1')
andrew_df["Country"] = andrew_df["Country"].replace(to_replace = ',\s?', value = '|', regex = True)
andrew_df["Country"] = andrew_df["Country"].replace(to_replace = '\|$', value = '', regex = True)
andrew_df["Country"] = andrew_df["Country"].str.strip()


#General Artist_Andrew cleanup
andrew_artist_df = andrew_artist_df.replace(r'^\s*$', np.nan, regex=True)


#Artist Prefix
andrew_artist_df["Artist Prefix"] = andrew_artist_df["Artist Prefix"].str.strip()

#Artist Suffix
andrew_artist_df["Artist suffix"] = andrew_artist_df["Artist Prefix"].str.strip()

#Artist Begin Date
andrew_artist_df["Artist Begin Date"] = andrew_artist_df["Artist Begin Date"].str.extract(r'(-*\d{4})')

#Create City Table
city_col_list = [12] # City Col
city_col_list.insert(0, 0) # Adding the first column as index
city_df = andrew_df.iloc[: , city_col_list]
city_df = split_rows(city_df)

#Create Country Table
country_col_list = [13] # Country COl
country_col_list.insert(0, 0) # Adding the first column as index
country_df = andrew_df.iloc[: , country_col_list]
country_df = split_rows(country_df)






#Consolidate Cleaning Tables

clean_df = df.copy()

for col in andrew_df:
    clean_df[col] = andrew_df[col]

clean_artist_df = artist_df.copy()

for col in andrew_artist_df:
    clean_artist_df[col] = andrew_artist_df[col]

# cleaning mikes columns
df["Dynasty_clean"] = df["Dynasty"].str.extract("(\d\d)")
df["Artist End Date_clean"] = df["Artist End Date"].str.extract("(-?\d\d\d\d\|?){1,10}")
clean_artist_df["Artist End Date_clean"] = clean_artist_df["Artist End Date"].str.extract("(\d\d\d\d)")



#Output Clean Tables

artist_df.to_pickle("./artist_df.pkl")
clean_df.to_pickle("./clean_df.pkl")
clean_artist_df.to_pickle("./clean_artist_df.pkl")
country_df.to_pickle("./country_df.pkl")
city_df.to_pickle("./city_df.pkl")