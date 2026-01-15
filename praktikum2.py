# PRAKTIKUM PETEMUAN 2
# Program "Kasir Toko Buku"

print("\n>>> KASIR TOKO BUKU <<<")
total_belanja = 0

# Looping untuk menginput harga buku
while True:
    harga_per_buku = int(input("Masukkan Satu Per Satu Harga Buku : Rp"))

    # Sentinel Value: Jika ketik "0" Program Input Behenti
    if harga_per_buku == 0:
        break # Program Berhenti Meminta Input Harga
    elif harga_per_buku < 0:
        print("Error: Harga Tidak Valid!")
    else:
        total_belanja += harga_per_buku

# Menghitung Diskon
if total_belanja > 500000:
    diskon = total_belanja * 0.2
elif total_belanja > 200000:
    diskon = total_belanja * 0.1
else:
    diskon = 0 # Tidak Ada Diskon

# Menghitung Total Setelah Diskon
total_bayar = total_belanja - diskon

# Menampilkan Pembayaran
print("\n=== STRUK PEMBAYARAN ===")
print(f"Total Belanja   : Rp {total_belanja}")
print(f"Diskon          : Rp {diskon}")
print(f"Total Bayar     : Rp {total_bayar}")
print ("\nTERIMAKASIH TELAH BERBELANJA!")
