class Persona {
    static contadorPersonas = 0;

    constructor(nombre, apellido, edad) {
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    get idPersona() {
        return this._idPersona;
    }

    get nombre() {
        return this._nombre;
    }

    set nombre(nombre) {
        this._nombre = nombre;
    }

    get apellido() {
        return this._apellido;
    }

    set apellido(apellido) {
        this._apellido = apellido;
    }

    get edad() {
        return this._edad;
    }

    set edad(edad) {
        this._edad = edad;
    }

    toString() {
        return `${this._idPersona} ${this._nombre} ${this._apellido} ${this._edad}`;
    }
}

class Empleado extends Persona {
    static contadorEmpleados = 0;

    constructor(nombre, apellido, edad, sueldo) {
        super(nombre, apellido, edad); // Elimina sueldo de super
        this._idEmpleado = ++Empleado.contadorEmpleados;
        this._sueldo = sueldo;
    }

    get idEmpleado() {
        return this._idEmpleado;
    }

    get sueldo() {
        return this._sueldo;
    }

    set sueldo(sueldo) {
        this._sueldo = sueldo;
    }

    toString() {
        return `${this._idEmpleado} ${this._nombre} ${this._apellido} ${this._edad} ${this._sueldo}`;
    }
}

class Cliente extends Persona {
    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fechaRegistro) {
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegistro = fechaRegistro; // Inicializa la propiedad correctamente
    }

    get idCliente() {
        return this._idCliente;
    }

    get fechaRegistro() {
        return this._fechaRegistro;
    }

    set fechaRegistro(fechaRegistro) {
        this._fechaRegistro = fechaRegistro;
    }

    toString() {
        return `${this._idCliente} ${this._nombre} ${this._apellido} ${this._edad} ${this._fechaRegistro}`;
    }
}

// Prueba clase Persona
let persona1 = new Persona('Carlos', 'Poblete', 40);
console.log(persona1.toString());

let persona2 = new Persona('Nicole', 'Riveros', 35);
console.log(persona2.toString());

// Prueba clase Empleado
let empleado1 = new Empleado('Maxi', 'Montenegro', 30, 5000)
console.log(empleado1.toString());

let empleado2 = new Empleado('Lionel', 'Messi', 39, 100.000)
console.log(empleado2.toString())

// Prueba clase cliente
let cliente1 = new Cliente('Lautaro', 'Martinez', new Date)
console.log(cliente1.toString())

let cliente2 = new Cliente('Julian', 'Alvarez', new Date)
console.log(cliente2.toString())

