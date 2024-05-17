import pandas as pd
import numpy as np
import os
from pathlib import Path

class DataLakeBuilder:
    def __init__(self):
        pass

    def read_csv(self, file_path):
        return pd.read_csv(file_path)

    def handle_missing_values(self, df):
        # Mengisi missing values dengan median untuk kolom numerik
        for col in df.select_dtypes(include=[np.number]):
            df[col].fillna(df[col].median(), inplace=True)
        
        # Mengisi missing values dengan mode untuk kolom kategorik
        for col in df.select_dtypes(include=[object]):
            df[col].fillna(df[col].mode()[0], inplace=True)
        
        return df

    def handle_outliers(self, df, column):
        # Menghitung Q1 dan Q3
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        
        # Menghitung IQR
        IQR = Q3 - Q1
        
        # Mengidentifikasi outliers
        outliers = df[(df[column] < Q1 - 1.5 * IQR) | (df[column] > Q3 + 1.5 * IQR)]
        
        # Menghapus outliers
        df = df[~df.index.isin(outliers.index)]
        
        return df

    def save_to_parquet(self, df, file_name):
        # Membuat direktori jika belum ada
        Path(file_name).parent.mkdir(parents=True, exist_ok=True)
        
        # Menyimpan DataFrame ke file Parquet
        df.to_parquet(file_name, engine='pyarrow')

    def validate_data(self, file_path):
        # Membaca data dari file Parquet
        df = pd.read_parquet(file_path)
        
        # Menampilkan informasi umum mengenai data
        print("Data Overview:")
        print(df.info())
        
        # Menampilkan statistik deskriptif
        print("\nDescriptive Statistics:")
        print(df.describe())


if __name__ == "__main__":
    # Buat instance dari DataLakeBuilder
    builder = DataLakeBuilder()

    # Daftar file CSV yang akan diolah
    csv_files = ['events.csv', 'customers.csv', 'tickets.csv', 'transactions.csv', 'customer_feedback.csv']

    parquet_dir = r"C:\Users\ASUS\OneDrive\Documents\GitHub\de_putri-dia-lestari\18_Code Competence 2 DE\Praktikum\data_parquet"
    if not os.path.exists(parquet_dir):
        os.makedirs(parquet_dir)
    
    # Loop untuk setiap file CSV
    data_source = r'C:\Users\ASUS\OneDrive\Documents\GitHub\de_putri-dia-lestari\18_Code Competence 2 DE\Praktikum\data_source'
    for file in csv_files:
        # Baca data dari file CSV
        file_path = os.path.join(data_source, file)
        df = builder.read_csv(file_path)
        
        # Handle missing values
        df = builder.handle_missing_values(df)
        
        # Simpan data ke format Parquet
        parquet_file = os.path.join(parquet_dir, file.split('.')[0] + '.parquet')
        builder.save_to_parquet(df, parquet_file)
        
        print(f"Data saved to: {parquet_file}\n")

    # Validasi data
    for file in os.listdir(parquet_dir):
        parquet_file = os.path.join(parquet_dir, file)
        print(f"Validating data: {parquet_file}")
        builder.validate_data(parquet_file)
        print("\n")