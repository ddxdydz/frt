let tm;//переменная для хранения объекта таймера. Переменная нужна для отключения таймера
let cars = [];//Массив картинок с автомобилями
let cx = [];//массив с координатами каждой машины
let gameBegin;//Проверяет повторное нажатие на кнопку Start

let summa = +prompt("Введите вашу сумму");
let c = +prompt("На какую машину (от 0 до 4) вы делаете ставку");
let stavka = +prompt("Сколько вы ставите на выигрыш");
function go()
{
	
	if (gameBegin==1) return;
	gameBegin = 1;	
	for (var i=0; i<5; i++)
	{
	   cars[i] = document.getElementById("p"+i);
       cars[i].style.border = "none";
	   cx[i] = 680;//начальная общая координата
	}
	
	tm = setInterval(timerGo, 50);
    
}

function timerGo()
{
	for (let i=0; i<5; i++)
	{
          //случайный шаг перемещения для автомобиля 
	   cx[i] -= parseInt((Math.random()*7+2));
	   if (cx[i]<=0)
	   {
		   clearInterval(tm);
           gameBegin = 0;
           if(i==c){
               alert("Вы победили");
               summa += stavka;
		   }
           else{
                alert("Вы проиграли. До финиша доехала машина с номером "+i);
                 summa -= stavka;
           }
           alert("Ваша сумма = "+summa);
           cars[i].style.border = "5px ridge yellow";
           return;
	   }else{
		cars[i].onclick = function(){
			cx[i]-=100;
		}
	   }
		cars[i].style.left = cx[i]+"px";	   
	}	
}