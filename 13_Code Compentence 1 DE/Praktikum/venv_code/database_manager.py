from pymysql import connect
import pandas as pd
import os

connection = connect(
    host='localhost',
    db='sentiment_chatgpt',
    user='root',
    password='',
    port=3307
)

cursor = connection.cursor()

def create_tables(self):
    try:
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sentiment_labels (
                label_id INT PRIMARY KEY,
                sentiment_label VARCHAR(10)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tweet_data (
                tweet_id INT AUTO_INCREMENT PRIMARY KEY,
                tweet_text VARCHAR(100),
                label_id INT,
                FOREIGN KEY(label_id) REFERENCES sentiment_labels(label_id)
            )
        ''')
        self.connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Error occurred during table creation: {e}")

def insert_csv(cursor, file_path):
    try:
        sentiment_csv = pd.read_csv(file_path, index_col=0)

        for index, row in sentiment_csv.iterrows():
            sentiment = row['sentiment'].lower()
            if sentiment == 'neutral':
                sentiment_id = 1
            elif sentiment == 'good':
                sentiment_id = 2
            elif sentiment == 'bad':
                sentiment_id = 3
            else:
                print(f"Ignoring row {index}: Unknown sentiment '{sentiment}'.")
                continue
            cursor.execute('INSERT INTO tweets (text, sentiment_id) VALUES (%s, %s)', (row['tweets'], sentiment_id))
    except Exception as e:
        print(f"Error occurred during CSV insertion: {e}")

# Correct the password if necessary
create_tables()
insert_csv()

connection.commit()
connection.close()