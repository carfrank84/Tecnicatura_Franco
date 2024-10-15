<template>
  <div
    class="projects-container"
    :style="{ backgroundImage: `url(${backgroundImage})` }"
  >
    <div class="overlay-background"></div> <!-- Superposición opcional para mejorar legibilidad -->
    <h2>Nuestros Proyectos</h2>
    <div class="projects-grid">
      <div
        class="project-card"
        v-for="(project, index) in projects"
        :key="index"
        @mouseover="hoverEffect(index, true)"
        @mouseleave="hoverEffect(index, false)"
      >
        <!-- Fondo adicional detrás del proyecto -->
        <div class="background-frame"></div>

        <!-- Contenido del proyecto con imagen de fondo -->
        <div class="project-content" :style="{ backgroundImage: `url(${project.image})` }">
          <div class="overlay" :class="{ 'show-overlay': project.isHovered }">
            <h3 class="project-title">{{ project.title }}</h3>
            <div class="texto-oculto">{{ project.description }}</div> <!-- Texto oculto -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Importa las imágenes de los proyectos
import websiteImage from '@/assets/web.jpg';
import gameImage from '@/assets/juego.jpg';
import appImage from '@/assets/app.jpg';

// Importa la imagen de fondo
import backgroundProjects from '@/assets/fondo.jpg';

export default {
  name: 'ProyectosComponente',
  data() {
    return {
      backgroundImage: backgroundProjects, // Imagen de fondo del contenedor
      projects: [
        {
          title: 'Página Web Corporativa',
          description: 'Desarrollamos una página web para una empresa de Producciones Musicales.',
          image: websiteImage,
          isHovered: false
        },
        {
          title: 'Videojuego de Aventura',
          description: 'Un videojuego de aventuras con gráficos en 3D.',
          image: gameImage,
          isHovered: false
        },
        {
          title: 'Aplicación Móvil',
          description: 'Una aplicación móvil para gestionar un E-commerce.',
          image: appImage,
          isHovered: false
        }
        // Puedes añadir más proyectos aquí
      ]
    };
  },
  methods: {
    /**
     * Maneja el efecto de hover en las tarjetas de proyecto.
     * @param {Number} index - Índice del proyecto en el array.
     * @param {Boolean} state - Estado del hover (true para entrar, false para salir).
     */
    hoverEffect(index, state) {
      this.projects[index].isHovered = state;
    }
  }
};
</script>

<style scoped>
.projects-container {
  position: relative; /* Necesario para posicionar la superposición */
  text-align: center;
  padding: 50px;
  background-size: cover; /* Asegura que la imagen cubra todo el contenedor */
  background-position: center; /* Centra la imagen */
  background-repeat: no-repeat; /* Evita que la imagen se repita */
  color: rgb(255, 255, 255); /* Cambia el color del texto si es necesario */
}
.project-title {
  font-size: 24px; /* Cambia el tamaño del texto */
  color: #ffffff; /* Cambia el color del texto a dorado, por ejemplo */
  font-weight: bold; /* Cambia el grosor de la fuente */
  text-shadow: 2px 2px 2px rgba(0, 0, 0, 5); /* Sombra para resaltar el texto */
}

/* Superposición para mejorar la legibilidad */
.overlay-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.1); /* Ajusta la opacidad según necesites */
  z-index: 0; /* Coloca la superposición detrás del contenido */
  border-radius: 8px;
}

.projects-grid {
  position: relative; /* Para asegurar que esté encima de la superposición */
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  z-index: 1; /* Asegura que las tarjetas estén encima de la superposición */
}

.project-card {
  position: relative;
  width: 320px;
  height: 220px;
  margin: 20px;
  cursor: pointer;
  perspective: 1000px;
}

.background-frame {
  position: absolute;
  top: 10px; /* Espacio para hacer el efecto de fondo detrás */
  left: 10px;
  right: 10px;
  bottom: 10px;
  background-color: #2c3e50; /* Color de fondo detrás del proyecto */
  z-index: 1; /* Asegura que esté detrás del contenido */
  border-radius: 10px;
  box-shadow: 0 25px 15px rgba(3, 197, 251, 0.774); /* Sombra para efecto 3D */
}

.project-content {
  position: relative;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  z-index: 2; /* Asegura que el contenido esté encima del fondo */
  border-radius: 10px;
  transition: transform 0.3s ease;
}

.project-content:hover {
  transform: scale(1.05);
}

.overlay {
  position: absolute;
  top: 0;
  left: 1;
  width: 100%;
  height: 100%;
  background-color: rgba(61, 132, 190, 0.6);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: rgb(249, 245, 245);
  opacity: 0;
  transition: opacity 0.3s ease;
  animation: fadeIn 0.s ease forwards;
}

.show-overlay {
  opacity: 1;
  animation: fadeIn 0.3s ease forwards;
}

.texto-oculto {
  display: none; /* Oculta el texto por defecto */
  position: absolute;
  bottom: 5px; /* Ajusta margen inferior del boton */
  left: 10px; /* Ajusta margen izquierdo del boton */
  right: 10px;/*Ajusta margen derecho del boton*/ 
  background: rgba(6, 6, 88, 0.833); /* Fondo semitransparente */
  padding: 5px;/* Ajusta el ancho del boton*/
  border-radius: 20px;/* Ajusta los bordes del boton*/
}

.project-card:hover .texto-oculto {
  display: block; /* Muestra el texto al pasar el cursor */
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsividad para pantallas pequeñas */
@media (max-width: 768px) {
  .projects-grid {
    flex-direction: column;
    align-items: center;
  }

  .project-card {
    width: 90%;
    height: 180px;
  }
}
</style>
