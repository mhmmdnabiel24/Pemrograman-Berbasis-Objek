# Ringkasan Pelanggaran Prinsip SOLID

Berdasarkan isi `sebelum_refactoring.py`, berikut ringkasan pelanggaran prinsip SOLID yang ditemukan pada implementasi `ValidatorManager`.

## Kode contoh (intisari)

```python
class ValidatorManager:
    def validate(self, sks, prasyarat_terpenuhi):
        if sks > 24:
            return "Registrasi gagal: SKS melebihi batas"
        elif not prasyarat_terpenuhi:
            return "Registrasi gagal: Prasyarat belum terpenuhi"
        else:
            return "Registrasi berhasil"

validator = ValidatorManager()
```

## Temuan pelanggaran

- **SRP (Single Responsibility Principle)**: `ValidatorManager` melakukan beberapa tugas sekaligus — pengecekan SKS, pengecekan prasyarat, dan menentukan hasil registrasi. Kelas ini memiliki lebih dari satu alasan untuk berubah sehingga sulit dipelihara.

- **OCP (Open/Closed Principle)**: Menambahkan aturan baru (mis. validasi IPK atau batas SKS berbeda) mengharuskan modifikasi langsung pada method `validate()` dengan menambahkan percabangan `if/elif`. Kode tidak mudah diperluas tanpa diubah.

- **DIP (Dependency Inversion Principle)**: Tidak ada abstraksi untuk aturan validasi; `ValidatorManager` bergantung pada implementasi konkret (logika kondisional). Tanpa interface/abstraksi dan injection, kode menjadi kaku dan sulit diuji.

## Contoh masalah praktis

- Jika ingin menambah validasi IPK minimum, developer harus menambah kondisi di `validate()` sehingga meningkatkan risiko bug dan membuat review lebih sulit.
- Untuk kebutuhan pengujian unit, sulit melakukan mocking atau menguji aturan individual karena semuanya terikat dalam satu method.

## Rekomendasi singkat

- Pisahkan tanggung jawab: buat kelas validator terpisah (mis. `SksValidator`, `PrasyaratValidator`).
- Definisikan abstraksi (mis. base `Validator` atau protocol) yang menyediakan method `validate()` atau `is_valid()`.
- Gunakan dependency injection untuk menyusun kumpulan validator di komponen registrasi.
- Tambahkan unit test untuk setiap validator.

## Cara menjalankan contoh

Jalankan file contoh asli untuk melihat output saat ini:

```bash
python tugas/sebelum_refactoring.py
```

