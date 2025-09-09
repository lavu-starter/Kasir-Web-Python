# Mini Project Kasir Kantin SMK

**Deskripsi:**
Aplikasi kasir sederhana untuk SMK kelas X menggunakan Python dan Flask.
Proyek ini melatih siswa membuat:

* Login & Register
* Dashboard dengan sidebar
* CRUD transaksi (Tambah, Daftar, Edit, Hapus)
* Perhitungan total pendapatan
* Tampilan harga dalam format Rupiah

**Fitur Utama:**

1. **Login & Register:** autentikasi sederhana menggunakan file CSV.
2. **Dashboard:** sidebar navigasi ke tambah transaksi dan daftar transaksi.
3. **Tambah Transaksi:** input item, harga, jumlah → total dihitung otomatis.
4. **Daftar Transaksi:** menampilkan semua transaksi, total pendapatan otomatis.
5. **Edit Transaksi:** ubah item, harga, jumlah, total diperbarui otomatis.
6. **Hapus Transaksi:** hapus transaksi secara langsung.
7. **Logout:** keluar dari aplikasi.

**Struktur Folder:**

```
kasir_Web/
├─ app.py
├─ users.csv
├─ transaksi.csv
├─ templates/
│   ├─ login.html
│   ├─ register.html
│   ├─ dashboard.html
│   ├─ tambah_transaksi.html
│   ├─ daftar_transaksi.html
│   └─ edit_transaksi.html
└─ static/  (opsional untuk CSS/JS)
```

**Cara Menjalankan:**

1. Pastikan Python 3 dan Flask sudah terinstall:

```bash
pip install flask
```

2. Jalankan aplikasi:

```bash
python app.py
```

3. Buka browser di:

```
http://127.0.0.1:5000
```

4. Praktik siswa: register → login → tambah transaksi → daftar → edit/hapus → logout

**Catatan:**

* CSV (`users.csv` dan `transaksi.csv`) akan otomatis dibuat saat aplikasi dijalankan pertama kali.
* Harga di input sebagai angka murni, format Rupiah hanya untuk tampilan.

**Lisensi:**
Proyek ini dibuat untuk pembelajaran di SMK, bebas digunakan dan dimodifikasi.
