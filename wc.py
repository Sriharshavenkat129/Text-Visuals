import streamlit as st
import pdfplumber
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from docx import Document
from bs4 import BeautifulSoup
import io
import requests

def visualize(text):
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)

def read_from_pdf(iofile):
    with pdfplumber.open(iofile) as pdf:
        return "\n".join(page.extract_text() or '' for page in pdf.pages)

def read_from_doc(iofile):
    doc = Document(iofile)
    return "\n".join(para.text for para in doc.paragraphs)

def read_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    raw_text = soup.get_text()
    return ''.join(c for c in raw_text if c != '\n' and (c.isalnum() or c.isspace()))

def main():
    st.title("🧠 WordCloud Generator")
    st.write("Choose your input mode to generate a word cloud from text, file, or URL.")

    # Initialize session state safely
    if "input_mode" not in st.session_state:
        st.session_state["input_mode"] = None
    if "vmode" not in st.session_state:
        st.session_state["vmode"] = None
    if "text_data" not in st.session_state:
        st.session_state["text_data"] = ""

    # Input mode buttons
    button1, button2, button3 = st.columns(3)
    with button1:
        if st.button("Text Mode"):
            st.session_state["input_mode"] = "text"
    with button2:
        if st.button("File Mode"):
            st.session_state["input_mode"] = "file"
    with button3:
        if st.button("URL Mode"):
            st.session_state["input_mode"] = "url"

    # Input handling
    if st.session_state["input_mode"] == "text":
        user_text = st.text_area("Enter your text below:")
        if user_text:
            st.session_state["text_data"] = user_text

    elif st.session_state["input_mode"] == "file":
        uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])
        if uploaded_file:
            iofile = io.BytesIO(uploaded_file.read())
            if uploaded_file.name.endswith(".pdf"):
                st.session_state["text_data"] = read_from_pdf(iofile)
            elif uploaded_file.name.endswith(".docx"):
                st.session_state["text_data"] = read_from_doc(iofile)

    elif st.session_state["input_mode"] == "url":
        url_input = st.text_input("Paste your URL here:")
        if url_input:
            st.session_state["text_data"] = read_from_url(url_input)

    # WordCloud trigger
    if st.button("Generate WordCloud"):
        st.session_state["vmode"] = "wc"

    # Display WordCloud
    if st.session_state["vmode"] == "wc" and st.session_state["text_data"]:
        visualize(st.session_state["text_data"])

# Run the app
if __name__ == "__main__":
    main()
