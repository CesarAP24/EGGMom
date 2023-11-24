<template>
  <div class="inicio-container">
    <CardInfo
      v-for="ejemplar in Ejemplares"
      :key="ejemplar.id"
      :GroupName="ejemplar.group"
      :EjemplarName="ejemplar.name"
      :temperatura="ejemplar.temperatura"
      :humedad="ejemplar.humedad"
      :peligro="ejemplar.peligro"
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
      Ejemplares: [
        {
          id: 1,
          group: "Grupo 1",
          name: "Ejemplar 1",
          temperatura: 25,
          humedad: 50,
          peligro: true,
        },
        {
          id: 2,
          group: "Grupo 1",
          name: "Ejemplar 2",
          temperatura: 25,
          humedad: 50,
          peligro: true,
        },
        {
          id: 3,
          group: "Grupo 1",
          name: "Ejemplar 3",
          temperatura: 25,
          humedad: 50,
          peligro: true,
        },
        {
          id: 4,
          group: "Grupo 1",
          name: "Ejemplar 4",
          temperatura: 25,
          humedad: 50,
          peligro: true,
        },
        {
          id: 5,
          group: "Grupo 1",
          name: "Ejemplar 5",
          temperatura: 25,
          humedad: 50,
          peligro: true,
        },
      ],
    };
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
