
/*
Ejercicio 3:Leer nuemros hasta que se introduzca un cero
para cada uno indicar si es par o impar.
Primero lo haremos con la calse Scanner
Luego con la calase JOptionPane
 */
package ejercicio_3;

import javax.swing.JOptionPane;

public class Ejercicio_3_JOptionPane {

    public static void main(String[] args) {
                int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog(" Digite un numero:"));
        while (numero != 0) {
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null, "El numero  " + numero + " es "
                        + "PAR");
            }
            
            else{
                JOptionPane.showMessageDialog(null, "El numero  " + numero + " es "
                        + "IMPAR");
            }
           numero = Integer.parseInt(JOptionPane.showInputDialog(" Digite otro numero:"));
        } 
        JOptionPane.showMessageDialog(null," El numero ingresado es "+numero+" finaliza el programa");
    }

   
}


