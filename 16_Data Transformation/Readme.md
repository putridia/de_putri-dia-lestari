# Summary Data Transformation Part 1

### Data Transformation
Proses convert data dari 1 format atau struktur ke dalam bentuk atau format yang lainnya dan tersebut merupakan fundamental dalam proses integrasi data.

Kenapa Data Transformation Penting?

1. Memungkinkan data dari berbagai sumber untuk digabungkan.

   Hal ini memungkinkan untuk melihat gambaran yang lebih lengkap tentang suatu situasi. Misalnya, jika ingin mencoba melacak tren penjualan, mungkin ingin menggabungkan data dari sistem POS, situs web e-niaga, dan CRM Anda. Hal ini akan memberikan pemahaman yang lebih baik tentang bagaimana kinerja bisnis secara keseluruhan.

2. Memastikan kualitas dan konsistensi data.

   Ketika ingin menggabungkan data dari berbagai sumber, dapat juga mengidentifikasi dan memperbaiki inkonsistensi. Ini akan membantu untuk memastikan bahwa data tersebut akurat dan dapat dipercaya.

3. Memudahkan analisis data dan intelijen bisnis.

   Ketika data yang terpusat di satu tempat, dapat dengan mudah menganalisisnya dan mendapatkan wawasan yang berharga. Hal ini dapat membantu untuk membuat keputusan yang lebih baik tentang bisnis.

### Jenis Data Transformation

Ada banyak jenis transformasi data yang berbeda, tetapi beberapa yang paling umum adalah:

- Normalisasi: Scaling data ke standar rentang. Hal ini dapat dilakukan dengan berbagai cara, seperti min-max scaling dan z-score normalization.
- Encoding: Mengubah data kategorikal ke format numerik. Hal ini dapat dilakukan dengan berbagai cara, seperti one-hot encoding dan label encoding.
- Agregasi: Meringkas data untuk analisis. Hal ini dapat dilakukan dengan berbagai cara, seperti mean, median, dan mode.

### Normalisasi Data

Normalisasi data adalah proses mengubah data dari satu skala ke skala lain. Hal ini dilakukan dengan tujuan untuk membuat data lebih mudah dianalisis dan dipahami.

- Tujuan: Memastikan bahwa setiap fitur memberikan kontribusi yang sama terhadap komputasi dalam algoritma pembelajaran mesin.
- Metode Umum: Penskalaan Min-Max, normalisasi skor Z.
- Kasus Penggunaan: Jaringan saraf, algoritme yang mengandalkan besaran fitur.

### Pengertian Encoding Data Kategori

Encoding data kategori adalah proses mengubah data kategori menjadi format numerik. Hal ini dilakukan karena algoritma pembelajaran mesin membutuhkan data numerik agar dapat bekerja dengan baik.

- Tujuan: Algoritme pembelajaran mesin memerlukan masukan numerik, sehingga data kategorikal harus dikonversi.
- Metode Umum: Pengkodean one-hot: Menetapkan kolom biner untuk setiap kategori. Pengkodean label: Menetapkan bilangan bulat unik untuk setiap kategori. (Catatan: Metode ini dapat memperkenalkan hubungan ordinal yang mungkin tidak ada.)
- Kasus Penggunaan: Analisis regresi, tugas klasifikasi.

### Aggregasi

- Tujuan: Memberikan gambaran ringkasan data, sering kali untuk mengubah rinciannya.

- Metode Umum:
  - Sum
  - Average
  - Count: Jumlah total titik data.
  - Maks: Nilai tertinggi dalam kumpulan data.
  - Min: Nilai terendah dalam kumpulan data.

- Kasus Penggunaan: Data deret waktu, analisis berbasis grup.

### Tantangan dalam data transformtion :

Mengatasi data yang hilang, nilai yang hilang bisa terjadi karena kesalahan entry data, data sengaja tidak dikumpulkan / data corrupt. Metode : deletion (menghapus baris dengan nilai yang hilang), implutation (mengisi nilai yang hilang dengan data point lain, bisa dilakukan dengan melaukan rata2 dari 2 data point), forward/backward fill (mengisi nilai yang hilang dengan nilai sebelumnya).

- Menangani outliers Outliers merupakan nilai yang sangat berbeda dari kebanyakan nilai dalam dataset, dapat mempengaruhi hasil analisis. Metode : Z-Score , IQR (Interquartile Range)

- Memastikan integrasi data selama proses penyimpanan /transfer. Metode : regular backups, validation checks, checksums.
