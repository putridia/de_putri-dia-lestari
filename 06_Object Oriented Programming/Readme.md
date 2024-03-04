# Summary Object Oriented Programming
OOP adalah paradigma yang memungkinkan kita untuk mengorganisir program sehingga properti dan perilaku dikemas dalam objek individu.

Properti ditentukan oleh nilai atribut, sedangkan Perilaku ditentukan oleh bagaimana objek tersebut bertindak atau bereaksi terhadap permintaan.

Terdapat 4 Fundamental dalam OOP :

## Encaptulation
Melibatkan pengelompokkan atribut dan metode dalam 1 unit yang dikenal sebagai class. Class adalah template atau blueprint yang dapat membuat sebuah object.

```bash
# Contoh membuat class 
class ClassRobot:
    pass

# instance
class Cat:
    def __init__(self, fur_color="No Name", num_of_leg=4):
        self._fur_color = fur_color
        self._num_of_leg = num_of_leg

manis = Cat("Hitam", 4)
pussy = Cat("Putih", 3)

class Mobil:
    def __init__(self, tipe, name, roda, platum):
        self.roda = roda
        self._type = tipe
        self.__name = name
        self.__platnum = platum

class Bebek:
    def speak(self, bunyi_suara):
        return bunyi_suara
    
# Membuat objek dari kelas Bebek
donald = Bebek()

# Memanggil method dari objek
suara_donald = donald.speak("Kwek kwek")
print(suara_donald)
```

## Data Abstraction
Konsep dimana kita hanya menampilkan fitur-fitur penting dari suatu objek dan data abstraction juga dapat menyembunyikan detail-detail yang kompleks seperti dengan menggunakan metode atau teknik getter dan setter.

```bash
class AkunBank:
    def __init__(self, nama, saldo_awal):
        self.__nama = nama
        self.__saldo = saldo_awal
    
    # Method getter
    def get_nama(self):
        return self.__nama
    
    def get_saldo(self):
        return self.__saldo
    
    # Method setter
    def setor(self, jumlah):
        self.__saldo += jumlah
        return self.__saldo
    
    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo anda tidak mencukupi")
            return
        else:
            self.__saldo -= jumlah
            return self.__saldo
        
akun = AkunBank("Alterra", 2000)
print(akun.get_nama())
print(akun.get_saldo())
akun.setor(1000)
print(akun.get_saldo())
akun.tarik(4000)
akun.tarik(500)
print(akun.get_saldo())
```

## Inheritance
Mekanisme dasar yang memungkinkan Anda untuk membuat kelas baru (subkelas, kelas anak, kelas turunan) berdasarkan kelas yang sudah ada (superkelas, kelas induk, kelas dasar).

```bash
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def identity(self):
        return self.first_name + " " + self.last_name
    
class Employee(Person):
    def __init__(self, first_name, last_name, staff_number):
        super().__init__(first_name, last_name)
        self.staff_number = staff_number
    
    def identity(self):
        return super().identity() + ", " + str(self.staff_number)
    
# Kita akan membuat 2 objek dari kelas Person dan kelas Employee
person_budi = Person("Budi", "Purnama")
employee_budi = Employee("Budi", "Purnama", 19821)

# Kita akan memanggil method identity dari kelas objek
identity_person_budi = person_budi.identity()
print(identity_person_budi)

# Kita akan memanggil method identity dari kelas employee
identity_employee_budi = employee_budi.identity()
print(identity_employee_budi)
```

## Polymorphism
Konsep di mana objek dari kelas yang berbeda dapat merespons secara berbeda terhadap pemanggilan metode yang sama dan dapat diimplementasikan secara berbeda oleh kelas yang berbeda.

```bash
class Animal:
    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):
        return "Mewoooo"
    
class Anjing(Animal):
    def speak(self):
        return "Gug gug"
    
class Bebek(Animal):
    def speak(self):
        return "Kwek kwek"
    
print(Cat().speak())
print(Anjing().speak())
print(Bebek().speak())
```