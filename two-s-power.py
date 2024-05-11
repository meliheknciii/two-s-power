import numpy as np

# Kurallar şunlar ;
    # Bir sayı girilecek ve bu sayı ikinin kuvvetiyse sonucu doğru değilse yanlış çıkarıcak !!


num = int(input("number enter : "))

def us():
    durum:bool
    for i in range(1,32):
        sayi = pow(2,i)
        if num == 1:
            durum = True
            print(durum)
            break
        else:
            if num % sayi == 0:
                durum = True
                print(durum)
                break
            else :
                durum = False
                print(durum)
                break

us()

