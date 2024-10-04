
package Ejercicio_4_Scanner;

import javax.swing.JOptionPane;


public class Ejercicio_4_JOptionPane {
    public static void main(String[] args) {
        int numero, contador = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){
            JOptionPane.showMessageDialog(null, "El numero "+numero+" Es POSITIVO" );
            contador ++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
                        
        }
        JOptionPane.showMessageDialog(null, "ha Ingresado "+contador+" numeros POSITIVOS" );
    }
    
}
    

