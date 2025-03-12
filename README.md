# Arabic Sentiment Preprocessing  

This repository contains Python scripts for **preprocessing Arabic sentiment datasets**, focusing on text cleaning, tokenization, feature extraction, and retweet network analysis. The goal is to enhance data quality for **sentiment classification models**, particularly **Convolutional Neural Networks (CNNs)** trained on word embeddings (GloVe, Skip-Gram, CBOW).  

This project was part of my **research internship under Prof. Hala Mulki** at **Ortadoğu Araştırmaları Merkezi - ORSAM**. My primary contribution was **data preprocessing and analysis**, ensuring the dataset was optimized for deep learning-based sentiment classification.  

📄 **Read the research paper of my Supervisor for Context:** [docs/Empirical-Evaluation-of-Word-Representations-on-Arabic-Sentiment-Analysis.pdf](docs/Empirical-Evaluation-of-Word-Representations-on-Arabic-Sentiment-Analysis.pdf) 

I have written paper on the tasks I did and how preprocessing ensure dataset was optimizsed for the deep-learning based sentimnet classification, you can find that at:  [docs/Reasearch_Paper.pdf](docs/Research_paperpdf) 

---

## 📂 Project Structure  

```
Arabic-Sentiment-Preprocessing/
│── data/                   # Raw and processed datasets
│   ├── raw_data.csv        # Original dataset
│   ├── cleaned_data.csv    # Preprocessed dataset
│── notebooks/              # Jupyter Notebooks for data analysis
│   ├── exploratory_analysis.ipynb  
│── scripts/                # Python preprocessing scripts
│   ├── text_cleaning.py    # Removes stopwords, special symbols, etc.
│   ├── tokenization.py     # Tokenization & normalization for Arabic text
│   ├── ngram_analysis.py   # Generates n-grams & word clouds
│   ├── network_analysis.py # Retweet network visualization
│── docs/                   # Research paper & documentation
│   ├── Arabic_Sentiment_Preprocessing.pdf  
│── README.md               # Project overview
│── requirements.txt        # Dependencies
│── .gitignore              # Ignore unnecessary files
```

---

## 🚀 Installation & Setup  

### 1️⃣ Clone the repository  
```sh
git clone https://github.com/yourusername/Arabic-Sentiment-Preprocessing.git
cd Arabic-Sentiment-Preprocessing
```

### 2️⃣ Install dependencies  
```sh
pip install -r requirements.txt
```

### 3️⃣ Run preprocessing scripts  

#### **1. Text Cleaning**  
```sh
python scripts/text_cleaning.py
```
Removes stopwords, punctuation, hashtags, and normalizes text.  

#### **2. Tokenization & Normalization**  
```sh
python scripts/tokenization.py
```
Tokenizes Arabic text, removes diacritics, and normalizes script variations.  

#### **3. N-gram Analysis & Word Cloud**  
```sh
python scripts/ngram_analysis.py
```
Extracts top unigrams/bigrams and generates word cloud visualization.  

#### **4. Retweet Network Analysis**  
```sh
python scripts/network_analysis.py
```
Builds and visualizes a retweet network graph for sentiment clustering.  

---

## 📊 Exploratory Data Analysis  

For **data visualization and insights**, open the Jupyter Notebook:  

```sh
jupyter notebook notebooks/exploratory_analysis.ipynb
```
Includes:
- Sentiment distribution graphs  
- Text length analysis  
- Word cloud visualization  

---


## 🛠 Dependencies  

Ensure you have the following Python libraries installed:  

```txt
pandas
numpy
nltk
matplotlib
seaborn
wordcloud
networkx
farasa
```

To install all dependencies:  
```sh
pip install -r requirements.txt
```

---
 

If you find this repository useful, consider **starring** ⭐ it on GitHub!  

---


