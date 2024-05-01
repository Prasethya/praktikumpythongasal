nilai_ujian = str(input("masukan nilai ujian: "))

#menentukan nilai kategori anda menggunakan operasi pembanding
if nilai_ujian == "A":
   kategori = "luar biasa"
elif nilai_ujian == "B":
   kategori = "baik"
elif nilai_ujian == "C":
   kategori = "cukup"
elif nilai_ujian == "D":
   kategori = "kurang"
else :
   kategori = "mengulang"

#menampilkan hasil kategori
print(f"nilai ujian anda adalah {nilai_ujian}, sehingga masuk kategori: {kategori}") 