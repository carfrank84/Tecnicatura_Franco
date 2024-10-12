<template>
    <nav class="navbar">
    <div class="navbar-menu">
      <ul>
       <a v-for="nav in navegacion" :key="nav.nombre" href="nav.enlace" class="nav-item">{{ nav.nombre }}</a>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import {ref} from 'vue';
const navegacion= ref([
    {id:1, nombre: 'Educacion', enlace: '#educacion'},
    {id:2, nombre: 'Experiencia', enlace: '#experiencia'},
    {id:3, nombre: 'Proyectos', enlace: '#proyectos'},
    {id:4, nombre: 'Habilidades', enlace: '#habilidades'},
    {id:5, nombre: 'Intereses', enlace: '#intereses'},
])
</script>

<style scoped>
.navbar {
  background-color:var(--vt-c-indigo);
  color: #fff;
  padding: 0.5rem 1rem;
  align-items: center;
}
.navbar-item {
  color: #fff;
  text-decoration: none;
  margin-right: 1rem;
}
.navbar-menu {
  display: flex;
  justify-content: flex-end;
}
.nav-list {
  list-style: none;
}
a {
    border: 1px solid;
    border-color: hsla(60, 10%, 96%, 0.886);
    border-radius: 5px;
    /*elimina el subrrayado de los enlaces y elementos con "clase green"*/
    text-decoration: none;
    /* añade una transicion suave para los cambios de estilo*/
    transition: 0.4s;
    /* añade padding al rededor del contenido*/
    padding: 5px;
}

a:hover {
    /* cambia el color del fondo al pasar el mouse sobre un enlace */
    background-color: hsla(53, 100%, 2%, 0.721);
}
@media (max-whidth: 768px) {
    .navbar-menu {
    display: flex;
    justify-content: flex-end;
    width: 100%;    
    }
}
</style>