# Soal Prioritas 1

1. Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:

![Screenshot 2024-05-03 233054](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/f3f01f65-aef9-4ce2-a985-83dcbe56caa4)

Catatan:

a. Satu task menggambarkan perintah bash yang harus dijalankan.

b. Gunakan BashOperator dalam membuat DAG.

![Screenshot 2024-05-04 041917](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/0f5a78c3-394d-45a3-b1aa-30542f2b8849)

![Screenshot 2024-05-04 042433](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/12c70d09-3296-4b8b-982c-464917b9f9e7)

![Screenshot 2024-05-04 042124](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/6f9df851-bbdb-4da9-a2be-ec2c69d9e9c7)

2. Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:

![Screenshot 2024-05-03 233105](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/1b1cd2a8-a260-42d6-95ac-8bfa31ef49eb)

Kriteria yang harus dipenuhi:

a. Task pertama adalah membuat sekumpulan bilangan acak dari 1 sampai 50 dengan jumlah bilangan adalah 25 bilangan.

b. Task kedua adalah menghitung jumlah dari semua bilangan yang didapatkan dari task pertama.

c. Task terakhir adalah menentukan apakah jumlah dari semua bilangan merupakan bilangan genap atau bukan. Jika merupakan bilangan genap tampilkan tulisan “Even Sum”. Jika tidak maka tampilkan tulisan “Odd Sum”.

d. Gunakan X-COM dalam proses pertukaran data antar task.

e. Gunakan PythonOperator dalam membuat DAG.

![Screenshot 2024-05-04 042824](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/a85ed691-f5e6-4b5b-a7d8-e0fb742703a9)

![Screenshot 2024-05-04 043848](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/9cf1a5e0-523a-4775-8bdc-847cbec59eb2)