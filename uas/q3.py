class Hewan:
    def __init__(self, nama):
        self.nama = nama
    def bunyi(self):
        pass
    
class Kucing(Hewan):
    def bunyi(self):
        return "mehong"

class Anjing(Hewan):
    def bunyi(self):
        return "gukkguk"
    
class Gajah(Hewan):
    def bunyi(self):
        return "preeet"
    
hewan = [Kucing("kucing"), Anjing("anjing"), Gajah("gajah")]

for hewan in hewan:
    print(hewan.nama + " : " + hewan.bunyi())
