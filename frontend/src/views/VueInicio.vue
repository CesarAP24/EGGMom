<template>
  <div class="inicio-container">
    <CardInfo
      v-for="ejemplar in Ejemplares"
      :key="ejemplar.id"
      :id="ejemplar.id"
      :GroupName="ejemplar.group"
      :EjemplarName="ejemplar.name"
      :temperatura="ejemplar.temperatura"
      :humedad="ejemplar.humedad"
      :peligro="ejemplar.peligro"
      :showHideWindow="showHideWindow"
    />
  </div>
</template>

<script>
import CardInfo from "@/components/CardInfo.vue";
export default {
  name: "VueInicio",
  components: { CardInfo },
  data() {
    return {
      Ejemplares: [],
    };
  },
  props: {
    showHideWindow: Function,
  },
};
</script>

<style scoped>
.inicio-container {
  width: 95%;
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-top: 30px;
  flex-wrap: wrap;
}
</style>
