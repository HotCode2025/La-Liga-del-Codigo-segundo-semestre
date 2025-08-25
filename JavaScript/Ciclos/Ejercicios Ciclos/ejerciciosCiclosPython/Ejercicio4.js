
//Ejercicio 4: 
//Ingrese “N” enteros. Visualizar la suma de los numeros para la lista.
//¿Cuántos numeros pares existen y cual es el promedio de los numeros impares?

const numeros = [13,20,23,16, 63, 2, 0, 9,77,36];//Arrgeglo 8lista) para simular la entrada de datos. 
let sumaNumeros = 0;//Variable para almacenar la suma de todos los numeros
let contador = 0;//Variable que actua como contador para recorrer 
let conteoPares = 0;//contara los numeros pares
let conteoImpares = 0;//contar los numeros Impares
let sumaImpares = 0;// Acumula la suma de todos los numeros impares

//Ejercicio usando Ciclo do - while
do{
    let numero = numeros[contador];//Para obtener el numero actual del arreglo de acuerdo a la posicion del contadors.
    sumaNumeros += numero;//suma el numero actual a sumaNumeros
    //Verificar si es par usando modulo
    if (numero % 2 == 0){
        conteoPares ++;//si es par se incrementa el contadorPares.
    }else{
        
        conteoImpares ++;//Si es impar se incrementa a ConteoPares
        sumaImpares += numero;//sumar a la variable  sumImpares el numero impar
    }
    contador ++;//Se incrementa el contador y pasa al siguiente numero

}while (contador < numeros.length);// la condicion del ciclo se repite mientras el contador sea < que el total de elementos del arreglo

// Mostrar Resultados
console.log("La suma de los N numeros es:",sumaNumeros);//Muestra la suma de numeros
console.log("La cantidad de los numeros pares es:",conteoPares);//Mostrar la cantidad de numeros pares
// con un if evito dividir por cero si no hay numers impares, porque sino me daria error
if (conteoImpares > 0) {
    console.log("El  Promedio de los Impares es :", sumaImpares / conteoImpares);//mostrar los numeros imparea y promedio
} else {
    console.log("No se encontraron numeros impares para calcular el promedio.");
}
console.log("--------------------------------- ")


//  Mismo ejercicio usando for
const numeros2 = [15, 20, 53, 16, 44, 2, 5, 9, 7, 36];
let sumaNumeros2 = 0;
let conteoPares2 = 0;
let conteoImpares2 = 0;
let sumaImpares2 = 0;

// Recorro el arreglo con for de principio a fin.
// En una sola linea defino contador,  condición e incremento
for (let i = 0; i < numeros2.length; i++) {
    let numero = numeros2[i];//obtener el numero acual en la posicion del arreglo
    
    sumaNumeros2 += numero;//sumar el numero actual a suma numeros
//Verificar si es par con % y aumentar contador si es par
    if (numero % 2 === 0) {
        conteoPares2++;
//Si es impar aumentar el contador y sumar a suma imopares        
    } else {
        conteoImpares2++;
        sumaImpares2 += numero;
    }
}
//Mostrar los resultados
console.log("La suma de los N numeros es:", sumaNumeros2);
console.log("La cantidad de los numeros pares es:", conteoPares2);
// con un if evito dividir por cero si no hay numers impares, porque sino me daria error
if (conteoImpares2 > 0) {
    console.log("El Promedio de los Impares es:", sumaImpares2 / conteoImpares2);
} else {
    console.log("No se encontraron números impares para calcular el promedio.");
}
console.log("----------------------------- ")