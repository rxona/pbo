from Anggrek import *

anggrek = Anggrek()

while True:
    v = input('Masukkan: 0 untuk memberi air, 1 untuk memberi pupuk, 999 untuk keluar: ')
    if v == '999':
        break
    match v:
        case '0':
            anggrek.beriAir()
        case '1':
            anggrek.beriPupuk()
        case _:
            break
    anggrek.displayPlant()

