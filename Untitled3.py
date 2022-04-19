#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import json
from pprint import pprint
from time import time
from time import sleep


# In[2]:


r = requests.get("https://disease.sh/v3/covid-19/historical/all?lastdays=all")
r.status_code
data_json = r.json()
df = pd.DataFrame(data_json)
print(df)


# In[3]:


df


# In[4]:


import pymysql

connection = pymysql.connect(host="localhost",
                             user="root",
                             password="password",
                             database="firstdb")
cursor = connection.cursor()


# In[5]:


# creating column list for insertion
cols = "`,`".join([str(i) for i in df.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in df.iterrows():
    sql = "INSERT INTO `secondtable` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
    connection.commit()


# In[6]:


# Execute query
sql = "SELECT * FROM `secondtable`"
cursor.execute(sql)

# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)


# In[ ]:




