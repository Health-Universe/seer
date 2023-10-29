


# Importing libraries

import pandas as pd
import streamlit as st
import spacy_streamlit
import spacy
from spacy import displacy
from PyPDF2 import PdfReader
import medspacy
from medspacy.ner import TargetRule
from medspacy.visualization import visualize_ent
from spacy_streamlit import visualize_parser


st.title('⚕️ S.E.E.R: System for Efficient Encoding and Reference')
uploaded_file = st.file_uploader("Choose a file")

# @st.cache(allow_output_mutation=True)
@st.cache_resource
def loading_ml_model(): 

  #problemlist=["allergies","asthma","diabetes"]
  #medilist=["Claritin","Zyrtec","Ortho Tri-Cyclen","Allegra"]

  #Getting disease list
  diseasedf = pd.read_csv('content/diseasedataset.csv')
  diseaselist = diseasedf['diseasename'].tolist()
  print("Completed loading disease dataset.")

  # Getting drug list
  drugdf = pd.read_csv('content/drugdataset.csv')
  druglist = drugdf['drugName'].tolist()
  dglist=[]

  # Here we are only using 2000 drugs names as input to maintain 
  for x in druglist[:2000]:
      dglist.append(x)
  print("Completed loading drug dataset.")

  
  # Load medspacy model

  nlp = medspacy.load()
  print(nlp.pipe_names)
  print("Started adding rules to nlp model..........")
  # Add rules for target concept extraction
  target_matcher = nlp.get_pipe("medspacy_target_matcher")
  for i in diseaselist:
    for j in dglist:
      target_rules = [
        TargetRule(i, "PROBLEM"),   
        TargetRule(j, "MEDICATION")
            ]
      target_matcher.add(target_rules)
  print("Completed making rules in nlp model")
  return nlp

def post_processing(doc):

    problem_label=[]
    medication_label=[]
    for ent in doc.ents:
        if ent.label_=='PROBLEM':
          problem_label.append(ent)
        if ent.label_=='MEDICATION':
          medication_label.append(ent) 
    print(problem_label)
    print(medication_label)
    prob_len=len(problem_label)
    med_len=len(medication_label)
    st.subheader("Summary:")
    st.write(f" Total number of identified diseases/problems in the file : {prob_len}")
    st.write(f" Total number of identified medications prescribed in the file : {med_len}")
    pass

if(uploaded_file is not None):
  reader = PdfReader(uploaded_file)
  print("Successfully read the file!")
  nlp=loading_ml_model()
  print("Completed loading the NLP model.")
  # st.markdown('**Successfully loaded NLP model.**')
  st.success('Successfully loaded the medspacy model.')
  if st.button('Extract'):
    st.subheader('Extracted Data:')
    st.info('The  first page of PDF is only considered for processing!')
   # st.markdown('Note: _The  first page of PDF is only considered for processing_!')
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text_data = page.extract_text()

    # Processing Data with nlp model

    doc = nlp(text_data)
    print("Extracted the data.")

    # Adding colors to the rules
    colors = {"PROBLEM": "orange", "MEDICATION": "green"}
    options = {"colors": colors}
    visualize_ent(doc)
    print("Starting visualization of the data....")

    # Visualization of extracted data
    html =displacy.render(doc, style="ent", page=True,options=options)
    st.components.v1.html(html, width=1000, height=1000, scrolling=True)
    print("Visualization Completed.")
    print("Calling post processing function")
    post_processing(doc)
     