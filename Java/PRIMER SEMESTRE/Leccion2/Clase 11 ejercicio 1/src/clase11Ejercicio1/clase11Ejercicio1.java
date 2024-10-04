
package clase11Ejercicio1;
import java.util.Scanner;
public class clase11Ejercicio1 {
    public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
        double nota1, nota2, nota3, promedio;

        System.out.println("Digite las calificaciones:");
        nota1 = scanner.nextDouble();
        nota2 = scanner.nextDouble();
        nota3 = scanner.nextDouble();

        promedio = (nota1 + nota2 + nota3) / 3;

        if (promedio >= 7) {
            System.out.println("El alumno esta aprobado con: " + promedio);
        } else {
            System.out.println("El alumno esta desaprobado con: " + promedio);
        }
    }
} 

 
