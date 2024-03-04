from Soal_Prioritas1 import KelasLatihan

class Yoga(KelasLatihan):
    def __init__(self, namaPelatih, spesialis, tahunPengalaman, jenisLatihan, jadwal, tingkatKesulitan):
        super().__init__(namaPelatih, spesialis, tahunPengalaman, jenisLatihan, jadwal)
        self.__tingkatKesulitan = tingkatKesulitan

    def setTingkatKesulitan(self, tingkatKesulitan):
        self.__tingkatKesulitan = tingkatKesulitan

    def getTingkatKesulitan(self):
        return self.__tingkatKesulitan

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Tingkat Kesulitan:", self.__tingkatKesulitan)

    def aturPosisiYoga(self, posisi):
        print("Posisi Yoga:", posisi)

class AngkatBeban(KelasLatihan):
    def __init__(self, namaPelatih, spesialis, tahunPengalaman, jenisLatihan, jadwal, beratMaksimum):
        super().__init__(namaPelatih, spesialis, tahunPengalaman, jenisLatihan, jadwal)
        self.__beratMaksimum = beratMaksimum
    
    def setBeratMaksimum(self, beratMaksimum):
        self.__beratMaksimum = beratMaksimum

    def getBeratMaksimum(self):
        return self.__beratMaksimum

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Berat Maksimum:", self.__beratMaksimum)

    def aturBeratBeban(self, beratBeban):
        print("Berat Beban:", beratBeban, "kg")

kelasLatihan1 = Yoga("Dhito", "Yoga", 5, "Yoga", "Senin", "Medium")
kelasLatihan2 = AngkatBeban("Deprin", "Angkat Beban", 7, "Angkat Beban", "Rabu", 100)

print("========================")
print("\nDemo")
print("========================")
kelasLatihan1.tampilkanInfo()
print("")
kelasLatihan2.tampilkanInfo()
print("")
    
# Demo Metode Khusus
def tampilkanInfoKelasLatihan(kelas):
    if isinstance(kelas, Yoga):
        kelas.tampilkanInfo()
    elif isinstance(kelas, AngkatBeban):
        kelas.tampilkanInfo()
    else:
        print("Kelas Latihan tidak dikenal")

print("========================")
print("Demo Metode Khusus")
print("========================")
print("Info Kelas Latihan Yoga")
print("========================")
tampilkanInfoKelasLatihan(kelasLatihan1)
kelasLatihan1.aturPosisiYoga("Posisi Lotus")
print("========================")

print("\n========================")
print("Info Kelas Latihan Angkat Beban")
print("========================")
tampilkanInfoKelasLatihan(kelasLatihan2)
kelasLatihan2.aturBeratBeban(50)
print("========================")