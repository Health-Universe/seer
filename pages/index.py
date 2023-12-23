import streamlit as st
import pymongo
import pandas as pd

@st.cache_resource
def init_connection():
    pwd = st.secrets["db_password"]
    username = st.secrets["db_username"]
    host = st.secrets["db_host"]
    uri = f"mongodb+srv://{username}:{pwd}@{host}/?retryWrites=true&w=majority"
    return pymongo.MongoClient(uri)

def get_collection(collection_name):
    db = client.icd10_data
    return db[collection_name]

client = init_connection()
collection_name = "icd10_codes"

def main():
    st.title('⚕️ S.E.E.R: System for Efficient Encoding and Reference')

    button_a = st.button("Search for ICD Codes", key="button_a")
    button_b = st.button("Search for Symptoms", key="button_b")

    if button_a:
        expand_tile_a()

    if button_b:
        expand_tile_b()

def expand_tile_a():
    st.header("ICD Code Search")
    st.write("You can use the option to search for ICD Codes and identify the diseases")

    search_query = st.text_input("Enter your search query")

    # Add functionality here
    if st.button("Search") and search_query:  # Check if search query is not empty
        results = perform_search_tile_a(search_query)
        # Convert results to a DataFrame for better display
        df_results = pd.DataFrame(list(results))
        st.subheader("Search Results:")
        st.table(df_results[["ICD10_Code", "Description"]])

def expand_tile_b():
    st.header("Search for Symptoms")
    st.write("You can use the option to search for symptoms and identify the ICD Codes for it")

    search_query = st.text_input("Enter your search query")  # Provide a label here

    # Add functionality here
    if st.button("Search") and search_query:  # Check if search query is not empty
        results = perform_search_tile_b(search_query)
        # Convert results to a DataFrame for better display
        df_results = pd.DataFrame(list(results))
        st.subheader("Search Results:")
        st.table(df_results[["ICD10_Code", "Description"]])

def perform_search_tile_a(search_query):
    collection = get_collection(collection_name)
    query = {"Description": {"$regex": search_query, "$options": "i"}}
    # Perform the search
    results = collection.find(query)
    return results

def perform_search_tile_b(search_query):
    collection = get_collection(collection_name)
    query = {"Description": {"$regex": search_query, "$options": "i"}}
    # Perform the search
    results = collection.find(query)
    return results

if __name__ == "__main__":
    main()
