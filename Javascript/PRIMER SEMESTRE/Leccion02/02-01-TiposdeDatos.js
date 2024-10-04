// Tipos de Datos en JavaScript
/*
la sintaxis en lo que es comentarios
es muy similar ala de Java realmentediriamos
que es identica
*/
var nombre = "Franco"; // tipo str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);

var numero = 3000; // Tipo numerico
console.log(typeof numero);

var objeto = { // Tipo Objeto
    nombre: "Franco",
    apellido: "Poblete",
    telefono: "2616661061"
}

console.log(objeto);

// Tipo de dato Boolean
var bandera = true;
console.log(typeof bandera);

// Tipo de dato Funcion
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo de dato Symboll
var simbolo = Symbol("Mi Simbolo");
console.log(simbolo);

// Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona);

// Tipo de dato undefined
var x;
console.log(typeof x);

x  = undefined;
console.log(typeof x)
//null: significa ausencia de valor
var y = null; // null no es un tipo de dato pero su origen es de tipo objet
console.log(typeof y); 


// tipo de dato array y Emty Script
var autos = ["Citroen","Audi","BMW","Ford" ];
console.log(autos);
console.log(typeof autos);//Preguntamos que tipo de datos es: 

var z="";
console.log(z); // esto es una cadena vacia
console.log(typeof z);






