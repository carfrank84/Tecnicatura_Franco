// Ejercicio 1 Calcular Estacion del año
let mes = 4;
let estacion;
if (mes == 1 || mes == 2 || mes == 2) {
  estacion = "verano";
} else if (mes == 3 || mes == 4 || mes == 5) {
  estacion = "otoño";
} else if (mes == 6 || mes == 7 || mes == 8) {
  estacion = "invierno";
} else if (mes == 9 || mes == 10 || mes == 11) {
  estacion = "primavera";
} else {
  estacion = "Mes inválido";
}

console.log("La estación correspondiente al mes:" + estacion);

// Ejercicio 2 calcular hora del dia
/*
de 6 a 11 nos saluda : Buenos dias
de 12 a 16 nos saluda : Es hora de la siesta
de 17 a 19 nos saluda : buenas tardes
de 20 a 23 nos saluda : buenas noches
*/

let horaDia = 19;
let mensaje;
if (horaDia >= 6 && horaDia <= 11) {
  mensaje = "Buenos dias";
} else if (horaDia >= 12 && horaDia <= 16) {
  mensaje = "Es hora de la siesta";
} else if (horaDia >= 17 && horaDia <= 19) {
  mensaje = "Buenas Tardes";
} else if (horaDia >= 20 && horaDia <= 23) {
  mensaje = "Buenas Noches";
} else {
  mensaje = "Valor incorrecto";
}
console.log(mensaje);

switch (mes) {
  case 1:
  case 2:
  case 12:
    estacion = "verano";
    break;
  case 3:
  case 4:
  case 5:
    estacion = "Otoño";
    break;
  case 6:
  case 7:
  case 8:
    estacion = "Invierno";
    break;
  case 9:
  case 10:
  case 11:
    estacion = "Primavera";
    break;
  default:
    estacion = "Valor Incorrecto";
}
console.log(" Bienvenido a la estacion de : " + estacion);

/* const se utiliza para valores constantes que no pueden ser reasignadas
 */
const fechaNacimiento = 2006;
console.log(fechaNacimiento);
// fechaNacimiento = 2003;
// console.log(fechaNacimiento); // solo se ejecuta el console anterior

// Evitar repetir tu codigo
// Dry dont't repeat yourself
// Estructura Switch

let days = 3;
switch (days) {
  case 1:
    console.log("Hoy es Lunes");
    break;
  case 2:
    console.log("Hoy es Martes ");
    break;
  case 3:
    console.log("Hoy es Miercoles");
    break;
  case 4:
    console.log("Hoy es Jueves");
    break;
  case 5:
    console.log("Hoy es Viernes");
    break;
  case 6:
    console.log("Hoy es Sabado");
    break;
  case 7:
    console.log("Hoy es Domingo");
    break;
  default:
    console.log("error en el ingreso del dia de la semana");
    break;
}
let days2 = [
  "Lunes",
  "Martes",
  "Miercoles",
  "Jueves",
  "Viernes",
  " Sabado",
  "Domingo",
];
function getDay(n) {
  if (n < 1 || n > 7) {
    throw new Error("out of range");
  }
  return days2[n - 1];
}
console.log(getDay(2));
// hacer un ejercicio similar al que esta hecho, pero ahora con los
// meses del año, debes hacerlo con la estructura switch y luego 
// la funcion mejorada

let month = 11;
switch (month) {
    case 1:
        console.log("Es Enero");
        break;
        case 2:
        console.log("Es Febrero");
        break;
        case 3:
        console.log("Es Marzo");
        break;
        case 4:
        console.log("Es Abril");
        break;
        case 5:
        console.log("Es Mayo");
        break;
        case 6:
        console.log("Es Junio");
        break;
        case 7:
        console.log("Es Julio");
        break;
        case 8:
        console.log("Es Agosto");
        break;
        case 9:
        console.log("Es Septiembre");
        break;
        case 10:
        console.log("Es Octubre");
        break;
        case 11:
        console.log("Es Noviembre");
        break;
        case 12:
        console.log("Es Diciembre");
        break;
        default:
            console.log("Error en el ingreso del mes del año")
            break;
}

// Esta es la opcion mejorada

let month2 = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
function getMonth(n){
    if(n < 1 || n > 12){
        throw new Error("Out of range");
    }
    return month2[n-1];
}
console.log(getMonth(5))
