# Arabic Sentiment Preprocessing

This repository contains scripts for preprocessing Arabic sentiment datasets, including text cleaning, tokenization, feature extraction, and retweet network analysis.

## Project Structure
Arabic-Sentiment-Preprocessing/ │── data/ # Raw and cleaned datasets │── notebooks/ # Jupyter Notebooks │── scripts/ # Python preprocessing scripts │── README.md # Project documentation │── requirements.txt # Dependencies │── .gitignore # Ignore unnecessary files


## Setup
1. Clone the repository:

git clone https://github.com/yourusername/Arabic-Sentiment-Preprocessing.git cd Arabic-Sentiment-Preprocessing

2. Install dependencies:
pip install -r requirements.txt

3. Run preprocessing:
python scripts/text_cleaning.py python scripts/tokenization.py python scripts/ngram_analysis.py python scripts/network_analysis.p


## Acknowledgments
This project was part of my research under Prof.Hala Mulki at Ortadoğu Araştırmaları Merkezi - ORSAM. It was a preprocessing and data analysis task for a research designed to improve sentiment classification using deep learning models. For more information read the paper i wrote on my internship under the docs folder. 

5. requirements.txt
pandas
numpy
nltk
matplotlib
seaborn
wordcloud
networkx
farasa
