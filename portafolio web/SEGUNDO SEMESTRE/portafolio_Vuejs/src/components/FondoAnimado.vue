<template>
    <div>
      <div class="square"></div>
      <div class="square"></div>
      <div class="square"></div>
      <div class="square"></div>
      <div class="square"></div>
      <div class="circle"></div>
      <div class="circle"></div>
      <div class="circle"></div>
      <div class="circle"></div>
      <div class="circle"></div>
      <div class="triangle"></div>
      <div class="triangle"></div>
      <div class="triangle"></div>
      <div class="triangle"></div>
      <div class="triangle"></div>
    </div>
  </template>
  
  <script>
  import anime from 'animejs'; 
  
  export default {
    name: 'AnimacionGeometrica',
    mounted() {
      this.randomValues();
    },
    methods: {
      randomValues() {
        anime({
          targets: '.square, .circle, .triangle',
          translateX: function () {
            return anime.random(-500, 500);
          },
          translateY: function () {
            return anime.random(-300, 300);
          },
          rotate: function () {
            return anime.random(0, 360);
          },
          scale: function () {
            return anime.random(0.2, 2);
          },
          duration: 3000,
          easing: 'easeInOutQuad',
          complete: this.randomValues, // Cambiar a this.randomValues para mantener el contexto
        });
      }
    }
  };
  </script>
  
  <style scoped>
  * {
    margin: 0;
    padding: 0;
  }
  
  body {
    background: #830707;
    overflow: hidden;
  }
  
  .square {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50px;
    height: 50px;
    background: linear-gradient(#e80404, #0c61ac);
    z-index: -5;
  }
  
  .circle {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50px;
    height: 50px;
    background: linear-gradient(#c027cee3,#0aa9e8d7 ) ;
    border-radius: 50%;
  }
  
  .triangle {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50px;
    height: 50px;
    background:linear-gradient(#2496b59f,#faf9f9f4, #2496b59f  ) ;
    clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
    -webkit-clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
  }
  </style>
  