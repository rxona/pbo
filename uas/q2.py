class Bunga:
    def __init__(self, nama, jenis, jumlah_bunga):
        self.__nama = nama
        self.__jenis = jenis
        self.__jumlah_bunga = jumlah_bunga
        
    def get_nama(self):
        return self.__nama
    
    def get_jenis(self):
        return self.__jenis
    
    def get_jumlah_bunga(self):
        return self.__jumlah_bunga
    
    def tambah_jumlah_bunga(self, jumlah):
        self.__jumlah_bunga += jumlah
    
    def kurangi_jumlah_bunga(self, jumlah):
        if jumlah <= self.__jumlah_bunga:
            self.__jumlah_bunga -= jumlah
        else:
            return "Jumlah bunga tidak cukup"

bunga = Bunga("Mawar Merah", "Mawar", 5)
print(bunga.get_nama()) # output: "Mawar Merah"
print(bunga.get_jenis()) # output: "Mawar"
print(bunga.get_jumlah_bunga()) # output: 5
bunga.tambah_jumlah_bunga(2)
print(bunga.get_jumlah_bunga()) # output: 7
print(bunga.kurangi_jumlah_bunga(4)) # output: 4
print(bunga.get_jumlah_bunga()) # output: 3
