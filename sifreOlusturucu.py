import random
karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


#Bir değişken oluşturun ve kullanıcıdan parolanın uzunluğunu girmesini isteyin
uzunluk=int(input("Parola uzunluğu:"))
#Programın oluşturulan parolayı saklayacağı bir değişken oluşturun
parola=""
#Karakter değişkeninden rastgele bir karakter seçmek ve
#bunu oluşturulan parolanın bulunduğu değişkene eklemeks
#için bir döngü ve random kütüphanesi kullanın
#kullanıcının girdiği değer kadar rastgele karakter oluşturabilecek 
#bir döngü oluşturun
for n in range(uzunluk):
    parola=parola+random.choice(karakterler)


#Elde edilen parolayı konsola yazdırın
print(parola)