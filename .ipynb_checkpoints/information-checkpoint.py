import streamlit as st

from utils import get_data, get_all_data, put_data, init_connection

st.set_page_config(page_title="Capstone Project Tool", layout="wide") 

if 'client' not in st.session_state:
    st.session_state['client'] = init_connection()
    
if 'db' not in st.session_state:
    st.session_state['db'] = st.session_state['client'].capstoneDB

# if 'collection' not in st.session_state:
#     st.session_state['collection'] = 'title_information_form'
    
if 'collection' not in st.session_state:
    st.session_state['collection'] = 'mapper'#'student_staff_map'

st.header("Information Board")

with st.container(border=True):

    st.markdown("""
    ## General Information:
    
    - Please be aware that :red[EEE501 defense] for the 2022/2023 academic session will take place on :red[Tuesday $16^{th}$ and Wednesday $17^{th}$] of the month of April 2024
    - It shall take the form of a poster presentation (see the poster template below) where the assessors and guests will have the chance to interact with the presenters
    - You will also need to write a concise report (3 to 5 pages) on your work (see the report link below)
    - Both the report and the poster are to be submitted with file upload menu, on or before :red[midnight Thursday $11^{th}$ of April 2024].
    - Each poster presentation transaction between an assessor and the student should not take more than :red[10 minutes]: :blue[5 minutes for the presentation] and :green[5 minutes for questions and answers]
    - You are required to print the poster on an A1 paper
    
    ## Material Links:
    
    - This is the link to the poster template (look for the poster named: :red[Kensington.pptx]): https://www.posterpresentations.com/free-poster-templates.html
    - This is the link to the report template: https://drive.google.com/file/d/1yLS-4gloZyNICn6eAJjDnM-AdGSjKSes/view?usp=sharing
    - You might need to compile the latex output with TexMaker (https://www.xm1math.net/texmaker/) or any other tool you are comfortable with

    ## Poster Presentation How-to: 
    
    - https://www.youtube.com/watch?v=vMSaFUrk-FA
    - https://www.youtube.com/watch?v=r0ezNEDWAiE
    """)

   