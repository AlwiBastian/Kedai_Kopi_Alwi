# Kedai_Kopi_Alwi
kode ini adalah program sederhana untuk memesan minuman kopi dengan menggunakan bahasa pemrograman Python. Program ini mencakup daftar menu, harga, diskon dan perhitungan total harga yang harus dibayarkan.

Struktur Kode

Program ini terdiri dari tiga kelas:

1. Diskon: kelas ini berisi atribut diskon yang menyimpan nilai diskon (dalam bentuk persen). Kelas ini memiliki metode get_diskon() untuk mengambil nilai diskon.

2. MenuKopi: kelas ini berisi atribut nama dan harga yang menyimpan nama dan harga dari sebuah menu minuman kopi. Kelas ini memiliki empat metode: get_nama() dan get_harga() untuk mengambil nilai dari atribut nama dan harga, dan set_nama(nama) dan set_harga(harga) untuk mengubah nilai dari atribut nama dan harga.

3. AnandaCoffee: kelas ini adalah inti dari program ini. Kelas ini berisi dua atribut: menu_kopi dan diskon. Atribut menu_kopi adalah sebuah list yang berisi empat objek MenuKopi, masing-masing mewakili satu menu minuman kopi. Atribut diskon adalah sebuah list yang berisi lima objek Diskon, masing-masing mewakili satu level diskon (tidak ada diskon, diskon 5%, diskon 10%, diskon 15%, dan diskon 20%). 

Kelas ini memiliki tiga metode: 
-show_menu() untuk menampilkan daftar menu minuman kopi
-pesan_menu(pesan, jumlahpesan) untuk memesan sebuah menu minuman kopi dengan jumlah tertentu
-hitung_total(harga, jumlahpesan) untuk menghitung total harga pesanan
