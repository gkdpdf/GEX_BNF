
import time as t
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import time as tt
import seaborn as sns
import numpy as np

from pymongo.mongo_client import MongoClient

#replace username and pwd from mongodb atlas
uri = "mongodb+srv://readb:readb@cluster0.ay8hame.mongodb.net/?retryWrites=true&w=majority"


# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
st.set_page_config(layout="wide")

# create database 
mydb = client["GEX_BNF"]

#create collection
records =mydb['records']

ab=records.find()

df=pd.DataFrame(ab)


st.title(f"Summary of BankNifty GEX")
st.dataframe(df)

# Initial run
current_time = datetime.now().time()

# Auto-refresh every 10 seconds
while True and current_time <=tt(9,55) and current_time >=tt(3,55):
    t.sleep(100)
    # Initial run
    current_time = datetime.now().time()
    st.rerun()
