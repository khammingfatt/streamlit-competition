# C:\Users\LENOVO YOGA CORE I5\Documents
# streamlit run app.py

from connection import KaggleDatasetConnection
import streamlit as st

conn = st.experimental_connection("kaggle_datasets", type=KaggleDatasetConnection)
df = conn.get(path='katherinehudak/pokemon-gen-1-to-gen-9', filename='netflix_titles.csv', ttl=3600)
