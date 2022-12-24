snisli = input("ведите число")
snisli = int(snisli)
if(snisli > 10):
    print("Верно")
else:
    print("Не Верно")
    rezult = "Не Верно"
    while(rezult == "Не Верно"):
        snisli = input("ведите число")
        snisli = int(snisli)
        if(snisli > 10):
         print("Верно")
        else:
            print("Не Верно")
            rezult = "Не Верно"

