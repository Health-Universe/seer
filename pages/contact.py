import streamlit as st
st.set_page_config(page_title="S.E.E.R", page_icon="⚕️")
def main():
    st.title('⚕️ S.E.E.R: System for Efficient Encoding and Reference')



    # Section: What is ICD
    st.header("What is ICD?  🤷")
    st.write("""Ever wondered how doctors🧑‍⚕️ and healthcare professionals universally identify and classify diseases?
                Enter the International Classification of Diseases (ICD) 📕. It's like a global dictionary for health issues, 
                helping everyone speak the same language when it comes to illnesses.
    """)
    st.write("""Whether you're in New York🗽 or Tokyo🗼, the ICD
                ensures that a specific condition is understood the same way worldwide. So, it's not just a code; it's the key to
                a common understanding of health concerns across borders ✅.
    """)

    # Section: What is our project
    st.header("Idea behind S.E.E.R 💡💡💡")
    st.write("""Imagine a tool designed to simplify the lives of doctors and medical coders,
                making the complex world of ICD codes and symptom types easily accessible with just a few clicks. 
                That's exactly what we've created with Seer! 🌟 Seer is not just a system; it's your ally in healthcare
                documentation. 

    """)

    st.header("What exactly is S.E.E.R 🧑‍💻️")
    st.write("""Picture this: A web-based application built with Streamlit, the magic wand 🧙 of interactive 
                web development in Python. We wanted to make the whole process smoother, so we incorporated MedSpaCy⚕️, a 
                specialized medical text processing library, into Seer. How does it work? You input your medical text🔠, and 
                Seer does the heavy lifting🏋. It analyzes the document, sifts through the jargon, and extracts those elusive 
                ICD10 codes🏆. But we didn't stop there—Seer also gives you a friendly interface to search for specific terms 
                and effortlessly search ICD10 codes. And here's the cherry on top: Seer uses MedSpaCy to highlight those 
                crucial code-related bits in the original text. It's not just about accuracy; it's about clarity and making your
                job easier. With Seer, navigating the medical coding landscape becomes a breeze. Because your time⌛ is precious,
                and we believe healthcare tech should be, too!❤️""")

    # Section: Contributors
    st.markdown("**Contributors 🧑‍🔧️:**")

    # Create two columns
    col2, col3 = st.columns(2)

    # Contributor 2
    col2.markdown("Arjun Raj [🪡](https://www.linkedin.com/in/arjun-raj-pala/)  [🐙](https://github.com/ArjunRAj77)")

    col3.markdown("Akshaymon K V[🪡](https://www.linkedin.com/in/akshaymonkvn3/) [🐙](https://github.com/Akshaymonkv)")


if __name__ == "__main__":
    main()
