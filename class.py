class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def perkenalan(self):
        return f"Nama saya {self.nama}, NIM {self.nim}, dari jurusan {self.jurusan}."

# Membuat instance dari class Mahasiswa
mahasiswa1 = Mahasiswa("Ali", "12345678", "Teknik Informatika")

# Menggunakan metode perkenalan
print(mahasiswa1.perkenalan())
