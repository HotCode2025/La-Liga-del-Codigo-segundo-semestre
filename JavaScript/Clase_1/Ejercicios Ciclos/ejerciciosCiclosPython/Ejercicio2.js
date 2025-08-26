
let positivos = 0;
let negativos = 0;
let neutros = 0;

let numeros = [5, -3, 0, 7, -1, 0, 9, -6, 2, 0]; 

console.log("Introduce 10 números:");

for (let i = 0; i < numeros.length; i++) {
    let num = numeros[i];
    console.log(`Número ${i + 1}: ${num}`);

    if (num > 0) {
        positivos++;
    } else if (num < 0) {
        negativos++;
    } else {
        neutros++;
    }
}

console.log("\nResumen:");
console.log(`Números positivos: ${positivos}`);
console.log(`Números negativos: ${negativos}`);
console.log(`Números neutros (cero): ${neutros}`);

