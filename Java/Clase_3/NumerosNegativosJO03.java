import javax.swing.JOptionPane;

public class NumerosNegativosJO03 {
    public static void main(String[] args) {
        int numero;
        int contador = 0;

        do {
            String input = JOptionPane.showInputDialog("Ingrese un número (negativo para salir):");
            if (input == null) break; 

            numero = Integer.parseInt(input);

            if (numero >= 0) {
                contador++;
            }
        } while (numero >= 0);

        JOptionPane.showMessageDialog(null, "Cantidad de números introducidos: " + contador);
    }
}