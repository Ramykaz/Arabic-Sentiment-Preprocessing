import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
arabic_stopwords = set(stopwords.words('arabic'))
english_stopwords = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'@\w+|#\w+|http\S+', '', text)  # Remove mentions, hashtags, URLs
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower().strip()  # Lowercase and strip spaces
    return text

def remove_stopwords(text, lang='arabic'):
    words = text.split()
    stopwords_set = arabic_stopwords if lang == 'arabic' else english_stopwords
    filtered_words = [word for word in words if word not in stopwords_set]
    return ' '.join(filtered_words)

if __name__ == "__main__":
    df = pd.read_csv("../data/raw_data.csv")
    df['cleaned_text'] = df['text'].apply(clean_text).apply(remove_stopwords)
    df.to_csv("../data/cleaned_data.csv", index=False)
    print("Text cleaning complete. Saved to cleaned_data.csv")
