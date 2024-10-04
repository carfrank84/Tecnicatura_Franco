let x = 10; // variable de tipo primitiva
console.log(x.length);
console.log('Tipos Primitivos')

// objeto
let persona = {
    nombre: 'Franco',
    apellido: ' Poblete',
    email: 'carfrank84@gmail.com',
    edad: 28,
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase(); // convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma =lang.toUpperCase();
    },
    nombreCompleto: function(){// metodo o funcoin en Javascript
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){ // este es el metodo get
        return ' El Nombre es: '+ this.nombre+' edad: '+this.edad;    
    }
    
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto');

let persona2 = new Object(); // debe crear un nuevo objeto en memoria
persona2.nombre = ' Maxi';
persona2.direccion = 'Valeria del Mar';
persona2.telefono = '011666106123'
console.log(persona2.telefono);
console.log('creamos un nuevo objeto');

console.log(persona['apellido']); // accedemos como si fuera un arreglo
console.log('Usamos el ciclo for in');

// for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

console.log('cambiamos y eliminamos un error')
persona.apellida = 'Montenegro';// cambiamos dinamicamente un valor del objeto
delete persona.apellida ; 
console.log(persona);

// distintas formas de imprimir un objeto
// numero 1 : la mas sencilla : concatenar cada valor de cada propiedad
console.log('Distinta formas de imprimir un objeto: forma1');
console.log(persona.nombre+', '+persona.apellido);

// Numero 2: A travez del ciclo for in
console.log('distintas formas de imprimir un objeto: forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

// numero 3: La funcion Objets.values()
console.log('Distintas formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

// Numero 4: Utilizamos el metodo JSON.Stringify
console.log('Distintas formas de imprimir un objeto: forma 4')
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log('Comenzamos a utilizar el metodo get')
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email ){// constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre +' '+ this.apellido
    }

}
let padre = new Persona3('Leo', 'Lopez', 'lopez@gmail.com'); 
padre.nombre = 'Luis'; // modificamos el nombre
padre.telefono = '511946466161'; // una propiedad esclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); // utilizamos la funcion
let madre = new Persona3('Laura', 'Contrera', 'contreral@gmail.com');
console.log(madre);
console.log(madre.telefono);// la propiedad no esta definida
console.log(madre.nombreCompleto());

// diferentes formas de crear objetos 
// Caso objeto 1
let miObjeto = new Object(); //Esta es una opcion formal
// caso objeto 2
let miObjeto2 = {}; // esta opcion es breve y recomendada

// caso string 1
let miCadena1 = new String('Hola'); // sintaxis formal
// caso String 2
let miCadena2 = 'Hola';//Esta es la sintaxis simplificada y recomendada

// cvaso con numeros 1
let miNumero = new Number(1);// es formal no recomendable
// caso con numeros 2
let miNumero2 = 1;// sintaxis recomendada

// caso boolean 1
let miBoolean1 = new Boolean(false);// Formal
// caso boolean 2
let miBoolean2 = false; // sintaxis recomendada

// caso arreglos 1
let miArreglo1 = new Array(); // formal
// caso arreglos 2
let miArreglo2 = [];// sintaxis recomendada

// caso function 1
let miFuncion1 = new function(){}; //todo despues de new es considerado objeto
// caso function 2
let miFuncion2 = function(){};// notacion simplificada y recomendada

// uso de prototype
Persona3.prototype.telefono = '2612365365';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '261222222222'
console.log(madre.telefono);

// uso de call
let persona4 ={
    nombre: 'Julian',
    apellido: ' Alvarez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
       //return this.nombre+' '+this.apellido;
    }
}

let persona5 ={
    nombre: 'Tony',
    apellido: 'Stark'
}

console.log(persona4.nombreCompleto2('Lic.', '261111111'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '261444444'));

// metodo apply
let arreglo = ['Ing.', '2612313132']
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));


