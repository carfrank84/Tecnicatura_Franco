<script setup>
import NavBar from './components/NavBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';
import Educacion from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
import ProyectosComponente from './components/ProyectosComponente.vue';
import HabilidadesComponente from './components/HabilidadesComponente.vue';

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
    <Educacion/>
  </section>
    <section id="Experiencia"><h2>Experiencia</h2>
    <ExperienciaComponente/>
    </section>
    <section id="Proyectos"><h2>Proyectos</h2>
    <ProyectosComponente/>
    </section>
    <section id="Habilidades"><h2>Habilidades</h2>
    <HabilidadesComponente/>
    </section>
    <section id="Intereses"><h2>Intereses</h2></section>
  </main>
</template>

<style scoped>

</style>
