{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "041937dc-6a4c-4c81-9154-96d9e8292c2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pdfplumber\n",
    "import matplotlib.pyplot as plt\n",
    "from wordcloud import WordCloud\n",
    "from docx import Document\n",
    "from textblob import TextBlob\n",
    "from bs4 import BeautifulSoup\n",
    "import io\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "c34e3351-840e-4c20-b01a-4a3a69ecc152",
   "metadata": {},
   "outputs": [],
   "source": [
    "def visualize(text):\n",
    "    we=WordCloud().generate(text)\n",
    "    plt.imshow(we)\n",
    "    st.pyplot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "90f5a398-03d5-4492-abf4-b3fbc05ec25c",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unindent does not match any outer indentation level (<string>, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m<string>:6\u001b[1;36m\u001b[0m\n\u001b[1;33m    visualize(text)\u001b[0m\n\u001b[1;37m                   ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unindent does not match any outer indentation level\n"
     ]
    }
   ],
   "source": [
    "text=''\n",
    "def read_from_pdf(iofile):\n",
    "    pdf=pdfplumber.open(iofile)\n",
    "    for page in pdf:\n",
    "        text+=page.extract_text()\n",
    "     visualize(text)\n",
    "def read_from_doc(iofile):\n",
    "    doc=Document(iofile)\n",
    "    text=''.join([para.text for para in doc.paragraphs])\n",
    "    visualize(text)\n",
    "def read_from_url(url):\n",
    "    response=requests.get(url)\n",
    "    soup=BeautifulSoup(response.text)\n",
    "    text=''.join(c for c in soup.gettext() if (c!='\\n' and c.isalnum()))\n",
    "    visualize(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "f50ce9bc-b4d1-4685-bd3c-3c33c13bc58b",
   "metadata": {},
   "outputs": [],
   "source": [
    "if \"input_mode\" not in st.session_state:\n",
    "    st.session_state.input_mode=None\n",
    "button1,button2,button3=st.columns(3)\n",
    "with button1:\n",
    "    if st.button(\"text mode\"):\n",
    "        st.session_state.input_mode=\"text\"\n",
    "with button2:\n",
    "    if st.button(\"file mode\"):\n",
    "        st.session_state.input_mode=\"file\"\n",
    "with button3:\n",
    "    if st.button(\"URL mode\"):\n",
    "        st.session_state.input_mode=\"url\"\n",
    "if st.session_state.input_mode == \"text\":\n",
    "    user_text = st.text_area(\"Enter your text below:\")\n",
    "    if user_text:\n",
    "        visualize(user_text)\n",
    "        \n",
    "elif st.session_state.input_mode == \"file\":\n",
    "    uploaded_file = st.file_uploader(\"Upload a PDF or DOC file\", type=[\"pdf\", \"docx\"])\n",
    "    if uploaded_file:\n",
    "        st.success(f\"File uploaded: {uploaded_file.name}\")\n",
    "        iofile=io.BytesIO(uploaded_file.read())\n",
    "        if uploaded_file.endswith(\".pdf\"):\n",
    "            read_from_pdf(iofile)\n",
    "        else:\n",
    "            read_from_doc(iofile)\n",
    "\n",
    "elif st.session_state.input_mode == \"url\":\n",
    "    url_input = st.text_input(\"Paste your URL here:\")\n",
    "    if url_input:\n",
    "        st.success(\"URL received!\")\n",
    "        st.write(f\"You entered: {url_input}\")\n",
    "        read_from_url(url_input)\n",
    "        # You can add logic here to fetch and process the URL content\n"
   ]
  },
  {
   "cell_type": "code",
   "id": "fe3d7483-0091-4d91-91a8-b61b24bc8183",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
