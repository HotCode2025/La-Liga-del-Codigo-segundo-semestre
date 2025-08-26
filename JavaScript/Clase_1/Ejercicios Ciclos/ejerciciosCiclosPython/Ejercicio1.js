/*
Ejercicio Año Bisiesto:
Diseñar un programa que ingresando un año,
nos devuelva por consola si es un año bisiesto.
Repetir la accion hasta que el usuario lo decida
*/

// Simulamos una lista de entradas como si el usuario las escribiera
let entradas = [2024, 1900, 2000, "hola", 2023];
let i = 0; // contador para recorrer la lista

while (i < entradas.length) {
  let entrada = entradas[i];
  let anioIngresado = parseInt(entrada);

  if (isNaN(anioIngresado)) {
    console.log(`Error: "${entrada}" no es un número.`);
  } else {
    if ((anioIngresado % 4 === 0 && anioIngresado % 100 !== 0) || (anioIngresado % 400 === 0)) {
      console.log(`El año ${anioIngresado} ES bisiesto`);
    } else {
      console.log(`El año ${anioIngresado} NO es bisiesto`);
    }
  }

  i++; // avanzar al siguiente elemento
}

console.log("Verificación finalizada.");

