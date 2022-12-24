snisli = int(input("Введите число"))    
def zadscha2():
    if(snisli<15):
        print('В первую четверть')
    elif(snisli>15) and (snisli<30):
        print('Во вторую четверть')
    else:
        if(snisli>30) and (snisli<45):
            print('В третью часть')
        else:
            if(snisli<=59):
                print("В четвертую четверть")
def zadscha2():
    otvet=(input("Тебе нужна подсказак по типам переменных в python"))
    def zadacha3():   
        if(otvet=="Да") or (otvet=="да") or (otvet=="ДА"):
            print('Числа')
            print('Строки')
            print('Кортежи')
            print('Списки')
            print('Словари')
            print('Множества')
        else:
            print("Молодец тебе не нужны подсказки")

def zadacha3():    
 def zadacha3():    
# В Python в отличии от js указывать тип ошибки от этого и будет скакать проверка на наличии ошибки(в js можно получить тип совершаемой ошибки в переменную)
    try: # пролверяемый блок кода оборачивается в try
         operachii=input()
         operachii=int(operachii)       
    except : 
        print("Ошибка")# План B Код в случае возникновении ошибки 
        
    else:
        print(5)
zadacha3()
         

        
def prostoi_calculetor():
    print("привет пользователь введи сначала два числа, а потом  желаемое действие ")
    chislo_one=int(input())
    chislo_two=int(input())
    deistvie=input()
    if(deistvie=="+"):
        print(chislo_one+chislo_two)
    else:
        if(deistvie=="-"):
            print(chislo_one-chislo_two)
        else:
            if(deistvie=="*"):
                print(chislo_one*chislo_two)
            else:
                #Нет зашиты от малолетнего дебила
                print(chislo_one/chislo_two)


def zigli():
    name = "FACK"
    
    for i in name:
        print(i)
    # Печатает строчки 
    for i in range(1,11):
        print(i)








          