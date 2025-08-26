//Imprimir en pantalla los numeros del 1 al 10.(en filas y con saltos de lineas)

console.log("Números en columna:");
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

console.log("\nNúmeros en fila:");

let fila = "";
for (let i = 1; i <= 10; i++) {
    fila += i + " ";
}
console.log(fila);
