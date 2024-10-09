package Ejercicio_9;

import javax.swing.JOptionPane;

public class Ejercicio_9_JOptionPane {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el día: "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes: "));
        int año = Integer.parseInt(JOptionPane.showInputDialog("Digite el año: "));
        
        if((dia >= 1 && dia <= 30) && (mes >= 1 && mes <= 12) && (año > 0)) {
            JOptionPane.showMessageDialog(null, "La fecha es correcta.");
        } else {
            JOptionPane.showMessageDialog(null, "La fecha es incorrecta.");
        }
    }
}

