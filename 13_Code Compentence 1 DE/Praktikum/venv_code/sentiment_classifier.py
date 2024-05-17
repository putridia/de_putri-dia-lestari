import pandas as pd
import os

sentiment_csv = None
classified = None

def load_sentiment():
    global sentiment_csv
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'data_source', 'file.csv')
        sentiment_csv = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
    except Exception as e:
        print("Error loading sentiment CSV:", str(e))
        return None

def classify_sentiment():
    global classified
    if sentiment_csv is None:
        print("Error: Dataset is not loaded.")
        return
    classified = sentiment_csv.groupby('labels')


def save_csv():
    global sentiment_csv
    global classified
    for label, group in classified:
        file_name = f"13_Code Compentence 1 DE/Praktikum/sentiment_{label}.csv"
        group.to_csv(file_name, index=False)

def summarize_count():
    global sentiment_csv
    if classified is None:
        print("Error: Dataset is not loaded.")
        return

    try:
        counts = sentiment_csv['labels'].value_counts().reset_index()
        counts.columns = ['label', 'count']
        counts.to_csv("13_Code Compentence 1 DE/Praktikum/sentiment_counts.csv", index=False)
        print("Sentiment counts summarized and saved to 13/sentiment_counts_summary.csv")
    except Exception as e:
        print("Error summarizing sentiment counts:", str(e))


if __name__ == "__main__":
    load_sentiment()
    classify_sentiment()
    save_csv()
    summarize_count()