
package clase.pkg9.ejercicio.pkg7;

import java.util.Scanner;

public class Clase9Ejercicio7 {
private static final int SALARIO_BASE = 1000;
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Ingrese el nuemro de carros vendidos");
        int numeroCarrosVendidos = entrada.nextInt();
        System.out.println("Ingrese el valor total de las ventas (en $) :");
        double valorTotalVentas = entrada.nextDouble();
        
        int comisionFija = numeroCarrosVendidos * 150;
        double comisionPorVentas = valorTotalVentas *0.5;
        
        double salarioMensual = SALARIO_BASE + comisionFija + comisionPorVentas;
        System.out.println("salarioMensual = " + salarioMensual);
        
    }
    
}
