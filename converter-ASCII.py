#character = input("masukan sebuah karakter")
#ascii_code = ord(character)
#print(f"kode ascii dari{character}adalah{ascii_code}")

ascii_code = int(input("masukan kode ascii: "))
if 0 <= ascii_code <=255:
    character = chr(ascii_code)
    print(f"karakter yang sesuai dengan kode ascii {ascii_code} adalah {character}")
else:
    print(f"kode ascii harus beradadalam rentang 0 sampai 255")
