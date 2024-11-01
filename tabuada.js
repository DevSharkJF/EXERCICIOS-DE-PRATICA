//Tabuada do 1
document.write('Tabuada do 1' + '<br>' +'<br>')
for(var x = 1; x<=10; x = x+1) {
    document.write('1 x ' +x+ ' = ' +(1*x)+ '<br>')
}
document.write('<hr>' + '<hr>' + '<br>')

//Tabuada do 1 ao 10 com laços
document.write('Tabuada do 1 ao 10' + '<br>' +'<br>')
for(var multiplicador = 1; multiplicador <= 10; multiplicador++) {
    for(var multiplicando = 1; multiplicando <=10; multiplicando++ ) {
        document.write(multiplicador + ' x ' + multiplicando + ' = ' + (multiplicador*multiplicando) + '<br>')
    }
    document.write('<hr>')
}