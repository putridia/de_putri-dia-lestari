# Program Menentukan Tarif Pengiriman Paket berdasarkan Berat dan Jarak

def hitung_biaya(kg):
    if kg <= 20:
        return 10000
    elif kg <= 30:
        return 15000
    elif kg <= 60:
        return 20000
    else:
        return 45000
    

def hitung_tarif(jarak):
    if jarak <= 5:
        return 2000
    elif jarak <= 15:
        return 5000
    elif jarak <= 30:
        return 10000
    else:
        return 15000
    
print("Program Menentukan Tarif Pengiriman Paket berdasarkan Berat dan Jarak")
print("=====================================================================")
kg = float(input("Masukkan berat barang (kg): "))
jarak = float(input("Masukkan jarak kirim (km): "))
print("=====================================================================")

print("Hasil Perhitungan")
print("=====================================================================")
biaya = hitung_biaya(kg)
tarif = hitung_tarif(jarak)
print("Biaya kirim adalah Rp.", biaya)
print("Tarif kirim adalah Rp.", tarif)
total = biaya + tarif
print("Total biaya kirim adalah Rp.", total)