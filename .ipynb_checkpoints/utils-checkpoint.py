import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# (kibtool) imachine@imachine:~$ mongosh "mongodb+srv://cluster0.lhxokzx.mongodb.net/" --apiVersion 1 --username bovenssolutions
# st.write(st.secrets["mongo"]["uri"])

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    # Create a new client and connect to the server
    return MongoClient(str(st.secrets["mongo"]["uri"]), server_api=ServerApi('1'))
    # return pymongo.MongoClient(**st.secrets["mongo"], authSource="admin")


# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
def get_data(uid):
    db = st.session_state['db']
    collection = st.session_state['collection']
    item = db[collection].find_one({'_id':uid})
    return item if item else {}

def get_all_data():
    db = st.session_state['db']
    collection = st.session_state['collection']
    
    items = db[collection].find({})#,{'_id':0})
    items = list(items)  # make hashable for st.cache_data
    return items if items else {}


# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
def put_data(uid, data):
    db = st.session_state['db']
    collection = st.session_state['collection']
    db[collection].replace_one({'_id':uid},data,True)


