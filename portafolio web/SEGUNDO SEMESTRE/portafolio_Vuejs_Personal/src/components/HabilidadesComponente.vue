<template>
    <div class="habilidades">
      <!-- Sección Lenguaje de Programación -->
      <section class="lenguajes">
        <h2>Lenguaje de Programación</h2>
        <div class="habilidad" v-for="(item, index) in lenguajes" :key="index">
          <img :src="item.logo" :alt="item.nombre" class="logo" />
          <p>{{ item.nombre }}: {{ item.nivel }}</p>
        </div>
      </section>
  
      <!-- Sección Frameworks y Librerías -->
      <section class="frameworks">
        <h2>Frameworks y Librerías</h2>
        <div class="habilidad" v-for="(item, index) in frameworks" :key="index">
          <img :src="item.logo" :alt="item.nombre" class="logo" />
          <p>{{ item.nombre }}: {{ item.nivel }}</p>
        </div>
      </section>
  
      <!-- Sección Herramientas y Software -->
      <section class="herramientas">
        <h2>Herramientas y Software</h2>
        <div class="habilidad" v-for="(item, index) in herramientas" :key="index">
          <img :src="item.logo" :alt="item.nombre" class="logo" />
          <p>{{ item.nombre }}: {{ item.nivel }}</p>
        </div>
      </section>
  
      <!-- Sección Bases de Datos -->
      <section class="basesDatos">
        <h2>Base de Datos</h2>
        <div class="habilidad" v-for="(item, index) in basesDatos" :key="index">
          <img :src="item.logo" :alt="item.nombre" class="logo" />
          <p>{{ item.nombre }}: {{ item.nivel }}</p>
        </div>
      </section>
  
      <!-- Sección Idiomas -->
      <section class="idiomas">
        <h2>Idiomas</h2>
        <div class="habilidad" v-for="(item, index) in idiomas" :key="index">
          <img :src="item.logo" :alt="item.nombre" class="logo" />
          <p>{{ item.nombre }}: {{ item.nivel }}</p>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  import JavaScript from '../assets/js.svg';
  import Python from '../assets/python.svg';
  import HTMLCSS from '../assets/html-css.svg';
  import Java from '../assets/java.svg';
  import SQL from '../assets/sql.svg';
  import React from '../assets/react.svg';
  import Vue from '../assets/vue.svg';
  import Node from '../assets/node.svg';
  import Django from '../assets/django.svg';
  import Bootstrap from '../assets/bootstrap.svg';
  import Git from '../assets/git.svg';
  import Docker from '../assets/docker.svg';
  import Cypress from '../assets/cypress.svg';
  import Figma from '../assets/figma.svg';
  import VSCode from '../assets/visual.svg';
  import MongoDB from '../assets/mongo.svg';
  import MySQL from '../assets/mysql.svg';
  import PostgreSQL from '../assets/postgres.svg';
  import Espanol from '../assets/arg.svg';
  import Inglés from '../assets/eeuu.svg';
  import Japones from '@/assets/japon2.png'; 
  
  export default {
    data() {
      return {
        lenguajes: [
          { nombre: 'JavaScript', nivel: 'Avanzado', logo: JavaScript },
          { nombre: 'Python', nivel: 'Intermedio', logo: Python },
          { nombre: 'HTML/CSS', nivel: 'Avanzado', logo: HTMLCSS },
          { nombre: 'Java', nivel: 'Intermedio', logo: Java },
          { nombre: 'SQL', nivel: 'Intermedio', logo: SQL }
        ],
        frameworks: [
          { nombre: 'React.js', nivel: 'Avanzado', logo: React },
          { nombre: 'Vue.js', nivel: 'Intermedio', logo: Vue },
          { nombre: 'Node.js', nivel: 'Avanzado', logo: Node },
          { nombre: 'Django', nivel: 'Intermedio', logo: Django },
          { nombre: 'Bootstrap', nivel: 'Avanzado', logo: Bootstrap }
        ],
        herramientas: [
          { nombre: 'Git', nivel: 'Avanzado', logo: Git },
          { nombre: 'Docker', nivel: 'Avanzado', logo: Docker },
          { nombre: 'Cypress', nivel: 'Intermedio', logo: Cypress },
          { nombre: 'Figma', nivel: 'Intermedio', logo: Figma },
          { nombre: 'VSCode', nivel: 'Avanzado', logo: VSCode }
        ],
        basesDatos: [
          { nombre: 'MongoDB', nivel: 'Avanzado', logo: MongoDB },
          { nombre: 'MySQL', nivel: 'Intermedio', logo: MySQL },
          { nombre: 'PostgreSQL', nivel: 'Intermedio', logo: PostgreSQL }
        ],
        idiomas: [
          { nombre: 'Español', nivel: 'Nativo', logo: Espanol },
          { nombre: 'Inglés', nivel: 'Avanzado (C1)', logo: Inglés },
          { nombre: 'Japones', nivel: 'Avanzado (C1)', logo:Japones }
        ]
      };
    }
  };
  </script>
  
  <style scoped>
.habilidades {
  display: inline-block;
  flex-direction: column;
  gap: 2rem;
}

section {
  margin-bottom: 1rem;
  padding: 1rem;
  background-size: cover;
  background-position: center;
  border-radius: 12px;
}

.lenguajes {
  background-image: url('@/assets/codigo2.jpg');
}

.frameworks {
  background-image: url('@/assets/frame1.jpg');
}

.herramientas {
  background-image: url('@/assets/pc.jpg');
}

.basesDatos {
  background-image: url('@/assets/basedatos1.jpg');
}

.idiomas {
  background-image: url('@/assets/mundi.jpg');
}

.habilidad {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  padding: 0.2rem;
  border: 1px solid #c91515;
  border-radius: 12px;
  box-shadow: 0 8px 12px rgba(12, 190, 104, 0.658);
  transition: transform 0.3s ease, opacity 0.3s ease;
  margin-bottom: 1rem;
  margin-right: 2rem;
  background-color: rgb(176, 5, 59);
}

.habilidad:hover {
  transform: scale(1.1);
  opacity: 2;
}

.logo {
  width: 40px;
  height: 40px;
}

p {
  margin: 0;
  font-size: 1rem;
  font-weight: 200;
  color: #f1f0f4;
  text-shadow: 2px 2px 3px rgba(0, 0, 0, 0.5);
}

@keyframes zoomIn {
  0% {
    transform: scale(0.8);
    opacity: 0;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

h2 {
  font-size: 3rem;
  font-weight: bold;
  color: #f7f6f2;
  text-align: center;
  margin-bottom: 1rem;
  transition: transform 0.9s ease;
  animation: zoomIn 3s ease;
}

h2:hover {
  transform: scale(1.1);
}
</style>
