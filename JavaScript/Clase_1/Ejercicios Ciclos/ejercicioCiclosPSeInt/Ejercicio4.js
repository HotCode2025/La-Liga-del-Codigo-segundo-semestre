//Calcular Salario y Sumatoria
//Dada las horas trabajadas de 5 personas y la tarifa de pago
//Calcular el salario y la sumatoria de todos los salarios

const empleados = [
  [4, 89],   // empleado 1
  [5, 90],   // empleado 2
  [23, 89],  // empleado 3
  [12, 8],   // empleado 4
  [19, 4]    // empleado 5
];

let suma = 0;

for (let i = 0; i < empleados.length; i++) {
  const horas = empleados[i][0];
  const tarifa = empleados[i][1];

  const salario = horas * tarifa;

  console.log(`Salario del empleado ${i + 1}:`);
  console.log(`Horas trabajadas: ${horas}`);
  console.log(`Tarifa por hora: ${tarifa}`);
  console.log(`El salario es: $${salario}`);
  console.log(""); // salto de línea

  suma += salario;
}

console.log("La suma de todos los salarios es: $", suma);
