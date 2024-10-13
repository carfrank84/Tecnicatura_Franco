<script setup>
import { ref } from 'vue';

// Títulos y fechas de la experiencia
const titulo = 'Desarrollador Full Stack en Golden Bytes';
const fecha = 'Desde Enero 2022 / Julio 2024';

// Definición de las experiencias laborales
const experiencias = ref([
    { id: 1, src: '/src/assets/SP.svg', parrafo: 'Lideré un equipo de desarrollo en la creación de aplicaciones móviles que mejoraron la retención de usuarios en un 30% durante el primer año.' },
    { id: 2, src: '/src/assets/NJ.svg', parrafo: 'Desarrollé soluciones de software utilizando tecnologías como Vue.js y Node.js, logrando aumentar la eficiencia del proceso de desarrollo en un 40%.' },
    { id: 3, src: '/src/assets/DV.svg', parrafo: 'Implementé prácticas de DevOps que optimizaron el ciclo de vida del desarrollo, reduciendo el tiempo de entrega de proyectos en un 25%.' },
    { id: 4, src: '/src/assets/AI.svg', parrafo: 'Colaboré con equipos de diseño para crear interfaces de usuario intuitivas, resultando en una mejora del 20% en la satisfacción del cliente.' },
    { id: 5, src: '/src/assets/jenkins.svg', parrafo: 'Automatizé pruebas y despliegues continuos con herramientas como Jenkins, aumentando la calidad del software y reduciendo los errores en producción.' },
]);
</script>

<template>
    <div class="card">
        <h3 class="titulo">{{ titulo.toLocaleUpperCase() }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class="item" v-for="experiencia in experiencias" :key="experiencia.id">
                <img class="imagen-svg" :src="experiencia.src" width="45rem" :alt="experiencia.parrafo">
                <p>{{ experiencia.parrafo }}</p>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    padding: 2rem;
    background-color: rgb(28, 41, 52);
    border-radius: 15px;
}

.titulo {
    font-size: 1.5rem;
    color: coral;
}

.fecha {
    font-size: 1rem;
    color: burlywood;
    margin-bottom: 1rem;
}

.listado {
    display: flex;
    flex-direction: column;
}

.item {
    align-items: center;
    display: flex;
    padding: 1rem;
    gap: 1.5rem;
}
</style>
