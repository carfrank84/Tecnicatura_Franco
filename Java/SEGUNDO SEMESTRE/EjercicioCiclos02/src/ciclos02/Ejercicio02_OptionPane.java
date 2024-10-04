/*
 * Ejercicio 2: Leer ubn numero e indicar si es positivo o negativo. El proceso se repetira hasta que se 
introduzca un cero
 */
package ciclos02;

import javax.swing.JOptionPane;

public class Ejercicio02_OptionPane{

    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog(" Digite un numero"));
        while (numero != 0) {
            if (numero > 0) {
                JOptionPane.showMessageDialog(null," El Numero " + numero + " es POSITIVO");
            } 
            else {
                JOptionPane.showMessageDialog(null, "El Numero " + numero + " es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog(" Digite Otro numero"));
        }
        JOptionPane.showMessageDialog(null, "El Numero " + numero + " finaliza el programa");

    }

}
