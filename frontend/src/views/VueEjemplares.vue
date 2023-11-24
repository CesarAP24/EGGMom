<template>
  <div class="ejemplares-container">
    <div class="GrupoFiltro">
      <select>
        <option v-for="grupo in Grupos" :key="grupo.id" :value="grupo.name">
          {{ grupo.name }}
        </option>
      </select>
    </div>
    <div class="cards">
      <CardInfo
        v-for="ejemplar in Ejemplares"
        :key="ejemplar.id"
        :EjemplarName="ejemplar.name"
        :GroupName="ejemplar.group"
        :temperatura="ejemplar.temperatura"
        :humedad="ejemplar.humedad"
        :peligro="ejemplar.peligro"
      />
    </div>
  </div>
</template>

<script>
import CardInfo from "@/components/CardInfo.vue";
export default {
  name: "VueEjemplares",
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
          peligro: false,
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
        {
          id: 6,
          group: "Grupo 1",
          name: "Ejemplar 6",
          temperatura: 25,
          humedad: 50,
          peligro: true,
        },
        {
          id: 7,
          group: "Grupo 1",
          name: "Ejemplar 7",
          temperatura: 25,
          humedad: 50,
          peligro: true,
        },
        {
          id: 8,
          group: "Grupo 1",
          name: "Ejemplar 8",
          temperatura: 25,
          humedad: 50,
          peligro: true,
        },
        {
          id: 9,
          group: "Grupo 1",
          name: "Ejemplar 9",
          temperatura: 25,
          humedad: 50,
          peligro: true,
        },
      ],
      Grupos: [
        {
          id: 10,
          name: "Grupo 1",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 20,
          name: "Grupo 2",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 30,
          name: "Grupo 3",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 40,
          name: "Grupo 4",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 50,
          name: "Grupo 5",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 60,
          name: "Grupo 6",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 70,
          name: "Grupo 7",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 80,
          name: "Grupo 8",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
      ],
    };
  },
};
</script>

<style scoped>
.ejemplares-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 20px;
}
.GrupoFiltro {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  margin: 20px 0px;
  padding: 0px 16px;
}
select {
  width: 15%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #e0e0e0;
  font-size: 16px;
  font-weight: 550;
  color: #333;
}
.cards {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-top: 30px;
  flex-wrap: wrap;
  padding: 0px 50px;
}
</style>
