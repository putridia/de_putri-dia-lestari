import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import requests

def initialize_firebase(cred_path, bucket_name):
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {'storageBucket': bucket_name})

def extract_data(json_url):
    try:
        response = requests.get(json_url)
        response.raise_for_status()  # Check for request errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def transform_data(data):
    if data is None or not data:
        print("No data to transform.")
        return None
    try:
        df = pd.DataFrame(data)
        if df.empty:
            print("DataFrame is empty.")
            return None
        selected_stocks = ['GOOGL', 'AMZN', 'MSFT', 'AAPL']
        filtered_data = df[df['stock_symbol'].isin(selected_stocks) & (df['trade_price'] > 500)]
        if filtered_data.empty:
            print("No data meets the criteria after filtering.")
            return None
        return filtered_data
    except KeyError as e:
        print(f"KeyError in data transformation: {e}")
        return None

def load_data_to_gcs(data, bucket_name, local_file_path, gcs_file_name):
    if data is None or data.empty:
        print("No data to load to Firebase.")
        return
    try:
        pq.write_table(pa.Table.from_pandas(data), local_file_path)
        bucket = storage.bucket(bucket_name)
        blob = bucket.blob(gcs_file_name)
        blob.upload_from_filename(local_file_path)
        print(f"Data successfully uploaded to Firebase: {gcs_file_name}")
    except Exception as e:
        print(f"Error uploading data to Firebase: {e}")

def main():
    cred_path = r"C:\Users\ASUS\OneDrive\Documents\GitHub\de_putri-dia-lestari\19_Data Engineering in the Cloud\Praktikum\accountKey.json"
    bucket_name = 'dataengineer-418818.appspot.com'
    json_url = 'https://gist.githubusercontent.com/nadirbslmh/93b62fdcfa694d4ec07bed9b3c94e401/raw/c07971341361e23fd4f3a880437c4d8e4ebcfafc/stock_trades.json'
    
    # Path for local file storage
    local_file_path = r'C:\Users\ASUS\OneDrive\Documents\GitHub\de_putri-dia-lestari\19_Data Engineering in the Cloud\Praktikum\stock_trades.parquet'
    gcs_file_name = 'stock_trades.parquet'

    initialize_firebase(cred_path, bucket_name)
    
    data = extract_data(json_url)
    cleaned_data = transform_data(data)
    load_data_to_gcs(cleaned_data, bucket_name, local_file_path, gcs_file_name)

if __name__ == "__main__":
    main()
