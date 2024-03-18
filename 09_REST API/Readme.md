# Summary REST API

## API (Application Programming Interface) 
Sebuah perantara yang memungkinkan dua aplikasi atau perangkat lunak untuk saling berkomunikasi dan bertukar data. API mendefinisikan cara aplikasi tersebut dapat bertukar informasi, seperti format data yang digunakan dan metode yang tersedia untuk melakukan berbagai tindakan.

API WORKFLOW : Client --> Request --> System/Server --> Response

Dengan memanfaatkan API, development sebuah product digital akan relatif lebih mudah, cepat dan maintanable.

- Sebuah proses atau fungsi cukup dikembangkan di satu tempat dan dapat digunakan diberbagai aplikasi
- Bisa memanfaatkan API yang disediakan 3rd party untuk proses-proses yang kompleks seperti AI dan ML, seperti Google Vision API atau Speech to Text

## REST API (Representational State Transfer Application Programming Interface) 
Jenis API yang mengikuti arsitektur REST. Arsitektur REST mendefinisikan seperangkat aturan dan batasan untuk membangun API yang mudah digunakan dan skalabel.

Manfaat menggunakan REST API:
- Mudah digunakan: REST API mudah dipahami dan digunakan oleh pengembang perangkat lunak.
- Skalabel: REST API dapat dengan mudah diubah untuk menangani lebih banyak pengguna dan data.
- Fleksibilitas: REST API dapat digunakan untuk berbagai macam aplikasi dan perangkat lunak.
- Interoperabilitas: REST API memungkinkan aplikasi dari berbagai vendor untuk saling berkomunikasi.

Cara kerja REST API:
REST API menggunakan metode HTTP untuk melakukan berbagai tindakan pada data. Berikut adalah beberapa metode HTTP yang umum digunakan:
- GET: Digunakan untuk mengambil data dari server.
- POST: Digunakan untuk mengirim data ke server.
- PUT: Digunakan untuk memperbarui data di server.
- DELETE: Digunakan untuk menghapus data dari server.

## JSON (JavaScript Object Notation)
Format data yang populer untuk pertukaran data antar aplikasi. JSON mudah dibaca manusia dan mesin, dan dapat digunakan untuk mewakili berbagai jenis data, seperti string, angka, array, dan objek.

JSON dalam Postman dapat digunakan untuk:
- Menyimpan data request: Anda dapat menyimpan data request dalam format JSON. Hal ini membantu Anda untuk membuat request yang terstruktur dan mudah dipahami.
- Memproses data response: Anda dapat memproses data response dalam format JSON. Hal ini membantu Anda untuk mengekstrak data yang Anda butuhkan dari response.
- Membuat test script: Anda dapat membuat test script menggunakan JSON. Hal ini membantu Anda untuk menguji API secara otomatis.

Berikut beberapa contoh penggunaan JSON dalam Postman:
- Menyimpan data request:
    ```bash
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "age": 30
    }
    ```

- Memproses data response:
    ```bash
    {
        "status": "success",
        "data": {
            "user": {
            "id": 123,
            "name": "John Doe",
            "email": "johndoe@example.com",
            "age": 30
            }   
        }
    }
    ```

## Postman 
Alat yang populer untuk menguji API. Postman menyediakan antarmuka yang intuitif untuk membantu developer:
- Membuat dan mengirim permintaan (request) ke API.
- Memeriksa respon (response) yang diterima dari API.
- Mengelola dan mendokumentasikan API.

Fitur Utama Postman:
- Membuat request: Postman memungkinkan Anda membuat request HTTP dengan berbagai metode, seperti GET, POST, PUT, dan DELETE.
- Menambahkan header: Anda dapat menambahkan header HTTP ke request Anda, seperti Authorization dan Content-Type.
- Mengelola variabel: Anda dapat menyimpan dan menggunakan variabel dalam request Anda.
- Membuat test script: Anda dapat menulis test script untuk menguji respon API.
- Mengelola koleksi: Anda dapat mengelompokkan request Anda ke dalam koleksi.
- Menerima response: Postman menampilkan respon API dalam format yang mudah dibaca.
- Mendokumentasikan API: Anda dapat menggunakan Postman untuk mendokumentasikan API Anda dalam format OpenAPI.