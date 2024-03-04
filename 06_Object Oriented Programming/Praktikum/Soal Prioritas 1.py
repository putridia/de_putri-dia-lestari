# Membuat Class Pelanggan
class Pelanggan:
    def __init__(self, nama, usia, ID_Pelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__ID_Pelanggan = ID_Pelanggan

    # Setter
    def setNama(self, nama):
        self.__nama = nama

    def setUsia(self, usia):
        self.__usia = usia

    def setID_Pelanggan(self, ID_Pelanggan):
        self.__ID_Pelanggan = ID_Pelanggan

    # Getter
    def getNama(self):
        return self.__nama

    def getUsia(self):
        return self.__usia

    def getID_Pelanggan(self):
        return self.__ID_Pelanggan
    
    # Menampilkan Informasi Data Pelanggan
    def infoPelanggan(self):
        print("Nama:", self.__nama)
        print("Usia:", self.__usia)
        print("ID Pelanggan:", self.__ID_Pelanggan)

# Membuat Class Pelatih
class Pelatih:
    def __init__(self, namaPelatih, spesialis, tahunPengalaman):
        self.__namaPelatih = namaPelatih
        self.__spesialis = spesialis
        self.__tahunPengalaman = tahunPengalaman
    
    # Setter
    def setNamaPelatih(self, namaPelatih):
        self.__namaPelatih = namaPelatih

    def setSpesialis(self, spesialis):
        self.__spesialis = spesialis

    def setTahunPengalaman(self, tahunPengalaman):
        self.__tahunPengalaman = tahunPengalaman

    # Getter
    def get_namaPelatih(self):
        return self.__namaPelatih
    
    def get_spesialis(self):
        return self.__spesialis
    
    def get_tahunPengalaman(self):
        return self.__tahunPengalaman
    
    # Menampilkan Informasi Data Pelatih
    def infoPelatih(self):
        print("Nama Pelatih:", self.__namaPelatih)
        print("Spesialis:", self.__spesialis)
        print("Tahun Pengalaman:", self.__tahunPengalaman)

# Membuat Class Kelas Latihan
class KelasLatihan(Pelatih):
    def __init__(self, namaPelatih, spesialis, tahunPengalaman, jenisLatihan, jadwal):
        super().__init__(namaPelatih, spesialis, tahunPengalaman)
        self.__jenisLatihan = jenisLatihan
        self.__jadwal = jadwal

    # Setter
    def setJenisLatihan(self, jenisLatihan):
        self.__jenisLatihan = jenisLatihan

    def setHari(self, jadwal):
        self.__jadwal = jadwal

    # Getter
    def getJenisLatihan(self):
        return self.__jenisLatihan
    
    def getjadwal(self):
        return self.__jadwal
    
    # Menampilkan Informasi Data Kelas Latihan
    def infoKelasLatihan(self):
        super().infoPelatih()
        print("Jenis Latihan:", self.getJenisLatihan())
        print("Jadwal:", self.getjadwal())

# Membuat Object Pelanggan
Pelanggan1 = Pelanggan("Jose", 20, "P001")

# Membuat Object Pelatih
Pelatih1 = Pelatih("Dhani", "Lari", 5)

# Membuat Object Kelas Latihan
KelasLatihan1 = KelasLatihan("Dhani", "Lari", 5, "Marathon", "Senin, Rabu, Jumat")

# Menampilkan Informasi
print("========================")
print("Informasi Pelanggan")
print("========================")
Pelanggan1.infoPelanggan()
print("========================\n")

print("========================")
print("Informasi Pelatih")
print("========================")
Pelatih1.infoPelatih()
print("========================\n")

print("========================")
print("Informasi Kelas Latihan")
print("========================")
KelasLatihan1.infoKelasLatihan()
print("========================")