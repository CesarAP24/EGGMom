<template>
  <div class="peligros-container">
    <CardInfo
      v-for="ejemplar in Ejemplares"
      :key="ejemplar.id"
      :id="ejemplar.id"
      :EjemplarName="ejemplar.name"
      :GroupName="ejemplar.group"
      :showHideWindow="showHideWindow"
      :loadCookie="loadCookie"
      :tempMax="ejemplar.tempMax"
      :tempMin="ejemplar.tempMin"
      :humMax="ejemplar.humMax"
      :humMin="ejemplar.humMin"
      :hideIfSecure="ejemplar.hideIfSecure"
    />
    <PantallaCarga v-if="cargando" />
  </div>
</template>

<script>
import CardInfo from "@/components/CardInfo.vue";
import PantallaCarga from "@/components/PantallaCarga.vue";
export default {
  name: "VuePeligros",
  components: {
    CardInfo,
    PantallaCarga,
  },
  data() {
    return {
      Ejemplares: [],
      cargando: false,
    };
  },
  props: {
    showHideWindow: Function,
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
                    hideIfSecure: true,
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
.peligros-container {
  width: 95%;
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-top: 30px;
  flex-wrap: wrap;
}
</style>
