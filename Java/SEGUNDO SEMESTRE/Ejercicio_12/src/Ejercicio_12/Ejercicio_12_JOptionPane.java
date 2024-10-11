
package Ejercicio_12;

import javax.swing.JOptionPane;

public class Ejercicio_12_JOptionPane {
    public static void main(String[] args) {
        String input = JOptionPane.showInputDialog("Introduce un número para calcular su factorial:");
        int numero = Integer.parseInt(input);
        long factorial = 1;

        for (int i = 1; i <= numero; i++) {
            factorial *= i; // Calcula el factorial
        }

        JOptionPane.showMessageDialog(null, "El factorial de " + numero + " es: " + factorial);
    }
}
