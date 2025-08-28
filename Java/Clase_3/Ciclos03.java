import java.util.Scanner;

public class Ciclos03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;

        System.out.println("Ingrese un número (0 para salir):");
        numero = entrada.nextInt();

        while (numero != 0) {
            if (numero % 2 == 0) {
                System.out.println(numero + " es PAR");
            } else {
                System.out.println(numero + " es IMPAR");
            }

            System.out.println("Ingrese otro número (0 para salir):");
            numero = entrada.nextInt();
        }

        System.out.println("Programa finalizado.");
    }
}