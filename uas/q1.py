class Bunga:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def mekar(self):
        print(f"{self.nama} sedang mekar")

class Anggrek(Bunga):
    def __init__(self, nama, jenis, warna):
        super().__init__(nama, jenis)
        self.warna = warna
    def berbunga_sepanjang_tahun(self):
        print(f"{self.nama} berbunga sepanjang tahun")

agrek = Anggrek("Anggrek Merah", "Anggrek", "Merah")
agrek.mekar() # output: "Anggrek Merah sedang mekar"
agrek.berbunga_sepanjang_tahun() # output: "Anggrek Merah berbunga sepanjang tahun"
