#for x in "indra":
#     print(x)

#___________________________________________________________________________________________________________________________________

#nested loop
#santri = ["abad","kenzie","zaydan"]
#kegiatan = ["pramuka","jujitsu","futsal"]
#for x in santri :
 #   for y in kegiatan :
#        print(x,y)

#___________________________________________________________________________________________________________________________________

#uncounted loop
#ulang = 50
#for i in range(ulang):
#    print(f"perulangan ke-{i}")

#ulang = 1000
#for i in range (ulang) :
#   print(f"perulangan ke-{i}")

#___________________________________________________________________________________________________________________________________

#for with steatment "break"
#penjelasan :

#mapel = ["mtk","biology","fisika","kimia","algoritma","siskom","tkj","bindo","dirasah","tafsit hadis"]
#for x in mapel :
#    print(x)
#    if x == "siskom" :
#        break

#___________________________________________________________________________________________________________________________________

#for mith steatment continu
#penjelasan =

#for x in mapel :
 #   if x == "siskom" :
 #       continue
  #  print(x)

#______________________________________________________________________________________________________
#nestened loop
#Contoh penggunaan Nested Loop
#Catatan: Penggunaan modulo pada kondisional mengasumsikan nilai selain nol sebagai True(benar) dan nol sebagai False(salah)

i = 2
while(i < 100):
  j = 2
while(j <= (i/j)):
  if not(i%j): break
  j = j + 1
  if (j > i/j) : print(i, " is prime")
  i = i + 1

print("Good bye!")