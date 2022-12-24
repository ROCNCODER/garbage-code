
from unicodedata import name


print("Привет, желаешь cоздать новый аккаунт")
otvet=input("")
if(otvet=="да" or otvet=="Да" or otvet=="ДА"):
    print("Введите следующие данные")
    print("Имя,Фамилия,Пароль")
    new_polzovatel=[
        input(),input(),input()
    ]

    print("Введи пароль")
    parol_two=input()
    parol_two=list(parol_two)
    parol=list(new_polzovatel[2])

    if(parol_two==parol):
        print("Пароль правельный")
    else:
        print("Пароль не верный")