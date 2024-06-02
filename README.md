# Image Restoration Project

## Deskripsi
Proyek ini adalah aplikasi untuk restorasi gambar yang rusak menggunakan algoritma inpainting naive stokes. Aplikasi ini menggunakan antarmuka pengguna grafis (GUI) sederhana untuk memuat gambar yang rusak, membuat mask otomatis, dan memperbaiki gambar menggunakan mask tersebut.

## Fitur
1. **Memuat Gambar Rusak**: Memungkinkan pengguna untuk memuat gambar yang rusak ke dalam aplikasi.
2. **Memuat Masking Gambar**: Memungkinkan pengguna untuk memuat mask gambar yang sudah dibuat secara manual.
3. **Restorasi Gambar**: Memperbaiki gambar yang rusak menggunakan algoritma inpainting naive stokes.
4. **Antarmuka Pengguna**: GUI yang sederhana dan mudah digunakan.

## Prasyarat
Pastikan Anda telah menginstal dependensi berikut sebelum menjalankan aplikasi:
- Python 3.x
- OpenCV
- NumPy
- Tkinter
- PIL (Python Imaging Library)

Anda dapat menginstal dependensi ini dengan perintah berikut:
```bash
pip install -r requirements.txt
```

## Cara Menjalankan
Clone repository ini ke dalam komputer Anda.
```bash
Copy code
git clone https://github.com/username/image-restoration.git
cd image-restoration
```
Jalankan aplikasi dengan perintah berikut:
```bash
python main.py
```

## Cara Penggunaan
1. Klik tombol "Gambar Rusak" untuk memuat gambar yang rusak.
2. Klik tombol "Mask Gambar" untuk memuat mask gambar secara manual (opsional).
3. Klik tombol "Masking Otomatis" untuk membuat mask gambar secara otomatis.
4. Klik tombol "Perbaiki Gambar" untuk memproses dan memperbaiki gambar yang rusak.
