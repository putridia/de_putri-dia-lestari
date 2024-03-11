# Summary Data Structure and Alogarithm

## Python List 
kumpulan dari berbagai nilai yang dapat kita sebut sebagai item atau elemen. elemen yang ada pada list bisa berupa berbagai tipe data berupa string, berupa number atau boolean ataupun mix campuran dari tipe data yang ada. Elemen atau item pada list kita dapat akses dan juga manipulasi artinya pada list kita dapat melakukan manipulasi data.

```bash
len(list) --> untuk berapa banyak data yang dimiliki list
list.append(value) --> untuk menambahkan elemen pada list
list.insert(index, value) --> untuk menambahkan elemen pada index yang spesifik
list.remove(value) --> menghapus pada spesifik elemen
list.pop(index) --> mengahpsu pada spesifik index

# Contoh List
list_number = [1, 2, 3, 4, 5]

del list_number[1]
print(list_number)

print(list_number)
print(list_number[1:3]) # [2, 3]

list_string = ["Bandung", "Jakarta", "Surabaya"]
list_string.append("Malang")
print(list_string)
print(list_string[0]) # Bandung

list_mixed = [1, "Bandung", True]
list_mixed.insert(1, False)
print(list_mixed)

list_mixed.remove("Bandung")
print(list_mixed)

list_mixed.pop(0)
print(list_mixed)
```

## Python Tuple
Pada tuple struktur data yang digunakan untuk menyimpan koleksi berurutan dari elemen-elemen, Berbeda dengan list, tuple bersifat tidak dapat diubah (immutable) setelah dibuat. Dibuat dengan tanda kurung biasa () dan elemen-elemen dipisahkan dengan koma. Urutan elemen penting dan bisa diakses menggunakan indeks. Dapat berisi berbagai tipe data seperti angka, string, list, dan lain-lain. Sering digunakan untuk menyimpan data yang tidak perlu diubah.

```bash
simple_tuple = (1, "Alterra", True)
print(simple_tuple)

del simple_tuple[2]
print(simple_tuple)
```

## Python dictionary
Tipe data yang digunakan untuk menyimpan kumpulan data terstruktur dalam bentuk pasangan kunci-nilai(key-value). Dictionary dibuat menggunakan kurung kurawal {}. Di dalam kurung kurawal ini, Anda bisa mendefinisikan pasangan kunci-nilai yang dipisahkan oleh titik dua ":" dan koma ",". Untuk mengakses nilai, Anda bisa menggunakan kunci terkaitnya yang diapit tanda kurung siku [].

```bash
simple_dict = {"angka": 1, "nama": "Alterra", "status": True}
print(simple_dict)

print(simple_dict["nama"])

simple_dict["new"] = 123

print(simple_dict)

simple_dict["nama"] = "Academy"
print(simple_dict)

del simple_dict["new"]
print(simple_dict)

second_dict = dict([("angka", 2), ("nama", "Academy")])
print(second_dict)

other_dict = dict({"key": "value"})
print(other_dict)
```

## Python Set
Kumpulan elemen yang unik dan tidak berurutan. Ini berbeda dengan tipe data lain seperti list yang bisa memiliki elemen duplikat dan terurut. Set dapat dibuat menggunakan kurung kurawal {} mirip dengan dictionary.  Namun, tidak seperti dictionary, elemen dalam set tidak dipisahkan oleh pasangan key-value.
- Menambah elemen: Gunakan method add() untuk menambahkan elemen baru ke dalam set.
- Menghapus elemen: Method remove() menghapus elemen tertentu. Jika elemen tidak ada, akan muncul error KeyError. Anda dapat menggunakan discard() sebagai alternatif yang lebih aman untuk menghindari error jika elemen tidak ada.

```bash
my_set = {1, 2, 3, 4, 5}

set_2 = set(["Alterra", "Academy"])

# my_set.ad () -> int
my_set.pop()
my_set.remove(2)
print(my_set)
```

## Python Search
pencarian mengacu pada proses menemukan elemen tertentu atau elemen yang memenuhi kriteria tertentu dalam suatu kumpulan data. 
- Pencarian Linear: Ini adalah algoritme pencarian dasar yang memeriksa setiap elemen dalam urutan (list, tuple) satu per satu hingga ditemukan elemen yang cocok. Mudah diterapkan tetapi bisa lambat untuk kumpulan data besar.
- Metode String: String Python memiliki metode find() dan index() untuk menemukan posisi awal substring di dalam string. Cocok untuk mencari pola tertentu dalam teks.
- Metode List: List memiliki metode index() dan count() untuk mencari elemen. index() mengembalikan indeks kemunculan pertama elemen yang dicari, sedangkan count() menghitung berapa kali elemen tersebut muncul dalam list.
- Operator "in": Operator ini berguna untuk mengecek apakah suatu elemen tertentu ada di dalam urutan (list, tuple, string) atau set. Mengembalikan True jika ditemukan, False jika tidak.

```bash
# Contoh Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i # Mengembalikan indeks elemen yang ditemukan
    return -1 # Mengembalikan -1 jika elemen tidak ditemukan

# Contoh penggunaan fungsi linear search
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

target = 4
result = linear_search(data, target)

if result != -1:
    print(f"{target} ditemukan pada indeks {result}.")
else:
    print(f"{target} tidak ditemukan dalam daftar.")

```

## Python Sorting 
proses mengatur elemen-elemen dalam suatu kumpulan data ke dalam urutan tertentu, biasanya berdasarkan nilai numerik atau kriteria yang telah ditentukan. 
- Metode sort(): Metode ini langsung mengurutkan list atau array secara permanen. Urutannya bisa menaik (ascending) atau menurun (descending) tergantung pada argumen yang diberikan.
- Fungsi sorted(): Fungsi ini mengembalikan copy baru dari list yang sudah diurutkan, tanpa mengubah list asli.

```bash
# Selection Search
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Cari nilai minimum pada sisa array
        index_min = i

        # Mencari elemen terkecil dalam sisa daftar
        for j in range(i + 1, n):
            if arr[j] < arr[index_min]:
                index_min = j

        # Menukar elemen terkecil dengan elemen ke-i
        arr[i], arr[index_min] = arr[index_min], arr[i]

# Contoh penggunaan selection sort
data = [64, 25, 12, 22, 11]

print("Data sebelum diurutkan:", data)
selection_sort(data)
print("Data setelah diurutkan:", data)

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # Menentukan titik tengah daftar

        # Membagi daftar menjadi dua bagian
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Memanggil merge_sort untuk kedua bagian
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Menggabungkan dua bagian menjadi satu daftar yang sudah diurutkan
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
# Contoh penggunaan merge sort
data = [38, 27, 43, 3, 9, 82, 10]

print("Data sebelum diurutkan:", data)
merge_sort(data)
print("Data setelah diurutkan:", data)

# Counting Sort
def counting_sort(arr):
    # Menemukan nilai maksimum dalam daftar untuk menentukan rating (range)
    max_value = max(arr)

    # Membuat array kosong untuk menghitung frekuensi masing-masing elemen
    count = [0] * (max_value + 1)

    # Menghitung frekuensi masing-masing elemen dalam daftar
    for num in arr:
        count[num] += 1
    
    # Mambangun daftar hasil yang diurutkan
    sorted_list = []
    for i in range(max_value + 1):
        sorted_list.append(i)
        print(i)
        count[i] -= 1

    return sorted_list

# Contoh penggunaan counting sort
data = [4, 2, 2, 8, 3, 3, 1]

print("Data sebelum diurutkan:", data)
sorted_data = counting_sort(data)
print("Data setelah diurutkan:", sorted_data)
```