
package Ejercicio_10;

import javax.swing.JOptionPane;

public class Ejercicio_10_JOptionPane {
    public static void main(String[] args) {
        int suma = 0;

        for (int i = 1; i <= 10; i++) {
            String input = JOptionPane.showInputDialog(null, "Ingresa el número " + i + ":");
            int numero = Integer.parseInt(input); // Convertimos el input en número
            suma += numero;
        }

        JOptionPane.showMessageDialog(null, "La suma total de los números es: " + suma);
    }
}

