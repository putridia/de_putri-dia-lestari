# Summary Relational Database

Database atau basis data adalah kumpulan data terorganisir yang disimpan secara elektronik di komputer. Data ini terhubung dan dikelola dengan sistem tertentu untuk memudahkan akses, manipulasi, dan pemrosesan.

Manfaat database:

- Efisiensi: Menyimpan dan mengelola data secara terpusat.
- Akurasi: Meminimalkan duplikasi dan kesalahan data.
- Keamanan: Melindungi data dari akses yang tidak sah.
- Kemudahan akses: Memungkinkan pengambilan data dengan cepat dan mudah.
- Fleksibilitas: Mendukung berbagai jenis data dan aplikasi.

Unsur Utama Database
Database terdiri dari beberapa unsur yang saling terkait untuk membentuk sistem penyimpanan dan pengelolaan data yang terstruktur. Berikut adalah penjelasan mengenai unsur-unsur database:

1. Data:
Merupakan elemen dasar dari database, yang dapat berupa teks, angka, gambar, audio, video, dan lain-lain. Data terorganisir dalam bentuk tabel, baris, dan kolom. Setiap data memiliki atribut yang mendeskripsikannya, seperti nama, jenis data, dan panjang data.

2. Tabel:
Kumpulan data yang terhubung secara logis dan memiliki struktur yang sama. Tabel terdiri dari baris dan kolom. Setiap baris dalam tabel mewakili satu entitas (misalnya, satu buku, satu pelanggan). Setiap kolom dalam tabel mewakili satu atribut (misalnya, nama buku, harga buku).

## Relational Database Management System (RDBMS)
RDBMS adalah singkatan dari Relational Database Management System, yaitu sistem manajemen basis data yang populer dan banyak digunakan karena kemudahannya dalam mengelola dan mengatur data. Model data relasional yang terstruktur dan query language SQL yang mudah digunakan menjadikan RDBMS pilihan yang tepat untuk berbagai kebutuhan penyimpanan data.

- Transfer data: JSON sering digunakan untuk mentransfer data antara aplikasi dan RDBMS. Data diekspor dari RDBMS dalam format JSON untuk dikonsumsi oleh aplikasi lain. Sebaliknya, data yang diterima dalam format JSON dapat diimpor ke dalam RDBMS.
- API (Application Programming Interface): Banyak RDBMS modern menyediakan API yang mengembalikan data dalam format JSON. Hal ini memudahkan developer untuk berinteraksi dengan database dari aplikasi web atau mobile.

## Penjelasan DDL dan DML
# DDL (Data Definition Language)

DDL adalah bagian dari SQL (Structured Query Language) yang digunakan untuk mendefinisikan dan menata struktur database. Perintah DDL digunakan untuk membuat, mengubah, dan menghapus objek database seperti tabel, kolom, dan indeks.

Contoh Perintah DDL:
- CREATE TABLE: Membuat tabel baru.
- ALTER TABLE: Mengubah struktur tabel yang ada.
- DROP TABLE: Menghapus tabel.
- CREATE INDEX: Membuat indeks untuk mempercepat pencarian data.
- DROP INDEX: Menghapus indeks.

# DML (Data Manipulation Language)
DML adalah bagian dari SQL yang digunakan untuk memanipulasi data dalam database. Perintah DML digunakan untuk memasukkan, memperbarui, menghapus, dan mengambil data dari tabel.

Contoh Perintah DML:
- INSERT INTO: Memasukkan data baru ke dalam tabel.
- UPDATE: Memperbarui data yang ada dalam tabel.
- DELETE FROM: Menghapus data dari tabel.
- SELECT: Mengambil data dari tabel.

DDL dan DML adalah dua bagian penting dari SQL yang digunakan untuk mengelola database. DDL digunakan untuk mendefinisikan struktur database, sedangkan DML digunakan untuk memanipulasi data dalam database.

## Penjelasan Join, Union, Agregasi, Subquery, dan Function dalam DBMS

1. Join: menggabungkan data dari dua tabel atau lebih berdasarkan kolom yang sama. Ada beberapa jenis join, seperti:
   - Inner join: Menggabungkan baris dari kedua tabel yang memiliki nilai yang sama pada kolom yang dijoin.
   - Left join: Menggabungkan semua baris dari tabel pertama dan baris dari tabel kedua yang memiliki nilai yang sama pada kolom yang dijoin.
   - Right join: Menggabungkan semua baris dari tabel kedua dan baris dari tabel pertama yang memiliki nilai yang sama pada kolom yang dijoin.
   
   Contoh:
   Misalkan Anda memiliki dua tabel: Customers dan Orders. Anda dapat menggunakan join untuk menggabungkan data dari kedua tabel untuk mendapatkan informasi tentang pelanggan yang telah melakukan pemesanan.

2. Union: menggabungkan data dari dua tabel atau lebih yang memiliki struktur yang sama. Union akan menghapus duplikat baris.

   Contoh:
   Misalkan Anda memiliki dua tabel: Products dan Sales. Anda dapat menggunakan union untuk menggabungkan data dari kedua tabel untuk mendapatkan daftar semua produk yang telah terjual.

3. Agregasi: menghitung nilai statistik dari data dalam satu tabel.
   Contoh fungsi agregasi:
   - COUNT: Menghitung jumlah baris.
   - SUM: Menghitung total nilai.
   - AVERAGE: Menghitung rata-rata nilai.
   - MAX: Menemukan nilai maksimum.
   - MIN: Menemukan nilai minimum.
   
   Contoh:
   Misalkan Anda memiliki tabel Orders. Anda dapat menggunakan agregasi untuk menghitung total penjualan.

4. Subquery: query yang di dalam query lain. Subquery dapat digunakan untuk menyaring data, melakukan perhitungan, dan menggabungkan data dari beberapa tabel.

   Contoh:
   Misalkan Anda memiliki tabel Customers dan Orders. Anda dapat menggunakan subquery untuk menemukan pelanggan yang telah melakukan pemesanan lebih dari 10 kali.

5. Function: blok kode yang dapat digunakan untuk melakukan perhitungan dan operasi pada data. Function dapat digunakan untuk membuat kode yang lebih ringkas dan mudah dibaca.

   Contoh:
   Misalkan terdapat tabel Products (id_produk, nama, harga). Kita dapat membuat function untuk menghitung harga diskon produk.
