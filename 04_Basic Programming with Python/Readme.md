# Summary Basic Programming with Python

## Python Introduction 

Python adalah salah satu bahasa yang populer dan bahasa yang serbaguna untuk digunakan dalam Pengembangan web, Pengembangan perangkat lunak, matematika dan penulisan skrip sistem.

Python digunakan untuk berbagai tujuan :
- Membuat aplikasi web
- membangun alur kerja(workflow)
- Terhubung dengan sistem database dan memodifikasi file
- Dapat menghandle data besar dan melakukan perhitungan matematika kompleks
- Dapat membuat prototype dengan cepat atau mengembangkan perangkat lunak siap produksi

Alasan mengapa python menjadi bahasa populer? dikarenakan python berjalan di berbagai platform, memiliki sintaks yang mudah dipahami(mirip bahasa inggris) dan baris kode yang di tulis akan lebih sedikit dibanding dengan bahasa pemrograman lainnya. 

run code python (terminal) 
```bash
  python "namafile"
``` 

### Python Indentation 
Python pada baris pertama harus di beri jarak 4 baris spasi pada awal codingan.

contoh : 
```bash
  if  5 > 2:
    print("Five is greater than two!")
``` 

### Variabel 
Wadah untuk menyimpan nilai data
```bash
  nama_variabel = "isi dari variabelnya"
  nama_variabel_number = 3
``` 

 
## TIPE DATA
- ### Boolean (True atau False) 
  Menyatakan benar **true** yang bernilai 1 atau salah **false** yang bernilai 0

  Contoh : 
  ```bash
    status = True 
  ```

- ### String ("kata atau kalimat") 
  Menyatakan karakter/kalimat bisa berupa huruf. 

  Contoh : 
  ```bash
    nama = "muchson"
  ``` 

- ### Integer (25 atau 1209) 
  Untuk bilangan bulat

  Contoh : 
  ```bash
    umur = 20
  ``` 

- ### Float (3.14 atau 0.99) 
  Bilangan yang punya koma

  Contoh : 
  ```bash
    tinggiBadan = 190.8
  ``` 

- ### Hexadecimal (9a atau 1d3) 
  Bilangan dalam format heksa (bilangan berbasis 16)

  Contoh :
  ```bash
    hexa = 0x9a
  ``` 

- ### Complex (1 + 5j) 
  Pasangan angka real dan imajiner

  Contoh :
  ```bash
    complex = 1 +5j
  ``` 

- ### List (['xyz', 786, 2.23]) 
  Data untaian yang menyimpan berbagai tipe data dan isinya bisa diubah

  Contoh : 
  ```bash
    my_list = [1,2,3,4,5]
    my_list2 = ["satu", "dua", "tiga"]
    my_list3 = ["satu", 2, 3.0]
  ``` 

- ### Tuple (('xyz', 786, 2.23)) 
  Data untaian yang menyimpan berbagai tipe data tapi isinya tidak bisa diubah

  Contoh :
  ```bash
    my_tuple = (1,2,3,4,5)
    my_tuple2 = ("satu", "dua", "tiga")
  ``` 

- ### Dictionary ({'nama': 'adi', 'id':2}) 
  Data untaian yang menyimpan berbagai tipe data berupa pasangan penunjuk dan nilai

  Contoh :
  ```bash
    my_dict = {"nama" : "Budi", "umur" : 20}
    print(type(my_dict)) --> mengecek jenis tipe data
  ``` 

## Function 
Seperti alat yang digunakan berulang kali untuk melakukan tugas atau task tertentu, dan dapat juga membagi code menjadi block - block yang berguna.

## Time Complexity
Untuk memungkinkan kita untuk waktu eksekusi maksimum untuk suatu program.

```bash
  fun dominant (n int) int {
	  var result int = 0
	  for i := 0; i < n; i++{
	    result += 1
	  }
	  Result = result + 10
	  return result
  }
``` 

### Constant Time - O(1)
Menentukan bilangan ganjil atau genap dan waktu eksekusi tidak bergantung pada ukuran nilai input n.

```bash
  def odd_or_even(n) :
	  if n % 2 == 0 :
		  return "Even"
	  return "Odd"
``` 


### Linear Time - O(n)
Untuk mengecek keberadaan nilai 0 pada array dan untuk eksekusi bergantung secara linear dengan ukuran input n.

```bash
  def linear(n, A):
	  for i in range(n):
		  if A[i] == 0:
			  return 0
		  return 1
``` 

### Logarithmic Time - O(log n)
Fungsi yang membagi nilai n menjadi setengah pada setiap iterasi dan waktu eksekusi meningkat secara logarithmic terhadap input n.
```bash
  def logarithmic(n):
	  result = 0
	  while n > 1:
		  n //= 2
		  result += 1
	  return result
``` 

### Quadrat Time - O(n^2)
Terdapat 2 looping, waktu eksekusi secara quadratic terhadap ukuran input n.

```bash
  def quadratic(n):
	  result = 0
	  for i in range(n):
		  for j in range(n):
			  result += 1
	  return result
``` 

### Factorial time O(n!) dan Exponential time O(2^n)
Hanya dapat menyelesaikan masalah untuk nilai n yang sangat kecil

### Time Limit
Komputer rata - rata dapat melakukan 10^8 operasi dalam kurung waktu 1 detik.
