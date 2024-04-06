# Step Code Compentence 1 DE

1. Persiapan Lingkungan Pengembangan
   - Buat virtual environment dengan Python dan namai sebagai venv_code untuk mengisolasi proyek.
   - Download dataset ChatGPT Sentiment Analysis dari tautan ini kemudian simpan kedalam folder data_source, yang terdiri dari atribut tweets sebagai teks tweet dan label yang merupakan penanda sentimen (good,bad,neutral).
  ![Screenshot 2024-04-06 045349](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/bc021e43-944a-4c7a-acf0-415804b8ffbc)

2. Persiapan dan Pemrosesan Dataset dengan OOP
   - Bangun class SentimentClassifier dalam Python didalam file sentiment_classifier.py yang memiliki metode untuk membaca dan memproses dataset.
     - Metode load_data() akan membaca dataset ke dalam struktur data yang sesuai.
     - Metode classify_sentiment() akan membagi tweets ke dalam kategori good, bad, atau neutral.
     - Metode save_to_csv() akan menyimpan tweets yang diklasifikasikan ke dalam file CSV terpisah: sentiment_good.csv, sentiment_bad.csv, dan sentiment_neutral.csv.
   - Hitung dan simpan jumlah tweets untuk masing-masing kategori sentimen ke dalam file sentiment_counts.csv menggunakan metode summarize_counts().

     ![Screenshot 2024-04-06 185308](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/1cba71e0-8056-4f1b-af59-6c341e8d2078)

3. Penyimpanan Data
   - Desain skema database dengan tabel yang saling berelasi:
     - tweets (id, text, sentiment_id)
     - sentiments (sentiment_id, sentiment_label)
     - Pastikan sentiment_id di tabel tweets merupakan foreign key yang merujuk ke sentiments.
   - Buat class Python DatabaseManager didalam file database_manager.py dengan library SQLAlchemy atau pymysql (jika menggunakan mysql) yang memiliki metode:
     - create_tables untuk mendefinisikan dan membuat tabel-tabel di atas jika belum ada.
     - insert_from_csv untuk membaca data dari CSV dan menginsert-nya ke dalam database sesuai tabel yang relevan.
   - Dokumentasi masing-masing tabel hasil insert dalam bentuk screenshot

     ![Screenshot 2024-04-06 183938](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/b94310ff-2b1d-4bbc-9211-6afc75472b9a)
     ![Screenshot 2024-04-06 184038](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/ed4d36b8-1526-4d54-bf46-6e754414b771)
     ![Screenshot 2024-04-06 184057](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/9e6396ba-43c1-42c2-8511-1e9e72334ab5)

4. Integrasi dengan Google Cloud Storage:
   - Buat satu bucket di Google Cloud Storage, dengan nama sentiment_chatgpt_storage, untuk menyimpan semua file yang relevan:
     - sentiment_good.csv
     - sentiment_bad.csv
     - sentiment_neutral.csv
     - sentiment_counts.csv
     - Backup database sentiment_chatgpt.sql
   nama bucket: sentiment_chatgpt_storage_pdl
   
   ![Screenshot 2024-04-06 183053](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/ee06e59d-dcac-457a-bead-05177ac37a82)
