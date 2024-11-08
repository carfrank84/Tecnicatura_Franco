
<script setup>
import {ref} from 'vue';

// Definición de los colores de las fechas
const fechaColor = ref([
  { color: 'hsla(165, 90%, 39%, 0.728)' }, // Color verde
  { color: 'hsla(154, 93%, 41%)' }, 
  { color: 'hsla(154, 93%, 41%)' }, 
  { color: 'hsla(165, 90%, 39%, 0.728)' }, 
  { color: 'hsla(154, 93%, 41%)' }, 
]);

// Definición de los datos de educación
const educacion = ref([
  { fecha: '2024', title: 'Especialización en Inteligencia Artificial', descripcion: 'Me especialice en la creación y manejo de modelos de IA para diversos sectores, mejorando procesos y generando insights valiosos.' },
  { fecha: '2023', title: 'Desarrollo de Juegos', descripcion: 'Diseñe y desarrolle videojuegos innovadores y atractivos, utilizando tecnologías como Unity y Unreal Engine.' },
  { fecha: '2022', title: 'Desarrollo de Páginas Web', descripcion: 'Creacion de sitios web dinámicos y responsivos, optimizados para SEO y con una experiencia de usuario impecable.' },
  { fecha: '2021', title: 'Desarrollo de Aplicaciones Móviles', descripcion: 'Desarrollo aplicaciones móviles intuitivas y funcionales para iOS y Android, utilizando frameworks como React Native y Flutter.' },
  { fecha: '2020', title: 'Fundación de K.O.T.A', descripcion: 'Mi formacion tiene una misión clara: innovar y liderar en el mundo del desarrollo tecnológico.' },
]);
</script>

<template>
  <ul>
    <!-- Se crea una lista de educación, iterando sobre los datos -->
    <li v-for="(item, index) in educacion" :key="index" :style="{ '--fecha-color': fechaColor[index].color }">
      <div class="fecha">{{ item.fecha }}</div>
      <h3 class="title">{{ item.title }}</h3>
      <div class="descripcion">{{ item.descripcion }}</div>
    </li>
  </ul>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap");

/* Estilo general y reset */
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Estilos del cuerpo */
body {
  --bgColor: #000000; /* Color de fondo */
  min-height: 100vh;
  display: grid;
  align-content: center;
  gap: 2rem;
  padding: 2rem;
  font-family: "Poppins", sans-serif;
  color: #000; /* Color del texto */
  background: var(--bgColor);
}

/* Estilos de la lista */
ul {
  margin-top: 2rem;
  --col-gap: 2rem; /* Espaciado entre columnas */
  --row-gap: 2rem; /* Espaciado entre filas */
  --line-w: 0.50rem; /* Ancho de la línea */
  display: grid;
  grid-template-columns: var(--line-w) 1fr; /* Una columna para la línea y otra para el texto */
  grid-auto-columns: max-content; /* Columna para el texto */
  column-gap: var(--col-gap); /* Espaciado entre columnas */
  list-style: none; /* Sin viñetas */
  width: min(60rem, 90%); /* Ancho de la lista */
  margin-inline: auto; /* Centrado horizontal */
}

/* Línea de conexión */
ul::before {
  content: ""; /* Contenido vacío para crear la línea */
  grid-column: 1; /* Columna de la línea */
  grid-row: 1 / span 20; /* Espacia en las filas */
  background: #014f0db6; /* Color de la línea */
  width: var(--line-w); /* Ancho de la línea */
}

/* Estilos de cada item de la lista */
ul li:not(:last-child) {
  margin-bottom: var(--row-gap); /* Espaciado entre filas */
}

ul li {
  grid-column: 2; /* Columna para el texto */
  --inlineP: 1.5rem; /* Espaciado interno */
  margin-inline: var(--inlineP); /* Margen interno */
  grid-row: span 2; /* Altura de la celda */
  display: grid; /* Usar grid para la disposición interna */
  grid-template-rows: min-content min-content min-content; /* Definición de filas */
}

/* Estilo del cuadro de la fecha */
ul li .fecha {
  height: 3rem; /* Altura de la fecha */
  margin-inline: calc(var(--inlineP) * -1); /* Margen negativo para alinear */
  text-align: center; /* Alineación de texto */
  background-color: var(--fecha-color); /* Color de fondo de la fecha */
  color: #0f0e0e; /* Color del texto de la fecha */
  font-size: 1.25rem; /* Tamaño de fuente */
  font-weight: 750; /* Peso de fuente */
  display: grid; /* Usar grid para centrar contenido */
  place-content: center; /* Centrando contenido */
  border-radius: 1.5rem; /* Bordes redondeados */
}

/* Estilo del pseudo-elemento antes de la fecha */
ul li .fecha::before {
  content: ""; /* Contenido vacío para crear la forma */
  width: var(--inlineP); /* Ancho de la forma */
  aspect-ratio: 2; /* Relación de aspecto cuadrada */
  background: var(--fecha-color); /* Color de fondo de la forma */
  position: absolute; /* Posicionamiento absoluto */
  top: 100%; /* Colocación debajo de la fecha */
  clip-path: polygon(0 0, 100% 0, 0 100%); /* Forma triangular */
  right: 0; /* Alineación a la derecha */
}

/* Estilo del círculo que conecta la línea con el cuadro de la fecha */
ul li .fecha::after {
  content: ""; /* Contenido vacío para el círculo */
  position: absolute; /* Posicionamiento absoluto */
  width: 1rem; /* Ancho del círculo */
  aspect-ratio: 1; /* Relación de aspecto cuadrada */
  background: var(--bgColor); /* Color de fondo */
  border: 0.3rem solid var(--fecha-color); /* Borde del círculo */
  border-radius: 50%; /* Forma circular */
  top: 50%; /* Centrado verticalmente */
  transform: translate(50%, -50%); /* Alineación */
  right: calc(100% + var(--col-gap) + var(--line-w) / 2);
}

/* Estilos del título y descripción */
ul li .title, ul li .descripcion {
  background: var(--bgColor); /* Color de fondo */
  position: relative; /* Para elementos hijos */
  padding-inline: 1.5rem; /* Espaciado interno */
}

/* Estilos del título */
ul li .title {
  overflow: hidden; /* Ocultar contenido excedente */
  padding-block-start: 1.5rem; /* Espaciado superior */
  padding-block-end: 1rem; /* Espaciado inferior */
  font-weight: 500; /* Peso de fuente */
}

/* Estilos de la descripción */
ul li .descripcion {
  padding-block-end: 1.5rem; /* Espaciado inferior */
  font-weight: 300; /* Peso de fuente */
}

/* Pseudo-elemento antes del título y descripción */
ul li .title::before, ul li .descripcion::before {
  content: ""; /* Contenido vacío */
  position: absolute; /* Posicionamiento absoluto */
  width: 90%; /* Ancho */
  height: 0.5rem; /* Altura */
  background: rgba(149, 254, 1, 0.852); /* Color de fondo */
  left: 50%; /* Alineación central */
  border-radius: 50%; /* Bordes redondeados */
  filter: blur(3px); /* Difuminado */
  transform: translate(-50%, 50%); /* Posicionamiento */
}

/* Posicionamiento del pseudo-elemento antes del título */
ul li .title::before {
  bottom: calc(100% + 0.125rem); /* Espaciado inferior */
}

/* Posicionamiento del pseudo-elemento antes de la descripción */
ul li .descripcion::before {
  z-index: -1; /* Enviar al fondo */
  bottom: 0.25rem; /* Espaciado inferior */
}

/* Media query para estilos responsivos */
@media (min-width: 40rem) {
  ul {
    grid-template-columns: 1fr var(--line-w) 1fr; /* Tres columnas */
  }

  ul::before {
    grid-column: 2; /* Colocar línea en la columna central */
  }

  ul li:nth-child(odd) {
    grid-column: 1; /* Columnas alternas */
  }

  ul li:nth-child(even) {
    grid-column: 3; /* Columnas alternas */
  }
}
</style>
