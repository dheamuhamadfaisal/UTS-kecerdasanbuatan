# Fungsi untuk mengidentifikasi hama berdasarkan gejala yang diberikan
def identifikasi_hama(gejala):
    # Cek apakah gejala mengandung daun menguning dan tanaman layu
    if "daun menguning" in gejala and "tanaman layu" in gejala:
        return "Hama: Kutu Putih"
    # Cek apakah gejala mengandung daun berlubang dan bercak hitam
    elif "daun berlubang" in gejala and "bercak hitam" in gejala:
        return "Hama: Ulat Grayak"
    # Cek apakah gejala mengandung daun menguning dan bercak hitam
    elif "daun menguning" in gejala and "bercak hitam" in gejala:
        return "Hama: Thrips"
    # Cek apakah gejala hanya daun berlubang tanpa bercak hitam
    elif "daun berlubang" in gejala and "bercak hitam" not in gejala:
        return "Hama: Kumbang Daun"
    else:
        # Jika gejala tidak cocok dengan aturan manapun
        return "Hama tidak diketahui"

# Contoh penggunaan fungsi
# Definisikan gejala tanaman dalam bentuk list
gejala_tanaman = ["daun menguning", "tanaman layu"]

# Panggil fungsi untuk mendapatkan hasil identifikasi hama
hasil = identifikasi_hama(gejala_tanaman)

# Cetak hasilnya
print(hasil)
