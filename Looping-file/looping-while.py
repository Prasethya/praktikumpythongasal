
#Looping while kompleks
# Jawab = 'ya'
# hitung = 0
# while(True):
#     hitung += 1
#     jawab = input("ulang lagi tidak? ")
#     if jawab == 'tidak':
#         break
# print(f"Total keseluruhan perulangan: {hitung}")


#looping while 
# i = 1 
# while i < 9 :
#     print (i)
#     i+= 1


#looping whie steatment break 
# i=1 
# while i < 6 :
#     print (i)
#     if i == 3:
#         break 
#     i+=1


#looping while witn steatment continue
# i=0
# while i < 6 :
#     i+= 1
#     if i == 3 :
#         continue
#     print (i)


#inisialisasi perantsren sebagai kamus (dictionary) untk penyimpan data santri
pesantren = {}

while True :
    print("\nMenu:")
    print("1. Tambah Data Santri")
    print("2. Lihat Data Santri")
    print("3. Keluar")

    Pilihan = input("pilih menu (1/2/3/):")

    if Pilihan == '1':
        nama = input ("masukan nama santri: ")
        usia = int(input("masukan usia santri" ))
        kelas = input("masukan kelas santri")
        pesantren[nama] = {'usia':usia, 'kelas': kelas}
        print(f"data santri {nama} telah di tambahkan.")

    elif Pilihan == '2' :
        if len(pesantren) == 0:
            print("tidak ada data santri yang tersedia.")
        else:
            print("\nData santri:")
            for nama, data in pesantren.items() :
                print(f"Nama: {nama}, Usia: {data['usia']}, kelas: {data['kelas']}")

    elif Pilihan =='3':
        print("terima kasih, progam selesai.")
        break

    else :
        print("pilihan tidak valid. silahkan pilih 1, 2, atau 3.")
