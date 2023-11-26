<template>
  <div class="grupos-container">
    <div class="cards">
      <CardGroup
        v-for="grupo in grupos"
        :key="grupo.id"
        :groupName="grupo.name"
        :temperaturaMin="grupo.temperaturaMin"
        :temperaturaMax="grupo.temperaturaMax"
        :humedadMin="grupo.humedadMin"
        :humedadMax="grupo.humedadMax"
      />
    </div>
    <PantallaCarga v-if="cargando" />
    <!--form-->
    <div class="form">
      <h2>Crea un grupo:</h2>
      <form id="formulario-grupo-bonito">
        <div class="campos">
          <div class="campo">
            <label>Nombre: </label>
            <input
              type="text"
              name="nombre"
              id="name"
              placeholder="Nombre del grupo"
            />
          </div>
          <div class="campo">
            <label>Temp min: </label>
            <input
              type="text"
              placeholder="Temperatura mínima"
              name="temperatura_min"
              id="temperaturaMin"
            />
          </div>
          <div class="campo">
            <label>Temp max: </label>
            <input
              type="text"
              placeholder="Temperatura máxima"
              name="temperatura_max"
              id="temperaturaMax"
            />
          </div>
          <div class="campo">
            <label>Hum min: </label>
            <input
              type="text"
              placeholder="Humedad mínima"
              name="humedad_min"
              id="humedadMin"
            />
          </div>
          <div class="campo">
            <label>Hum max: </label>
            <input
              type="text"
              placeholder="Humedad máxima"
              name="humedad_max"
              id="humedadMax"
            />
          </div>
        </div>
        <p id="errorCrearGrupo"></p>
        <div class="boton">
          <button type="submit" @click="crearGrupo" id="btn-create-group">
            Crear
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import CardGroup from "@/components/CardGroup.vue";
import PantallaCarga from "@/components/PantallaCarga.vue";
export default {
  name: "VueGrupos",
  components: {
    CardGroup,
    PantallaCarga,
  },
  data() {
    return {
      grupos: [],
      cargando: false,
    };
  },
  props: {
    showHideWindow: Function,
    loadCookie: Function,
  },
  methods: {
    crearGrupo(e) {
      e.preventDefault();
      document.getElementById("errorCrearGrupo").innerHTML = "";

      let form = document.getElementById("formulario-grupo-bonito");
      form = new FormData(form);
      form = Object.fromEntries(form);
      console.log(form);
      //verificaciones
      if (
        form["nombre"] === "" ||
        form["temperatura_max"] === "" ||
        form["temperatura_min"] === "" ||
        form["humedad_max"] === "" ||
        form["humedad_min"] === ""
      ) {
        document.getElementById("errorCrearGrupo").innerHTML =
          "Llenar todos los campos";
        return;
      } else {
        if (form["temperatura_max"] != parseInt(form["temperatura_max"])) {
          document.getElementById("errorCrearGrupo").innerHTML =
            "Temperatura máxima debe ser un número";
          return;
        }
        if (form["temperatura_min"] != parseInt(form["temperatura_min"])) {
          document.getElementById("errorCrearGrupo").innerHTML =
            "Temperatura mínima debe ser un número";
          return;
        }
        if (form["humedad_max"] != parseInt(form["humedad_max"])) {
          document.getElementById("errorCrearGrupo").innerHTML =
            "Humedad máxima debe ser un número";
          return;
        }
        if (form["humedad_min"] != parseInt(form["humedad_min"])) {
          document.getElementById("errorCrearGrupo").innerHTML =
            "Humedad mínima debe ser un número";
          return;
        }
      }
      form = JSON.stringify(form);

      //poner boton disables
      const button = document.getElementById("btn-create-group");
      button.disabled = true;

      let empresa = this.loadCookie("empresa");
      let sede = this.loadCookie("token");

      fetch(
        "http://localhost:5000/empresa/" +
          empresa +
          "/sedes/" +
          sede +
          "/grupos",
        {
          method: "POST",
          body: form,
          headers: {
            "Content-Type": "application/json",
          },
        }
      )
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          button.disabled = false;
          this.grupos.push({
            id: data["data"]["grupo_id"],
            name: data["data"]["grupo_id"],
            temperaturaMin: data["data"]["temperatura"]["min"],
            temperaturaMax: data["data"]["temperatura"]["max"],
            humedadMin: data["data"]["humedad"]["min"],
            humedadMax: data["data"]["humedad"]["max"],
          });
          document.getElementById("errorCrearGrupo").innerHTML =
            "Grupo creado con éxito";
          //pausar 3 segundos
          setTimeout(() => {
            document.getElementById("errorCrearGrupo").innerHTML = "";
            //limpiar formulario
            document.getElementById("formulario-grupo-bonito").reset();
          }, 3000);
        })
        .catch((err) => {
          console.log(err);
          button.disabled = false;
          document.getElementById("errorCrearGrupo").innerHTML =
            "Error al crear el grupo";
        });
    },
    loadGroups(sede) {
      let empresa = this.loadCookie("empresa");
      fetch(
        "http://localhost:5000/empresa/" +
          empresa +
          "/sedes/" +
          sede +
          "/grupos"
      )
        .then((res) => res.json())
        .then((data) => {
          this.grupos = [];
          console.log(data);
          let grupos = data["data"];
          grupos.forEach((grupo) => {
            this.grupos.push({
              id: grupo["grupo_id"],
              name: grupo["grupo_id"],
              temperaturaMin: grupo["temperatura"]["min"],
              temperaturaMax: grupo["temperatura"]["max"],
              humedadMin: grupo["humedad"]["min"],
              humedadMax: grupo["humedad"]["max"],
            });
          });
          this.cargando = false;
        })
        .catch((err) => console.log(err));
    },
  },
  mounted() {
    let sede = this.loadCookie("token");
    this.cargando = true;
    this.loadGroups(sede);
  },
};
</script>

<style scoped>
#errorCrearGrupo {
  color: red;
  font-size: 15px;
  margin-left: 10px;
  margin-top: 10px;
}

.grupos-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  width: 100%;
}

#btn-create-group:disabled {
  background-color: #e0e0e0;
  color: #9e9e9e;
  border: 1px solid #e0e0e0;
  cursor: not-allowed;
}

.cards {
  display: flex;
  width: 95%;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  overflow-x: scroll;
  padding: 0 20px;
  margin: 0 20px;
  flex-wrap: nowrap;
}
.cards::-webkit-scrollbar {
  /*estilo minimalista moderno*/
  width: 5px;
  height: 5px;
  background-color: #f5f5f5;
}
.cards::-webkit-scrollbar-thumb {
  /*estilo barra*/
  border-radius: 10px;
  background-color: #ff6320;
}
.form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: baseline;
  width: 100%;
  border-radius: 10px;
  box-shadow: 0px 0px 30px 0px rgba(0, 0, 0, 0.03);
  padding: 30px 20px;
}
.form form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  width: 80%;
}

.campos {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  flex-wrap: wrap;
  width: 100%;
  margin-bottom: 0px;
  padding-left: 15px;
}

h2 {
  margin-left: 20px;
  margin-bottom: 20px;
}

.form form .campo {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin: 5px 10px;
  width: 30%;
}
.form form .campo input {
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  padding: 10px;
}
.form form .campo label {
  margin-right: 10px;
  font-size: 15px;
  font-weight: 500;
}
.input {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  margin: 10px;
}
.boton {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin: 10px;
  margin-top: 0px;
}
.boton button {
  margin-left: 12px;
  padding: 8px;
  border-radius: 5px;
  border: none;
  font-size: 15px;
  cursor: pointer;
  color: white;
  background-color: #ff6320;
  border: 1px solid #ff6320;
  transition: 0.3s;
  padding: 10px 30px;
  margin-top: 20px;
}

.boton button:hover {
  background-color: white;
  color: #ff6320;
  transition: 0.3s;
}
</style>
