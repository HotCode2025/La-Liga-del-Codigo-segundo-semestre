import javax.swing.JOptionPane;

public class Clase03JuegoJo {
    public static void main(String[] args) {
        int numeroAleatorio = (int)(Math.random() * 101); // 0 a 100
        int intento;
        int contador = 0;

        JOptionPane.showMessageDialog(null, "¡Adivina el número entre 0 y 100!");

        do {
            String input = JOptionPane.showInputDialog("Introduce tu número:");
            if (input == null) return; // Por si se cierra la ventana

            intento = Integer.parseInt(input);
            contador++;

            if (intento < numeroAleatorio) {
                JOptionPane.showMessageDialog(null, "Es mayor.");
            } else if (intento > numeroAleatorio) {
                JOptionPane.showMessageDialog(null, "Es menor.");
            } else {
                JOptionPane.showMessageDialog(null, "Correcto! numero de nitentos: " + contador);
            }
        } while (intento != numeroAleatorio);
    }
}