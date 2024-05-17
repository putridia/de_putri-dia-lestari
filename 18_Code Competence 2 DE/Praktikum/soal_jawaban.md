# Code Competence 2

1. Persiapan Lingkungan Pengembangan
    - Gunakan virtual environment venv_code yang telah ada. Modifikasi environment ini untuk memasukkan dependencies baru yang diperlukan, seperti library pandas, airflow, dan library lain yang diperlukan.

    ![Screenshot 2024-05-17 154123](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/393617d6-c0ff-4f7a-9a69-fab700fe97b1)

    - Update requirements.txt untuk mencerminkan perubahan tersebut.
    - Download dataset dan kemudian simpan kedalam folder data_source
    
    ![Screenshot 2024-05-17 153918](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/dee010e6-6dfa-4759-8ebc-b4f439e6e70b)

    - Struktur file csv

2. Data Ingestion dan Persiapan Data Lake / Data Werehouse
    - Penyiapan Skrip Python
        - Buat file Python dengan nama data_ingestion.py.
        - Dalam file ini, buat kelas dengan nama DataLakeBuilder.
    - Kelas DataLakeBuilder
        - Kelas ini harus memiliki metode untuk membaca data dari file CSV, menangani missing values dan outliers, dan menyimpan data ke format yang sesuai untuk Data Lake
        - read_csv_data(self, file_path): Metode untuk membaca data dari file CSV
        - handle_missing_values(self, df): Metode untuk menangani missing values dalam DataFrame.
        - handle_outliers(self, df, column): Metode untuk menangani outliers dalam kolom tertentu dari DataFrame
        - save_to_parquet(self, df, file_name): Metode untuk menyimpan DataFrame ke file Parquet.

        ![Screenshot 2024-05-17 155024](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/c5734b70-bf02-4992-92ab-9a9639fc4443)

    - Metode read_csv_data
        - Gunakan pandas untuk membaca file CSV
        - Contoh: pd.read_csv(file_path) di mana file_path adalah path ke file CSV.

        ![Screenshot 2024-05-17 155141](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/0b1e0ee5-d5ba-4a3d-bb03-88e489b4d2d8)

    - Metode handle_missing_values
        - Terapkan strategi untuk menangani missing values, seperti pengisian nilai (imputation) atau penghapusan baris/kolom
        - Contoh: Menggunakan df.fillna() atau df.dropna() dari pandas.

        ![Screenshot 2024-05-17 155248](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/e7f8b243-1a6c-4a6c-9d3d-26d497441efe)

    - Metode handle_outliers
        - Gunakan teknik statistik untuk mendeteksi dan menangani outliers.
        - Contoh: IQR (Interquartile Range) untuk mengidentifikasi outliers dan kemudian menggantinya atau menghapusnya.

        ![Screenshot 2024-05-17 155329](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/d4579309-45df-47cf-a4e9-ab7ce07d60fd)

    - Metode save_to_parquet
        - Simpan DataFrame yang telah diolah ke format Parquet, yang efisien untuk Data Lake.
        - Contoh: df.to_parquet(file_name).

        ![Screenshot 2024-05-17 155407](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/e792c67d-bf90-4203-8fa8-e7144ba06cb4)

    - Eksekusi Script
        - Buat instance dari DataLakeBuilder dan panggil metode-metodenya untuk setiap file CSV (events.csv, customers.csv, tickets.csv, transactions.csv, dan customer_feedback.csv).
        - Pastikan semua file terbaca dan diolah dengan benar, lalu simpan dalam format Parquet.
    - Validasi Data
        - Setelah semua data disimpan dalam format Parquet, buat metode untuk memvalidasi atau menampilkan ringkasan data.
        - Contoh: Metode validate_data(self, file_path) yang membaca file Parquet dan menampilkan ringkasan statistik atau beberapa baris awal data.

    ![Screenshot 2024-05-17 220741](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/170ecf36-d831-45e1-8464-d17fa01a8074)

    ![Screenshot 2024-05-17 220831](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/455272af-e719-4509-b4a9-6cc6d0facd3a)

3. Transformasi Data dan Pemuatan ke Data Warehouse
    - Penyiapan Skrip Python untuk Transformasi Data
        - Buat file Python baru dengan nama data_transformation.py.
        - Dalam file ini, buat kelas dengan nama DataWarehouseLoader.
    - Kelas DataWarehouseLoader
        - Kelas ini harus memiliki metode untuk membaca data dari Data Lake, melakukan transformasi data, dan menyimpan data yang telah ditransformasi ke Data Warehouse.
        - load_data(self, file_path): Metode untuk membaca data dari Data Lake (format Parquet).
        - transform_data(self, df): Metode umum untuk melakukan transformasi data.
        - save_to_warehouse(self, df, table_name): Metode untuk menyimpan data ke Data Warehouse.
    - Metode load_data
        - Gunakan pandas untuk membaca file Parquet dari Data Lake.
        - Load data dari file Parquet untuk tabel events, customers, tickets, transactions, dan customer_feedback.
        - Contoh: pd.read_parquet(file_path).
    - Metode Transform Data
        - Menggabungkan Data untuk Analisis
            - Gabungkan tabel transactions dengan tickets berdasarkan ticket_id, dan kemudian dengan events berdasarkan event_id.
        - Menghitung Jumlah Tiket yang Terjual per Acara
            - Gunakan groupby pada kolom event_id atau name dari tabel events.
            - Hitung jumlah tiket yang terjual dengan mengagregasi kolom quantity menggunakan fungsi sum.
        - Menghitung Total Pendapatan dari Setiap Acara
            - Dari DataFrame yang digabungkan sebelumnya, gunakan groupby pada kolom event_id atau name.
            - Hitung total pendapatan dengan mengagregasi total_amount menggunakan fungsi sum.
        - Analisis Feedback Pelanggan
            - Gabungkan tabel customer_feedback dengan transactions berdasarkan transaction_id untuk mengaitkan feedback dengan transaksi.
            - Analisis rating rata-rata per acara.
    - Metode Save to Werehouse
        - Penamaan File Hasil Transformasi
            - Tickets_sold_per_event.parquet
            - Revenue_per_event.parquet
            - Feedback_analysis.parquet
        - Setup Google Cloud Storage
            - Pastikan Anda memiliki akses ke Google Cloud Storage.
            - Buat bucket yang akan digunakan sebagai Data Warehouse, jika belum ada.
        - Struktur Folder Berdasarkan DateTime
            - Untuk mengorganisir data, gunakan struktur folder berdasarkan tanggal. Format yang umum adalah YYYY/MM/DD atau YYYY-MM-DD.
            - Contoh: Untuk data yang diproses pada tanggal 20 November 2023, folder bisa bernama 2023/11/20 atau 2023-11-20.

        ![Screenshot 2024-05-17 220612](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/ad8def87-8278-4e11-97de-a0ea68a9f379)

        ![Screenshot 2024-05-17 230202](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/cd4b9226-217f-4765-a586-6f5e0ac5c7cc)

4. Orkestrasi Workflow dengan Apache Airflow
    - Buatlah DAG (Directed Acyclic Graph) di Apache Airflow untuk mengotomatisasi proses pengambilan data, transformasi, dan pemuatan ke Data Warehouse.
    - DAG harus mencakup task untuk data ingestion, data transformation, dan loading data ke warehouse.
    - Jelaskan bagaimana Anda akan menjadwalkan DAG ini dan mengatur dependencies antar tasks.

    ![Screenshot 2024-05-17 230823](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/8ba25f94-5574-47b8-be26-dc66ca581dd9)