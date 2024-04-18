# DATA WAREHOUSE DAN DATA LAKE PART 2

## Sharding in Citus (Distributed Table)
```bash
  CREATE TABLE companies (
       id bigint NOT NULL,
       name text. NOT NULL,
       inage orl text,
       created at timestamp without time zone NOT NULL, updated at timestamp without time zone NOT NULLa
  );

  ALTER TABLE companies ADD PRIMARY KEY (id): SELECT create distributed table('companies', 'id'):
```

## Skema Data

- Star Skema: Skema data yang sederhana dan mudah dipahami.
- Snowflake Schema: Skema data yang lebih ternormalisasi dan efisien.
- One Big Table (OBT): Skema data yang tidak ternormalisasi dengan kinerja yang baik.

## Best Practices Sharding

#### Multitenant:

- Partisi tabel terdistribusi dengan kolom id tenant umum.
- Ubah tabel kecil lintas tenant menjadi tabel referensi.
- Batasi filter semua kueri aplikasi berdasarkan id tenant.

#### Aplikasi Real-Time:

- Pilih kolom dengan kardinalitas tinggi sebagai kolom distribusi.
- Pilih kolom dengan distribusi merata.
- Distribusikan tabel fakta dan dimensi pada kolom umum mereka.
- Ubah beberapa tabel dimensi menjadi tabel referensi.

#### Data Time Series:

- Ubah beberapa tabel dimensi menjadi tabel referensi.
- Gunakan PostgreSQL, partisi tabel untuk waktu sebagai gantinya.

## Colocation

```bash
  CREATE TABLE event(
     tenant_id int,
     event_id bigint,
     page_id int,
     payload jsonb,
     primary key (tenant_id, event_id)
  );

  CREATE TABLE page (
     tenant_id int,
     page_id int,
     path taxt,
     primary key (tenant_id, page_id)
  );

SELECT create_distributed_table ('event','tenant_id');
SELECT creats_distributed_table ('page', 'tenant_id', 'colacate_with' => 'event');
```

Colocation adalah praktik menempatkan server dan infrastruktur jaringan di lokasi fisik yang sama, biasanya di pusat data pihak ketiga. Hal ini memungkinkan organisasi untuk meningkatkan kinerja, skalabilitas, dan keamanan aplikasi mereka.

#### sebagai informasi tambahan:
### Manfaat Colocation

- Peningkatan Kinerja: Colocation dapat membantu meningkatkan kinerja aplikasi dengan mengurangi latensi dan meningkatkan throughput. Hal ini karena server colocated terletak di dekat satu sama lain dan memiliki akses langsung ke jaringan berkecepatan tinggi.
- Skalabilitas: Colocation memungkinkan organisasi untuk dengan mudah menskalakan infrastruktur mereka sesuai kebutuhan. Hal ini karena mereka dapat menambahkan server dan perangkat keras lainnya ke pusat data colocated tanpa perlu membangun infrastruktur mereka sendiri.
- Keamanan: Colocation dapat membantu meningkatkan keamanan aplikasi dengan menyediakan lingkungan yang aman dan terkendali. Pusat data colocated biasanya memiliki keamanan fisik yang kuat, seperti kontrol akses biometrik dan kamera CCTV.
- Pengurangan Biaya: Colocation dapat membantu mengurangi biaya TI dengan memungkinkan organisasi untuk berbagi biaya infrastruktur dengan penyedia layanan colocation.

### Jenis Colocation
Terdapat 3 jenis pada colacation sebagai berikut:

- Dedicated Colocation: Jenis colocation ini memberi organisasi ruang khusus di pusat data. Ruang ini dapat dikonfigurasi sesuai dengan kebutuhan organisasi.
- Cage Colocation: Jenis colocation ini memberi organisasi ruang yang dikelilingi oleh pagar di pusat data. Hal ini memberikan tingkat keamanan tambahan.
- Shared Colocation: Jenis colocation ini memberi organisasi ruang bersama dengan organisasi lain di pusat data. Hal ini merupakan pilihan yang paling hemat biaya.

## Google Cloud Platform 

#### Apa itu Google Cloud Platform (GCP)?

**Google Cloud Platform (GCP)** adalah platform komputasi awan yang ditawarkan oleh Google. GCP berjalan di atas infrastruktur yang sama yang digunakan oleh Google untuk produk internalnya, seperti Google Search, YouTube, dan Gmail.

### Manfaat Menggunakan GCP

Ada banyak manfaat menggunakan GCP, antara lain:

Meningkatkan produktivitas: GCP dapat membantu Anda meningkatkan produktivitas dengan menyediakan akses ke berbagai layanan dan infrastruktur yang dapat Anda gunakan untuk membangun, meluncurkan, dan mengelola aplikasi dengan cepat dan mudah.
Meningkatkan efisiensi: GCP dapat membantu Anda meningkatkan efisiensi dengan mengotomatiskan tugas dan proses, dan dengan menyediakan skalabilitas yang Anda butuhkan untuk memenuhi permintaan yang fluktuatif.
Mengurangi biaya: GCP dapat membantu Anda mengurangi biaya dengan menyediakan model penetapan harga yang fleksibel dan dengan membantu Anda mengoptimalkan penggunaan sumber daya.
Meningkatkan keamanan: GCP dapat membantu Anda meningkatkan keamanan dengan menyediakan berbagai fitur keamanan yang canggih, seperti enkripsi data, kontrol akses, dan deteksi intrusi.

### Jenis Layanan GCP

GCP menawarkan berbagai jenis layanan, antara lain:

- Komputasi: GCP menawarkan berbagai layanan komputasi, seperti Compute Engine, Kubernetes Engine, dan Cloud Functions.
- Penyimpanan: GCP menawarkan berbagai layanan penyimpanan, seperti Cloud Storage, Cloud SQL, dan Cloud Spanner.
- Jaringan: GCP menawarkan berbagai layanan jaringan, seperti Cloud Load Balancing, Cloud CDN, dan Cloud VPC.
- Data dan analitik: GCP menawarkan berbagai layanan data dan analitik, seperti BigQuery, Dataproc, dan Cloud Dataflow.
- Kecerdasan buatan dan pembelajaran mesin: GCP menawarkan berbagai layanan kecerdasan buatan dan pembelajaran mesin, seperti Cloud AI Platform, Cloud TPUs, dan Cloud AutoML.
- Pengembangan aplikasi: GCP menawarkan berbagai layanan pengembangan aplikasi, seperti Cloud App Engine, Cloud Build, dan Cloud Source Repositories.
