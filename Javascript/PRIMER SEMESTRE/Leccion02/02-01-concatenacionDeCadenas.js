var nombre = "Jose";
var apellido = " Montes";
var nombreCompleto = nombre+" "+apellido;//Primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = "Franco"+" "+"Poblete";// Segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre +219 // lle de izq a derecha siguendo la cadena lee el niemrop como str
console.log(juntos);
juntos = nombre + (78 + 17); // Aquie se puede diferenciar a traves de los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; // Tercerta concatenacion con el operador de asignacion simplificado 
console.log(nombre);

// Hoy ya no se usa var, se utiliza let y const
let nombre2 = " Pedro";
console.log(nombre2);

const apellido2 = " Lepes";
// apellido2 = "peres"; una constante no puede ser modificada

let x, y ; // se peuden crear varias variables dentro de una misma linea
x = 17, y = 21; // se pueden hacer asignacion de varias variables dentro de una isma linea
let z = x + y ;
console.log(z);

let $1num = 31;// no utilizar numeros para inciapre el nombre de una variable 
let rompiendo = "rompe"; // no utilizar palabras reservadas paa varioanles  

console.log($1num);
console.log(rompiendo);













