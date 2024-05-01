from pytube import YouTube

url = str(input('[+] Masukan url : '))
my_vidio = YouTube(url)
print(my_vidio.title)

my_vidio = my_vidio.streams.get_highest_resolution()
my_vidio.download()

