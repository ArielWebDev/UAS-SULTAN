"main.py"
'''
### `task_manager.py` (Modul Utama)

```python
# Import class TaskManager dari modul task_functions
from task_functions import TaskManager
```

- **Line 1:** Mengimport class `TaskManager` dari modul `task_functions`.

```python
# Membuat objek TaskManager
task_manager = TaskManager()
```

- **Line 3-4:** Membuat objek `TaskManager` dengan nama `task_manager`.

```python
# Loop utama program
while True:
```

- **Line 6-7:** Memulai loop utama program.

```python
    # Menampilkan menu
    task_manager.display_menu()
```

- **Line 8-9:** Memanggil metode `display_menu` dari objek `task_manager` untuk menampilkan menu.

```python
    # Menerima input pilihan menu dari pengguna
    pilihan = input("Pilih menu (1/2/3/4/5): ")
```

- **Line 10-11:** Menerima input dari pengguna untuk memilih opsi menu.

```python
    # Memproses pilihan menu
    task_manager.process_menu(pilihan)
```

- **Line 12-13:** Memanggil metode `process_menu` dari objek `task_manager` untuk memproses pilihan menu.

```python
    # Keluar dari loop jika pilihan menu adalah 5
    if pilihan == "5":
        break
```

- **Line 14-15:** Menghentikan loop jika pilihan menu adalah 5 (keluar).

'''
"task_functions.py"
'''

```python
# Import modul datetime untuk bekerja dengan objek waktu dan tanggal
from datetime import datetime
```

- **Line 2:** Mengimport modul `datetime` untuk bekerja dengan objek waktu dan tanggal.

```python
# Class untuk mengelola tugas-tugas
class TaskManager:
```

- **Line 4:** Mendefinisikan class `TaskManager` untuk mengelola tugas-tugas.

```python
    # Constructor untuk inisialisasi objek TaskManager
    def __init__(self):
```

- **Line 6-8:** Constructor class `TaskManager` untuk inisialisasi objek dengan atribut `daftar_tugas`.

```python
        # Atribut untuk menyimpan daftar tugas
        self.daftar_tugas = []
```

- **Line 10-11:** Membuat atribut `daftar_tugas` sebagai list kosong.

```python
    # Metode untuk menampilkan menu pilihan
    def display_menu(self):
        print("\n===== Menu =====")
        print("1. Tambah Tugas")
        print("2. Tandai Selesai")
        print("3. Tampilkan Daftar Tugas")
        print("4. Tugas Belum Selesai dan Simpan ke File")
        print("5. Keluar")
```

- **Line 13-20:** Metode `display_menu` untuk menampilkan menu pilihan.

```python
    # Metode untuk memproses pilihan menu
    def process_menu(self, pilihan):
        if pilihan == "1":
            self.tambah_tugas()
        elif pilihan == "2":
            self.tandai_selesai()
        elif pilihan == "3":
            self.tampilkan_daftar_tugas()
        elif pilihan == "4":
            self.tugas_belum_selesai()
        elif pilihan == "5":
            print("Program selesai.")
        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")
```

- **Line 22-33:** Metode `process_menu` untuk memproses pilihan menu dengan memanggil metode yang sesuai.

```python
    # Metode untuk menambahkan tugas ke dalam daftar
    def tambah_tugas(self):
```

- **Line 35-37:** Metode `tambah_tugas` untuk menambahkan tugas ke dalam daftar.

```python
        # Menerima input nama tugas dari pengguna
        nama_tugas = input("Masukkan nama tugas: ")
```

- **Line 39:** Menerima input dari pengguna untuk nama tugas.

```python
        # Menerima input deadline tugas dari pengguna
        deadline_str = input("Masukkan deadline (format: dd/mm/yyyy, kosongkan jika tidak ada deadline): ")
```

- **Line 41-42:** Menerima input dari pengguna untuk deadline tugas.

```python
        try:
            # Mengonversi string deadline ke objek datetime jika tidak kosong, jika kosong, set menjadi None
            deadline = datetime.strptime(deadline_str, "%d/%m/%Y").date() if deadline_str else None
```

- **Line 44-46:** Menggunakan `try-except` untuk mengonversi string deadline menjadi objek `datetime`, menangani pengecualian jika format tidak valid.

```python
            # Menambahkan tugas ke dalam daftar_tugas
            self.daftar_tugas.append({'nama': nama_tugas, 'deadline': deadline, 'selesai': False})
```

- **Line 48-50:** Menambahkan tugas baru ke dalam `daftar_tugas`.

```python
            # Menampilkan pesan bahwa tugas berhasil ditambahkan
            print("Tugas berhasil ditambahkan!")
```

- **Line 52:** Menampilkan pesan bahwa tugas berhasil ditambahkan.

```python
        except ValueError:
            # Menangani pengecualian jika format deadline tidak valid
            print("Format deadline tidak valid. Gunakan format dd/mm/yyyy.")
```

- **Line 54-56:** Menangani pengecualian jika format deadline tidak valid.

```python
    # Metode untuk menandai tugas sebagai selesai
    def tandai_selesai(self):
```

- **Line 58-60:** Metode `tandai_selesai` untuk menandai tugas sebagai selesai.

```python
        # Menampilkan daftar tugas
        self.tampilkan_daftar_tugas()
```

- **Line 62:** Memanggil metode `tampilkan_daftar_tugas` untuk menampilkan daftar tugas.

```python
        # Menerima input indeks tugas yang selesai dari pengguna
        indeks_selesai = int(input("Masukkan indeks tugas yang selesai: ")) - 1
```

- **Line 64-65:** Menerima input dari pengguna untuk indeks tugas yang selesai.

```python
        # Memeriksa apakah indeks selesai valid
        if 0 <= indeks_selesai < len(self.daftar_tugas):
```

- **Line 67-68:** Memeriksa apakah indeks selesai yang dimasukkan pengguna valid.

```python
            # Menandai tugas sebagai selesai
            self.daftar_tugas[indeks_selesai]['selesai'] = True
```

- **Line

 70:** Menandai tugas sebagai selesai berdasarkan indeks yang dimasukkan pengguna.

```python
            # Menampilkan pesan bahwa tugas telah selesai
            print(f"Tugas '{self.daftar_tugas[indeks_selesai]['nama']}' ditandai sebagai selesai.")
```

- **Line 72:** Menampilkan pesan bahwa tugas tertentu telah ditandai sebagai selesai.

```python
        else:
            # Menangani jika indeks tidak valid
            print("Indeks tugas tidak valid.")
```

- **Line 74-75:** Menangani situasi jika indeks yang dimasukkan pengguna tidak valid.

```python
    # Metode untuk menampilkan daftar tugas
    def tampilkan_daftar_tugas(self):
```

- **Line 77-79:** Metode `tampilkan_daftar_tugas` untuk menampilkan daftar tugas.

```python
        # Memeriksa apakah daftar tugas kosong
        if not self.daftar_tugas:
```

- **Line 81-82:** Memeriksa apakah daftar tugas kosong.

```python
            # Menampilkan pesan jika daftar tugas kosong
            print("Daftar tugas kosong.")
```

- **Line 84:** Menampilkan pesan jika daftar tugas kosong.

```python
        else:
            # Menampilkan daftar tugas
            print("\nDaftar Tugas:")
```

- **Line 86-87:** Menampilkan daftar tugas jika tidak kosong.

```python
            for i, tugas in enumerate(self.daftar_tugas):
```

- **Line 89:** Melakukan iterasi pada daftar tugas menggunakan fungsi `enumerate` untuk mendapatkan indeks dan nilai.

```python
                status = "Selesai" if tugas['selesai'] else "Belum Selesai"
                print(f"{i + 1}. {tugas['nama']} (Deadline: {tugas['deadline']}, Status: {status})")
```

- **Line 91-93:** Menampilkan informasi setiap tugas termasuk nama, deadline, dan status (selesai/belum selesai).

```python
    # Metode untuk menampilkan dan menyimpan daftar tugas yang belum selesai ke dalam file teks
    def tugas_belum_selesai(self):
```

- **Line 95-97:** Metode `tugas_belum_selesai` untuk menampilkan dan menyimpan daftar tugas yang belum selesai ke dalam file teks.

```python
        # Membuat list belum_selesai yang berisi tugas-tugas yang belum selesai
        belum_selesai = [tugas for tugas in self.daftar_tugas if not tugas['selesai']]
```

- **Line 99-100:** Membuat list `belum_selesai` yang berisi tugas-tugas yang belum selesai.

```python
        # Memeriksa apakah ada tugas yang belum selesai
        if belum_selesai:
```

- **Line 102-103:** Memeriksa apakah ada tugas yang belum selesai.

```python
            # Menampilkan tugas yang belum selesai
            print("\nTugas yang belum selesai:")
            for tugas in belum_selesai:
                print(f"- {tugas['nama']}")
```

- **Line 105-108:** Menampilkan nama tugas yang belum selesai.

```python
            # Menyimpan daftar tugas ke dalam file teks
            with open("tugas_belum_selesai.txt", "w") as file:
                file.write("Tugas yang belum selesai:\n")
                for tugas in belum_selesai:
                    file.write(f"- {tugas['nama']}\n")
```

- **Line 110-113:** Menyimpan daftar tugas yang belum selesai ke dalam file teks.

```python
            # Menampilkan pesan bahwa daftar tugas yang belum selesai disimpan dalam file teks
            print("Daftar tugas yang belum selesai disimpan dalam file 'tugas_belum_selesai.txt'.")
```

- **Line 115:** Menampilkan pesan bahwa daftar tugas yang belum selesai telah disimpan.

```python
        else:
            # Menampilkan pesan bahwa semua tugas sudah selesai jika tidak ada tugas yang belum selesai
            print("Semua tugas sudah selesai.")
```

- **Line 117-118:** Menampilkan pesan bahwa semua tugas sudah selesai jika tidak ada tugas yang belum selesai.

'''
