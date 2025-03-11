from farasa.segmenter import FarasaSegmenter

segmenter = FarasaSegmenter()

def tokenize_text(text):
    return ' '.join(segmenter.segment(text))

if __name__ == "__main__":
    df = pd.read_csv("../data/cleaned_data.csv")
    df['tokenized_text'] = df['cleaned_text'].apply(tokenize_text)
    df.to_csv("../data/tokenized_data.csv", index=False)
    print("Tokenization complete. Saved to tokenized_data.csv")
