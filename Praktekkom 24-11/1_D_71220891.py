# nomor 1a
print("Selamat Datang di Kalkulator Sederhana")
print("Ketik 1 untuk menghitung penjumlahan.")
print("Ketik 2 untuk menghitung pengurangan.")
print("Ketik 3 untuk menghitung perkalian.")
print("Ketik 4 untuk menghitung pembagian.")
print("Ketik 5 untuk menghitung sisa hasil bagi (modulus).")
print("Ketik 6 untuk menghitung pemagkatan.")
operasi = int(input("Masukkan pilihan anda: "))
bil_1 = eval(input("Masukkan bilangan pertama: "))
bil_2 = eval(input("Masukkan bilangan kedua: "))
if operasi == '1':
    hasil = bil_1 + bil_2
    print("Hasil dari" {bil_1} "dijumlahkan dengan" {bil_2} "adalah" {hasil}"")
