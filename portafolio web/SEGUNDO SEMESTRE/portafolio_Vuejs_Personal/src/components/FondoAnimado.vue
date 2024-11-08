<template>
  <div class="wave-background">
    <canvas ref="canvas" class="wave-canvas"></canvas>
  </div>
</template>

<script>
export default {
  name: 'FondoOndasMultiples',
  mounted() {
    this.createWaves();
  },
  methods: {
    createWaves() {
      const canvas = this.$refs.canvas;
      const ctx = canvas.getContext('2d');
      let width = canvas.width = window.innerWidth;
      let height = canvas.height = window.innerHeight;

      window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
      });

      const waves = [
        { y: height / 2, length: 0.02, amplitude: 100, frequency: 0.02, color: 'rgba(255, 215, 0, 0.5)' },
        { y: height / 2.5, length: 0.015, amplitude: 80, frequency: 0.015, color: 'rgba(255, 165, 0, 0.4)' },
        { y: height / 1.8, length: 0.025, amplitude: 120, frequency: 0.025, color: 'rgba(255, 255, 0, 0.3)' }
      ];

      let increment = 0;

      function animate() {
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = '#000'; // Fondo negro (puedes cambiarlo)
        ctx.fillRect(0, 0, width, height);

        waves.forEach(wave => {
          ctx.beginPath();
          ctx.moveTo(0, wave.y);
          for (let i = 0; i < width; i++) {
            ctx.lineTo(i, wave.y + Math.sin(i * wave.length + increment) * wave.amplitude * Math.cos(increment));
          }
          ctx.strokeStyle = wave.color;
          ctx.stroke();
        });

        increment += 0.02;
        requestAnimationFrame(animate);
      }

      animate();
    }
  }
};
</script>

<style scoped>
.wave-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.wave-canvas {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}
</style>
