import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\ASUS\OneDrive\Documents\GitHub\de_putri-dia-lestari\19_Data Engineering in the Cloud\Praktikum\accountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'dataengineer-418818.appspot.com'
})

def extract_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

def transform_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def load_data_to_gcs(df, bucket_name, local_file_path, gcs_file_name):
    bucket = storage.bucket(bucket_name)
    blob = bucket.blob(gcs_file_name)
    df.to_csv(local_file_path, index=False)
    blob.upload_from_filename(local_file_path)
    print(f"Data successfully uploaded to Firebase: {gcs_file_name}")

# Main function
def main():
    csv_file = r'C:\Users\ASUS\OneDrive\Documents\GitHub\de_putri-dia-lestari\19_Data Engineering in the Cloud\Praktikum\survey.csv'
    bucket_name = 'dataengineer-418818.appspot.com'

    # Nama file untuk disimpan di Google Storage Firebase
    local_output_path = r'C:\Users\ASUS\OneDrive\Documents\GitHub\de_putri-dia-lestari\19_Data Engineering in the Cloud\Praktikum\survey_cleaned.csv'
    gcs_file_name = 'survey_cleaned.csv'

    # Ekstraksi data dari file CSV
    df = extract_data(csv_file)
    cleaned_data = transform_data(df)

    # Memuat data
    load_data_to_gcs(cleaned_data, bucket_name, local_output_path, gcs_file_name)

if __name__ == "__main__":
    main()
