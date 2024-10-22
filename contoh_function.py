# Fungsi bawaan: len(), print(), sum(), dll.
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Mengembalikan panjang list (5)
print(sum(my_list))  # Mengembalikan jumlah elemen list (15)

# Fungsi untuk menghitung luas persegi
def luas_persegi(sisi):
    return sisi * sisi

# Menggunakan fungsi
hasil = luas_persegi(4)
print("Luas persegi:", hasil)

def sapa(nama="Teman"):
    print(f"Halo, {nama}!")

# Memanggil fungsi tanpa argumen
sapa()  # Output: Halo, Teman!

# Memanggil fungsi dengan argumen
sapa("Dewi")  # Output: Halo, Dewi!
