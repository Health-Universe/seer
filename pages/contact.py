import streamlit as st

def main():
    st.title('⚕️ S.E.E.R: System for Efficient Encoding and Reference')

    image_filename = "dna-banner.jpg"
    
    st.image(image_filename, use_column_width=True)

    # Section: What is ICD
    st.header("What is ICD?")
    st.write("""
    The International Classification of Diseases (ICD) is a standardized system for 
    identifying and classifying diseases and health conditions globally.
    """)

    # Section: What is our project
    st.header("Insight behind SEER")
    st.write("""
    S.E.E.R is implemented as a web-based application built using Streamlit, a Python library for creating interactive web applications.

    It leverages MedSpaCy, a specialized medical text processing library, to analyze input medical documents and extract relevant ICD10 codes. The application provides users with a user-friendly interface to input medical text, search for specific terms, and generate ICD10 codes. It utilizes MedSpaCy's capabilities to highlight code-related content in the original text, ensuring accuracy and clarity.

    """)

    # Section: Contributors
    st.header("Contributors")

    # Create two columns
    col1, col2 = st.columns(2)

    # Contributor 1
    col1.write("[Arjun Raj](https://www.linkedin.com/in/arjun-raj-pala/)")

    # Contributor 2
    col2.write("[Akshaymon K](https://www.linkedin.com/in/akshaymonkvn3/)")


if __name__ == "__main__":
    main()
