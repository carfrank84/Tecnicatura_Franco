
import java.util.Scanner;

public class HolaMundo {

    public static void main(String[] args) {
        //System.out.println("Hola Mundo desde Java");

        /* int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programacion";
        System.out.println(miVariableCadena);*/
        // Var - inferencia de tipos en Java
        /*int miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        //soutv + tab
        //Reglas para definir un variable en Java*/
 /*var usuario = "Franco";
        var titulo = "Programador";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);

        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        // Ejercicio: caracteres especiales con Java
        var nombre = "Franco";
        System.out.println("\nNueva linea: \n " + nombre);//\diagonal inversa y letra n
        System.out.println("Tabulador \t" + nombre);// tabulador para centrar
        System.out.println("\t\t.:Menu:.");
        System.out.println("Retroceso: \b\b"+nombre);//caracter de retroceso
        System.out.println("comillas simples: \'"+nombre+"\'");
        System.out.println("comillas dobles: \""+nombre+"\"");*/
        //clase scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre:");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado:"+titulo2+" "+usuario2);*/
 /*Scanner scanner = new Scanner(System.in);
        // escribe tu solucion aqui
        System.out.println("Proporciona el titulo:");
        String titulo = scanner.nextLine();
        System.out.println("Proporciona el Autor:");
        String autor = scanner.nextLine();
        System.out.println(titulo + " Fue escrito por " + autor);*/
 /*byte numEnteroByte = (byte)127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte:"+Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte:"+Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo de Short:"+Short.MIN_VALUE);
        System.out.println("Valor Maximo de Short:"+Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo de Int:"+Integer.MIN_VALUE);
        System.out.println("Valor Maximo de Int:"+ Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo de long:"+Long.MIN_VALUE);
        System.out.println("Valor Maximo de long:"+Long.MAX_VALUE);*/
        // variables tipo float
        /* float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El Valor minimo de float:"+Float.MIN_VALUE);
        System.out.println("El valor Maximo de float:"+Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El Valor minimo de double:"+Double.MIN_VALUE);
        System.out.println("El valor maximo de double:"+Double.MAX_VALUE);*/
        // inferencia de tipo var y de tipo primitivo
        /* var numEntero = 20; //las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero); 
       var numfloat = 10.0F; // automaticamente con el punto se transforma en un tipo double
        System.out.println("numfloat = " + numfloat);
       var numDouble = 10.0;
       System.out.println("numDouble = " + numDouble);*/
        // Tipos Primitivos char
        /* char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);

        char varCaracter = '\u0024';// indicamos a Java con el codigo Unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; // valor decimal del juego de de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$';// un caracter especial , podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024';
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char)36;
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSibolo1 = '$';
        System.out.println("varCaracterSibolo1 = " + varCaracterSibolo1);
        
        int varEnterochar = '$';
        System.out.println("varEnterochar = " + varEnterochar);
        int caracterChar = 'p';
        System.out.println("caracterChar = " + caracterChar);*/
        //
//       var edad = Integer.parseInt("20");
//        System.out.println("edad = " + (edad + 1));
//                
//        var  valorPI = Double.parseDouble("3.1416");
//        System.out.println("valorPI = " + valorPI);
//        
        // Pedir un valora
        /* var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad:");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad);

        // Conversion de tipos promitivos en Java Parte 2
//      var edadTexto = String.valueOf(10);
//        System.out.println("edadTexto = " + edadTexto);
//        
//        var fraseChar = "programadores".charAt(0);
//        System.out.println("fraseChar = " + fraseChar);
//        
//        System.out.println("Digite un caracter:");
//        fraseChar = entrada.nextLine().charAt(0);
//        System.out.println("fraseChar = " + fraseChar);
            
         /* int num1 = 5,num2 = 4;
          var solucion = num1 + num2;
          System.out.println("solucion de la suma suma = " + solucion);
          
          solucion = num1 - num2;
          System.out.println("solucion de la resta = " + solucion);
          
          solucion = num1 * num2;
          System.out.println("solucion de la multiplicacion = " + solucion);
          
          solucion = num1 / num2;
          System.out.println("solucion de la division = " + solucion);

          var solucion2 = 3.4 /num2;
          System.out.println("solucion2 = " + solucion2);
          
          solucion = num1 % num2;// guarda el residuo entero de la division
          System.out.println("solucion2  = " + solucion2);//5/4
          
          if (num2 % 2 == 0)
              System.out.println("Es un numero Par");
          else
              System.out.println("Es un numero Impar");*/
        // Operadores de Asignacion      
        /*     int varNum1 = 10, varNum2 = 4;
          var varNum3 = varNum1 + 6 - varNum2; // le asignamos una operacion
          System.out.println("varNum3 = " + varNum3);
          
          varNum1 += 1; // varNum1 = varNum + 1 ;//suma
         System.out.println("varNum1 suma = " + varNum1);
         
         varNum1 -= 2; // resta
         System.out.println("varNum1 resta= " + varNum1);
         
         varNum1 *= 2; // multiplicacion
         System.out.println("varNum1 multiplicacion = " + varNum1);
         
         varNum1 /= 3; // division
         System.out.println("varNum1 = " + varNum1);
         
         varNum1 %= 2; // resto
         System.out.println("varNum1 residuo= " + varNum1);*/
        // Operadores unarios: Cambio de signo
        /* var varA = 7;
         var varB= -varA;
         System.out.println("varA = " + varA);
         System.out.println("varB = " + varB);// el resultado sera Negativo
         
         // Operador de Negacion
         var varC = true; // esta Literal por  dedefault en Java es de tipo boolean
         var varD = !varC;// aqui esta invirtiendo el valor
         System.out.println("varC = " + varC);
         System.out.println("varD = " + varD);
         
         // Operadores unarios de incremento: preincremento
         var varE = 9; // se va a modificar su valor
         var varF = ++varE;// simbolo antes de la variable
         // primero se ioncrementa la variable y despues se usa su valor
         System.out.println("varE = " + varE);// se incrementa en la unidad
         System.out.println("varF = " + varF);// va a sumar uno
         
         // postincremento (el simbolo va despues de la variable)
         var varG = 3;
         var varH = varG ++; // primero el valor de la variable , luego el incremento
         System.out.println("varG = " + varG);
         System.out.println("varH = " + varH);
         
         // operadores unarios de decremento: Predecremento
         var varI = 4;
         var varJ = --varI;
         System.out.println("varI = " + varI);// La variable ya esta en decremento 
         System.out.println("varJ = " + varJ);
         
         //postdecremento
         var varK= 8;
         var varL= varK--;// Primero el valor de la variable, luego queda el decremento
         System.out.println("varK = " + varK);// aqui va a decrementar 1
         System.out.println("varL = " + varL);*/
        //Operadores de igualdad y Relacionales
        /*var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);

        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);

        var cadenaA = "Hello";
        var cadenaB = "Bye Bye";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);

        var fvarf = cadenaA.equals(cadenaB);
        System.out.println("fvarf = " + fvarf);

        var gVar = aNum != bNum;//< <= > >= == !=
        System.out.println("gVar = " + gVar);

        if (bNum % 2 == 0) {
            System.out.println("El numero es Par");
        } else{
                    System.out.println(" El Numero es Impar");
                    
        }
        var edad = 15;
        var adulto = 18;
        if (edad >= adulto) {
            System.out.println("Es Mayor de edad");
        }
        else {
            System.out.println("Es Menor de Edad");
        }*/
        // operadores condicionales
        /*var valorA = 0;
        var valorMinimo = 0;
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;

        if (respuesta) {
            System.out.println("Esta dentro del Rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }

        var vacaciones = false;
        var diaLibre = false;
        if (vacaciones || diaLibre) {
            System.out.println("Papa puede asistior al juego de su hijo");
        } else {
            System.out.println("Papa no puede asisitirt al juego de su hijo");
        }*/
        // Operador ternario
        /* var resultadoT= (5 > 4) ? "Verdadero" : "Falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0) ? " Es Par" : "Es Impar";
        System.out.println("resultadoT = " + resultadoT);*/
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);// 6
        System.out.println("y = " + y);// 9
        System.out.println("z = " + z);// 16

        var solucionAritmetica = 4 + 5 * 6 / 3;// 4 + (5 * 6) / 3) = 30 / 3 = 10 + 4 = 14
        System.out.println("solucionAritmetica = " + solucionAritmetica);

        solucionAritmetica = (4 + 5) * 6 / 3;// 4 + 5 = 9 * 6 = 54 / 3 = 18
        System.out.println("solucionAritmetica = " + solucionAritmetica);

    }
}
