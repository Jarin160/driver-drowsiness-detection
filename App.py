import nltk
nltk.download('stopwords')

import streamlit as st
import pandas as pd
import base64,random
import time,datetime

from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter

import io
from streamlit_tags import st_tags
from PIL import Image
import pymysql




#DATABASE

connection = pymysql.connect(host='localhost',user='root',password='1802Jarin@160',db='Resume')
cursor = connection.cursor()

def insert_data(name,email,res_score,timestamp,no_of_pages,reco_field,cand_level,skills,recommended_skills,courses):
    DB_table_name = 'user_data'
    insert_sql = "insert into " + DB_table_name + """
    values (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    rec_values = (name, email, str(res_score), timestamp,str(no_of_pages), reco_field, cand_level, skills,recommended_skills,courses)
    cursor.execute(insert_sql, rec_values)
    connection.commit()

st.set_page_config(
   page_title="Resume Analyzer",
   page_icon='static/logo.jpg',
)

def run():
    img = Image.open('static/logo.jpg')
    st.image(img)
    st.title("Resume Analazer")
    st.sidebar.markdown('#Choose User')
    activities = ['User','Admin']
    choice = st.sidebar.selectbox("Choose among the given options:", activities)