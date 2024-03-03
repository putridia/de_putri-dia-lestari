# Menghitung Volume Bola

phi = 3.14
def Volume_Bola(jari_jari):
    Volume = 4/3 * phi * jari_jari**3
    return Volume

print("Menghitung Volume Bola")
print("=======================")
jari_jari = float(input("Masukkan jari-jari: "))
print("=======================")

print("Proses Perhitungan")
print("=======================")
print("Jari-jari adalah", jari_jari, "cm")
print("=======================")

print("Hasil Perhitungan")
print("=======================")
Volume = Volume_Bola(jari_jari)
print("Volume Bola adalah", Volume, "cm^3")
