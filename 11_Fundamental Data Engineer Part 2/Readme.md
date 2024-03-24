# Summary Fundamental Data Engineer Part 2

# Data Terstruktur
Data terstruktur adalah jenis data yang terorganisir dengan rapi dan mengikuti format yang telah ditentukan sebelumnya.  Mirip seperti formulir, data terstruktur memiliki:

- **Model data:** Ini seperti kerangka yang menentukan jenis informasi yang dapat disimpan. Pikirkan seperti kategori dalam formulir, misalnya "Nama", "Alamat", atau "Kode Pos".
- **Format:** Ini menentukan cara penulisan informasi tersebut. Misalnya, Nama harus berupa teks, sedangkan Kode Pos harus berupa angka.
- **Skema:** Ini seperti keseluruhan struktur data, yang mencakup model data dan formatnya. Skema memastikan konsistensi dalam penyimpanan data.

Sebagai contoh, bayangkan data pelanggan dalam sebuah toko online.  Data terstruktur untuk pelanggan mungkin memiliki kolom-kolom seperti "Nama Depan", "Nama Belakang", "Email", dan "Alamat".  Semua informasi ini disimpan dengan format yang konsisten, memudahkan pencarian dan pengelolaan data.

## Kelebihan Data Terstruktur:
- **Mudah Dicari:** Karena terorganisir dengan baik, data terstruktur mudah dicari menggunakan bahasa khusus bernama SQL (Structured Query Language). Dengan SQL, Anda dapat mengajukan pertanyaan tertentu tentang data, seperti "Temukan semua pelanggan yang tinggal di kota Jakarta".
- **Membutuhkan Lebih Sedikit ruang penyimpanan:** Efisiensi dalam penyimpanan data terstruktur membuatnya hemat ruang penyimpanan. Ini penting untuk perusahaan yang memiliki banyak data.

Meskipun berguna, perkiraan hanya 20% data perusahaan berupa data terstruktur.  Jenis data lain, seperti email, foto, dan pesan media sosial, umumnya tidak terstruktur atau semi-terstruktur.

# Data Tidak Terstruktur
Data tidak terstruktur adalah data yang memiliki struktur internal, namun tidak terorganisir melalui model atau skema data yang telah ditentukan sebelumnya.  Data ini tidak dapat dengan mudah disimpan dalam database relasional seperti SQL dan memerlukan pemrosesan lanjutan agar bisa dicari.

## Contoh Data Tidak Terstruktur:
- Dokumen teks, PDF, gambar, video
- Media sosial: data dari Twitter, Facebook, Instagram

Diperkirakan 80% data perusahaan saat ini berupa data tidak terstruktur. Jenis data ini membutuhkan penyimpanan yang lebih besar dibandingkan dengan data terstruktur.

Dengan memahami dan mengolah data tidak terstruktur, perusahaan bisa mendapatkan berbagai manfaat, seperti:

- Meningkatkan Pengambilan Keputusan: Data ini bisa memberikan insights berharga yang tidak bisa didapatkan dari data terstruktur saja.
- Mengembangkan Produk dan Layanan Baru: Menganalisis data media sosial misalnya, bisa membantu memahami kebutuhan dan preferensi pelanggan.
- Mencegah Penipuan: Analisa data transaksi keuangan bisa membantu mendeteksi aktivitas mencurigakan.

# Data Semi-Terstruktur
Data semi-terstruktur berada di antara data terstruktur dan tidak terstruktur.

- Berbeda dengan data terstruktur: Data semi-terstruktur tidak memiliki skema yang kaku. Artinya, data ini tidak mengikuti format tabel data atau struktur database relasional yang ketat.
- Mirip dengan data tidak terstruktur: Data semi-terstruktur tidak memiliki format yang baku dan fleksibel.

Namun, ada hal yang membedakan data semi-terstruktur dengan data tidak terstruktur, yaitu:

- Memiliki penanda pengklasifikasian: Data semi-terstruktur memiliki karakteristik berupa penanda pengklasifikasian, seperti metadata. Metadata ini memungkinkan data untuk dianalisis.
- Mirip dengan metadata pada data tidak terstruktur: Metadata pada data semi-terstruktur ini mirip fungsinya dengan metadata pada data tidak terstruktur, yang membantu memberikan informasi dan konteks pada data itu sendiri.

# Relational vs NoSQL Database

## Relational Database:
Definisi: Sebuah sistem penyimpanan data yang terstruktur dalam tabel-tabel dengan baris dan kolom. Setiap tabel mewakili entitas atau objek dalam sistem, dan setiap baris dalam tabel mewakili satu contoh dari entitas tersebut. Kolom dalam tabel mewakili atribut atau karakteristik entitas tersebut.
Struktur: Data teroganisir dalam tabel dengan skema yang kaku dan terdefinisi. Skema menentukan kolom apa yang ada di setiap tabel, tipe data apa yang disimpan di setiap kolom, dan hubungan apa yang ada antar tabel.
Contoh: MySQL, PostgreSQL, Oracle

# Database Normalization
Normalisasi database adalah sebuah teknik untuk mengatur dan merestrukturisasi tabel-tabel dalam database relasional. Tujuannya adalah untuk:

- Mengurangi redundansi data: Menghilangkan duplikasi data yang tidak perlu, sehingga menghemat space penyimpanan dan mengurangi risiko inkonsistensi data.
- Meningkatkan integritas data: Memastikan keakuratan dan keandalan data dengan meminimalkan kemungkinan kesalahan saat memasukkan, memperbarui, atau menghapus data.
- Mempermudah pengelolaan data: Membuat struktur database lebih efisien dan mudah dipahami, sehingga memudahkan query, update, dan pemeliharaan data.
Proses Normalisasi:

Normalisasi database dilakukan melalui tahapan-tapan tertentu, yang dinamakan bentuk normal. Semakin tinggi bentuk normal, semakin baik struktur dan integritas data dalam database. Berikut beberapa bentuk normal yang umum digunakan:

1. First Normal Form (1NF):
- Setiap atribut (kolom) dalam tabel harus memiliki tipe data yang jelas dan tidak mengandung grup data berulang.
- Setiap baris (record) dalam tabel harus bisa diidentifikasi secara unik menggunakan primary key (kunci utama).

2. Second Normal Form (2NF):
- Memenuhi semua kriteria 1NF.
- Tidak ada atribut yang tergantung sebagian pada primary key. Artinya, semua atribut harus bergantung sepenuhnya pada primary key atau keseluruhan primary key.

3. Third Normal Form (3NF):
- Memenuhi semua kriteria 2NF.
- Tidak ada atribut yang tergantung transitif pada primary key. Artinya, tidak ada atribut yang bergantung pada atribut lain yang bergantung pada primary key.

## NoSQL Database:

Definisi: Sebuah sistem penyimpanan data non-relasional yang dirancang untuk menangani berbagai jenis data dan skala data yang besar. NoSQL database tidak memiliki skema yang kaku seperti relational database, dan mereka menawarkan fleksibilitas yang lebih besar dalam hal bagaimana data disimpan dan diakses.
Struktur: Data disimpan dalam berbagai format, seperti dokumen, key-value pairs, atau graph.
Contoh: MongoDB, Cassandra, redis

## NoSQL : Key-value Database
Data sebagai Pasangan Key-Value: Data disimpan dalam bentuk pasangan key-value.
- Key (Kunci): bertindak sebagai pengenal unik untuk setiap item data. Kunci ini bisa berupa string, angka, atau identifier lainnya.
- Value (Nilai): berisi data aktual yang ingin Anda simpan. Nilai ini bisa berupa berbagai format, seperti string, angka, list, object, atau bahkan dokumen JSON.

Key-value database menawarkan performa dan skalabilitas yang sangat baik, menjadikannya pilihan ideal untuk aplikasi yang membutuhkan penyimpanan data sederhana dan cepat. Namun, keterbatasannya dalam query kompleks perlu dipertimbangkan sebelum memilih jenis database ini untuk kebutuhan. 

## Use Case untuk Key-Value Database

Berikut beberapa use case umum untuk Key-Value Database:

1. Cache: Key-Value Database sering digunakan sebagai cache untuk menyimpan data yang sering diakses dari sumber data lain yang lebih lambat, seperti database relasional. Ini dapat secara signifikan meningkatkan performa aplikasi dengan mengurangi beban pada sumber data utama.

Contoh:
Sebuah website e-commerce dapat menggunakan KVDB untuk menyimpan informasi produk yang dilihat baru-baru ini oleh pengguna, sehingga produk tersebut dapat dimuat dengan cepat pada kunjungan berikutnya.

2. Session Management:  Key-Value Database sangat cocok untuk menyimpan informasi sesi pengguna, seperti keranjang belanja, ID sesi, dan preferensi pengguna. Karena datanya bersifat sementara dan dihapus setelah sesi berakhir, struktur sederhana Key-Value Database ideal untuk menyimpan dan mengambil informasi ini dengan cepat.

Contoh:
Aplikasi web yang membutuhkan pelacakan keranjang belanja atau sesi login pengguna dapat memanfaatkan Key-Value Database untuk menyimpan dan mengelola data ini.

3. Leaderboard dan Ranking:  Key-Value Database berguna untuk menyimpan skor dan peringkat pengguna dalam game atau aplikasi. Struktur sederhana KVDB memungkinkan update skor yang cepat dan efisien, serta pemindaian untuk menampilkan peringkat teratas.

Contoh:
Game mobile dengan leaderboard skor tertinggi dapat menggunakan KVDB untuk menyimpan skor pemain dan menampilkan peringkat secara real-time.

4. Configurasi Aplikasi:  Key-Value Database dapat menyimpan berbagai konfigurasi aplikasi, seperti pengaturan global atau preferensi pengguna individual. Ini memungkinkan pembaharuan konfigurasi yang mudah dan fleksibel tanpa perlu memodifikasi kode aplikasi.

Contoh:
Sebuah aplikasi mobile dapat menggunakan Key-Value Database untuk menyimpan pengaturan bahasa yang dipilih pengguna atau konfigurasi lainnya yang perlu diakses dengan cepat.

5. Real-time Analytics:  Key-Value Database dapat digunakan untuk mengumpulkan dan menyimpan data real-time dari berbagai sumber, seperti sensor IoT atau log aplikasi. Struktur sederhana Key-Value Database memungkinkan penyimpanan data yang cepat dan pengambilan data yang efisien untuk analisis real-time.

Contoh:
Sistem pemantauan IoT dapat menggunakan Key-Value Database untuk menyimpan data sensor real-time dari perangkat yang terhubung, seperti suhu atau tingkat energi.

## NoSQL: Mengenal Wide-Column Database
Di antara berbagai jenis database NoSQL, Wide-Column Database (W-CDB) menawarkan pendekatan unik untuk menyimpan dan mengelola data.  Berbeda dengan database relasional yang menggunakan skema terdefinisi ketat, W-CDB menggunakan struktur yang lebih fleksibel dan dapat menangani data terstruktur, semi-terstruktur, dan bahkan tidak terstruktur.

## NoSQL: Document DB
Di dunia database NoSQL, Document Database menawarkan cara yang fleksibel dan efisien untuk menyimpan dan mengelola data.  Berbeda dengan database relasional yang menggunakan tabel terstruktur, Document Database menyimpan data dalam format dokumen, seperti JSON, XML, atau BSON. Namun, keterbatasan dalam melakukan kueri kompleks dan konsistensi data perlu dipertimbangkan sebelum memilih Document Database untuk kebutuhan yang spesifik.

## NoSQL: Graph DB
Di antara varian database NoSQL, Graph Database menawarkan pendekatan unik untuk menyimpan dan memodelkan hubungan antar data.  Berbeda dengan database relasional yang menggunakan tabel terstruktur, Graph Database menggunakan konsep graf yang terdiri dari node (entitas) dan edges (hubungan) untuk merepresentasikan hubungan antar data.

# OLTP vs OLAP

OLTP (Online Transaction Processing) dan OLAP (Online Analytical Processing) adalah dua sistem pemrosesan data yang berbeda dengan fungsi dan tujuan yang saling melengkapi.

## OLTP (Online Transaction Processing)

**Fokus:** Berfokus pada pemrosesan transaksi online secara efisien dan real-time.
**Contoh:** Sistem kasir di toko retail, pemesanan online di website e-commerce, atau aplikasi mobile banking.
**Karakteristik:**
- Menangani volume transaksi yang tinggi.
- Memprioritaskan kecepatan dan respon real-time.
- Menggunakan database relasional ternormalisasi untuk optimalisasi query transaksi.
- Fokus pada akurasi dan konsistensi data.

## OLAP (Online Analytical Processing)

**Fokus:** Berfokus pada analisa data historis untuk pengambilan keputusan dan intelijen bisnis.
**Contoh:** Analisis penjualan bulanan, laporan tren pelanggan, atau peramalan permintaan produk.
**Karakteristik:**
- Menangani data dalam jumlah besar (big data).
- Memprioritaskan kueri kompleks untuk analisa data.
- Menggunakan database atau data warehouse yang terdenormalisasi untuk mempercepat agregasi data.
- Fokus pada tren dan pola data historis.

# Dake Lake
Repository penyimpanan data terpusat dalam format mentah (raw) dan terstruktur. Data Lake menyimpan berbagai macam data dari berbagai sumber, tanpa perlu terlebih dahulu didefinisikan strukturnya dengan tools seperti, Amazon S3 dan Google Cloud Storage.

# Data Warehouse
Data warehouse adalah sistem penyimpanan data terpusat yang dirancang khusus untuk analitik data. Berbeda dengan data lake yang menyimpan data mentah dalam berbagai format, data warehouse menyimpan data terstruktur, terintegrasi, dan historis yang telah melalui proses pembersihan, transformasi, dan pemuatan (extract, transform, load - ETL).

# Data Mart
Data mart adalah bagian integral dari ekosistem data warehouse. Bisa dibilang, data mart adalah versi mini atau subset dari data warehouse yang berfokus pada kebutuhan analisa data departemen atau tim tertentu.

**Contoh Penggunaan Data Mart:**

- Tim pemasaran: Data mart pemasaran mungkin berisi data pelanggan, kampanye pemasaran, dan data penjualan untuk membantu tim menganalisa efektivitas kampanye dan membuat keputusan pemasaran yang lebih strategis.
- Tim penjualan: Data mart penjualan mungkin berisi data prospek, peluang penjualan, dan riwayat interaksi pelanggan untuk membantu tim penjualan melacak kemajuan dan mengidentifikasi peluang penjualan baru.