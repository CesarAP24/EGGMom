<template>
  <div class="ejemplares-container">
    <div class="GrupoFiltro">
      <label for="grupo">Filtrar por grupo:</label>
      <select v-model="SelectedGroup">
        <option v-for="grupo in Grupos" :key="grupo.id" :value="grupo.name">
          {{ grupo.name }}
        </option>
      </select>
      <button @click="showCrearEjemplar()" id="crear-ejemplar">
        Crear Ejemplar
      </button>
    </div>
    <PantallaCarga v-if="cargando" />
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
        :tempMax="ejemplar.tempMax"
        :tempMin="ejemplar.tempMin"
        :humMax="ejemplar.humMax"
        :humMin="ejemplar.humMin"
        :showHideWindow="showHideWindow"
        :loadCookie="loadCookie"
      />
    </div>
  </div>
</template>

<script>
import CardInfo from "@/components/CardInfo.vue";
import PantallaCarga from "@/components/PantallaCarga.vue";
export default {
  name: "VueEjemplares",
  components: { CardInfo, PantallaCarga },
  data() {
    return {
      Ejemplares: [],
      Grupos: [],
      SelectedGroup: "",
      cargando: false,
    };
  },
  props: {
    showHideWindow: Function,
    showCrearEjemplar: Function,
    loadCookie: Function,
  },
  methods: {
    loadEjemplares(sede) {
      let empresa = this.loadCookie("empresa");
      fetch(
        "http://localhost:5000/empresa/" +
          empresa +
          "/sedes/" +
          sede +
          "/grupos"
      )
        .then((response) => response.json())
        .then((data) => {
          this.Grupos = [];
          this.Ejemplares = [];
          let grupos = data["data"];
          grupos.forEach((grupo) => {
            //llenar la lista Grupos
            this.Grupos.push({
              id: grupo["grupo_id"],
              name: grupo["grupo_id"],
            });
            //fetch de ejemplares(objeto) por cada grupo
            fetch(
              "http://localhost:5000/empresa/" +
                empresa +
                "/sedes/" +
                sede +
                "/grupos/" +
                grupo["grupo_id"] +
                "/objetos"
            )
              .then((response) => response.json())
              .then((data) => {
                let ejemplares = data["data"];
                console.log(grupo);
                ejemplares.forEach((ejemplar) => {
                  this.Ejemplares.push({
                    id: ejemplar["objeto_id"],
                    group: grupo["grupo_id"],
                    name: ejemplar["objeto_id"],
                    tempMax: grupo["temperatura"]["max"],
                    tempMin: grupo["temperatura"]["min"],
                    humMax: grupo["humedad"]["max"],
                    humMin: grupo["humedad"]["min"],
                  });
                });
                this.cargando = false;
              })
              .catch((err) => console.log(err));
          });
        });
    },
  },
  mounted() {
    let sede = this.loadCookie("token");
    this.cargando = true;
    this.loadEjemplares(sede);
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

#crear-ejemplar {
  width: 15%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #e0e0e0;
  font-size: 16px;
  font-weight: 550;
  color: #333;
  background-color: #fff;
  cursor: pointer;
  transition: 0.3s;
  margin-left: 20px;
}

#crear-ejemplar:hover {
  background-color: #ff6320;
  color: #fff;
}

@media (max-width: 768px) {
  .GrupoFiltro {
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 20px;
  }
  .GrupoFiltro label {
    margin-bottom: 10px;
  }
  select {
    width: 100%;
    margin-bottom: 20px;
  }
  #crear-ejemplar {
    width: 100%;
    margin-left: 0px;
  }
}
</style>
