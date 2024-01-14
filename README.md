# S.E.E.R: System for Efficient Encoding and Reference

Welcome to [S.E.E.R](https://whatismyicdcode.streamlit.app/), your ally in healthcare documentation! 🌟 

This web-based application simplifies the complex world of ICD codes and symptom types, making it easily accessible with just a few clicks.

## What is ICD? 🤷

Ever wondered how doctors and healthcare professionals universally identify and classify diseases? Enter the International Classification of Diseases (ICD). It's like a global dictionary for health issues, ensuring a common understanding of illnesses worldwide.

## Idea behind S.E.E.R 💡💡💡

S.E.E.R is designed to simplify the lives of doctors and medical coders, making the complex world of ICD codes and symptom types easily accessible. It's not just a system; it's your ally in healthcare documentation.

## What exactly is S.E.E.R 🧑‍💻️

S.E.E.R is a web-based application built with Streamlit, the magic wand of interactive web development in Python. We've incorporated MedSpaCy, a specialized medical text processing library, to analyze medical text, extract ICD10 codes, and provide a friendly interface for effortless code searching.

## How it works 🏋
> The live site can be accessed via [S.E.E.R](https://whatismyicdcode.streamlit.app/)
1. Input your medical text 🔠.
2. S.E.E.R analyzes the document with MedSpaCy.
3. It extracts ICD10 codes and highlights code-related bits in the original text.
4. Effortlessly search for specific terms and navigate the medical coding landscape.

It's not just about accuracy; it's about clarity and making your job easier. With S.E.E.R, healthcare tech becomes a breeze.

## Installation

Use the following commands to install the required dependencies and run the application locally.

```bash
pip install -r requirements.txt
streamlit run seer.py

```
# Screenshots
![Seer  ICD10 Code generator](https://github.com/ArjunRAj77/seer/assets/23217592/f8c2042c-ae51-4b58-9db1-2824437340e9)

![Seer  ICD10 Code generator (1)](https://github.com/ArjunRAj77/seer/assets/23217592/5f4451a2-26ec-4c35-aedb-c44352c80171)
![Seer  ICD10 Code generator (2)](https://github.com/ArjunRAj77/seer/assets/23217592/1b43563e-6617-4bd9-9aa7-2ae8de34bf7b)

![Seer  ICD10 Code generator (3)](https://github.com/ArjunRAj77/seer/assets/23217592/50fa793e-2b86-4c16-ab07-4825a1b19fc8)
![Seer  ICD10 Code generator (4)](https://github.com/ArjunRAj77/seer/assets/23217592/6d0f06bf-ca09-45c7-8dad-8fb464b8b29c)
![Seer  ICD10 Code generator (5)](https://github.com/ArjunRAj77/seer/assets/23217592/4ddec96b-a54c-49d6-86bd-70a15fd603c8)
![Seer  ICD10 Code generator (6)](https://github.com/ArjunRAj77/seer/assets/23217592/396606d8-0d57-4930-a545-99af193f3347)
![Seer  ICD10 Code generator (7)](https://github.com/ArjunRAj77/seer/assets/23217592/8656b0a7-d850-4a80-993a-127e98d161f1)





# Resources

- A sample data set for reference is being used : [Charmhealth Hackathon Resource Files](https://workdrive.zohoexternal.com/external/f5c821ad2d5bf1245b2110efe1c66a2cb3db7aa4f4bd0a7dbcb617cd61c8b20e?layout=list)
- [ICD 10 Codes](https://www.cms.gov/medicare/coding-billing/icd-10-codes/2023-icd-10-cm)
- [Medspacy Modules](https://github.com/medspacy/medspacy)
