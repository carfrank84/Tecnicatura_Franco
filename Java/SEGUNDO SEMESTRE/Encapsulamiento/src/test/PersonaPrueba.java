
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        System.out.println("persona1 = " + persona1); 
        System.out.println("Persona1 su nombre es :"+persona1.getNombre());
        //Modificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
      //persona1.nombre ="Juan Ignacio"; //ya no se puede utilizar 
      //System.out.println("Nombre es : "+persona1.nombre);// Error
        System.out.println("Persona1 con su nombre modificado :"+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo :"+persona1.getSueldo());
        System.out.println("persona1 para obtener el boolean: "+persona1.isEliminado());
        
    //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial 
    // e imprimir, luego modificar sus valores y volver a imprimir 
    
        Persona persona2 = new Persona("Franco", 950.000, true);
        System.out.println("Persona2 su nombre es :"+persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo :"+persona2.getSueldo());
        System.out.println("persona2 ha sido eliminada : "+persona2.isEliminado());
        
        //Modificacion de los datos
        persona2.setNombre("Maximiliano");
        persona2.setSueldo(865.000);
        persona2.setEliminado(false);
        
        // Imprimo los resultados de las modificaciones
        
        System.out.println("Persona2 su nombre modificado es :"+persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo modificado es  :"+persona2.getSueldo());
        System.out.println("persona2 ha sido eliminada con su cambio modificado : "+persona2.isEliminado());
        
        System.out.println("persona1 = " + persona1); 
        
    }
}
