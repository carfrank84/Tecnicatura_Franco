/* Ejercicio 5_: Realizar un juego para adivinar un numero
para ello generar un numero aleatorio entre 0-100, y lugo
ir pidiendo numeros indicando " es mayor" o " es menor", segun sea mayor o menor 
con respecto al Numero N.
El proceso termina cuando el usuario acierta , y mosgtramos el numero de intentos hechos.
 */
package Ejercicio_5_JuegoNumerico;

import javax.swing.JOptionPane;

public class Ejercicio_5_JuegoNumerico_JOptionPane {
    public static void main(String[] args) {
        int numeroSecreto = (int) (Math.random() * 100);
        int intentos = 0;

        JOptionPane.showMessageDialog(null, "Bienvenido al juego de adivinar el número.");
        JOptionPane.showMessageDialog(null, "Intenta adivinar el número secreto entre 0 y 100.");

        while (true) {
            String input = JOptionPane.showInputDialog("Ingresa tu Numero:");
            int intento = Integer.parseInt(input);
            intentos++;

            if (intento < numeroSecreto) {
                JOptionPane.showMessageDialog(null, "El número secreto es mayor.");
            } else if (intento > numeroSecreto) {
                JOptionPane.showMessageDialog(null, "El número secreto es menor.");
            } else {
                JOptionPane.showMessageDialog(null, "¡Felicidades! Adivinaste el número en " + intentos + " intentos.");
                break;
            }
        }
    }
}