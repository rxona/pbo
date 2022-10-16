import datetime

class Mahasiswa:
    def __init__(self):
        self.nim = '20210801306'
        self.nama = 'Luhut Andreas'
        self.gender = 'Laki-laki'
        self.tgl_input_nilai = datetime.datetime.now()
        self.matkul = 'Pemrograman Berorientasi Objek'
        self.absensi = 100
        self.tugas = 90
        self.uts = 80
        self.uas = 80
        self.nilai_akhir = None
        self.grade_nilai_akhir = None
        self.keterangan_nilai = None

    def print_nilai_akhir(self):
        self.nilai_akhir = (self.tugas * 25 + self.uts * 35 + self.uas * 40) / 100
        if self.nilai_akhir < 50:
            self.grade_nilai_akhir = 'Grade E'
        elif self.nilai_akhir < 59:
            self.grade_nilai_akhir = 'Grade D'
        elif self.nilai_akhir < 64:
            self.grade_nilai_akhir = 'Grade C'
        elif self.nilai_akhir < 68:
            self.grade_nilai_akhir = 'Grade C+'
        elif self.nilai_akhir < 71:
            self.grade_nilai_akhir = 'Grade B-'
        elif self.nilai_akhir < 74:
            self.grade_nilai_akhir = 'Grade B'
        elif self.nilai_akhir < 77:
            self.grade_nilai_akhir = 'Grade B+'
        elif self.nilai_akhir < 80:
            self.grade_nilai_akhir = 'Grade A-'
        elif self.nilai_akhir < 101:
            self.grade_nilai_akhir = 'Grade A'
        
        self.keterangan_nilai = 'Tidak Lulus' if self.nilai_akhir < 59 else 'Lulus'
            
        print(self.nilai_akhir, '(' + self.grade_nilai_akhir + '):', self.keterangan_nilai)


Mahasiswa().print_nilai_akhir()