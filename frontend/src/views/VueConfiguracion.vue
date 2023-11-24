<template>
  <div class="configuracion-container">
    h,piujh
    <GraficaLineas />
  </div>
</template>

<script>
import GraficaLineas from "@/components/GraficaLineas.vue";

export default {
  name: "VueConfiguracion",
  components: { GraficaLineas },
};
</script>

<style scoped>
.configuracion-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 90%;
}
</style>
