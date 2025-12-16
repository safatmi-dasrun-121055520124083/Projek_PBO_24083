# =========================================
# Proyek PBO: Sistem Kasir Sederhana
# Dibuat oleh: Safatmi Dasrun
# =========================================

class Barang:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"{self.nama} - Rp{self.harga}"


class Kasir:
    def __init__(self):
        self.keranjang = []

    def tambah_barang(self, barang):
        self.keranjang.append(barang)

    def hitung_total(self):
        total = 0
        for barang in self.keranjang:
            total += barang.harga
        return total

    def tampilkan_struk(self):
        print("\n=== STRUK BELANJA ===")
        for barang in self.keranjang:
            print(barang.info())
        print("--------------------")
        print(f"Total Bayar: Rp{self.hitung_total()}")
        print("====================")


# ===== Program Utama =====
kasir = Kasir()

barang1 = Barang("Beras", 12000)
barang2 = Barang("Gula", 8000)
barang3 = Barang("Minyak", 15000)

kasir.tambah_barang(barang1)
kasir.tambah_barang(barang2)
kasir.tambah_barang(barang3)

kasir.tampilkan_struk()
