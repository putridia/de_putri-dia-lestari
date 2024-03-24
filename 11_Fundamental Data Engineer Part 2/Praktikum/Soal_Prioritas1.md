# Soal Prioritas 1

# 1. Jelaskan perbedaan antara data terstruktur dan data tidak terstruktur. Berikan contoh untuk masing-masing dan bahas bagaimana mereka biasanya disimpan dan diproses.

### Perbedaan antara Data Struktur dan Data Tidak Terstruktur
**Data Struktur** mengacu pada data yang diatur dalam format yang teratur dan terstruktur. Data ini biasanya ditemukan dalam basis data relasional atau data yang diatur dalam format lain yang memungkinkan untuk diorganisir dalam tabel, baris, dan kolom. Data yang cocok dengan tabel data dan mencakup tipe data diskret, seperti angka, teks pendek, dan tanggal. Contoh data struktur adalah data dalam tabel basis data seperti SQL atau spreadsheet seperti Excel.

Pada Format Data, Data terstruktur harus selalu mematuhi format yang ketat, yang dikenal sebagai model data atau skema yang telah ditentukan sebelumnya.

Contoh:
Data penjualan yang disimpan dalam basis data relasional. Data ini mungkin mencakup tabel untuk produk, pelanggan, dan pesanan, dengan kolom untuk nama produk, harga, nama pelanggan, dll.

**Data Tidak Terstruktur**, di sisi lain, adalah data yang tidak diatur dalam format yang terstruktur. Data ini tidak cocok dengan tabel data karena ukuran atau sifatnya. Terkadang, data numerik atau tekstual dapat menjadi tidak terstruktur karena pemodelannya sebagai tabel tidak efisien. Data ini mungkin tidak memiliki format yang jelas atau mudah diidentifikasi, dan sering kali sulit untuk diolah dengan cara yang sama seperti data terstruktur. Contoh data tidak terstruktur termasuk teks bebas, email, media sosial, dan file multimedia seperti gambar dan video.

Pada Format Data, Data tidak terstruktur tidak sesuai dengan skema. Format data tidak terstruktur yang ditentukan mungkin sama sederhananya dengan mengharuskan semua rekaman rapat dalam format MP3, atau semua peristiwa sistem harus dikumpulkan dalam penyimpanan tertentu. 

Contoh:
Data Tidak Terstruktur: Tweet dari Twitter. Data ini tidak memiliki format yang terstruktur dan mungkin berisi teks, gambar, dan tautan dalam format yang tidak teratur. Untuk menganalisis data ini, perlu dilakukan ekstraksi dan pemrosesan untuk mengidentifikasi informasi yang berguna seperti sentimen atau topik yang dibahas.

### Proses dan Penyimpanan Data Struktur dan Tidak Terstruktur
**Data Struktur:** Proses untuk data struktur melibatkan identifikasi kebutuhan data, perancangan basis data yang sesuai, pengembangan skema basis data, dan implementasi basis data menggunakan sistem manajemen basis data (DBMS) seperti MySQL, PostgreSQL, atau Oracle. Data struktur disimpan dalam format yang terorganisir dan biasanya diakses menggunakan bahasa kueri seperti SQL.

**Data Tidak Terstruktur:** Proses untuk data tidak terstruktur melibatkan pengidentifikasian sumber data, pengumpulan data, dan mungkin penggunaan algoritma pemrosesan bahasa alami (NLP) atau teknik pembelajaran mesin lainnya untuk mengorganisir dan menganalisis data. Penyimpanan data tidak terstruktur dapat dilakukan dalam format file, database NoSQL seperti MongoDB atau Cassandra, atau dalam sistem penyimpanan objek seperti Amazon S3 atau Azure Blob Storage.

Sumber Referensi: 
- [Referensi 1](https://aws.amazon.com/id/compare/the-difference-between-structured-data-and-unstructured-data/)
- [Referensi 2](https://apriandito.medium.com/data-terstruktur-semi-struktur-dan-tidak-terstruktur-fc5227cf233b)

# 2. Apa itu basis data relasional dan bagaimana cara kerjanya? Berikan contoh penggunaannya dalam dunia nyata.

Basis Data Relasional (Relational Database)
Basis data relasional adalah jenis basis data yang menggunakan format tabel dengan baris dan kolom untuk mengatur data. Setiap tabel mewakili objek dalam sistem, dengan setiap baris berisi data spesifik untuk objek tersebut. Kolom dalam tabel mencerminkan atribut atau karakteristik dari objek tersebut.

Cara Kerja Basis Data Relasional:
Basis data relasional bekerja dengan menyediakan lingkungan tempat aplikasi mengakses data dan menyusunnya kembali dengan berbagai cara tanpa harus mengatur ulang tabel data dari dalam kode aplikasi.
- Struktur Data: Data disimpan dalam tabel-tabel yang terdiri dari baris dan kolom.
- Relasi antar Tabel: Tabel-tabel dihubungkan satu sama lain melalui kolom-kolom yang sama, yang disebut kunci (key).
- Kunci Utama: Setiap tabel memiliki satu kolom yang disebut kunci utama (primary key) yang uniquely identifies each row.
- Kunci Asing: Kolom yang menghubungkan satu tabel dengan tabel lain disebut kunci asing (foreign key).
- Querying Data: Data dapat diakses dan dimanipulasi melalui bahasa query seperti SQL.

Contoh Basis Data Relasional dalam Dunia Nyata:
- Sistem Penjualan: Menyimpan data tentang produk, pelanggan, dan transaksi penjualan.
- Sistem Perpustakaan: Menyimpan data tentang buku, anggota, dan peminjaman buku.

Sumber Referensi: 
- [Referensi 1](https://aws.amazon.com/id/relational-database/#:~:text=sangat%20nyaman%20digunakan.-,Bagaimana%20cara%20kerja%20basis%20data%20relasional,data%20dari%20dalam%20kode%20aplikasi.)
- [Referensi 2](https://appmaster.io/id/blog/apa-itu-basis-data-relasional)

# 3. Jelaskan konsep normalisasi basis data dan mengapa hal ini penting dalam konteks basis data relasional.

### Normalisasi Basis Data

Normalisasi basis data adalah proses menata struktur tabel dalam basis data relasional untuk meminimalkan redundansi dan inkonsistensi data. Proses ini melibatkan pengelompokan data terkait dalam tabel yang terpisah dan mendefinisikan hubungan antar tabel tersebut.

Tahapan Normalisasi
- Normalisasi Tingkat Pertama (1NF): Memastikan setiap kolom dalam tabel hanya berisi satu nilai, tidak ada nilai yang berulang, dan setiap entitas memiliki kunci unik.
- Normalisasi Tingkat Kedua (2NF): Memastikan setiap non-kunci atribut sepenuhnya bergantung pada kunci utama, bukan pada bagian dari kunci.
- Normalisasi Tingkat Ketiga (3NF): Memastikan setiap non-kunci atribut tidak bergantung pada atribut non-kunci lainnya, melainkan hanya pada kunci utama.

### Pentingnya Normalisasi dalam Konteks Basis Data Relasional
- Mengurangi Redudansi Data: Dengan menghapus data yang berulang, normalisasi menghemat ruang penyimpanan dan mengurangi kemungkinan inkonsistensi data.

- Meningkatkan Fleksibilitas: Basis data yang sudah dinormalisasi lebih mudah untuk diubah dan diperbarui tanpa mengorbankan integritas data.

- Memastikan Konsistensi Data: Normalisasi membantu memastikan bahwa data yang dimasukkan ke dalam basis data adalah akurat dan konsisten.

- Meningkatkan Kinerja Query: Dengan struktur yang lebih terorganisir, query dapat dieksekusi lebih efisien, karena tidak perlu mengakses data yang tidak relevan.