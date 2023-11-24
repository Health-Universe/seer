import streamlit as st

def main():
    st.title('⚕️ S.E.E.R: System for Efficient Encoding and Reference')

    button_a = st.button("Search for ICD Codes")
    button_b = st.button("Search for Symptoms")

    if button_a:
        expand_tile_a()

    if button_b:
        expand_tile_b()

def expand_tile_a():

    st.header("ICD Code Search")
    st.write("You can use the option to search for ICD Codes and identify the diseases")


    search_query = st.text_input("")

    # Add functionality here
    if st.button("Search"):
        perform_search_tile_a(search_query)

def expand_tile_b():
 
    st.header("Search for Symptoms")
    st.write("You can use the option to search for symtomps and identify the ICD Codes for it")

   
    search_query = st.text_input("")

    # Add functionality here
    if st.button("Search"):
        perform_search_tile_b(search_query)

def perform_search_tile_a(query):

    st.write(f"Searching for '{query}'")

def perform_search_tile_b(query):

    st.write(f"Searching for '{query}'")

if __name__ == "__main__":
    main()
