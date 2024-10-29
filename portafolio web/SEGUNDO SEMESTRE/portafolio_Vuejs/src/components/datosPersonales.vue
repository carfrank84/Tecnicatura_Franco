<script setup>
const title = 'Knigths of the Algoritmo (K.O.T.A)';
const descripcion = 'Equipo de estudiantes de la Tecnicatura Universitaria en Programación de la UTN-San Rafael';
const residencia = 'San Rafael, Mendoza, Argentina';
const presentacion = 'Hola bienvenidos al portafolio web del equipo K.O.T.A, integrado por los alumnos : Maxi Montenegro - Franco Poblete.-';
const redesSociales = [
  { id: 1, name: 'linkedin', src: '/src/assets/linkedin_icon.svg', url: 'https://www.linkedin.com/in/jose-perez/' },
  { id: 2, name: 'Instagram', src: '/src/assets/instagram_icon.svg', url: 'https://www.instagram.com/joseperez/' },
  { id: 3, name: 'github', src: '/src/assets/github_icon.svg', url: '' },
  { id: 4, name: 'curriculum', src: '/src/assets/cv_resume_icon.svg', url: '' },
];
const telefono = '+54 9 2604-661061';
</script>

<template>
<section class="datos-personales">
    <div class="card">
      <h1>{{ title }}</h1>
      <h2>{{ descripcion }}</h2>
      <p>{{ presentacion }}</p>
      <ul class="container-lista">
        <li v-for="red in redesSociales" :key="red.id">
          <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
        </li>
      </ul>
      <h3>☎ Nuestro Teléfono: {{ telefono }}</h3>
      <h4>{{ residencia }}</h4>
    </div>
  </section>
</template>

<style scoped>
h1 {
  font-size: 2.5rem;
}

p {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.card {
  position: relative; /* Necesario para que el pseudo-elemento ::before se posicione dentro de .card */
  border-radius: 10px; /* Borde redondeado de la tarjeta */
  padding: 20px; /* Espacio interno de la tarjeta */
  margin: 10px; /* Espacio externo */
  text-align: center; /* Alinea el texto al centro */
  overflow: hidden; /* Asegura que el pseudo-elemento ::before no se salga de la tarjeta */
  color: white; /* Cambia el color del texto a blanco para mayor legibilidad */
}
.card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('/src/assets/FondoAzul.jpg'); /* Ruta de la imagen */
  background-size: cover;
  background-position: center;
  opacity: 0.9; /* Ajusta la opacidad según desees */
  z-index: -1;
  border-radius: 10px;
}

.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: center;
}

.icon-redsocial {
  align-items: center;
  background-color: rgba(240, 244, 248, 0.998);
  border-radius: 50%;
  padding: 2px;
  margin: 5px;
  box-shadow: 0 0 5px rgba(83, 104, 163, 0.934);
}

.icon-redsocial:hover {
  background-color: rgb(28, 41, 52);
  box-shadow: 0 0 5px rgba(107, 88, 88, 0.934);
}

h3 {
  font-size: 1.2rem;
  font-weight: 600;
}

</style>
