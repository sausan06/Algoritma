# Pembahasan Logika (Deskriptif)
# Simulasi Logika ATM
import os

# Variabel Global untuk Menyimpan Saldo
saldo_nasabah = 1500000
pin_benar = "54321"

# Membersihkan Layar
def clear_screen():
    # Membarsihkan Layar Terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# Autentikasi Login
def login():
    """ Fungsi untuk Autentikasi Login Looping Max 3x Percobaan"""

    percobaan = 0
    # Looping hingga 3x Percobaan
    while percobaan < 3:
        pin = input("Masukkan 5 Digit PIN Anda:")
        # Cek PIN
        if pin == pin_benar:
            return True
        else:
            percobaan += 1
            print(f"PIN SALAH! Sisa Percobaan: {3 - percobaan}")
    return False

# Fungsi Menampilkan Saldo
def info_saldo():
    print(f"\n>>> Sisa Saldo Anda: Rp {saldo_nasabah:,}".replace(',','.')) # Format Rupiah

# Fungsi Untuk Setor Tunai
def setor_tunai():
    global saldo_nasabah # Mengakses Variabel Global untuk Diubah
    # Input Nominal Setor
    try:
        nominal = int(input("Masukkan Nominal Setor Tunai: +Rp"))
        # Validasi Input Positif
        if nominal > 0:
            saldo_nasabah += nominal
            print(" Setor Tunai Berhasil!")
            info_saldo()
        else:
            print("Error: Nominal Harus Positif!")
    except ValueError:
        print("Error: Masukkan Angka.")

# Fungsi Untuk Tarik Tunai
def tarik_tunai():
    global saldo_nasabah
    try:
        nominal = int(input("Masukkan Nominal Tarik Tunai: -Rp"))
        # Validasi Logika Bersarang
        if nominal <= 0:
            print("Error: Nominal Harus Positif!")
        elif nominal > saldo_nasabah:
            print("Error: Saldo Tidak Cukup!")
        else:
            saldo_nasabah -= nominal
            print("Penarikan Berhasil! Silahkan Ambil Uang Anda.")
    except ValueError:
        print("Error: Masukkan Angka.")

# Fungsi utama dengan menu
def main_menu():
    """ Looping Utama Aplikasi"""

    if not login():
        print("Akun Terblokir! Silahkan Hubungi CS.")
        return
    
# Jika Login Berhasil, Lanjut ke Menu Utama
    while True:
        print("\n=== WELECOME TO MENU ATM ===")
        print("1. CEK SALDO")
        print("2. SETOR TUNAI")
        print("3. TARIK TUNAI")
        print("4. KELUAR")

        pilihan = input("Pilih Menu (1-4):")
        if pilihan == '1':
            info_saldo()
        elif pilihan == '2':
            setor_tunai()
        elif pilihan == '3':
            tarik_tunai()
        elif pilihan == '4':
            print("Terima Kasih Telah Menggunakan Layanan ATM ini.")
            break
        else:
            print("Pilihan Tidak Valid!")

# Akhir dari Looping/Menu Utama
if __name__ == "__main__":
    main_menu()
