<template>
  <div class="ejemplares-container">
    <div class="GrupoFiltro">
      <label for="grupo">Filtrar por grupo:</label>
      <select v-model="SelectedGroup">
        <option v-for="grupo in Grupos" :key="grupo.id" :value="grupo.name">
          {{ grupo.name }}
        </option>
      </select>
    </div>
    <div class="cards">
      <CardInfo
        v-for="ejemplar in Ejemplares"
        :style="{
          display:
            SelectedGroup === ejemplar.group || !SelectedGroup
              ? 'flex'
              : 'none',
        }"
        :key="ejemplar.id"
        :id="ejemplar.id"
        :EjemplarName="ejemplar.name"
        :GroupName="ejemplar.group"
        :temperatura="ejemplar.temperatura"
        :humedad="ejemplar.humedad"
        :peligro="ejemplar.peligro"
        :peligroH="ejemplar.peligroH"
        :peligroT="ejemplar.peligroT"
        :showHideWindow="showHideWindow"
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
          peligroH: false,
          peligroT: false,
        },
        {
          id: 2,
          group: "Grupo 1",
          name: "Ejemplar 2",
          temperatura: 25,
          humedad: 50,
          peligro: true,
          peligroH: false,
          peligroT: true,
        },
        {
          id: 3,
          group: "Grupo 1",
          name: "Ejemplar 3",
          temperatura: 25,
          humedad: 50,
          peligro: true,
          peligroH: false,
          peligroT: true,
        },
        {
          id: 4,
          group: "Grupo 1",
          name: "Ejemplar 4",
          temperatura: 25,
          humedad: 50,
          peligro: true,
          peligroH: false,
          peligroT: true,
        },
        {
          id: 5,
          group: "Grupo 1",
          name: "Ejemplar 5",
          temperatura: 25,
          humedad: 50,
          peligro: true,
          peligroH: true,
          peligroT: true,
        },
        {
          id: 6,
          group: "Grupo 1",
          name: "Ejemplar 6",
          temperatura: 25,
          humedad: 50,
          peligro: true,
          peligroH: true,
          peligroT: false,
        },
        {
          id: 7,
          group: "Grupo 1",
          name: "Ejemplar 7",
          temperatura: 25,
          humedad: 50,
          peligro: true,
          peligroH: true,
          peligroT: false,
        },
        {
          id: 8,
          group: "Grupo 1",
          name: "Ejemplar 8",
          temperatura: 25,
          humedad: 50,
          peligro: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 9,
          group: "Grupo 1",
          name: "Ejemplar 9",
          temperatura: 25,
          humedad: 50,
          peligro: true,
          peligroH: true,
          peligroT: false,
        },
        // grupo 2
        {
          id: 10,
          group: "Grupo 2",
          name: "Ejemplar 10",
          temperatura: 25,
          humedad: 50,
          peligro: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 11,
          group: "Grupo 2",
          name: "Ejemplar 11",
          temperatura: 25,
          humedad: 50,
          peligro: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 12,
          group: "Grupo 2",
          name: "Ejemplar 12",
          temperatura: 25,
          humedad: 50,
          peligro: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 13,
          group: "Grupo 2",
          name: "Ejemplar 13",
          temperatura: 25,
          humedad: 50,
          peligro: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 14,
          group: "Grupo 2",
          name: "Ejemplar 14",
          temperatura: 25,
          humedad: 50,
          peligro: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 15,
          group: "Grupo 2",
          name: "Ejemplar 15",
          temperatura: 25,
          humedad: 50,
          peligro: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 16,
          group: "Grupo 2",
          name: "Ejemplar 16",
          temperatura: 25,
          humedad: 50,
          peligro: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 17,
          group: "Grupo 2",
          name: "Ejemplar 17",
          temperatura: 25,
          humedad: 50,
          peligror: false,
          peligroH: false,
          peligroT: false,
        },
        // grupo4
        {
          id: 18,
          group: "Grupo 4",
          name: "Ejemplar 18",
          temperatura: 25,
          humedad: 50,
          peligror: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 19,
          group: "Grupo 4",
          name: "Ejemplar 19",
          temperatura: 25,
          humedad: 50,
          peligror: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 20,
          group: "Grupo 4",
          name: "Ejemplar 20",
          temperatura: 25,
          humedad: 50,
          peligror: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 21,
          group: "Grupo 4",
          name: "Ejemplar 21",
          temperatura: 25,
          humedad: 50,
          peligror: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 22,
          group: "Grupo 4",
          name: "Ejemplar 22",
          temperatura: 25,
          humedad: 50,
          peligror: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 23,
          group: "Grupo 4",
          name: "Ejemplar 23",
          temperatura: 25,
          humedad: 50,
          peligror: false,
          peligroH: false,
          peligroT: false,
        },
        {
          id: 24,
          group: "Grupo 4",
          name: "Ejemplar 24",
          temperatura: 25,
          humedad: 50,
          peligror: false,
          peligroH: false,
          peligroT: false,
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
      SelectedGroup: "",
    };
  },
  props: {
    showHideWindow: Function,
  },
};
</script>

<style scoped>
.ejemplares-container {
  width: 95%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.GrupoFiltro {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  margin: 20px 0px 0px 0px;
  padding: 0px 40px;
}
.GrupoFiltro label {
  font-size: 20px;
  font-weight: 550;
  color: #333;
  margin-right: 10px;
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
}
</style>
