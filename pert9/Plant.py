class Plant():
    def __init__(self):
        self.statusTumbuh = 0
        self.jumlahAir = 0
        self.jumlahPupuk = 0

    def tumbuh(self):
        if self.statusTumbuh < 4:
            self.jumlahAir -= 3
            self.jumlahPupuk -= 1
            self.statusTumbuh += 1

    def cekKondisiTumbuh(self):
        if self.jumlahAir >= 3 and self.jumlahPupuk >= 1:
            self.tumbuh()

    def beriAir(self):
        self.jumlahAir += 1
        self.cekKondisiTumbuh()
    
    def beriPupuk(self):
        self.jumlahPupuk += 1
        self.cekKondisiTumbuh()

    def getStatusTumbuhText(self):
        match self.statusTumbuh:
            case 0:
                return 'Benih'
            case _:
                return 'Berbunga'

    def displayPlant(self):
        print(self.getStatusTumbuhText())
        print('Jumlah air:', self.jumlahAir)
        print('Jumlah pupuk:', self.jumlahPupuk)