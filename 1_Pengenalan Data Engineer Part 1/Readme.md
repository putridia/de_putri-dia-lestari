
# Summary Pengenalan Data Engineer Part #1

## Fundamental Data Engineer

**Data Engineering** adalah sebuah proses yang kita ambil dari data mentah(raw data) yang nantinya akan dilakukan proses seperti, proses cleaning, proses transforming, proses analisis dan proses publish.

### Proses gambaran Data Engineering :
- Mengumpulkan beberapa data **(Data Ingestion)**
- Data yang dikumpulkan akan di **transformation** melalui beberapa tahapan seperti, cleaning dan sebagainya.
- Hasil data yang selesai di transformation selanjutnya ke **Data Serving**, pada data serving berisi sekumpulan data yang siap digunakan untuk aplikasi seperti, aplikasi analytic, aplikasi bisnis intelegent dan sebagainya.

### Keterampilan atau Skill yang dipersiapkan untuk menjadi Data Engineer : 
- Bahasa Pemrograman : **Phyton** (salah satu bahasa yang cukup populer untuk digunakan seorang data engineer)
- Menguasasi **SQL** (Structured Query Language), dikarenakan untuk melakukan query ke database kita perlu menggunakan SQL.
- Menguasai pengetahuan dasar **Cloud (AWS, GCP)**
- Menguasai **tools** yang digunakan untuk **pemrosesan BIG DATA** seperti, Apache Hadoop, Scala dan Apache Hive. 

### Bagaimana kita mendapatkan data mentah?
Yang harus perlu kita ketahui untuk mendapatkan data mentah dari berbagai sumber seperti:
- **Consumer Software System** (Tiktok, Amazon)
- **Internal System** (Salesforce, CRM, Accounting, HR)
- **Internal Business Users** (Excel, Spreadsheet)
- **IoT Devices** (Solar Panels, Automobilies, Cell Phones)

## Definisi Data Pipeline 
**Data Pipeline** adalah sekumpulan pemrosesan untuk mepersiapkan data yang nantinya data ini siap untuk digunakan. Pada Data Pipeline terdapat beberapa tahapan yaitu : 

- **Data Ingestion** : Pengumpulan data dari berbagai sumber seperti, dari aplikasi, database, dan cloud storage. 

- **Data Transformation** : Melakukan proses data seperti, data preparation, distributed processing dan bahkan pemrosesan stream dan batch processing.

Selesai dari data transformation dapat dimanfaatkan melalui data warehousing bisa digunakan untuk aplikasi AI. Kemudian dapat dimanfaatkan Query & Analytics Engine yang bisa digunakan untuk framework machine learning seperti, tensorflow.

### Jenis - Jenis Data Pipeline 

![Screenshot (1908)](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/5c512091-c423-4348-9251-2e035bbccc3c)

Data Pipeline dibedakan 2 jenis yaitu :

- **Berdasarkan Urutan Aliran Tranformasi :** ETL dan ELT 

  - **ETL (Extract-Transform-Load)** adalah Proses saluran data mengekstrak data mentah dari berbagai sumber, selanjutnya akan menyimpan sementara di staging area. Transformation data di staging area dan memuat ke dalam data warehouse atau data lake (berisi data yang sudah diolah) yang selanjutnya akan dimanfaatkan untuk analisis.

  - **ELT (Extract-Load-Transform)** adalah Proses dimulai data pipeline mengekstrak dan memuat data langsung ke data warhouse atau data lake (berisi data yang masih mentah). Kemudian setelah melakukan transformation atau perubahan data bisa digunakan untuk analisis.

  #### Perbedaan ETL dan ELT : 
  
  |     | ETL    | ELT   |
  | ----| -------| ------|
  | **Keuntungan**       | Data lebih bersih mengenai duplikat dihapus, memungkinkan analisis lebih cepat dan stabil. Penyimpanan lebih hemat dan mempunyai teknologi yang matang. | Lebih fleksibel : ekstrak, muat, transformasi data, percepat iterasi laporan, dan minimalkan perawatan. |
  | **Kekurangan**       | Kurang fleksibel, proses transformasi data sebelum memuat memperlambat proses dan kesalahan dapat mencegah pemuatan. | Menyimpan data mentah, penyimpanan cloud membutuhkan banyak ruang |
  | **Waktu Penggunaan** | Perusahaan yang diatur oleh GDPR, HIPAA, atau CCPA harus mematuhi peraturan privasi data dan melindungi alamat IP klien. | Saat analisis mendesak, ELT lebih cepat daripada ETL. ELT juga berguna untuk pengembangan model machine learning. | 

- **Berdasaran Sumber Data :** Batch Pipeline dan Stream Pipeline  

   - **Batch Pipeline** : Batch processing sendiri adalah saat pemrosesan dan analisis terjadi pada sekumpulan data yang telah disimpan selama periode waktu tertentu, dan nantinya hasil dari pengolahan ini dapat ditulis pada database atau HDFS. Contoh: Sistem penggajian dan penagihan yang harus di proses mingguan atau bulanan.

   - **Stream Pipeline** : Data yang digunakan yaitu data yang secara real-time atau secara langsung. Definisi nya sendiri Stream pipeline adalah proses berurutan dalam menyerap, memproses, dan mengelola aliran data secara terus menerus saat data tersebut masih bergerak.

### Apa itu Streaming Data?
**Streaming Data** adalah sebuah proses untuk membaca sekumpulan data secara berkelanjutan, seperti contoh kita melacak aktivitas klien dalam sebuah game, membaca informasi dari sosial media dan mentracking user pada halaman web.

#### Perbedaan dari Batch dan Streaming Data Pipeline :

  |     | Batch Data Pipeline    | Stream Data Pipeline   |
  | ----| -----------------------| -----------------------|
  | Performance | Latensi bisa dalam hitungan menit, jam, atau hari | Litensi harus dijamin dalam milidetik |
  | Dataset     | Sejumlah data besar | Aliran data yang berkelanjutan |
  | Analysis    | Komputasi dan analisis yang cukup kompleks dalam jangka waktu yang lebih besar | Pelaporan atau perhitungan sederhana |
