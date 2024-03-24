# Summary Docker

## Virtual Machine
Sebuah perangkat lunak yang mensimulasikan komputer fisik.  Ibarat sebuah komputer di dalam komputer, VM memungkinkan untuk menjalankan sistem operasi dan aplikasi lain secara independen dari sistem operasi utama pada perangkat. VM  mensimulasikan  sebuah komputer fisik secara keseluruhan.  VM memiliki  sistem operasi  sendiri (guest OS) yang berjalan di atas lapisan perangkat lunak yang disebut hypervisor.  Hypervisor  bertanggung jawab mengalokasikan sumber daya hardware (CPU, RAM, storage) dan mengelola beberapa VM pada satu perangkat fisik.

## Container 
Container adalah unit mandiri yang mengemas sebuah aplikasi beserta dependensinya  (perangkat lunak yang dibutuhkan aplikasi untuk berjalan) menjadi satu kesatuan yang ringan dan portabel. Container  memvirtualisasikan  tingkat  sistem operasi  bukan hardware.  Container berbagi  kernel  dengan sistem operasi host,  hanya  mengemas  sebuah aplikasi beserta  dependensinya  (library dan binary yang dibutuhkan aplikasi) menjadi satu kesatuan yang portabel.

# Docker Basic 

## Docker 
Sebuah container manager yang dapat digunakan untuk mengelola aplikasi dalam bentuk container. Platform perangkat lunak open-source yang menggunakan konsep kontainerisasi untuk pengembangan, deployment, dan pengelolaan aplikasi. 

### Komponen Penting dalam Docker:
- Image: Blueprint atau cetakan yang mendefinisikan isi dari kontainer, termasuk kode aplikasi, library, dan dependensi lainnya. Anda dapat membuat image Anda sendiri atau menggunakan image yang sudah ada di public repository seperti Docker Hub.
- Container: Instance yang sedang berjalan dari sebuah image Docker. Anda dapat menjalankan beberapa kontainer dari image yang sama.
- Docker Engine: Perangkat lunak yang diinstal pada mesin Anda dan bertugas membuat dan menjalankan kontainer dari image Docker.
- Docker Registry: Gudang penyimpanan image Docker. Docker Hub adalah public registry yang populer, namun organisasi juga dapat memiliki registry privat untuk image internal.

### Alur Kerja Docker:
- Pengembang: Mengembangkan aplikasi dan membangun image Docker yang berisi kode aplikasi dan dependensinya.
- Deployment: Image Docker di-push ke registry (misalnya Docker Hub) atau disimpan di internal registry organisasi.
- Pengguna: Menjalankan kontainer dari image tertentu pada mesin dengan Docker engine terinstal. Docker engine mengambil image dari registry (bila perlu) dan membuat instance kontainer yang sedang berjalan.
- Aplikasi Berjalan: Kontainer yang berjalan mengeksekusi kode aplikasi dan dependensi yang tersimpan di dalamnya.

## Dockerfile Cheat Sheet

- FROM: Menspesifikasikan image dasar yang digunakan untuk membangun image baru.
- RUN: Menjalankan perintah shell pada saat pembuatan image.
- CMD: Menspesifikasikan perintah default yang dijalankan ketika container dimulai.
- COPY: Menyalin file atau folder dari host machine ke dalam container.
- WORKDIR: Mendefinisikan direktori kerja default di dalam container.
- EXPOSE: Mengekspos port pada container sehingga dapat diakses dari luar.
- ENV: Menetapkan variabel lingkungan yang dapat digunakan di dalam container.
- VOLUME: Mendefinisikan volume yang persisten, datanya akan tersimpan terpisah dari container.

Contoh:
```bash
FROM node:18

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY . .

CMD [ "npm", "start" ]
```

## Docker Basic Commands
1. Docker ps: Menampilkan daftar kontainer yang sedang berjalan. -a digunakan Menampilkan semua kontainer (termasuk yang berhenti).
   Contoh :
   ```bash
   docker ps
   docker ps -a
   ```

2. Docker Container Create: Membuat Container baru
   Contoh :
   ```bash
   docker container create -it --name redis1 redis:latest
   ```

3. Docker Container start: Menjalankan container

   Contoh:
   ```bash
   docker container start redis1
   ```

4. Docker Container stop: menghentikan container

   Contoh:
   ```bash
   docker container stop redis1
   ```

5. Docker Container rm: menghapus container dalam kondisi harus mati.

   Contoh:
   ```bash
   docker container rm redis1
   ```

6. Docker Container rm -f: Menghapus container meskipun masih running

   Contoh:
   ```bash
   docker container rm -f redis2
   ```

7. Melihat Semua Container yang Sedang Running

   Contoh:
   ```bash
   docker container ls docker ps
   ```

8. Melihat semua container (running maupun mati)

  Contoh:
  ```bash
  docker container ls -a docker ps -a
  ```

9. Melihat semua docker image dalam local

   Contoh:
   ```bash
   docker image
   ```

10. Docker pull: Mengunduh docker image

   Contoh:
   ```bash
   docker pull redis:latest
   ```

11. Docker push: Mempublish docker image ke docker hub

   Contoh:
   ```bash
   docker push myimage: 1.0.0
   ```

12. Docker run: Membuat dan menjalankan container

   Contoh:
   ```bash
   docker run -itd-name redis-app redis: latest
   ```

13. Docker exec: Menjalankan command di dalam container

   Contoh:
   ```bash
   docker exec-it redis-app redis-cli
   ```

14. Docker logs: Melihat log dari container

   Contoh: 
   ```bash
   docker logs redis-app
   ```

15. Docker inspect: Melihat informasi secora rinci mengenai container

   Contoh:
   ```bash
   docker inspect redis-app
   ```

16. Docker volume create: Membuat docker volume baru

   Contoh:
   ```bash
   docker volume create myvolume
   ```

17. Docker volume 1s: Menampilkan semua docker volume

18. Docker volume prune: Menghapus docker volume yang tidak terpakai

19. Docker network create: Membuat docker network baru.

   Contoh:
   ```bash
   docker network create mynetwork
   ```

20. Docker network connect: Membuat docker network baru

   Contoh:
   ```bash
   docker network create mynetwork
   ```

21. Docker network connect: Menyambungkan docker network kepada container yang sedang running maupun yang mati

   Contoh:
   ```bash
   docker network connect mynetwork myapi
   ```

## Docker Volume

Dalam dunia kontainer Docker, volume berperan sebagai tempat penyimpanan data yang persisten (tetap ada)  walaupun kontainer dihentikan atau dihapus.

Keuntungan menggunakan Docker Volume:
- Persistensi Data: Data yang disimpan dalam volume tidak akan hilang ketika kontainer dihentikan atau dihapus. Ini sangat penting untuk aplikasi yang perlu menyimpan data, seperti database, aplikasi web dengan upload file, atau sistem logging.
- Keamanan Data: Volume dapat disimpan di lokasi terpisah dari image dan kontainer Docker, sehingga meningkatkan keamanan data Anda.
- Kemandirian Kontainer: Kontainer dapat dengan mudah dipindahkan atau di-scale tanpa perlu khawatir kehilangan data yang tersimpan di volume.
- Kolaborasi: Volume dapat dibagikan di antara beberapa kontainer, sehingga memudahkan kolaborasi antar kontainer yang membutuhkan akses ke data yang sama.

## Docker network

Dalam dunia kontainer Docker, jaringan memungkinkan kontainer untuk saling berkomunikasi satu sama lain, serta dapat diakses dari host machine (mesin tempat Docker engine berjalan) atau kontainer lain di jaringan eksternal.

## Docker Compose

Docker Compose adalah alat yang dibangun di atas Docker untuk mendefinisikan dan menjalankan aplikasi yang terdiri dari beberapa kontainer.  Dengan Docker Compose, Anda dapat menentukan semua layanan yang membentuk aplikasi Anda dan bagaimana mereka saling terkait dalam  sebuah file YAML (Yet Another Markup Language).

### Container Orchestration
Container Orchestration (Container Orkestrasi) adalah proses mengotomatiskan deployment, manajemen, scaling, dan networking  sejumlah kontainer yang tersebar di beberapa host kontainer.

Keuntungan menggunakan Container Orchestration:
- Menjalankan Aplikasi Multi-Kontener: Sebagian besar aplikasi modern dibangun dengan arsitektur microservices, yang melibatkan pemecahan aplikasi menjadi layanan kecil dan independen. Container Orchestration membantu mengelola dan menjalankan layanan tersebut secara terkoordinasi.
- Skalabilitas: Container Orchestration memungkinkan Anda untuk dengan mudah menambah atau mengurangi jumlah kontainer yang sedang berjalan untuk menangani perubahan beban pada aplikasi.
- High Availability: Container Orchestration dapat digunakan untuk menjalankan kontainer secara redundant di beberapa host kontainer. Jika salah satu kontainer mengalami kesalahan, Orchestrator dapat secara otomatis memindahkan kontainer tersebut ke host lain untuk menjaga agar aplikasi tetap berjalan.
- Manajemen Sumber Daya: Container Orchestration membantu mengalokasikan dan memantau penggunaan sumber daya komputasi (CPU, memory, storage) secara efisien di antara kontainer yang berjalan.
