<script setup>
import { ref } from 'vue';
import SP from '/src/assets/SP.svg'
import NJ from '/src/assets/NJ.svg'
import DV from '/src/assets/DV.svg'
import AI from '/src/assets/AI.svg'
import jenkins from '/src/assets/jenkins.svg'



// Títulos y fechas de la experiencia
const titulo = 'Desarrollador Full Stack ';
const fecha = 'Desde Enero 2022 / Julio 2024';

// Definición de las experiencias laborales
const experiencias = ref([
    { id: 1, src: SP, parrafo: 'Lidere un equipo de desarrollo en la creación de aplicaciones móviles que mejoraron la retención de usuarios en un 30% durante el primer año.' },
    { id: 2, src: NJ, parrafo: 'Desarrolle soluciones de software utilizando tecnologías como Vue.js y Node.js, logrando aumentar la eficiencia del proceso de desarrollo en un 40%.' },
    { id: 3, src: DV, parrafo: 'Implemente prácticas de DevOps que optimizaron el ciclo de vida del desarrollo, reduciendo el tiempo de entrega de proyectos en un 25%.' },
    { id: 4, src: AI, parrafo: 'Colaboro con equipos de diseño para crear interfaces de usuario intuitivas, resultando en una mejora del 20% en la satisfacción del cliente.' },
    { id: 5, src: jenkins, parrafo: 'Automatizo pruebas y despliegues continuos con herramientas como Jenkins, aumentando la calidad del software y reduciendo los errores en producción.' },
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
    background-image: url('/src/assets/fondoCard.jpg'); /* Reemplaza con tu ruta */
    background-size: cover;
    background-position: center;
    border-radius: 15px;
}


.titulo {
    font-size: 1.5rem;
    color: rgb(202, 244, 201);
    
}

.fecha {
    font-size: 1rem;
    color: rgb(246, 248, 244);
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
