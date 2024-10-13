<template>
  <!-- Barra de navegación -->
  <nav class="navbar">
    <div class="navbar-menu">
      <ul>
        <!-- Itera sobre el array de navegación y crea un enlace para cada elemento -->
        <a v-for="nav in navegacion" :key="nav.nombre" :href="nav.enlace" class="nav-item">{{ nav.nombre }}</a>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue';

// Definición del array de navegación
const navegacion = ref([
  { id: 1, nombre: 'Educacion', enlace: '#Educacion' },
  { id: 2, nombre: 'Experiencia', enlace: '#Experiencia' },
  { id: 3, nombre: 'Proyectos', enlace: '#proyectos' },
  { id: 4, nombre: 'Habilidades', enlace: '#habilidades' },
  { id: 5, nombre: 'Intereses', enlace: '#intereses' },
]);
</script>

<style scoped>
/* Estilos para la barra de navegación */
.navbar {
  background-color: var(--vt-c-indigo); /* Color de fondo de la barra */
  color: #fff; /* Color del texto */
  padding: 1rem 1rem; /* Espaciado interno */
  align-items: center; /* Alineación de los elementos */
}

/* Estilos para los elementos de la lista de navegación */
.navbar-item {
  color: #fff; /* Color del texto de los enlaces */
  text-decoration: none; /* Elimina el subrayado de los enlaces */
  margin-right: 1rem; /* Espaciado a la derecha */
}

/* Contenedor de los elementos de la barra de navegación */
.navbar-menu {
  display: flex; /* Utiliza flexbox para alinear los elementos */
  justify-content: flex-end; /* Alinea los elementos al final */
}

/* Elimina las viñetas de la lista */
.nav-list {
  list-style: none; /* Elimina el estilo de la lista */
}

/* Estilos generales para los enlaces */
a {
  border: 1px solid; /* Borde de los enlaces */
  border-color: hsla(60, 10%, 96%, 0.886); /* Color del borde */
  border-radius: 5px; /* Bordes redondeados */
  text-decoration: none; /* Elimina el subrayado de los enlaces */
  transition: 0.4s; /* Transición suave para cambios de estilo */
  padding: 7px; /* Espaciado interno */
}

/* Efecto hover para los enlaces */
a:hover {
  background-color: hsla(103, 76%, 23%, 0.616); /* Cambia el color de fondo al pasar el mouse */
}

/* Estilos para pantallas más pequeñas */
@media (max-width: 768px) { /* Corrige el error tipográfico de 'max-whidth' a 'max-width' */
  .navbar-menu {
    display: flex; /* Asegura que el menú se muestre en flexbox */
    justify-content: flex-end; /* Alinea los elementos al final */
    width: 100%; /* Establece el ancho al 100% */
  }
}
</style>
