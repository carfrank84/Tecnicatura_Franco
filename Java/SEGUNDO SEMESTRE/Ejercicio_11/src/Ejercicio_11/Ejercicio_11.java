
package Ejercicio_11;
/*Ejercicio 11: Diseñar un programa que muestre el producto de los 10 primeros numeros impares 
    hacerlo con JOptionPane*/    
import javax.swing.JOptionPane;

public class Ejercicio_11 {
    public static void main(String[] args) {
        long producto = 1; // Usamos 'long' porque el resultado puede ser grande.
        int numero = 1; // Primer número impar

        for (int contador = 0; contador < 10; contador++) {
            producto *= numero; // Multiplicamos el producto por el número impar
            numero += 2; // Avanzamos al siguiente número impar
        }

        JOptionPane.showMessageDialog(null, "El producto de los 10 primeros números impares es: " + producto);
    }
}

    

