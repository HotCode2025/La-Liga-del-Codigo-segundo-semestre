import javax.swing.JOptionPane;

public class CiclosJo03 {
    public static void main(String[] args) {
        int numero;

        do {
            String input = JOptionPane.showInputDialog("Ingrese un número (0 para salir):");
            if (input == null) break;

            numero = Integer.parseInt(input);

            if (numero != 0) {
                String resultado = (numero % 2 == 0) ? "PAR" : "IMPAR";
                JOptionPane.showMessageDialog(null, numero + " es " + resultado);
            }
        } while (numero != 0);

        JOptionPane.showMessageDialog(null, "Programa finalizado.");
    }
}