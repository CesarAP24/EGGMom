<template>
  <LoadingDraw />
  <div class="configuracion-container"></div>
</template>

<script>
import LoadingDraw from "@/components/LoadingDraw.vue";
export default {
  name: "VueConfiguracion",
  components: { LoadingDraw },
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
