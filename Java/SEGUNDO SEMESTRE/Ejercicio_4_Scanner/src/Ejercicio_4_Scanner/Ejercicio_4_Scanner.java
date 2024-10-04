/*
 Ejercicio 4: Pedir números hasta que se teclee uno negativo
y mostrar cuantos números se han introducido.
lo hacemos primero con la clase Scanners y luego con 
la clase JOptionPane
 */
package Ejercicio_4_Scanner;

import java.util.Scanner;


public class Ejercicio_4_Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, contador = 0;
        System.out.println("Digite un numero : ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            System.out.println("El numero "+numero+" Es Positivo");
            contador ++;
            System.out.println("Digite otro numero ");
            numero = Integer.parseInt(entrada.nextLine());
            
        }
        System.out.println("A Ingresado "+contador+" Numeros que no son negativos");
    }
    
}
