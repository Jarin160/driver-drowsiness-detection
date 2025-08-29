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




st.set_page_config(
   page_title="Resume Analyzer",
   page_icon='static/logo.jpg',
)

def run():
    img = Image.open('static/logo.jpg')
    st.image(img)
    st.title("Resume Analazer")

