<script setup>
import NavBar from './components/NavBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';
import Educacion from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
import ProyectosComponente from './components/ProyectosComponente.vue';
import HabilidadesComponente from './components/HabilidadesComponente.vue';
import InteresesComponente from './components/InteresesComponente.vue';
</script>

<template>
  <header id="top">
    <!-- Barra de navegacion -->
    <NavBar/> <!-- Ahora está con la primera letra en mayúscula -->
    <!-- Componente datos personales -->
    <DatosPersonales/>
  </header>
  <main>
    <section id="Educacion"><h2>Educación - Cursos</h2>
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
    <section id="Intereses"><h2>Intereses</h2>
    <InteresesComponente/>
    </section>
  </main>
  <footer>
    <div class="btn">
      <a href="#top">Inicio</a> <!-- Cambiado a #top -->
    </div>
    
    <p>Portafolio web - Carlos Franco Poblete - Tecnico Universitario en Programación</p>
  </footer>
</template>

<style scoped> 
footer {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  font-size: 1.3rem;
}

.btn {
  position: relative;
  top: 10%;
  left: 10%;
  border-radius: 3em;
  padding: 0.2em 0.2em;
  transform: translate(-50%, -50%);
  background-image: linear-gradient(90deg, #15b974, #04acff, #eaaaaa, #e11adc, #a0a00f, #3e56a7, #14accc);
  background-size: 350%;
}

a {
  letter-spacing: .3em;
  font-weight: 1000;
  font-size: 1.1em;
  padding: .1em .3em;
  background-color: none;
  font-family: 'Raleway', sans-serif;
  text-transform: uppercase;
  color: white;
  border-radius: 1.5em;
  text-align: center;
  text-decoration: none;
}

.btn:hover {
  animation: animate 3s ease-out infinite;
}

a:hover {
  text-shadow: 0 0 .5em rgba(255, 255, 255, 0.8);
}

@keyframes animate {
  0% {
    background-position: 0%;
    box-shadow: 0 0 .8em #04acff;
  }
  50% {
    background-position: 60%;
    box-shadow: 0 0 .8em #e11adc;
  }
  100% {
    background-position: 100%;
    box-shadow: 0 0 .8em #3e56a7;
  }
}
</style>
