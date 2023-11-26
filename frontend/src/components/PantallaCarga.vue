<template>
  <div class="carga-container">
    <div class="carga">
      <div class="carga-icono">
        <img src="../assets/circulo.svg" alt="circulo" />
      </div>
    </div>
  </div>
</template>

<script scoped>
export default {
  name: "VueGrupos",
};
</script>

<style scoped>
.carga-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 618px;
  overflow: hidden;
  background-color: rgba(0, 0, 0, 0.7);
}
.carga-icono {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: baseline;
}
.carga-icono img {
  width: 40px;
  height: 100px;
  animation: rotar 1.5s linear infinite;
}

@keyframes rotar {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
