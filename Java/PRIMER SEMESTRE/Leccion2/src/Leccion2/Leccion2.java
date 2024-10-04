package Leccion2;

import java.util.Scanner;

public class Leccion2 {

    public static void main(String[] args) {
        var condicion = true;
        if (condicion) {
            System.out.println("Condicion verdadera"); // condicional simple
        } else {
            System.out.println("Condicion Falsa"); // condicional doble
        }
        
        var numero = 2;
        var numeroTexto = "Numero desconocido";
        if (numero == 1) {
            numeroTexto = "numero uno";
        } else if (numero == 2) {
            numeroTexto = "numero dos";
        } else if (numero == 3) {
            numeroTexto = "numero tres"; // corregir "tes" a "tres"
        } else if (numero == 4) {
            numeroTexto = "numero cuatro";
        } else {
            numeroTexto = "numero no encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        var numeroIngresado = Integer.parseInt(entrada.nextLine());
        
        numeroTexto = "Valor desconocido"; // reiniciar variable numeroTexto
        switch (numeroIngresado) {
            case 1:
                numeroTexto = "Numero uno";
                break;
            case 2:
                numeroTexto = "Numero dos";
                break;
            case 3:
                numeroTexto = "Numero tres";
                break;
            case 4:
                numeroTexto = "Numero cuatro";
                break;
            default:
                numeroTexto = "Valor desconocido"; // corregir para mostrar el valor correcto en default
        }
        
        System.out.println("numeroTexto = " + numeroTexto);
    }
}