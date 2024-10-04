/* Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el proceso hasta que se 
se introduzca un numero negativo
 */
package ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio01  {
    public static void main(String[] args) {
        int numero, cuadrado;
        numero = Integer.parseInt(JOptionPane.showInputDialog(" Digite un numero"));
       
        while (numero >= 0) {// mientras el numero sea igual a cero o positivo
            cuadrado = (int) Math.pow(numero, 2);
            System.out.println("El numero  " + numero + "  elevado al cuadrado es :  " + cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog(" Digite Otro numero"));
        }
        System.out.println("El Programa a finalizado por numero negativo");

    }

}

