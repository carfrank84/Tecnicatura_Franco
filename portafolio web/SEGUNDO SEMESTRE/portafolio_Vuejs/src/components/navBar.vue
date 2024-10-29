<template>
  <!-- Barra de navegación -->
  <nav class="navbar">
    <div class="navbar-menu">
      <ul class="nav-list">
        <!-- Itera sobre el array de navegación y crea un enlace para cada elemento -->
        <li v-for="nav in navegacion" :key="nav.nombre" class="nav-item-container">
          <a :href="nav.enlace" class="nav-item">{{ nav.nombre }}</a>
        </li>
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
  { id: 3, nombre: 'Proyectos', enlace: '#Proyectos' },
  { id: 4, nombre: 'Habilidades', enlace: '#Habilidades' },
  { id: 5, nombre: 'Intereses', enlace: '#Intereses' },
]);
</script>

<style scoped>
/* Estilos para la barra de navegación */
.navbar {
  background-image: url('/src/assets/FondoAzul.jpg'); /* Color de fondo de la barra */
  color: #fff; /* Color del texto */
  padding: 1rem; /* Espaciado interno */
  display: flex; /* Asegura que los elementos se alineen */
  justify-content: center; /* Centra la barra de navegación */
  align-items: center; /* Alinea los elementos verticalmente */
}

/* Contenedor de los elementos de la barra de navegación */
.navbar-menu {
  display: flex; /* Utiliza flexbox para centrar el contenido */
  justify-content: center; /* Centra los elementos dentro de navbar-menu */
  width: 100%; /* Asegura que ocupe el ancho completo de la barra */
}

/* Lista de elementos de navegación */
.nav-list {
  list-style: none; /* Elimina el estilo de la lista */
  padding: 0; /* Elimina el padding de la lista */
  margin: 0; /* Elimina el margen de la lista */
  display: flex; /* Usar flexbox para los elementos de la lista */
  flex-wrap: wrap; /* Permite que los elementos se ajusten en varias líneas */
  justify-content: center; /* Centra los botones en modo web */
}

/* Contenedor de cada item de navegación */
.nav-item-container {
  margin-right: 1rem; /* Espaciado a la derecha */
  margin-bottom: 15px; /* Espaciado inferior para separación */
}

/* Estilos generales para los enlaces */
.nav-item {
  border: 2px solid; /* Borde de los enlaces */
  border-color: hsl(247, 93%, 41%); /* Color del borde */
  border-radius: 5px; /* Bordes redondeados */
  text-decoration: none; /* Elimina el subrayado de los enlaces */
  transition: 0.4s; /* Transición suave para cambios de estilo */
  padding: 12px 16px; /* Espaciado interno aumentado */
}

/* Efecto hover para los enlaces */
.nav-item:hover {
  background-color: hsla(0, 90%, 39%, 0.728); /* Cambia el color de fondo al pasar el mouse */
}

/* Estilos para pantallas más pequeñas */
@media (max-width: 768px) {
  .navbar {
    flex-direction: column; /* Cambia a columna en pantallas pequeñas */
    align-items: center; /* Alinea el contenido al centro */
  }

  .nav-list {
    flex-direction: column; /* Cambia la lista a columna */
    align-items: center; /* Alinea los elementos al centro */
    width: 100%; /* Asegura que ocupe todo el ancho */
  }

  .nav-item-container {
    margin-right: 0; /* Elimina el margen derecho en pantallas pequeñas */
    margin-bottom: 20px; /* Aumenta el espaciado inferior entre enlaces */
    width: 100%; /* Asegura que cada elemento ocupe el ancho completo */
  }

  .nav-item {
    padding: 14px 20px; /* Aumenta el espaciado interno para un diseño más aireado */
  }
}
</style>
