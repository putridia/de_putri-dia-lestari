import os
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\ASUS\OneDrive\Documents\GitHub\de_putri-dia-lestari\19_Data Engineering in the Cloud\Praktikum\accountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'dataengineer-418818.appspot.com'
})

# Function to extract data from a JSON file
def extract_data(json_file):
    data = pd.read_json(json_file)
    return data

# Function to transform data
def transform_data(data):
    # Select transactions with credit card payment method and success status
    credit_card_data = data[data['payment_method'] == 'credit card']
    success_data = credit_card_data[credit_card_data['status'] == 'success']
    
    return success_data[['transaction_id', 'transaction_date', 'customer_name', 'transaction_amount', 'item_category', 'item_name', 'payment_method', 'status']]

# Function to load data to Google Cloud Storage in CSV format
def load_data_to_gcs(local_file_path, bucket_name, gcs_file_name):
    bucket = storage.bucket()  # Use the default bucket from initialization
    blob = bucket.blob(gcs_file_name)
    blob.upload_from_filename(local_file_path)
    print(f"Data successfully uploaded to Firebase: {gcs_file_name}")

# Main function
def main():
    # Name of the JSON file
    json_file = r'C:\Users\ASUS\OneDrive\Documents\GitHub\de_putri-dia-lestari\19_Data Engineering in the Cloud\Praktikum\ecommerce.json'
    
    # Name of the directory to save the cleaned CSV file locally
    local_dir = r'C:\Users\ASUS\OneDrive\Documents\GitHub\de_putri-dia-lestari\19_Data Engineering in the Cloud\Praktikum'
    
    # Name of the file to be saved in Google Cloud Storage
    gcs_file_name = 'result-prioritas1_2.csv'
    
    # Full local path to save the cleaned CSV file
    local_file_path = os.path.join(local_dir, gcs_file_name)

    # Extract, transform, and load data
    data = extract_data(json_file)
    cleaned_data = transform_data(data)
    
    # Save cleaned data locally
    cleaned_data.to_csv(local_file_path, index=False)

    # Upload the local file to Google Cloud Storage
    load_data_to_gcs(local_file_path, 'dataengineer-418818.appspot.com', gcs_file_name)

if __name__ == "__main__":
    main()

