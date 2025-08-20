// Ciclo While
let contador = 0;
while(contador < 3){
    console.log(contador)
    contador++;
}
console.log("Fin del ciclo while");

// Ciclo do while
let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log("Fin del ciclo do while")

// Ciclo For
for(let contando = 0; contando < 3; contando++){
    console.log(contando); 0, 1, 2
}

// Palabra reservado break
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        break;
    }

// La palabra Continue y Etiqueta Labels
inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        break inicio; // ir a la siguiente iteracion
    }
}    
