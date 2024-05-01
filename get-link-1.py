import pyshorteners

link_asli = input("masukan link: ")
Shortener = pyshorteners.Shortener()

result = Shortener.tinyurl.short(link_asli)
print(result)
