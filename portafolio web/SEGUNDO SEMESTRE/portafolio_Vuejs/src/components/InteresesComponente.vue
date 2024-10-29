<script setup>
import { ref } from 'vue';
import FondoAnimado from './FondoAnimado.vue';
//Este es un arreglo con ref para que se pueda reactivar el cambio de los intereses
const intereses = ref([
    'Desarrollo de Software de Código Abierto: Contribuimos a proyectos en GitHub, colaborando con otros desarrolladores para mejorar herramientas y librerías populares, sobre todo en el desarrollo de video juegos.',
    'Deportes al Aire Libre: Disfrutamos del deporte y el ciclismo , actividades que practicamos regularmente para mantener un equilibrio entre el trabajo y la vida personal.',
    'Tecnología de Innovación: Nos apasiona el mundo Tec, sobre todo en el desarrollo de nuevas aplicaciones, inovacion tecnologica dentro del mercado , y ver las nuevas tendencias en lo referido al mundo de los video juegos .',
    'Música: Practicamos la musica  como un hobby, y de manera profesional, lo que nos ayuda tener una mente creativa , conectada con el arte y sobre todo el poder de conjugar la miusica con la tecnologia , esto es fundamental para crear una soimbiosis de ambos mundos.'
]);
</script>

<template>
    <div class="intereses-contenedor">
        <FondoAnimado/>
        <ul class="contenedor-lista">
            <li class="item" v-for="interes in intereses" :key="interes">
                {{ interes }}
            </li>
        </ul>
    </div>
    
</template>

<style scoped>
.intereses-contenedor {
    display: flex;
    position: relative;
    margin: 0 auto;
    max-width: 85%;
    padding: 1rem;
}

.contenedor-lista {
    list-style-type: none;
    padding: 1rem;
    margin-bottom: .5rem;
    color: var(--vt-c-white-soft);
    font-size: 1.4rem;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 1);
    text-align: justify;
}

.item {
    margin-bottom: 1rem;
}
</style>