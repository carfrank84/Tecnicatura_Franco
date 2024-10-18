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
  export default {
    data() {
      return {
        lenguajes: [
          { nombre: 'JavaScript', nivel: 'Avanzado', logo: 'src/assets/js.svg' },
          { nombre: 'Python', nivel: 'Intermedio', logo: 'src/assets/python.svg' },
          { nombre: 'HTML/CSS', nivel: 'Avanzado', logo: 'src/assets/html-css.svg' },
          { nombre: 'Java', nivel: 'Intermedio', logo: 'src/assets/java.svg' },
          { nombre: 'SQL', nivel: 'Intermedio', logo: 'src/assets/sql.svg' }
        ],
        frameworks: [
          { nombre: 'React.js', nivel: 'Avanzado', logo: 'src/assets/react.svg' },
          { nombre: 'Vue.js', nivel: 'Intermedio', logo: 'src/assets/vue.svg' },
          { nombre: 'Node.js', nivel: 'Avanzado', logo: 'src/assets/node.svg' },
          { nombre: 'Django', nivel: 'Intermedio', logo: 'src/assets/django.svg' },
          { nombre: 'Bootstrap', nivel: 'Avanzado', logo: 'src/assets/bootstrap.svg' }
        ],
        herramientas: [
          { nombre: 'Git', nivel: 'Avanzado', logo: 'src/assets/git.svg' },
          { nombre: 'Docker', nivel: 'Avanzado', logo: 'src/assets/docker.svg' },
          { nombre: 'Cypress', nivel: 'Intermedio', logo: 'src/assets/cypress.svg' },
          { nombre: 'Figma', nivel: 'Intermedio', logo: 'src/assets/figma.svg' },
          { nombre: 'VSCode', nivel: 'Avanzado', logo: 'src/assets/visual.svg' }
        ],
        basesDatos: [
          { nombre: 'MongoDB', nivel: 'Avanzado', logo: 'src/assets/mongo.svg' },
          { nombre: 'MySQL', nivel: 'Intermedio', logo: 'src/assets/mysql.svg' },
          { nombre: 'PostgreSQL', nivel: 'Intermedio', logo: 'src/assets/postgres.svg' }
        ],
        idiomas: [
          { nombre: 'Español', nivel: 'Nativo', logo: 'src/assets/arg.svg' },
          { nombre: 'Inglés', nivel: 'Avanzado (C1)', logo: 'src/assets/eeuu.svg' }
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
    background-image: url('src/assets/codigo.jpg');
  }
  
  .frameworks {
    background-image: url('src/assets/frame.jpg');
  }
  
  .herramientas {
    background-image: url('src/assets/herramientas.jpg');
  }
  
  .basesDatos {
    background-image: url('src/assets/basedatos.jpeg');
  }
  
  .idiomas {
    background-image: url('src/assets/mundo.jpg');
  }
  
  .habilidad {
    display: inline-flex;
    align-items: center;
    gap: 1rem;
    padding: 0.2rem;
    border: 1px solid #c91515;
    border-radius: 12px;
    box-shadow: 0 8px 12px rgba(12, 12, 190, 0.658);
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
  font-size: 1rem; /* Aumenta el tamaño de la fuente */
  font-weight: 200; /* Cambia el peso de la fuente */
  color: #f1f0f4; /* Cambia el color del texto */
  text-shadow: 2px 2px 3px rgba(0, 0, 0, 0.5); /* Añade una sombra sutil */
  }
  @keyframes zoomIn {
  0% {
    transform: scale(0.8); /* Inicia más pequeño */
    opacity: 0; /* Comienza invisible */
  }
  100% {
    transform: scale(1); /* Termina al tamaño normal */
    opacity: 1; /* Termina visible */
  }
}
  h2 {
  font-size: 3rem; /* Ajusta el tamaño de la fuente */
  font-weight: bold; /* Peso de la fuente */
  color: #f7f6f2; /* Cambia el color del texto */
  text-align: center; /* Centrar el texto */
  margin-bottom: 1rem; /* Espacio debajo del título */
  transition: transform 0.9s ease; /* Transición para la animación */
  animation: zoomIn 3s ease; /* Aplica la animación */
}
h2:hover {
  transform: scale(1.1); /* Aumentar el tamaño al pasar el cursor */
}
  </style>
  