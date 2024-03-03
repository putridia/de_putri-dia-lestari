# Menentukan Prioritas Proyek berdasarkan budget, waktu pengerjaan, dan tingkat kesulitan

def hitung_budget(budget):
    if budget <= 50:
        return 4
    elif budget <= 80:
        return 3
    elif budget <= 100:
        return 2
    else:
        return 1
    
def hitung_waktu(waktu):
    if waktu <= 20:
        return 10
    elif waktu <= 30:
        return 5
    elif waktu <= 50:
        return 2
    else:
        return 1
    
def hitung_kesulitan(kesulitan):
    if kesulitan <= 3:
        return 10
    elif kesulitan <= 6:
        return 5
    elif kesulitan <= 10:
        return 1
    else:
        return 0

def hitung_total_skor(budget, waktu, kesulitan):
    skor_nilaiBudget = hitung_budget(budget)
    skor_nilaiWaktu = hitung_waktu(waktu)
    skor_nilaiKesulitan = hitung_kesulitan(kesulitan)
    return skor_nilaiBudget + skor_nilaiWaktu + skor_nilaiKesulitan

def tentukan_prioritas(total_skor):
    if total_skor >= 17:
        return "High"
    elif total_skor >= 10:
        return "Medium"
    elif total_skor >= 3:
        return "Low"
    else:
        return "Impossible"

print("Menentukan Prioritas Proyek berdasarkan budget, waktu pengerjaan, dan tingkat kesulitan")
print("=====================================================================================")
budget = int(input("Masukkan nilai budget: "))
waktu = int(input("Masukkan nilai waktu pengerjaan: "))
kesulitan = int(input("Masukkan nilai tingkat kesulitan: "))
print("=====================================================================================")

print("Hasil Perhitungan")
print("=====================================================================================")
print("Nilai Budget adalah", budget)
print("Nilai Waktu adalah", waktu)
print("Nilai Kesulitan adalah", kesulitan)

total_skor = hitung_total_skor(budget, waktu, kesulitan)
print("Total Skor adalah", total_skor)
print("Prioritas Proyek adalah", tentukan_prioritas(total_skor))