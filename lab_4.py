# DDP LAB-4
# Nama: Djaya Pamungkas
# NIM: 0110120007

# SOAL 1 - Mencetak nama
# Tuliskan program untuk Soal 1 di bawah ini

nama = input("Silahkan Masukkan Nama Anda : ")
#variabel nama yang menyimpan inputan dan mengeluarkan nama di terminal
jumlah = len(nama)
#variabel jumlah yang menghitung berapa jumlah karakter dari nama yang di masukan
x = 0
#variable kosong
while x < jumlah :
# x < jumlah ini akan melakukan perulangan
  x += 1
  # x += 1 setiap perualangan di jumlah 1
  print(nama[0:x])
  # mencetak hasil yang mecetak dari setiap kata
print()





# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini

while True:
#kosndisi dimana perulangan di nyatakan true
  text = input ("Silahkan Masukkan Sebuah Teks :")
  #variabel yang menyimpan inputan dan mengeluarkan nama di terminal
  a = len(text)
  #variabel a yang menghitung berapa jumlah karakter dari text yang di masukan
  if (a >=8 
  # memvalidasi bahwa a/text itu berjumalah lebih dari 8
  and (text.endswith("YYY") or text.endswith("yyy"))
  # memvalidasi text yang huruf akhiran "yyy" atau "YYY"
  and (text.startswith("NF") or text.startswith("nf") or
  # memvaidasi text yang huruf awalan nya "NF" atau "nf"
  text.startswith("Nf") or text.startswith("nF")) and
  # memvalidasi text yang huruf awalan nya "Nf" atau "nF"
  not (text.isalpha())):
  # memvalidasi yang bukan merupakan text
    print("teks valid, Welcome.")
    # mencetak text valid yang teks nya semua tersedia
    break
    # memberhentikan 
  else:
    print("teks tidak valid")
    # meencetak jika salah satu teks nya tidak ada maka tidak valid

print("\n Terimakasih dan Sampai Jumpa \n")
