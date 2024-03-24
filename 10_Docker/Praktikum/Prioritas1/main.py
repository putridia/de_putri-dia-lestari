import pandas as pd

def calculate_average(csv_file_path):
    # Membaca file CSV menjadi DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Menghitung rata-rata dari kolom 'score'
    average_score = df['score'].mean()
    
    return average_score

if __name__ == "__main__":
    csv_file_path = 'data.csv'
    result = calculate_average(csv_file_path)
    print("Rata-rata skor adalah:", result)