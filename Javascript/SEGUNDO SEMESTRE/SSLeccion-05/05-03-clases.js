//let persona3 = new Persona('Carla', 'Popnce'); esto no se debe hacer : Persona is not defined

class Persona{// Clase Padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }
    get nombre (){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    get apellido(){
        return this._apellido
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
    nombreCompleto(){
        return this._nombre+' '+this._apellido;
    }
     // sobreescribiendo el metodo de la clase padre(Objet)
     toString(){// regresa un String
        //Se aplñica el polimorfismo que significa = multiples formas de ejecucion
        // El metodo que se ejecuta dependen si es una referencia de tipo padre o hija
        return this.nombreCompleto();
    }
}

class empleado extends Persona{// clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }

    // Sobreescritura
    nombreCompleto(){
        return super.nombreCompleto()+','+this._departamento;
    }
   
}


let persona1 = new Persona('Martin','Perez' );
console.log(persona1.nombre);
console.log(persona1.apellido);
persona1.nombre = 'Juan Carlos';
persona1.apellido = 'Poblete';
console.log(persona1.nombre);
console.log(persona1.apellido);
//console.log(persona1)
let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
console.log(persona2.apellido);
persona2.nombre = 'Maria Laura';
persona2.apellido = 'Moyano';
console.log(persona2.nombre);
console.log(persona2.apellido);
//console.log(persona2);

let empleado1 = new empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

//Object.prototype.toString esta es la manera de acceder a atributos de forma dinamica

console.log(empleado1.toString());
console.log(persona1.toString());
 
