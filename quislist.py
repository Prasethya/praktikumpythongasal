# 1. Buatlah variabel dengan nama kata benda
# 2. Isikan data pada variabel tersebut sejumlah 17 data
kamar = ["bantal","guling","selimut","kasur","buku","lemari","ranjang","sabun mandi","sabun cuci","pintu","jendela","keset","baju","celana","hangger","kabel","laptop"]

# 3. Tambahkan 1 data paling belakang pada variabel tersebut
kamar.append("peci")

# 4. Tambahkan 1 data pada indeks ke-3
kamar.insert(3,"jam")
#print(kamar)

#cetak variable dengan menggunakan fungsi for
print ("semua barang: ada {} barang".format(len(kamar)))
for barang in kamar:
    print(barang)
