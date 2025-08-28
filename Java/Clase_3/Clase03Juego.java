import java.util.Scanner;

public class Clase03Juego {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeroAleatorio = (int)(Math.random() * 101); // 0 a 100
        int intento;
        int contador = 0;

        System.out.println("¡Adivina el número entre 0 y 100!");

        do {
            System.out.print("Introduce tu número: ");
            intento = entrada.nextInt();
            contador++;

            if (intento < numeroAleatorio) {
                System.out.println("Es mayor.");
            } else if (intento > numeroAleatorio) {
                System.out.println("Es menor.");
            } else {
                System.out.println("correcto! Número de intentos: " + contador);
            }
        } while (intento != numeroAleatorio);
    }
}