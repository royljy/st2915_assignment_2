#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 12:41:30 2021

@author: roylee
@topic: st2195_assignment_2
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

wiki_url = "https://en.wikipedia.org/wiki/Comma-separated_values"
wiki_page = requests.get(wiki_url).text
soup = BeautifulSoup(wiki_page, "html.parser") 

content_table = soup.find('table',{'class':'wikitable'})
content_table

# read.html() reads html into dataframe
content_df = pd.read_html(str(content_table))

# concat() arranges indexes properly
content_df = pd.concat(content_df)

# to_csv() write content_df to csv file, remove index
content_df.to_csv("/Users/roylee/repositories/st2915/st2195_assignment_2/python_csv/py_wikitable.csv", index=False)

#read_csv() to write csv to df, check csv
check_df = pd.read_csv("/Users/roylee/repositories/st2915/st2195_assignment_2/python_csv/py_wikitable.csv")
print(check_df)