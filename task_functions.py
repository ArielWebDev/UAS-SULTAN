# Import modul datetime untuk bekerja dengan objek waktu dan tanggal
from datetime import datetime

# Class untuk mengelola tugas-tugas
class TaskManager:
    # Constructor untuk inisialisasi objek TaskManager
    def __init__(self):
        # Atribut untuk menyimpan daftar tugas
        self.daftar_tugas = []

    # Metode untuk menampilkan menu pilihan
    def display_menu(self):
        print("\n===== Menu =====")
        print("1. Tambah Tugas")
        print("2. Tandai Selesai")
        print("3. Tampilkan Daftar Tugas")
        print("4. Tugas Belum Selesai dan Simpan ke File")
        print("5. Keluar")

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

    # Metode untuk menambahkan tugas ke dalam daftar
    def tambah_tugas(self):
        # Menerima input nama tugas dari pengguna
        nama_tugas = input("Masukkan nama tugas: ")

        # Menerima input deadline tugas dari pengguna
        deadline_str = input("Masukkan deadline (format: dd/mm/yyyy, kosongkan jika tidak ada deadline): ")

        try:
            # Mengonversi string deadline ke objek datetime jika tidak kosong, jika kosong, set menjadi None
            deadline = datetime.strptime(deadline_str, "%d/%m/%Y").date() if deadline_str else None

            # Menambahkan tugas ke dalam daftar_tugas
            self.daftar_tugas.append({'nama': nama_tugas, 'deadline': deadline, 'selesai': False})

            # Menampilkan pesan bahwa tugas berhasil ditambahkan
            print("Tugas berhasil ditambahkan!")

        except ValueError:
            # Menangani pengecualian jika format deadline tidak valid
            print("Format deadline tidak valid. Gunakan format dd/mm/yyyy.")

    # Metode untuk menandai tugas sebagai selesai
    def tandai_selesai(self):
        # Menampilkan daftar tugas
        self.tampilkan_daftar_tugas()

        # Menerima input indeks tugas yang selesai dari pengguna
        indeks_selesai = int(input("Masukkan indeks tugas yang selesai: ")) - 1

        # Memeriksa apakah indeks selesai valid
        if 0 <= indeks_selesai < len(self.daftar_tugas):
            # Menandai tugas sebagai selesai
            self.daftar_tugas[indeks_selesai]['selesai'] = True

            # Menampilkan pesan bahwa tugas telah selesai
            print(f"Tugas '{self.daftar_tugas[indeks_selesai]['nama']}' ditandai sebagai selesai.")

        else:
            # Menangani jika indeks tidak valid
            print("Indeks tugas tidak valid.")

    # Metode untuk menampilkan daftar tugas
    def tampilkan_daftar_tugas(self):
        # Memeriksa apakah daftar tugas kosong
        if not self.daftar_tugas:
            # Menampilkan pesan jika daftar tugas kosong
            print("Daftar tugas kosong.")
        else:
            # Menampilkan daftar tugas
            print("\nDaftar Tugas:")
            for i, tugas in enumerate(self.daftar_tugas):
                status = "Selesai" if tugas['selesai'] else "Belum Selesai"
                print(f"{i + 1}. {tugas['nama']} (Deadline: {tugas['deadline']}, Status: {status})")

    # Metode untuk menampilkan dan menyimpan daftar tugas yang belum selesai ke dalam file teks
    def tugas_belum_selesai(self):
        # Membuat list belum_selesai yang berisi tugas-tugas yang belum selesai
        belum_selesai = [tugas for tugas in self.daftar_tugas if not tugas['selesai']]

        # Memeriksa apakah ada tugas yang belum selesai
        if belum_selesai:
            # Menampilkan tugas yang belum selesai
            print("\nTugas yang belum selesai:")
            for tugas in belum_selesai:
                print(f"- {tugas['nama']}")

            # Menyimpan daftar tugas ke dalam file teks
            with open("tugas_belum_selesai.txt", "w") as file:
                file.write("Tugas yang belum selesai:\n")
                for tugas in belum_selesai:
                    file.write(f"- {tugas['nama']}\n")

            # Menampilkan pesan bahwa daftar tugas yang belum selesai disimpan dalam file teks
            print("Daftar tugas yang belum selesai disimpan dalam file 'tugas_belum_selesai.txt'.")

        else:
            # Menampilkan pesan bahwa semua tugas sudah selesai jika tidak ada tugas yang belum selesai
            print("Semua tugas sudah selesai.")
