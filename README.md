Image Restoration Project
Deskripsi
Proyek ini adalah aplikasi untuk restorasi gambar yang rusak menggunakan algoritma inpainting naive stokes. Aplikasi ini menggunakan antarmuka pengguna grafis (GUI) sederhana untuk memuat gambar yang rusak, membuat mask otomatis, dan memperbaiki gambar menggunakan mask tersebut.

Fitur
Memuat Gambar Rusak: Memungkinkan pengguna untuk memuat gambar yang rusak ke dalam aplikasi.
Masking Gambar Secara Manual: Memungkinkan pengguna untuk memuat mask gambar secara manual.
Masking Otomatis: Membuat mask gambar secara otomatis menggunakan teknik thresholding.
Restorasi Gambar: Memperbaiki gambar yang rusak menggunakan algoritma inpainting naive stokes.
Antarmuka Pengguna: GUI yang sederhana dan mudah digunakan.
Prasyarat
Pastikan Anda telah menginstal dependensi berikut sebelum menjalankan aplikasi:

Python 3.x
OpenCV
NumPy
Tkinter
PIL (Python Imaging Library)
Anda dapat menginstal dependensi ini dengan perintah berikut:

bash
Copy code
pip install opencv-python numpy pillow
Cara Menjalankan
Clone repository ini ke dalam komputer Anda.
bash
Copy code
git clone https://github.com/username/image-restoration.git
cd image-restoration
Jalankan aplikasi dengan perintah berikut:
bash
Copy code
python main.py
Cara Penggunaan
Klik tombol "Gambar Rusak" untuk memuat gambar yang rusak.
Klik tombol "Mask Gambar" untuk memuat mask gambar secara manual (opsional).
Klik tombol "Masking Otomatis" untuk membuat mask gambar secara otomatis.
Klik tombol "Perbaiki Gambar" untuk memproses dan memperbaiki gambar yang rusak.
Struktur Proyek