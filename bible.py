import pandas as pd
import streamlit as st
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

# Streamlit title
st.title("Word Frequency in the Bible")

try:
    data = pd.read_csv('bible_data_set.csv')  # Ensure the path is correct
    st.success("Dataset loaded successfully!")
except FileNotFoundError:
    st.error("Dataset not found. Please ensure 'dataset/bible_data_set.csv' exists.")
    st.stop()

# Preprocessing function
lem = WordNetLemmatizer()
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [lem.lemmatize(word) for word in words]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

st.text("Preprocessing the dataset...")
data['processed_text'] = data['text'].apply(preprocess)
preprocessed_text = ' '.join(data['processed_text'])

target_word = st.text_input("Enter the word you want to count:")

if target_word:
    count = preprocessed_text.lower().split().count(target_word.lower())
    st.write(f"The word **'{target_word}'** appears **{count} times** in the dataset.")
else:
    st.warning("Please enter a word to count.")


#sub-dataset of actual dataset to collect releveant information
mining_data = data[['citation', 'text']]

for index, row in mining_data.iterrows():
    citation = row['citation']
    text = row['text']
    
    # Check for the target word in the text
    words = [word for word in text.lower().split() if word == target_word]
    
    # If target word is found, print or process
    if words:
        st.write(f"**Citation:** {citation}")
        st.write(f"**Text:** {text}")
        st.write("---")  # Add a separator for better readability
