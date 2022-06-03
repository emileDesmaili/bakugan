# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:29:40 2022

@author: EmileESMAILI
"""

import gzip
import json
import os
from datetime import datetime
import pandas as pd
import streamlit as st
import pickle



#get list of shortlisted firms
excel = pd.read_excel(r'C:\Users\EmileESMAILI\Ekimetrics\Open Rothschild & Co - GA data roadmap - Documents\GA data roadmap\3. Use Cases\Use Case 4 - Non Listed Companies Enriched Profiles\Docs APIs\List of firms for Orbis API.xlsx')
excel = excel.drop(['Country','Sector'],axis=1).dropna()
names = list(excel['Name'])


#set path
path = os.getcwd()
path = os.path.join(path,"data/raw")

#open all json.gzip files and concat them

data_list = []
for root, directories, files in os.walk(path):
    for file in files:
        filepath = os.path.join(root, file)
        if filepath.endswith('.json.gz'):
            with gzip.open(filepath, "r") as f:
                data = [json.loads(line) for line in f]
                data_list.extend(data)
                
            
#keeping only 'fr' and 'en' articles

data_lang=[]
for article in data_list:
    if (article['language_code'] == 'en' or article['language_code'] == 'fr'):
        data_lang.append(article)
        


def json_date(article):
    timestamp = article['publication_date'][:10]
    return datetime.fromtimestamp(abs(int(timestamp)))

news_list = []
for name in names:
    keys = []
    values = []
    for article in data_lang:
        if name.title() in article['title']:
            keys.append(json_date(article))
            values.append(article)
    news_dict = dict(zip(keys,values))
    news_list.append(news_dict)

if __name__ == "__main__":
    my_file = "streamlit_app/news_list.txt"
    with open(my_file, 'wb') as f:
        pickle.dump(news_list, f)
    

    

