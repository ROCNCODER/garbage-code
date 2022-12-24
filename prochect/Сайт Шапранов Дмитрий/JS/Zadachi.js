window.onload = function () {
document.querySelector("#ZADACHA_one").onclick = function (){
//Задача 1 
let number=prompt(); 

if(number==10){
    console.log("Верно");
    alert("Верно задача 1");
}
else{
    console.log("Не верно");
    alert("Не Верно задача 1");
}
}


//Задача 2 
document.querySelector("#ZADACHA_two").onclick = function (){
let vremi = prompt();
if(vremi<15){
    console.log("В первую четверть");
    alert("В первую четверть задача 2");

}else{
    if(vremi>15 && vremi<30){
        console.log("В Вторую четверть");
        alert("В Вторую четверть задача 2");
    }
    else{
        if(vremi>30 && vremi<45){
            console.log("В Третью четверть");
            alert("В Третью четверть задача 2");
        }else{
            if(vremi>45 && vremi<=59){
            console.log("В Четвертую четверть");
            alert("В Четвертую четверть задача 2");
        }else{
            console.log("Ошибка");
            alert("Ошибка");
        }
        }

        
    }
}
}



//Задача 3 
document.querySelector("#ZADACHA_tree").onclick = function (){
    alert("Нужна шпаргалка по типам переменных. Да или нет ")
    let otwet = prompt();
    if(otwet=="да" || otwet=="Да"){
        alert("Числа (Numbers) - Целые числа, числа с плавающей точкой");
        alert("Строки (Strings) - Любые данные в одинарных или двойных кавычках");
        alert("Булевые (boolean) - true или false значения");
        alert("Null - пустое значение или нет значения");
        alert("Undefined - объявленная переменная без значения");

}else{
    alert("Молодец,Тебе не нужны подсказки");
}
}
}

//Задача 4 Консольный перехват ошибки


document.querySelector("#ZADACHA_fo").onclick= function(){
    try{
        alert("введите число с плавающей точкой");
        let shislo = prompt();
        let H = imput();
        let pro = shislo + shislo;
        alert(pro);
        shislo = int(shislo);

    } catch(oshibka){
        alert("Число с плавающей точкой не может быть преобразовано в целочисленый тип данных");
        alert(oshibka);
    }
//П.С в javas
    const obazalovca=5;
    try{
        let one=1/0;
        alert(one);
    }catch(Error_Recording){
        one=1/1;
        alert(one);
        alert(Error_Recording);
    }finally{
        alert(obazalovca);s
    }
      
}

    





//Простой калькулятор может, кто угодно. А я учил сторелочную функцию

document.querySelector("#ZADACHA_fo").onclick= function(){
    alert("Привет пользователь это простой калькулятор");
    alert("Ты можешь делать 4 основных действия (Умножения,Деление, Сложение, Вычитание ");
    alert('Вненси число 1 и 2')
    let chislo_one = prompt();
    let chislo_two = prompt();
    let destwie = prompt();
    let resait = (znack, znack_one) => znack + znack_one;
        


    alert(resait(chislo_one, chislo_two));


}

/*Програма по регистрации пользователя и проверке пароля*/

document.querySelector('#ZADACHA_fa').onclick = function(){
    alert("Привет, желаешь cоздать новый аккаунт");
    let otvet=prompt(); //Попробовать imput
    if(otvet=="ДА" || otvet =="Да" || otvet=="да"){
        alert('Ведите по порядку следующие данные');
        alert("Имя,Фамилия,  Возраст, Электроную почту, Пароль для аккаунта")
       let new_user={
        nama:nama=prompt(),
        fum:fum=prompt(),
        age:age=prompt(),
        mail:mail=prompt(),
        pasvord:pasvord=prompt(),
       }
    console.log(new_user);

    alert("Веди пароль еще раз еще раз ");
    let proverca_passvord=prompt();
    let new_prov=proverca_passvord.split("");
    let prov=new_user.pasvord;
    prov=prov.split("");//Проще сравнивать строки 
    let choslo = prov.length;
    console.log(choslo);
    let fust=0;

    let a = choslo;  //Условная функция отказывается работать с перемеными в которые на прямую передана длина массива. ?

    if(a > 0) {
     if(new_prov[fust]==prov[fust]){
        for(a;a>0;a--){
                 fust=fust++;   
        }
    }
        else {
            alert("Пароль не верный");
            }
            console.log("Конец");   
            
            
        
    }
}

}