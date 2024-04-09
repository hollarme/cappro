import streamlit as st
import re
import gridfs

from utils import get_data


st.set_page_config(page_title="Capstone Project Tool", layout="wide") 

st.header("Files Upload")


try:
    
    fs_report = gridfs.GridFS(st.session_state['db'], 'report')

    fs_poster = gridfs.GridFS(st.session_state['db'], 'poster')

    placeholder = st.empty()

    with st.container(border=True):
        matric_number = st.text_input('Enter your matric number', placeholder='XXX/YYYY/ZZZ', max_chars=12, key='matricno')

        try:
            if matric_number:                
                placeholder.text(re.findall("[A-Z]{3}/[0-9]{4}/[0-9]{3}", matric_number)[0])
                placeholder.empty()
                
                get_data(matric_number)['Names']

                report = st.file_uploader('Upload report here (pdf only)', type='pdf', key='report')

                if report:
                    if fs_report.exists({"_id": matric_number}):
                        fs_report.delete(matric_number)
                    file_id = fs_report.put(report, _id=matric_number, filename=f'{matric_number}_report.pdf')

                try:
                    out_report = fs_report.get(matric_number)
                    st.write(out_report.filename, out_report.upload_date)
                except:
                    pass

                poster = st.file_uploader('Upload poster here (pdf only)', type='pdf', key='poster')

                if poster:
                    if fs_poster.exists({"_id": matric_number}):
                        fs_poster.delete(matric_number)
                    file_id = fs_poster.put(poster, _id=matric_number, filename=f'{matric_number}_poster.pdf')

                try:
                    out_poster = fs_poster.get(matric_number)
                    st.write(out_poster.filename, out_poster.upload_date)
                except:
                    pass

            else:
                st.info('You need to input your matric number to enable file upload!')

        except:
            st.warning('Make sure the matric number is correct and eligible', icon="⚠️")

except:
    st.switch_page("information.py")


