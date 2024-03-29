# Summary Data Warehouse and Data Lake 

Data Warehouse adalah penyimpanan terstruktur yang berisi data historis yang telah melalui proses pembersihan dan pemrosesan untuk tujuan tertentu, misalnya analisa bisnis atau pembuatan laporan. Sistem yang mengumpulkan data dari berbagai sumber ke dalam satu tempat penyimpanan data yang terpusat dan konsisten untuk mendukung Data Analyst, Data Mining, Artificial Intelligence(AI), dan Machine Learning.

Data Lake yaitu sebaliknya, adalah penyimpanan yang bisa menampung segala macam data, baik terstruktur maupun tidak terstruktur, dalam bentuk mentah. Data Lake ibarat danau yang menampung semua aliran data dari berbagai sumber, tanpa peduli apakah datanya sudah siap pakai atau belum.  Para saintis data dapat memanfaatkan Data Lake untuk keperluan analisa yang lebih luas, termasuk misalnya Machine Learning.

## Data Lake vs Data Warehouse
- Sebuah Data Lake cenderung mencakup data mentah dalam jumlah besar, yang tujuannya mungkin belum ditentukan.
- Data Warehouse adalah tempat penyimpanan data terstruktur dan tersaring yang telah diproses untuk tujuan tertentu.

## Definisi Citus
- Ekstensi sumber terbuka untuk PostgreSQL yang mengubah Postgres menjadi basis data terdistribusi.
- Menggunakan tabel terdistribusi, tabel referensi, dan mesin kueri SQL terdistribusi

## Keuntungan Citus
- Tabel terdistribusi dipecah-pecah di sekelompok node PostgreSQL untuk menggabungkan CPU, memori, penyimpanan, dan kapasitas I/O.
- Tabel referensi direplikasi ke semua node untuk penggabungan dan kunci asing dari tabel terdistribusi dan kinerja pembacaan maksimum.
- Rute mesin kueri terdistribusi dan memparalelkan SELECT, DML, dan operasi lainnya pada tabel terdistribusi di seluruh cluster.
- Penyimpanan kolumnar memampatkan data, mempercepat pemindaian, dan mendukung proyeksi cepat, baik pada tabel biasa maupun tabel terdistribusi.
- Kueri dari node mana pun memungkinkan Anda memanfaatkan kapasitas penuh cluster Anda untuk kueri terdistribusi

## Columnar Table
Penyimpanan data berorientasi kolom menawarkan beberapa keuntungan dalam hal kecepatan akses dan kompresi data. Namun, perlu dipertimbangkan juga kompleksitas dan waktu penulisan yang lebih lambat sebelum memilih metode ini.

## Replication vs Sharding
- Replikasi: Data yang sama disalin di antara beberapa nodedan digunakan untuk pencadangan / ketersediaan tinggi 
- Sharding: Data dipotong-potong menjadi beberapa bagian dan didistribusikan di antara beberapa node Digunakan untuk pemrosesan/penyimpanan terdistribusi dapat menyimpan data yang lebih besar dari kapasitas node.