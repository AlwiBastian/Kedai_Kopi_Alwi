class Diskon:
    def __init__(self, diskon):
        self.__diskon = diskon

    def get_diskon(self):
        return self.__diskon

class MenuKopi:
    def __init__(self, nama, harga):
        self.__nama = nama
        self.__harga = harga

    # Get untuk mengambil nilai dari sebuah variabel
    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    # Set untuk mengubah nilai dari sebuah variabel
    def set_nama(self, nama):
        self.__nama = nama

    def set_harga(self, harga):
        self.__harga = harga

class AnandaCoffee:
    def __init__(self):
        self.__menu_kopi = [
            MenuKopi("ES Kopi Susu", 11000),
            MenuKopi("ES Kopi Coklat", 12000),
            MenuKopi("ES Kopi Hitam", 11000),
            MenuKopi("ES Americano", 14000)
        ]
        
        self.__diskon = [
            Diskon(0),
            Diskon(0.05),
            Diskon(0.1),
            Diskon(0.15),
            Diskon(0.2)
        ]

    def show_menu(self):
        print("""
        ==============================
        Ananda Coffe
        List Menu Minuman Kopi
        ==============================
        A. ES Kopi Susu : Rp 11.000
        B. ES Kopi Coklat : Rp 12.000
        C. ES Kopi Hitam : Rp 11.000
        D. Ice Americano : Rp 14.000
        ==============================
        """)

    def pesan_menu(self, pesan, jumlahpesan):
        harga = 0
        ppn = 0
        diskon = 0
        totalharga = 0

        if pesan == "a":
            menu = self.__menu_kopi[0]
            harga = menu.get_harga() * jumlahpesan
            ppn = int(harga * 0.1)
            if jumlahpesan >= 5:
                diskon = harga * self.__diskon[4].get_diskon()
                totalharga = harga - diskon + ppn
            elif jumlahpesan >= 4:
                diskon = harga * self.__diskon[3].get_diskon()
                totalharga = harga - diskon + ppn
            elif jumlahpesan >= 3:
                diskon = harga * self.__diskon[2].get_diskon()
                totalharga = harga - diskon + ppn
            elif jumlahpesan >= 2:
                diskon = harga * self.__diskon[1].get_diskon()
                totalharga = harga - diskon + ppn
            else:
                totalharga = harga + ppn
        elif pesan == "b":
            menu = self.__menu_kopi[1]
            harga = menu.get_harga() * jumlahpesan
            ppn = int(harga * 0.1)
            if jumlahpesan >= 5:
                diskon = harga * self.__diskon[4].get_diskon()
                totalharga = harga - diskon + ppn
            elif jumlahpesan >= 4:
                diskon = harga * self.__diskon[3].get_diskon()
                totalharga = harga - diskon + ppn
            elif jumlahpesan >= 3:
                diskon = harga * self.__diskon[2].get_diskon()
                totalharga = harga - diskon + ppn
            elif jumlahpesan >= 2:
                diskon = harga * self.__diskon[1].get_diskon()
                totalharga = harga - diskon + ppn
            else:
                totalharga = harga + ppn
        elif pesan == "c":
            menu = self.__menu_kopi[2]
            harga = menu.get_harga() * jumlahpesan
            ppn = int(harga * 0.1)
            if jumlahpesan >= 5:
                diskon = harga * self.__diskon[4].get_diskon()
                totalharga = harga - diskon + ppn
            elif jumlahpesan >= 4:
                diskon = harga * self.__diskon[3].get_diskon()
                totalharga = harga - diskon + ppn
            elif jumlahpesan >= 3:
                diskon = harga * self.__diskon[2].get_diskon()
                totalharga = harga - diskon + ppn
            elif jumlahpesan >= 2:
                diskon = harga * self.__diskon[1].get_diskon()
                totalharga = harga - diskon + ppn
            else:
                totalharga = harga + ppn
        elif pesan == "d":
            menu = self.__menu_kopi[3]
            harga = menu.get_harga() * jumlahpesan
            ppn = int(harga * 0.1)
            if jumlahpesan >= 5:
                diskon = harga * self.__diskon[4].get_diskon()
                totalharga = harga - diskon + ppn
            elif jumlahpesan >= 4:
                diskon = harga * self.__diskon[3].get_diskon()
                totalharga = harga - diskon + ppn
            elif jumlahpesan >= 3:
                diskon = harga * self.__diskon[2].get_diskon()
                totalharga = harga - diskon + ppn
            elif jumlahpesan >= 2:
                diskon = harga * self.__diskon[1].get_diskon()
                totalharga = harga - diskon + ppn
            else:
                totalharga = harga + ppn
        else:
            print("Pilihan menu tidak valid!")

        if totalharga > 0:
            print("Detail Pesanan:")
            print("Menu: ", menu.get_nama())
            print("Jumlah Pemesanan: ", jumlahpesan)
            print("Harga: Rp", harga)
            print("Diskon: Rp", diskon)
            print("PPN: Rp", ppn)
            print("Total Harga: Rp", totalharga)

# output
while True:
    ananda_coffee = AnandaCoffee()
    ananda_coffee.show_menu()
    pesan = input("Pilih menu (a/b/c/d): ")
    jumlah_pesan = int(input("Masukkan jumlah pesanan: "))
    ananda_coffee.pesan_menu(pesan, jumlah_pesan)

    lanjutkan = input("Apakah ingin melanjutkan pemesanan? (y/n): ")
    if lanjutkan.lower() != "y":
        break