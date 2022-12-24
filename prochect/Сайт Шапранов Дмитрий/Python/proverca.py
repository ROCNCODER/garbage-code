from operator import index




znachenie=list("6*2*4+1+5/3")
def raschets():
    global znachenie
    print(znachenie)
    dlina =len(znachenie)
    while dlina>1:
        if(znachenie[0] != "-"):
        
            if("*" in znachenie and "/" in znachenie):
                index_umn=znachenie.index("*")
                print(index_umn)
                imdex_del=znachenie.index("/")
                print(imdex_del)
            if(index_umn<imdex_del):
                index_operand_one=index_umn-1
                print(index_operand_one)  
                index_operand_two=index_umn+1
                print(index_operand_two) 
                preobrazovanie=float(znachenie[index_operand_one])*float(znachenie[index_operand_two])
                print(preobrazovanie)
                preobrazovanie=str(preobrazovanie)
                znachenie.insert(index_operand_one, preobrazovanie)
                znachenie.pop(index_operand_one+1)
                znachenie.pop(index_operand_one+1)
                znachenie.pop(index_operand_one+1)
                print(znachenie)
                imdex_del=znachenie.index("/")
                print(imdex_del)
                index_operand_one=imdex_del-1
                print(index_operand_one)  
                index_operand_two=imdex_del+1
                print(index_operand_two) 
                preobrazovanie=float(znachenie[index_operand_one])/float(znachenie[index_operand_two])
                print(preobrazovanie)
                preobrazovanie=str(preobrazovanie)
                znachenie.insert(index_operand_one, preobrazovanie)
                znachenie.pop(index_operand_one+1)
                znachenie.pop(index_operand_one+1)
                znachenie.pop(index_operand_one+1)
                print(znachenie) 

            else:
                index_del=znachenie.index("/")
                print(imdex_del)
                index_operand_one=index_del-1
                print(index_operand_one)  
                index_operand_two=imdex_del+1
                print(index_operand_two) 
                preobrazovanie=int(znachenie[index_operand_one])/int(znachenie[index_operand_two])
                print(preobrazovanie)
                preobrazovanie=str(preobrazovanie)
                znachenie.insert(index_operand_one, preobrazovanie)
                znachenie.pop(index_operand_one+1)
                znachenie.pop(index_operand_one+1)
                znachenie.pop(index_operand_one+1)
                print(znachenie)  

                index_umn=znachenie.index("*")
                print(index_umn)
                index_operand_one=index_umn-1
                print(index_operand_one)  
                index_operand_two=index_umn+1
                print(index_operand_two) 
                preobrazovanie=float(znachenie[index_operand_one])*float(znachenie[index_operand_two])
                print(preobrazovanie)
                preobrazovanie=str(preobrazovanie)
                znachenie.insert(index_operand_one, preobrazovanie)
                znachenie.pop(index_operand_one+1)
                znachenie.pop(index_operand_one+1)
                znachenie.pop(index_operand_one+1)
                print(znachenie)
       
            if("*" in znachenie):
                index_umn=znachenie.index("*")
                print(index_umn)
                index_operand_one=index_umn-1
                print(index_operand_one)  
                index_operand_two=index_umn+1
                print(index_operand_two) 
                index_umn=znachenie.index("*")
                index_operand_one=index_umn-1
                print(index_operand_one)  
                index_operand_two=index_umn+1
                print(index_operand_two) 
                preobrazovanie=float(znachenie[index_operand_one])*float(znachenie[index_operand_two])
                print(preobrazovanie)
                preobrazovanie=str(preobrazovanie)
                znachenie.insert(index_operand_one, preobrazovanie)
                znachenie.pop(index_operand_one+1)
                znachenie.pop(index_operand_one+1)
                znachenie.pop(index_operand_one+1)
                print(znachenie)
                print('выкл')
            if("/" in znachenie):
                imdex_del=znachenie.index("/")
                index_operand_one=imdex_del-1
                print(index_operand_one)  
                index_operand_two=imdex_del+1
                print(index_operand_two) 
                preobrazovanie=float(znachenie[index_operand_one])/float(znachenie[index_operand_two])
                print(preobrazovanie)
                preobrazovanie=str(preobrazovanie)
                znachenie.insert(index_operand_one, preobrazovanie)
                znachenie.pop(index_operand_one+1)
                znachenie.pop(index_operand_one+1)
                znachenie.pop(index_operand_one+1)
                print(znachenie)
            if("+" in znachenie and "-" in znachenie):
                index_sum=znachenie.index("+")
                print(index_sum)
                imdex_vich=znachenie.index("-")
                print(imdex_vich)
                if(index_sum<imdex_vich):
                    imdex_sum=znachenie.index("+")
                    index_operand_one=imdex_sum-1
                    print(index_operand_one)  
                    index_operand_two=imdex_sum+1
                    print(index_operand_two)
                    preobrazovanie=float(znachenie[index_operand_one])+float(znachenie[index_operand_two])
                    print(preobrazovanie)
                    preobrazovanie=str(preobrazovanie)
                    znachenie.insert(index_operand_one, preobrazovanie)
                    znachenie.pop(index_operand_one+1)
                    znachenie.pop(index_operand_one+1)
                    znachenie.pop(index_operand_one+1)
                    print(znachenie)
                    imdex_vich=znachenie.index("-")
                    index_operand_one=imdex_vich-1
                    print(index_operand_one)  
                    index_operand_two=imdex_vich+1
                    print(index_operand_two)
                    preobrazovanie=float(znachenie[index_operand_one])-float(znachenie[index_operand_two])
                    print(preobrazovanie)
                    preobrazovanie=str(preobrazovanie)
                    znachenie.insert(index_operand_one, preobrazovanie)
                    znachenie.pop(index_operand_one+1)
                    znachenie.pop(index_operand_one+1)
                    znachenie.pop(index_operand_one+1)
                    print(znachenie)
                else:
                    imdex_vich=znachenie.index("-")
                    index_operand_one=imdex_vich-1
                    print(index_operand_one)  
                    index_operand_two=imdex_vich+1
                    print(index_operand_two)
                    preobrazovanie=float(znachenie[index_operand_one])-float(znachenie[index_operand_two])
                    print(preobrazovanie)
                    preobrazovanie=str(preobrazovanie)
                    znachenie.insert(index_operand_one, preobrazovanie)
                    znachenie.pop(index_operand_one+1)
                    znachenie.pop(index_operand_one+1)
                    znachenie.pop(index_operand_one+1)
                    print(znachenie)
                    imdex_sum=znachenie.index("+")
                    index_operand_one=imdex_sum-1
                    print(index_operand_one)  
                    index_operand_two=imdex_sum+1
                    print(index_operand_two)
                    preobrazovanie=float(znachenie[index_operand_one])+float(znachenie[index_operand_two])
                    print(preobrazovanie)
                    preobrazovanie=str(preobrazovanie)
                    znachenie.insert(index_operand_one, preobrazovanie)
                    znachenie.pop(index_operand_one+1)
                    znachenie.pop(index_operand_one+1)
                    znachenie.pop(index_operand_one+1)
                    print(znachenie)
            else:
                if("+" in znachenie):
                    imdex_sum=znachenie.index("+")
                    index_operand_one=imdex_sum-1
                    print(index_operand_one)  
                    index_operand_two=imdex_sum+1
                    print(index_operand_two)
                    preobrazovanie=float(znachenie[index_operand_one]) + float(znachenie[index_operand_two])
                    print(preobrazovanie)
                    preobrazovanie=str(preobrazovanie)
                    znachenie.insert(index_operand_one, preobrazovanie)
                    znachenie.pop(index_operand_one+1)
                    znachenie.pop(index_operand_one+1)
                    znachenie.pop(index_operand_one+1)
                    print(znachenie)
                if("-" in znachenie):
                    imdex_vich=znachenie.index("-")
                    index_operand_one=imdex_vich-1
                    print(index_operand_one)  
                    index_operand_two=imdex_vich+1
                    print(index_operand_two)
                    preobrazovanie=float(znachenie[index_operand_one])-float(znachenie[index_operand_two])
                    print(preobrazovanie)
                    preobrazovanie=str(preobrazovanie)
                    znachenie.insert(index_operand_one, preobrazovanie)
                    znachenie.pop(index_operand_one+1)
                    znachenie.pop(index_operand_one+1)
                    znachenie.pop(index_operand_one+1)
                    print(znachenie)
                    dlina =len(znachenie)


print(raschets())






      
