#jika ingin membuat pasword yg sulit, inilah codingnya
import random

kecil = "abcdefghijklmnopqrstuvwxyz"
besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
angka = "1234567890"
simbol= "!@#$%^&*():;'<>,/?'~[]\|}{"

string = kecil + besar + angka + simbol
length = 16
password = "".join (random.sample(string, length))

print("password : " + password)
