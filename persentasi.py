'''
Tentu, berikut adalah penjelasan dalam bentuk paragraf untuk setiap bagian dari program Python untuk manajemen tugas:

### `task_manager.py`

Program dimulai dengan mengimpor class `TaskManager` dari modul `task_functions`.
Ini memungkinkan penggunaan fungsionalitas yang didefinisikan di dalam class tersebut.
Selanjutnya, objek `task_manager` dibuat sebagai instance dari class `TaskManager`.
Program berada dalam loop utama yang terus berjalan selama pengguna tidak memilih untuk keluar (menu pilihan 5).
Dalam setiap iterasi, program menampilkan menu menggunakan metode `display_menu` dari objek `task_manager` 
dan memproses pilihan pengguna dengan memanggil metode `process_menu`.

### `task_functions.py`

File ini berisi definisi class `TaskManager`, yang bertanggung jawab untuk mengelola tugas-tugas. 
Constructor class inisialisasi objek dengan atribut `daftar_tugas`, yang digunakan untuk menyimpan informasi tugas-tugas. 
Metode `display_menu` menampilkan menu pilihan kepada pengguna.
Metode `process_menu` memproses pilihan pengguna dan memanggil metode yang sesuai untuk setiap opsi. 
Ada juga metode-metode lain seperti `tambah_tugas`, `tandai_selesai`, `tampilkan_daftar_tugas`, dan `tugas_belum_selesai` 
yang mengelola operasi spesifik seperti menambahkan tugas baru, menandai tugas sebagai selesai, 
menampilkan daftar tugas,dan menyimpan tugas yang belum selesai ke dalam file teks.
Setiap metode di dalam class memiliki penjelasan yang mendetail. Metode `tambah_tugas` menerima input dari pengguna, 
seperti nama tugas dan deadline, dan menangani kasus-kasus khusus seperti format deadline yang tidak valid.
Metode `tandai_selesai` meminta pengguna untuk memilih tugas yang selesai dari daftar dan menandainya. 
Metode `tampilkan_daftar_tugas` dan `tugas_belum_selesai` menampilkan informasi daftar tugas saat ini dan 
daftar tugas yang belum selesai, masing-masing.
Program juga memanfaatkan modul `datetime` untuk bekerja dengan tanggal dan waktu. 
Pengecualian ditangani secara elegan untuk memastikan program tidak mengalami kegagalan yang tidak
diinginkan akibat input yang tidak valid. Terakhir, jika pengguna memilih untuk menyimpan daftar tugas yang
belum selesai ke dalam file teks, program akan menyimpannya dalam file "tugas_belum_selesai.txt" dan memberikan pesan konfirmasi.
Semoga penjelasan ini membantu dan menjelaskan fungsionalitas masing-masing bagian dari program. 
Jika ada pertanyaan lebih lanjut atau klarifikasi yang diperlukan, silakan beri tahu.
'''
