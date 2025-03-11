  
import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_ngrams(text, n=2):
    words = text.split()
    ngrams = zip(*[words[i:] for i in range(n)])
    return [' '.join(ngram) for ngram in ngrams]

def plot_wordcloud(texts):
    text = ' '.join(texts)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("../data/tokenized_data.csv")
    all_text = ' '.join(df['tokenized_text'])
    bigrams = generate_ngrams(all_text, n=2)
    
    # Save top 100 bigrams
    bigram_counts = Counter(bigrams).most_common(100)
    pd.DataFrame(bigram_counts, columns=["Bigram", "Count"]).to_csv("../data/top_bigrams.csv", index=False)
    
    # Generate word cloud
    plot_wordcloud(df['tokenized_text'])
    print("N-gram analysis complete.")
