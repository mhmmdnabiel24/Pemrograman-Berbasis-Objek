# diskon_service.py
import pdb

class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""
    
    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        # Step 1: Hitung diskon
        jumlah_diskon = harga_awal * persentase_diskon / 100
        
        # Step 2: Hitung harga setelah diskon
        harga_akhir = harga_awal - jumlah_diskon

        # --- MASUKKAN BUG DISINI (Sesuai instruksi D.1) ---
        # Tambahkan PPN 10% secara tidak sengaja
        harga_akhir = harga_akhir 
        
        return harga_akhir

if __name__ == '__main__':
    calc = DiskonCalculator()
    hasil = calc.hitung_diskon(1000, 10)
    print(f"Hasil: {hasil}")