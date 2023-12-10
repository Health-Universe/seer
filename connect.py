import streamlit as st
import pymongo
import pandas as pd
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient


@st.cache_resource
def init_connection():
    pwd=st.secrets["db_password"]
    username=st.secrets["db_username"]
    host=st.secrets["db_host"]
    uri = f"mongodb+srv://{username}:{pwd}@{host}/?retryWrites=true&w=majority"
    return pymongo.MongoClient(uri, server_api=ServerApi('1'))
client = init_connection()
collection_name = "icd10_codes"

# Function to load the database. One time operation.
def load_database():
    # Read the CSV file into a DataFrame
    icdData = pd.read_csv('Resources/ICD10-Data/icd10_data.csv')
    db = client.icd10_data
    items = db.icd10_codes.find()
    # Insert the DataFrame records into the MongoDB collection
    db['icd10_codes'].insert_many(icdData.to_dict(orient='records'))

# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    db = client.icd10_data
    items = db.icd10_codes.find()
    items = list(items)  # make hashable for st.cache_data
    return items

items = get_data()

# Function to search across all records in ICD10 database.
def searchICD(search_term):
    db = client.icd10_data
    collection = db['icd10_codes']
    query = {"Description": {"$regex": search_term, "$options": "i"}}
    # Perform the search
    results = collection.find(query)
    return results


search_term = st.text_input("Enter search term:")  
if search_term:
    # Perform search and display results
    results = searchICD(search_term)
    # Convert results to a DataFrame for better display
    df_results = pd.DataFrame(list(results))
    st.subheader("Search Results:")
    st.table(df_results[["ICD10_Code", "Description"]])
    # for result in results:
    #     st.write(result)

st.write(items)