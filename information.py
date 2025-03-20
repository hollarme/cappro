import streamlit as st

from utils import get_data, get_all_data, put_data, init_connection

st.set_page_config(page_title="Capstone Project Tool", layout="wide") 

if 'client' not in st.session_state:
    st.session_state['client'] = init_connection()
    
if 'db' not in st.session_state:
    st.session_state['db'] = st.session_state['client'].capstoneDB_2324

# if 'collection' not in st.session_state:
#     st.session_state['collection'] = 'title_information_form'
    
if 'collection' not in st.session_state:
    st.session_state['collection'] = 'mapper'#'student_staff_map'

st.header("Information Board")

with st.container(border=True):

    st.markdown("""
    ## General Information:
    
    - Please be aware that :red[EEE501 defense] for the 2023/2024 academic session will take place on :red[Tuesday $25^{th}$ and Wednesday $26^{th}$] of the month of March 2025
    - You will also need to write a concise report (3 to 5 pages) on your work (see the link to the report template below)
    - Submit your report with file upload menu, on or before :red[midnight Saturday $22^{nd}$ of March 2025].
    - Come with a printed copy of your report to the defence session
    
    ## Material Links:
    
    - This is the link to the report template: https://drive.google.com/file/d/1yLS-4gloZyNICn6eAJjDnM-AdGSjKSes/view?usp=sharing
    - You might need to compile the latex output with TexMaker (https://www.xm1math.net/texmaker/) or any other tool you are comfortable with

    """)

   