document.querySelector('button').onclick = function(){
    document.querySelector('h1').style.color = 'red';
    this.remove();
}