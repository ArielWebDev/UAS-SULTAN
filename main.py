# Import class TaskManager dari modul task_functions
from task_functions import TaskManager

# Membuat objek TaskManager
task_manager = TaskManager()

# Loop utama program
while True:
    # Menampilkan menu
    task_manager.display_menu()

    # Menerima input pilihan menu dari pengguna
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    # Memproses pilihan menu
    task_manager.process_menu(pilihan)

    # Keluar dari loop jika pilihan menu adalah 5
    if pilihan == "5":
        break
