import pandas as pd
import os
from datetime import datetime
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import storage

class DataWarehouseLoader:
    def __init__(self):
        cred = credentials.Certificate(r'C:\Users\ASUS\OneDrive\Documents\GitHub\de_putri-dia-lestari\18_Code Competence 2 DE\Praktikum\venv_code1\accountKey.json')
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'dataengineer-418818.appspot.com'
        })
        self.bucket = storage.bucket()

    def load_data(self, file_path):
        df = pd.read_parquet(file_path)
        return df

    def transform_data(self, df):
        # Menggabungkan tabel transactions dengan tickets berdasarkan ticket_id, dan kemudian dengan events berdasarkan event_id
        df_merged = df['transactions'].merge(df['tickets'], on='ticket_id').merge(df['events'], on='event_id')

        # Menghitung Jumlah Tiket yang Terjual per Acara
        tickets_sold_per_event = df_merged.groupby('event_id')['quantity'].sum().reset_index()

        # Menghitung Total Pendapatan dari Setiap Acara
        revenue_per_event = df_merged.groupby('event_id')['total_amount'].sum().reset_index()

        if 'customer_id' in df['transactions']:
            feedback_analysis = pd.merge(df['customer_feedback'], df['transactions'], on='transaction_id', how='inner')
            if 'event_id' in feedback_analysis:
                avg_feedback_per_event = feedback_analysis.groupby('event_id')['rating'].mean().reset_index()
            else:
                avg_feedback_per_event = pd.DataFrame()
        else:
            avg_feedback_per_event = pd.DataFrame()

        return tickets_sold_per_event, revenue_per_event, avg_feedback_per_event

    def save_to_warehouse(self, df, table_name):
        current_date = datetime.now().strftime('%Y-%m-%d')
        base_directory = r"C:\Users\ASUS\OneDrive\Documents\GitHub\de_putri-dia-lestari\18_Code Competence 2 DE\Praktikum"
        directory = f'{base_directory}/{current_date}'
        os.makedirs(directory, exist_ok=True)

        file_name = f'{directory}/{table_name}.parquet'
        df.to_parquet(file_name, engine='pyarrow')

        blob = self.bucket.blob(file_name)
        blob.upload_from_filename(file_name)
        print("Data saved to Data Warehouse: ", file_name)


if __name__ == "__main__":
    loader = DataWarehouseLoader()

    # Load data from Parquet files
    transactions = loader.load_data('C:/Users/ASUS/OneDrive/Documents/GitHub/de_putri-dia-lestari/18_Code Competence 2 DE/Praktikum/data_parquet/transactions.parquet')
    tickets = loader.load_data('C:/Users/ASUS/OneDrive/Documents/GitHub/de_putri-dia-lestari/18_Code Competence 2 DE/Praktikum/data_parquet/tickets.parquet')
    events = loader.load_data('C:/Users/ASUS/OneDrive/Documents/GitHub/de_putri-dia-lestari/18_Code Competence 2 DE/Praktikum/data_parquet/events.parquet')   
    customer_feedback = loader.load_data('C:/Users/ASUS/OneDrive/Documents/GitHub/de_putri-dia-lestari/18_Code Competence 2 DE/Praktikum/data_parquet/customer_feedback.parquet')
    customer = loader.load_data('C:/Users/ASUS/OneDrive/Documents/GitHub/de_putri-dia-lestari/18_Code Competence 2 DE/Praktikum/data_parquet/customers.parquet')

    # Transform data
    tickets_sold, revenue, feedback = loader.transform_data({
        'transactions': transactions,
        'tickets': tickets,
        'events': events,
        'customer_feedback': customer_feedback,
        'customers': customer
    })
    
    # Save data to Data Warehouse
    loader.save_to_warehouse(tickets_sold, 'tickets_sold_per_event')
    loader.save_to_warehouse(revenue, 'revenue_per_event')
    loader.save_to_warehouse(feedback, 'avg_feedback_per_event')