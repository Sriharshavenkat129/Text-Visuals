import streamlit as st
import pdfplumber
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from docx import Document
from textblob import TextBlob
from bs4 import BeautifulSoup
import io
import requests

# Global text variable
text = ''

# WordCloud visualization
def visualize(text):
    we=WordCloud().generate(text)
    plt.imshow(we)
    st.pyplot()

# Read from PDF
def read_from_pdf(iofile):
    global text
    text = ''
    with pdfplumber.open(iofile) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    visualize(text)

# Read from DOCX
def read_from_doc(iofile):
    global text
    text = ''
    doc = Document(iofile)
    text = ''.join([para.text for para in doc.paragraphs])
    visualize(text)

# Read from URL
def read_from_url(url):
    global text
    text = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    raw_text = soup.get_text()
    text = ''.join(c for c in raw_text if c != '\n' and (c.isalnum() or c.isspace()))
    visualize(text)

# Streamlit UI
st.title("🧠 WordCloud Generator")
st.write("Choose your input mode to generate a word cloud from text, file, or URL.")

if "input_mode" not in st.session_state:
    st.session_state.input_mode = None

button1, button2, button3 = st.columns(3)
with button1:
    if st.button("Text Mode"):
        st.session_state.input_mode = "text"
with button2:
    if st.button("File Mode"):
        st.session_state.input_mode = "file"
with button3:
    if st.button("URL Mode"):
        st.session_state.input_mode = "url"

# Text Mode
if st.session_state.input_mode == "text":
    user_text = st.text_area("Enter your text below:")
    if user_text:
        visualize(user_text)

# File Mode
elif st.session_state.input_mode == "file":
    uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])
    if uploaded_file:
        st.success(f"File uploaded: {uploaded_file.name}")
        iofile = io.BytesIO(uploaded_file.read())
        if uploaded_file.name.endswith(".pdf"):
            read_from_pdf(iofile)
        elif uploaded_file.name.endswith(".docx"):
            read_from_doc(iofile)

# URL Mode
elif st.session_state.input_mode == "url":
    url_input = st.text_input("Paste your URL here:")
    if url_input:
        st.success("URL received!")
        st.write(f"You entered: {url_input}")
        read_from_url(url_input)
