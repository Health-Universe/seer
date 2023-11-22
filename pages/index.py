import streamlit as st

def main():
    st.title('⚕️ S.E.E.R: System for Efficient Encoding and Reference')


    selected_tile = st.sidebar.radio("Select Tile", ['Search for ICD Codes', 'Search for Symptoms'])


    if selected_tile == 'Search for ICD Codes':
        st.header("ICD Code search")
        expand_tile_a()
    elif selected_tile == 'Search for Symptoms':
        st.header("Symptoms type search")
        expand_tile_b()

def expand_tile_a():
    st.write("You can use the option to search for ICD Codes and identify the diseases")

    if st.button("Enter Code"):
        show_search_bar('A')

def expand_tile_b():
    st.write("You can use the option to search for symtomps and identify the ICD Codes for it")

    if st.button("Enter Symptoms"):
        show_search_bar('B')

def show_search_bar(tile):
    search_query = st.text_input(f"Search", "")


    if st.button(f"Search"):
        st.write(f"Searching for '{search_query}' in Tile {tile}")

if __name__ == "__main__":
    main()