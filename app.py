import streamlit as st
import matplotlib.pyplot as plt
import bs4 as bs
import urllib.request
import re
import nltk
import heapq
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

# Update NLTK data paths to avoid issues with missing resources
nltk.data.path.append(r"C:/Users/MSI-NB/AppData/Roaming/nltk_data")
nltk.download('punkt')
nltk.download('stopwords')

# Page configuration for the Streamlit app
st.set_page_config(page_title="Wikipedia Article Summarizer", page_icon="📝", layout="wide")

# Set the title and description of the app
st.title("Wikipedia Article Summarizer")
st.markdown("""
This tool summarizes the text of the Wikipedia article you provide.
Simply enter the URL of the article.
""")

# Input field for the URL of the Wikipedia article
url = st.text_input("Enter the URL of the Wikipedia article you want to summarize:")

# If URL is provided, start summarizing
if url:
    try:
        # Fetch the article data from the URL
        scraped_data = urllib.request.urlopen(url)
        article = scraped_data.read().decode('utf-8')

        # Parse the HTML content using BeautifulSoup
        parsed_article = bs.BeautifulSoup(article, 'lxml', from_encoding="utf-8")
        
        # Extract paragraphs from the article
        paragraphs = parsed_article.find_all('p')
        article_text = ""
        for p in paragraphs:
            article_text += p.text  # Append the text of each paragraph

        # Clean the text (remove references and normalize spaces)
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  # Remove references
        article_text = re.sub(r'\s+', ' ', article_text)  # Remove extra spaces
        formatted_article_text = re.sub('[^a-zA-ZçğıöşüÇĞİÖŞÜ]', ' ', article_text)  # Keep only alphabetic characters
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)  # Normalize spaces

        # Split the cleaned article into sentences
        sentence_list = re.split(r'(?<=[.!?]) +', formatted_article_text)

        # Load English stopwords from NLTK
        stop_words = set(stopwords.words('english'))

        # Calculate word frequencies excluding stopwords and non-alphabetic characters
        word_frequencies = {}
        for sentence in sentence_list:
            for word in sentence.split():
                word = word.lower()
                if word not in stop_words and word.isalpha():
                    word_frequencies[word] = word_frequencies.get(word, 0) + 1

        # Find the highest frequency word for normalization
        max_frequency = max(word_frequencies.values())

        # Normalize word frequencies
        for word in word_frequencies:
            word_frequencies[word] = (word_frequencies[word] / max_frequency)

        # Calculate sentence scores based on word frequencies
        sentence_scores = {}
        for sentence in sentence_list:
            sentence_score = 0
            for word in sentence.split():
                word = word.lower()
                if word in word_frequencies:
                    sentence_score += word_frequencies[word]  # Add word frequency to sentence score
            sentence_scores[sentence] = sentence_score

        # Select the top 7 sentences with the highest scores to form the summary
        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

        # Create the summary
        summary = ' '.join(summary_sentences)

        # Statistics (Comparison of the text before and after summarization)
        original_sentence_count = len(sentence_list)
        original_character_count = len(article_text)
        summary_sentence_count = len(summary_sentences)
        summary_character_count = len(summary)

        # Display the summary and statistics in the Streamlit app
        st.subheader('Article Summary:')
        st.write(summary)

        st.subheader('Text Statistics:')
        st.write(f"Number of sentences before summarization: {original_sentence_count}")
        st.write(f"Number of characters before summarization: {original_character_count}")
        st.write(f"Number of sentences in the summary: {summary_sentence_count}")
        st.write(f"Number of characters in the summary: {summary_character_count}")

        # Display a bar chart to compare the character count before and after summarization
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        ax2.bar(['Before Summarization', 'After Summarization'],
                [original_character_count, summary_character_count], color=['#1f77b4', '#ff7f0e'])
        ax2.set_ylabel('Character Count', fontsize=12)
        ax2.set_title('Character Count Comparison Before and After Summarization', fontsize=14)
        ax2.set_ylim(0, max(original_character_count, summary_character_count) * 1.1)

        st.pyplot(fig2)

    except Exception as e:
        # Display an error message if something goes wrong
        st.error(f"An error occurred: {e}")