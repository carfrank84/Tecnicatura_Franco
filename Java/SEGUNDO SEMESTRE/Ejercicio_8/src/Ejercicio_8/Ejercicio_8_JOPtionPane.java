
package Ejercicio_8;

import javax.swing.JOptionPane;

public class Ejercicio_8_JOPtionPane {
    public static void main(String[] args) {
        String input = JOptionPane.showInputDialog("Digite un numero: ");
        int numero = Integer.parseInt(input);
        int i = 1;
        StringBuilder resultado = new StringBuilder();
        while(i <= numero){
            resultado.append(i).append("\n");
            i++;
        }
        JOptionPane.showMessageDialog(null, resultado.toString(), "Numeros del 1 al " + numero, JOptionPane.INFORMATION_MESSAGE);
    }
}
