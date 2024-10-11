
package dominio;

public class Persona {
    // Atributos
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    
    // Constructor
    public Persona (String nombre, double sueldo, boolean eliminado){
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }

    public String getNombre() {//get
        return nombre;
    }

    public void setNombre(String nombre) {//set
        this.nombre = nombre;
    }

    public double getSueldo() {// get
        return sueldo;
    }

    public void setSueldo(double sueldo) {// set
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {// para el tipo boolean se usa la palabra is en lugar de get
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {// set
        this.eliminado = eliminado;
    }
    
    public String toString(){// convierte en una cadena cada atributo
        return "Persona [nombre: "+this.nombre+
                ", sueldo: "+this.sueldo+
                " , eliminado: "+this.eliminado+"]";
    }
    
}
