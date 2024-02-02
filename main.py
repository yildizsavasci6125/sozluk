sozluk = {
    "esef" : "Olmaması , yapılmaması gereken veya yapılamayan bir şey için duyulan üzüntü.",
    "emin" : "Güvenilir, doğru"
}

print(*sozluk)

kullanici_istek = input("hangi kelimenin anlamını öğrenmek istiyorsunuz?:")

if kullanici_istek in sozluk.keys():
    print ("girdiğiniz kelimenin anlamı:" , sozluk[kullanici_istek])    
else:
    print ("bu kelime sözlükte bulunmuyor")
