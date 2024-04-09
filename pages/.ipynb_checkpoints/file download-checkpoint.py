import streamlit as st
import pandas as pd
import gridfs

from utils import get_data, get_all_data, put_data, init_connection


st.set_page_config(page_title="Capstone Project Tool", layout="centered") 

st.header("Download Files")

try:

    fs_report = gridfs.GridFS(st.session_state['db'], 'report')

    fs_poster = gridfs.GridFS(st.session_state['db'], 'poster')

    with st.container(border=True):
        opts = ["",'Mr. Olorunniwo', 'Mr. Aransiola', 'Dr. Obayiuwana', 'Dr. Yesufu', 'Dr. Ariyo', 'Dr. Ogunseye', 'Mr. Olayiwola', 'Dr. Ayodele', 'Dr. Ilori', 'Mr. Akinboboye', 'Dr. Olawole', 'Dr. Babalola', 'Dr. Ogunba', 'Dr. Fisusi', 'Dr. Jubril']

        assessor = st.selectbox('Assessor', options=opts, index=0, key='superd')

        # st.dataframe(get_all_data())

        data = pd.DataFrame(get_all_data())

        # data.where(data.Assessors.str.contains(assessor, regex=False, case=False)).dropna()._id

        matric_number = st.selectbox('Students in the group', options=[""]+list(data.where(data.Assessors.str.contains(assessor, regex=False, case=False)).dropna()._id))

        try:
            st.download_button('download poster', fs_poster.get(matric_number).read() if matric_number else "", mime='text/pdf', disabled=True if not matric_number else False, use_container_width=True, file_name=f'{matric_number}_poster.pdf')
        except:
            st.warning('The student you selected is yet to upload the requested file', icon="⚠️")

        try:
            st.download_button('download report', fs_report.get(matric_number).read() if matric_number else "", file_name=f'{matric_number}_report.pdf', mime='text/pdf', disabled=True if not matric_number else False, use_container_width=True)
        except:
            st.warning('The student you selected is yet to upload the requested file', icon="⚠️")
except:
    st.switch_page("information.py")