import pyttsx3
engine=pyttsx3.init()
adres=input("lütfen dosyanın adresini giriniz :")
dosya=open(adres,"r+")
#dosya=open("merhaba.txt","r+")#dosya açtım
dosya.write("helo ")#dosyanın içine yazılacakları girer
for i in dosya:

    engine.say(i)
    engine.runAndWait()
dosya.close()

"""
r	Mevcut dosyayı okumak için açar, yoksa hata verir
w	Dosya yoksa oluşturur, varsa içeriği silerek sıfır dosya açar
a	Dosya yoksa oluşturur, varsa dosyanın sonunda imleçten başlayarak ekleme yapar
r+	Dosyayı hem okuma, hem yazma(w) modunda açar
"""