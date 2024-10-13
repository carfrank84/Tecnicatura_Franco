<script setup>
import NavBar from './components/navBar.vue';  // Aquí empieza en mayúscula
import DatosPersonales from './components/datosPersonales.vue';
import Educacion from './components/Educacion.vue';

</script>

<template>
  <header>
    <!-- Barra de navegacion -->
    <NavBar/> <!-- Ahora está con la primera letra en mayúscula -->
    <!-- Componente datos personales -->
    <DatosPersonales/>
  </header>
  <main>
    <section id="Educacion"><h2>Educacion - Cursos</h2>
    <Educacion />
  </section>
    <section id="Experiencia"><h2>Experiencia</h2></section>
    <section id="Proyectos"><h2>Proyectos</h2></section>
    <section id="Habilidades"><h2>Habilidades</h2></section>
    <section id="Intereses"><h2>Intereses</h2></section>
  </main>
</template>

<style scoped>

</style>
