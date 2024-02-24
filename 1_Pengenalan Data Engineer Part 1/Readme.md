
# Summary Pengenalan Data Engineer Part #1

## Fundamental Data Engineer

**Data Engineering** adalah sebuah proses yang kita ambil dari data mentah(raw data) yang nantinya akan dilakukan proses seperti, proses cleaning, proses transforming, proses analisis dan proses publish.

### Keterampilan atau Skill yang dipersiapkan untuk menjadi Data Engineer : 
- Bahasa Pemrograman : **Phyton** 
- Menguasasi **SQL** (Structured Query Language)
- Menguasai pengetahuan dasar **Cloud (AWS, GCP)**
- Menguasai **tools** yang digunakan untuk **pemrosesan BIG DATA** seperti, Apache Hadoop, Scala dan Apache Hive. 

## Definisi Data Pipeline 
**Data Pipeline** adalah sekumpulan pemrosesan untuk mepersiapkan data yang nantinya data ini siap untuk digunakan. 

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

#### Perbedaan dari Batch dan Streaming Data Pipeline :

  |     | Batch Data Pipeline    | Stream Data Pipeline   |
  | ----| -----------------------| -----------------------|
  | Performance | Latensi bisa dalam hitungan menit, jam, atau hari | Litensi harus dijamin dalam milidetik |
  | Dataset     | Sejumlah data besar | Aliran data yang berkelanjutan |
  | Analysis    | Komputasi dan analisis yang cukup kompleks dalam jangka waktu yang lebih besar | Pelaporan atau perhitungan sederhana |
