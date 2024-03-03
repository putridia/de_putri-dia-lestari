# Menghitung Luas Persegi Panjang dan Menentukan Even atau Odd

def Luas_persegi_panjang(panjang, lebar):
    Luas = panjang * lebar
    return Luas

def Even_or_Odd_Luas(Luas):
    if Luas % 2 == 0:
        return "Even Rectangel"
    else:
        return "Odd Rectangel"
    

print("Menghitung Luas Persegi Panjang dan Menentukan Even atau Odd")
print("=============================================================")    
panjang = int(input("Masukkan sisi panjang: "))
lebar = int(input("Masukkan sisi lebar: "))
print("=============================================================")

print("Proses Perhitungan")
print("=============================================================")
print("Sisi Panjang adalah", panjang, "cm")
print("Sisi Lebar adalah", lebar, "cm")
print("=============================================================")

print("Hasil Perhitungan")
print("=============================================================")
Luas = Luas_persegi_panjang(panjang, lebar)
print("Luas Persegi Panjang adalah", Luas, "cm^2")
print("Luas Persegi Panjang termasuk", Even_or_Odd_Luas(Luas))