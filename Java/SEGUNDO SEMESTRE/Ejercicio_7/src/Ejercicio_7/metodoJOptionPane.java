
package Ejercicio_7;
import javax.swing.JOptionPane;
public class metodoJOptionPane {
    public static void main(String[] args) {
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero >= 0) { //Mientras el nuemro sea negativo
            suma += numero;
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        if(conteo==0){
            JOptionPane.showMessageDialog(null,"\nError, la division entre 0 no existe");
        }
        else{
            promedio = (float)suma/conteo;
            JOptionPane.showMessageDialog(null, "\nEl promedio es : " +promedio);
        }
    }
}
