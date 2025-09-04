{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 102,
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
   "execution_count": 114,
   "id": "c34e3351-840e-4c20-b01a-4a3a69ecc152",
   "metadata": {},
   "outputs": [],
   "source": [
    "def visualize(text):\n",
    "    we=WordCloud().generate(text)\n",
    "    plt.imshow(we)\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "90f5a398-03d5-4492-abf4-b3fbc05ec25c",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "We need at least 1 word to plot a word cloud, got 0.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[116], line 13\u001b[0m\n\u001b[0;32m     11\u001b[0m     soup\u001b[38;5;241m=\u001b[39mBeautifulSoup(response\u001b[38;5;241m.\u001b[39mtext)\n\u001b[0;32m     12\u001b[0m     text\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;241m.\u001b[39mjoin(c \u001b[38;5;28;01mfor\u001b[39;00m c \u001b[38;5;129;01min\u001b[39;00m soup\u001b[38;5;241m.\u001b[39mgettext() \u001b[38;5;28;01mif\u001b[39;00m (c\u001b[38;5;241m!=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m'\u001b[39m \u001b[38;5;129;01mand\u001b[39;00m c\u001b[38;5;241m.\u001b[39misalnum()))\n\u001b[1;32m---> 13\u001b[0m visualize(text)\n",
      "Cell \u001b[1;32mIn[114], line 2\u001b[0m, in \u001b[0;36mvisualize\u001b[1;34m(text)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mvisualize\u001b[39m(text):\n\u001b[1;32m----> 2\u001b[0m     we\u001b[38;5;241m=\u001b[39mWordCloud()\u001b[38;5;241m.\u001b[39mgenerate(text)\n\u001b[0;32m      3\u001b[0m     plt\u001b[38;5;241m.\u001b[39mimshow(we)\n\u001b[0;32m      4\u001b[0m     plt\u001b[38;5;241m.\u001b[39mshow()\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\wordcloud\\wordcloud.py:642\u001b[0m, in \u001b[0;36mWordCloud.generate\u001b[1;34m(self, text)\u001b[0m\n\u001b[0;32m    627\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mgenerate\u001b[39m(\u001b[38;5;28mself\u001b[39m, text):\n\u001b[0;32m    628\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Generate wordcloud from text.\u001b[39;00m\n\u001b[0;32m    629\u001b[0m \n\u001b[0;32m    630\u001b[0m \u001b[38;5;124;03m    The input \"text\" is expected to be a natural text. If you pass a sorted\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    640\u001b[0m \u001b[38;5;124;03m    self\u001b[39;00m\n\u001b[0;32m    641\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m--> 642\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mgenerate_from_text(text)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\wordcloud\\wordcloud.py:624\u001b[0m, in \u001b[0;36mWordCloud.generate_from_text\u001b[1;34m(self, text)\u001b[0m\n\u001b[0;32m    607\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"Generate wordcloud from text.\u001b[39;00m\n\u001b[0;32m    608\u001b[0m \n\u001b[0;32m    609\u001b[0m \u001b[38;5;124;03mThe input \"text\" is expected to be a natural text. If you pass a sorted\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    621\u001b[0m \u001b[38;5;124;03mself\u001b[39;00m\n\u001b[0;32m    622\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    623\u001b[0m words \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprocess_text(text)\n\u001b[1;32m--> 624\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mgenerate_from_frequencies(words)\n\u001b[0;32m    625\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\wordcloud\\wordcloud.py:410\u001b[0m, in \u001b[0;36mWordCloud.generate_from_frequencies\u001b[1;34m(self, frequencies, max_font_size)\u001b[0m\n\u001b[0;32m    408\u001b[0m frequencies \u001b[38;5;241m=\u001b[39m \u001b[38;5;28msorted\u001b[39m(frequencies\u001b[38;5;241m.\u001b[39mitems(), key\u001b[38;5;241m=\u001b[39mitemgetter(\u001b[38;5;241m1\u001b[39m), reverse\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n\u001b[0;32m    409\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(frequencies) \u001b[38;5;241m<\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0\u001b[39m:\n\u001b[1;32m--> 410\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWe need at least 1 word to plot a word cloud, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    411\u001b[0m                      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgot \u001b[39m\u001b[38;5;132;01m%d\u001b[39;00m\u001b[38;5;124m.\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m%\u001b[39m \u001b[38;5;28mlen\u001b[39m(frequencies))\n\u001b[0;32m    412\u001b[0m frequencies \u001b[38;5;241m=\u001b[39m frequencies[:\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mmax_words]\n\u001b[0;32m    414\u001b[0m \u001b[38;5;66;03m# largest entry will be 1\u001b[39;00m\n",
      "\u001b[1;31mValueError\u001b[0m: We need at least 1 word to plot a word cloud, got 0."
     ]
    }
   ],
   "source": [
    "text=''\n",
    "def read_from_pdf(iofile):\n",
    "    pdf=pdfplumber.open(iofile)\n",
    "    for page in pdf:\n",
    "        text+=page.extract_text()\n",
    "def read_from_doc(iofile):\n",
    "    doc=Document(iofile)\n",
    "    text=''.join([para.text for para in doc.paragrahps])\n",
    "def read_from_url(url):\n",
    "    response=requests.get(url)\n",
    "    soup=BeautifulSoup(response.text)\n",
    "    text=''.join(c for c in soup.gettext() if (c!='\\n' and c.isalnum()))\n",
    "visualize(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
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
    "        visualize(uset_text)\n",
    "        \n",
    "elif st.session_state.input_mode == \"file\":\n",
    "    uploaded_file = st.file_uploader(\"Upload a PDF or DOC file\", type=[\"pdf\", \"docx\"])\n",
    "    if uploaded_file:\n",
    "        st.success(f\"File uploaded: {uploaded_file.name}\")\n",
    "        iofile=io.BytesIO(uploaded_file.read())\n",
    "        if uploaded_file.endswith(\"pdf\"):\n",
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
   "execution_count": null,
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
