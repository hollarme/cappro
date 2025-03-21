import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
import re

from utils import get_data, get_all_data, put_data, init_connection

st.set_page_config(page_title="Capstone Project Tool", layout="wide") 

# try:
placeholder = st.empty()

with st.status("", expanded=True) as status:
    col1, col2 = st.columns([0.7,0.3])

    with col1:
        st.title("Capstone Project Information Form")

        # with st.form('info_form'):
        with st.container(border=True):
            matric_number = st.text_input('Enter your matric number', placeholder='XXX/YYYY/ZZZ', max_chars=12, key='matric')

            try:
                if matric_number:
                    placeholder.text(re.findall("[A-Z]{3}/[0-9]{4}/[0-9]{3}", matric_number)[0])
                    placeholder.empty()

                full_name = st.text_input('Enter your full name (surname first)', value="" if not matric_number else get_data(matric_number).get('Names', ""), key='full')

                title = st.text_input('Enter the title of your project work', value="" if not matric_number else get_data(matric_number).get('Title', ""), key='title')

                opts = ["",'Mr. O. Olorunniwo', 'Dr. A. Aransiola', 'Dr. E. Obayiuawana', 'Prof. T. K. Yesufu', 'Dr. F. K. Ariyo', 'Dr. A. A. Ogunseye', 'Mr. Olayiwola Pipelolu', 'Dr. K. P. Ayodele', 'Dr. O. Ilori', 'Mr. E. Akinboboye', 'Dr. A. A. Olawole', 'Dr. A. A. Fisusi', 'Dr. A. M. Jubril']

                supervisor = st.selectbox('Who is your supervisor?', options=opts, index=0 if not matric_number else opts.index(get_data(matric_number).get('Supervisor', "").title().strip()), key='super')

                option = get_data(matric_number).get('Option', "")
                group = get_data(matric_number).get('Group', "")
                st.caption(f'Your defence group is: :red[{group}]')
                assessors = get_data(matric_number).get('Assessors', "")
                st.caption(f'Your assessors are: :red[{assessors}]')

                readiness = st.slider('How ready are you for a presentation?', min_value=0.0, max_value=10.0, value=0.0 if not matric_number else float(get_data(matric_number).get('Readiness', 0.0)), key='read')

                # submitted = st.form_submit_button("Submit")
                submitted = st.button("Submit")

                if submitted:
                    if not all([matric_number=="", full_name=="", title=="", supervisor==""]):
                        put_data(matric_number, {"_id": matric_number, "Title": title, "Names": full_name, "Supervisor": supervisor, "Option": option, "Group": group, "Assessors": assessors, "Readiness": readiness})
                        status.update(label="upload complete!", state="complete")
                    else:
                        st.warning('Make sure all the fields are properly filled', icon="⚠️")
                        status.update(label="upload not complete!", state="error")

            except:
                st.warning('Make sure the matric number is correct', icon="⚠️")


    with col2:  
        st.title("Readiness at a glance!")
        arr = []

        for x in get_all_data():
            arr.append(x.get('Readiness', 0))

        fig, ax = plt.subplots()
        ax.hist(arr, bins=11, align='mid')

        st.pyplot(fig)

# except:
#     st.switch_page("information.py")