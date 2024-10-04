
package calse.pkg9.ejercicio.pkg5;

import java.util.Scanner;

public class Calse9Ejercicio5 {

   
    public static void main(String[] args) {
     Scanner scanner = new Scanner (System.in);
     // pedir al usuario las tres calificaciones
        System.out.println("Ingrese la primera calificacion");
        double calificacion1 = scanner.nextDouble();
        
        System.out.println("Ingrese la segunda calificacion");
        double calificacion2 = scanner.nextDouble();
        
        System.out.println("Ingrese la tercera calificacion");
        double calificacion3 = scanner.nextDouble();
        
        double suma = calificacion1 + calificacion2 + calificacion3;
        
        System.out.println("la suma de las tres calificaciones es : = " + suma);
        
        
        
    }
    
}
