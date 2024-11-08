<template>
  <div
    class="projects-container"
    :style="{ backgroundImage: `url(${backgroundImage})` }"
  >
    <div class="overlay-background"></div>
    <h2>Nuestros Proyectos</h2>
    <div class="projects-grid">
      <div
        class="project-card"
        v-for="(project, index) in projects"
        :key="index"
        @mouseover="hoverEffect(index, true)"
        @mouseleave="hoverEffect(index, false)"
      >
        <div class="background-frame"></div>
        <div
          class="project-content"
          :style="{ backgroundImage: `url(${project.image})` }"
        >
          <div class="overlay" :class="{ 'show-overlay': project.isHovered }">
            <h3 class="project-title">{{ project.title }}</h3>
            <div class="texto-oculto">{{ project.description }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import websiteImage from '@/assets/web2.png';
import gameImage from '@/assets/juego2.jpg';
import appImage from '@/assets/app3.jpg';
import backgroundProjects from '@/assets/fondoTec.jpg';

export default {
  name: 'ProyectosComponente',
  data() {
    return {
      backgroundImage: backgroundProjects,
      projects: [
        {
          title: 'Página Web Corporativa',
          description: 'Desarrollamos una página web para una empresa de Gestion Comercial.',
          image: websiteImage,
          isHovered: false
        },
        {
          title: 'Videojuego de Accion Belico',
          description: 'Un videojuego de accion Belico con gráficos en 3D.',
          image: gameImage,
          isHovered: false
        },
        {
          title: 'Aplicación Móvil',
          description: 'Una aplicación móvil para un e-commerce',
          image: appImage,
          isHovered: false
        }
      ]
    };
  },
  methods: {
    hoverEffect(index, state) {
      this.projects[index].isHovered = state;
    }
  }
};
</script>

<style scoped>
.projects-container {
  position: relative;
  text-align: center;
  padding: 50px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  color: rgb(255, 255, 255);
}

.project-title {
  font-size: 24px;
  color: #ffffff;
  font-weight: bold;
  text-shadow: 2px 2px 2px rgba(0, 0, 0, 5);
}

.overlay-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.1);
  z-index: 0;
  border-radius: 8px;
}

.projects-grid {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  z-index: 1;
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
  top: 10px;
  left: 10px;
  right: 10px;
  bottom: 10px;
  background-color: #82f375;
  z-index: 1;
  border-radius: 10px;
  box-shadow: 0 25px 15px rgba(3, 251, 102, 0.774);
}

.project-content {
  position: relative;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  z-index: 2;
  border-radius: 10px;
  transition: transform 0.3s ease;
}

.project-content:hover {
  transform: scale(1.05);
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(61, 190, 160, 0.6);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: rgb(249, 245, 245);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.show-overlay {
  opacity: 1;
}

.texto-oculto {
  margin-top: 10px;
  padding: 5px;
  background: rgba(15, 77, 11, 0.833);
  border-radius: 20px;
  transition: transform 0.3s ease;
}

.project-card:hover .texto-oculto {
  transform: translateY(10px);
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
