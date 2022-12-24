/*Объекты в JavaScript */

/*Объекты вкладываются в переменую*/ 

let Ob = new Object();
let ob = {};

/*Структура (Свойстра) ключ:Значение,
*/

let Obstr = {
site: "Личный блог Шапранов Дмитрия",
CMS:"WordPress",
/*Для двух и более слов*/
"Cposop obechenie": Conspect,
};

console.log(Obstr.site);

/*Вычисления с обьектами */
let pro = "good"
let fist = "Nick";
let vichslenia_Obstr ={
ver: "1.00",
[fist + "dem"]: true,
[pro]: dark,
};
console.log(vichslenia_Obstr["Nick dem"]);
console.log(vichslenia_Obstr[pro]);

/*Внутри списков обьектов можно использовать зарезервированые имена*/

let id = Symbol("id");