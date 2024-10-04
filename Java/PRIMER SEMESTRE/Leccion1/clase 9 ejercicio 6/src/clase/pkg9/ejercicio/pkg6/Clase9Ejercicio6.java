
package clase.pkg9.ejercicio.pkg6;

import java.util.Scanner;


public class Clase9Ejercicio6 {

   
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Ingrese la cantidad de dinero que tiene Guillermo");
        double dineroGuillermo = scanner.nextDouble();
        double dineroLuis = dineroGuillermo / 2;
        double dineroJuan = (dineroGuillermo+dineroLuis) / 2;
        double dineroTotal = dineroGuillermo + dineroLuis + dineroJuan;
        System.out.println("El Dinero Total es :"+dineroTotal);
    }
    
}
