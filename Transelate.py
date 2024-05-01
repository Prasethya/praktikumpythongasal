from googletrans import Translator
tl = Translator()
text = input("masukan text : ")
result = tl.translate(text, dest='en')
print(result.text)