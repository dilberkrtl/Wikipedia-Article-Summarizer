# Wikipedia Article Summarizer

Wikipedia Article Summarizer is a tool that automatically summarizes Wikipedia articles using Natural Language Processing (NLP) techniques. You can input any Wikipedia article URL, and the tool will fetch, clean, process, and summarize the content. It also provides useful statistics and visualizations to compare the article’s length before and after summarization.

## Features
- Article Summarization: Fetches the content from a given Wikipedia URL and generates a concise summary.
- Word Frequency Analysis: Calculates word frequencies and uses them to score sentences for better summarization.
- Text Cleaning: Removes irrelevant references, special characters, and extra spaces for better accuracy.
- Visualizations: Compares the character count of the original article vs. the summary with bar charts.
- Statistics: Provides insights on the number of sentences and characters before and after summarization.

## Usage
1.Clone the repository to your local machine:

git clone https://github.com/your-username/wikipedia-article-summarizer.git
cd wikipedia-article-summarizer

2.Run the summarizer script in your terminal or Jupyter notebook:
python summarizer.py

3.Enter the URL of any Wikipedia article when prompted. The tool will fetch the article, clean the content, process it, and generate a summary.

4.The summary will be printed on the screen along with useful statistics like:
- Number of sentences and characters before and after summarization.
- A bar chart comparing the character count.

## Streamlit Version (Web Interface)
There’s also a Streamlit version of the summarizer, which provides a more interactive web-based interface. You can run the app with the following command:

1.Install Streamlit if you don't have it:
pip install streamlit

2.Run the Streamlit app:
streamlit run app.py

3.Open your browser and navigate to http://localhost:8501 to use the summarizer.

## Streamlit App Interface

Here is a screenshot of the Streamlit application interface:

![streamlit_app_screenshot1](https://github.com/user-attachments/assets/35d576dd-3b91-4723-8d30-4d9e0164c0ef)
![streamlit_app_screenshot2](https://github.com/user-attachments/assets/6432ee45-28e2-4d1f-915e-8f4b617c1e8f)
![streamlit_app_screenshot3](https://github.com/user-attachments/assets/190e3952-7b7f-4ce4-ab1d-cc0187f5c743)


## How It Works
1.Fetching the Article: The tool fetches the article from Wikipedia by using the provided URL.
2.Cleaning the Content: It removes references, special characters, and extra spaces to clean the content.
3.Sentence Tokenization: The cleaned text is split into sentences.
4.Word Frequency Calculation: The tool calculates the frequency of each word in the article, excluding common stopwords.
5.Sentence Scoring: It scores sentences based on word frequencies, with higher scores for more important sentences.
6.Summary Generation: The highest-scoring sentences are selected to form a summary.
7.Statistics and Visualization: The application displays statistics and visualizes the difference in character count before and after summarization.

## Example
# Example 1: Running the script
Enter the URL of the Wikipedia article you want to summarize:
https://en.wikipedia.org/wiki/Turkey

## Summary:
Turkey is a country located at the crossroads of Europe and Asia. It has a rich cultural heritage and is home to numerous historical landmarks. The country has been a significant political and economic player in the region for centuries.

Text Statistics:
Number of sentences before summarization: 35
Number of characters before summarization: 3500
Number of sentences in the summary: 5
Number of characters in the summary: 550
Example 2: Streamlit Interface
The web interface will prompt you for a URL, and the summary and statistics will be displayed in a user-friendly format.

Dependencies
The following libraries are required to run the summarizer:

- nltk: For Natural Language Processing tasks (tokenization, stopwords).
- beautifulsoup4: For web scraping the Wikipedia article.
- requests: For sending HTTP requests to fetch the article.
- lxml: For HTML parsing.
- matplotlib: For creating visualizations (e.g., character count comparison).
- streamlit: For the web interface version.

## Contribution
Feel free to fork the repository, submit pull requests, and open issues. Contributions to improve the tool’s functionality, UI, or performance are welcome.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- NLTK: The Natural Language Toolkit used for text processing and stopwords.
- BeautifulSoup: For parsing and extracting content from Wikipedia.
- Streamlit: For providing an easy-to-use web framework for deployment.
