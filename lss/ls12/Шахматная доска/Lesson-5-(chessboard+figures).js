function chessboard1() {
    let newTable = document.createElement( 'table' ),
        lets = [ '','A','B','C','D','E','F','G','H','' ],
        blackFigs1 = [ '8','&#9820;','&#9822;','&#9821;','&#9819;','&#9818;','&#9821;','&#9822;','&#9820;','8' ],
        whiteFigs1 = [ '1','&#9814;','&#9816;','&#9815;','&#9813;','&#9812;','&#9815;','&#9816;','&#9814;','1' ],
        blackFigs2 = [ '7','&#9823;','&#9823;','&#9823;','&#9823;','&#9823;','&#9823;','&#9823;','&#9823;','7' ],
        whiteFigs2 = [ '2','&#9817;','&#9817;','&#9817;','&#9817;','&#9817;','&#9817;','&#9817;','&#9817;','2' ];
        let figure;
    
        for ( var i = 0, a = 9; i < 10, a >= 0; i++, a-- ) {
        var newTr = newTable.insertRow(i);//i - номер строки с нуля
        for ( var j = 0; j < 10; j++ ) {//j - номер столбца
            var newTd = newTr.insertCell( j );//в строку вставляем ячейку
            newTd.classList.add("x_" + j);
            switch (i) {
                    case 0:
                        newTd.innerText = lets[ j ];
                        break;
                    case 1:
                        newTd.innerHTML = blackFigs1[ j ];
                        break;
                    case 2:
                        newTd.innerHTML = blackFigs2[ j ];
                        newTd.onclick = e=>{
                            e.target.style.border = '5px solid red';
                            figure = e.target;
                            console.log(figure);
                        }
                        break;
                    case 7:
                        newTd.innerHTML = whiteFigs2[ j ];
                        break;
                    case 8:
                        newTd.innerHTML = whiteFigs1[ j ];
                        break;
                    case 9:
                        newTd.innerText = lets[ j ];
                        break;
                default:
                    if ( j == 0 || j == 9 ) {
                        newTd.innerHTML = a;
                    }else{
                        newTd.onclick = e => {
                           if(figure.className.split("_")[1] == e.target.className.split("_")[1]){
                                figure.removeAttribute('style');
                                e.target.innerHTML = figure.innerHTML;
                                figure.innerHTML = "";
                           }else{
                                alert('Ход недопустим!');
                           }
                        }
                    }
                    break;
            }
        }
    }
   // var elem = document.getElementsByClassName( 'task511' );
    document.body.append( newTable );
}
chessboard1();