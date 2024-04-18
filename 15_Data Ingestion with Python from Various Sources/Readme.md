# Summary Data Ingestion

## Pengertian Data Ingestion

Data ingestion adalah proses mengumpulkan, mengimpor, dan memproses data dari berbagai sumber untuk kemudian disimpan dalam database atau data warehouse. Tujuan utama data ingestion adalah untuk menyediakan data yang siap digunakan untuk analisis dan pengambilan keputusan.

##  Kenapa Data Ingestion Penting?

Ada banyak manfaat menggunakan data ingestion, antara lain:

- Enhanced Data Analysis: Dengan data ingestion, Anda dapat menganalisis data dari berbagai sumber dengan lebih mudah dan efisien.
- Data Integration: Data ingestion dapat membantu Anda membuat keputusan yang lebih baik berdasarkan informasi yang akurat dan terkini.
- Real-time Analytics: Data ingestion dapat membantu Anda menghemat waktu dan sumber daya dengan mengotomatiskan tugas dan proses.
- Facilitation of ETL and ELT: Data ingestion dapat membantu Anda menemukan pola dan tren dalam data Anda, sehingga Anda dapat memperoleh wawasan yang lebih berharga.

## Komponen Utama Data Ingestion di GCP

Data Ingestion di GCP terdiri dari tiga komponen utama, yaitu:

- Data Source: Sumber data adalah tempat data berasal. Data dapat berasal dari berbagai sumber, seperti database, aplikasi, sensor, dan file.
- Data Target: Data target adalah tempat data disimpan setelah diproses. Data target dapat berupa data lake, data warehouse, atau sistem penyimpanan cloud lainnya.
- Data Pipeline: Data pipeline adalah serangkaian proses dan alur kerja yang mengelola transfer dan transformasi data dari sumber data ke data target.

## Proses Data Ingestion di GCP

Proses data Ingestion di GCP umumnya terdiri dari beberapa langkah, yaitu:

- Ekstraksi: Data diekstrak dari sumber data.
- Transformasi: Data diubah ke dalam format yang standar dan konsisten.
- Pemuatan: Data dimuat ke dalam data target.

## Jenis-jenis Data Ingestion

GCP menawarkan tiga jenis data ingestion, yaitu:

- Batch Ingestion: Data dikumpulkan dan diproses dalam batch pada interval yang dijadwalkan. Hal ini ideal untuk volume data yang besar yang tidak memerlukan pemrosesan real-time.
- Real-time Ingestion: Data diproses segera setelah dihasilkan. Hal ini penting untuk aplikasi yang memerlukan wawasan instan, seperti deteksi penipuan.
- Hybrid Ingestion: Kombinasi batch dan real-time ingestion, memungkinkan fleksibilitas berdasarkan kebutuhan data dan bisnis.

## Data Source and How to Ingest with Python

### 1.1 Ingest with Python - File Based Source

CSV

Format file yang digunakan untuk menyimpan data tabular yang setiap kolomnya dipisahkan dengan koma, titik koma, dll.

Python Libraries: pandas

```bash 
  Import pandas as pd 
  from IPython.display import display

  #Read the CSV file into a pandas Dataframe 
  df = pd.read_csv("example.csv")

  display(df.head()) 
  display(df.tail())
```

### 1.2 Ingest with Python - File Based Source

Excel

Format file yang digunakan oleh Microsoft Excel.

Python Libraries: openpyxl, pandas

```bash
  import pandas as pd 
  from IPython.display import display

  df = pd.read_excel("example.xlsx")

  display (df.head())

  display(df.tail())
```

### 1.3 Ingest with Python - File Based Source

JSON (JavaScript Object Notation)

Format ringan untuk pertukaran data. Sangat mudah bagi manusia untuk membaca dan menulis dan mudah bagi mesin untuk menguraikan dan menghasilkan.

Python Libraries: json, pandas

```bash
  import pandas as pd 
  from IPython.display import display

  df pd.read_json("example.json")

  display(df)
```

### 1.4 Ingest with Python - File Based Source

- Feather
- XML
- Parquet
- HDF5 (Hierarchical Data Format version 5)

```bash
  df_feather = pd.read_feather("example. feather")
  df_xml = pd.read_xml("example.xml") 
  df_perquet = pd.read_parquet("example.parquet")
  df_hdf5 = pd.read_hdf5("example.hdf5")
```

### 2.1 Ingest with Python - Databases

MySQL

Salah satu sistem manajemen basis data relasional sumber terbuka paling populer di dunia.

Python Libraries: pymysql

```bash
  from pymysql import connect
  import pandas as pd

  connection = connect(
       host='127.0.0.1', 
       db='alta_example,
       user='root',
       password=' '
  )

  cursor = connection.cursor()

  cursor.execute('SELECT * FROM customers')

  results = cursor.fetchall()

  connection.close()

  df_customer = pd.DataFrame(results, columns=['id',  'name',  'email', 'phone', 'address')

  df_customer.head()
```

### 2.2 Ingest with Python - Databases

PostgreSQL

Salah satu sistem manajemen basis data relasional sumber terbuka paling populer di dunia.

Python Libraries: psycopg2-binary

```bash
  from psycopg2 import connect
 
  connection = connect(
       host="db.jhximcazqrglhlvoonlf.supabase.co",
       port=5432, 
       database="postgres",
       user="postgres",
       password="Lnnuox0i3dxEAov7",
  )

  if connection:
        print("Connection successful")
```

### 3 Ingest with Python - APIs

APIs

API (Antarmuka Pemrograman Aplikasi) memungkinkan aplikasi perangkat lunak yang berbeda untuk berkomunikasi satu sama lain. Mereka menyediakan seperangkat aturan dan protokol untuk mengakses dan menggunakan layanan, alat, atau fungsi aplikasi perangkat lunak lain.

Python Libraries: requests

```bash
  import requests
  import pandas as pd

  url = "https://jsonplaceheloer.typicode.com/posts" 
  df = pd.Dataframe(requests.get(url).json())
  
  df.head()
```

### 4 Ingest with Python - Web Scraping

Web Scraping

Web scraping adalah proses mengekstraksi data dari situs web. Ini melibatkan pengambilan halaman web dan kemudian mengekstraksi informasi yang diperlukan.

Python Libraries: requests, beautifulsoup4

```bash
  import requests
  from bs4 import BeautifulSoup
  import pandas as pd

  url = "https://todo-app-simple-next-js.vercel.app/"
  response = requests.get(url)
  soup = BeautifulSoup (response.content, 'html.parser')

  cards = soup.find_all('div', class_='card text-left mt-2')

  data = []
  for card in cards:
       title card.find('h4', class_='card-title').text
       description = card.find('p', class_='card-text').text
       data.append([title, description])

  df = pd.DataFrame(data, columns=['title', 'description'])
  df
```

### 5 Ingest with Python - Cloud Storage

Google Cloud Storage

Google Cloud Storage adalah layanan web penyimpanan file online RESTful untuk menyimpan dan mengakses data pada infrastruktur Google Cloud Platform.

Python Libraries: google-cloud-storage

```bash
  import json
  import google.cloud.storage
  import pandas as pd

  with open("data-engineer-alta-405316-e7dcdf0855b1.json") as f:
        service_account_info = json.load(f)

  credentials = google.oauth2.service_account.Credentials.from_service_account_info( 
       service_account_info
  )
  storage_client = google.cloud.storage.Client(credentials=credentials)

  buckets = list(storage_client.list_buckets())
  print(buckets)

  bucket = storage_client.get_bucket("transaction-data-ecomerce")
  blob bucket.get_blob("example.csv")
  blob.download_to_filename("example.csv")

  df = pd.read_csv("example.csv") 
  df
```