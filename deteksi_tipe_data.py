# Contoh variabel dengan berbagai tipe data
data_integer = 10
data_float = 3.14
data_string = "Hello, Python!"
data_boolean = True
data_list = [1, 2, 3]
data_tuple = (1, 2, 3)
data_set = {1, 2, 3}
data_dict = {"a": 1, "b": 2}

# Fungsi untuk mendeteksi dan mencetak tipe data
def deteksi_tipe_data(data):
    print(f"Data: {data} | Tipe: {type(data)}")

# Menggunakan fungsi untuk mendeteksi tipe data dari setiap variabel
deteksi_tipe_data(data_integer)
deteksi_tipe_data(data_float)
deteksi_tipe_data(data_string)
deteksi_tipe_data(data_boolean)
deteksi_tipe_data(data_list)
deteksi_tipe_data(data_tuple)
deteksi_tipe_data(data_set)
deteksi_tipe_data(data_dict)
