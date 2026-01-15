# Sistem Reservasi Tiket Bioskop Sederhana
kursi = [] # Inisialisasi List Kursi Tersedia

# Fungsi untuk Menampilkan Denah Kursi
def denah_kursi():
    print("\n>>> DENAH KURSI <<<")
    if len(kursi) == 0:
        print("Semua kursi kosong.")
    else:
        for i in range(1, 6): # List of lists: 5 kursi (Bisa memilih nomor kursi)
            if i not in kursi:
                print(f"Kursi {i}: Kosong")
            else:
                print(f"Kursi {i}: Terisi")
                nama_pemesan : str = input("Masukkan Nama Pemesan Kursi: ")
                print(f" Pemesan: {nama_pemesan}")

# Fungsi untuk Memilih Nomor Kursi
def nomor_kursi():
    nomor = int(input("Masukkan Nomor Kursi yang Dipilih : "))
    if nomor in kursi:
        print("Maaf! Kursi Sudah Dipesan.")
    else:
        kursi.append(nomor)
        print("Kursi Berhasil Dipesan.")

# Fungsi utama dengan menu
def main_menu():
    while True:
        print("\n=== RESERVAASI TIKET BIOSKOP ===")
        print("1. DENAH KURSI")
        print("2. PILIH KURSI")
        print("3. KELUAR")

        pilihan = input("Pilih Menu (1-3):")
        if pilihan == '1':
            denah_kursi()
        elif pilihan == '2':
            nomor_kursi()
        elif pilihan == '3':
            print("Terimakasih Telah Memesan Tiket Bioskop Disini!")
            break
        else:
            print("Pilihan Tidak Valid!")

# Akhir dari Looping/Menu Utama
if __name__ == "__main__":
    main_menu()
