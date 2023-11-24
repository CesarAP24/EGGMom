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
    <!--form-->
    <div class="form">
      <h2>Crea un grupo:</h2>
      <form action="">
        <div class="campos">
          <div class="campo">
            <label>Nombre: </label>
            <input
              type="text"
              name="name"
              id="name"
              placeholder="Nombre del grupo"
            />
          </div>
          <div class="campo">
            <label>Temp min: </label>
            <input
              type="text"
              placeholder="Temperatura mínima"
              name="temperaturaMin"
              id="temperaturaMin"
            />
          </div>
          <div class="campo">
            <label>Temp max: </label>
            <input
              type="text"
              placeholder="Temperatura máxima"
              name="temperaturaMax"
              id="temperaturaMax"
            />
          </div>
          <div class="campo">
            <label>Hum min: </label>
            <input
              type="text"
              placeholder="Humedad mínima"
              name="humedadMin"
              id="humedadMin"
            />
          </div>
          <div class="campo">
            <label>Hum max: </label>
            <input
              type="text"
              placeholder="Humedad máxima"
              name="humedadMax"
              id="humedadMax"
            />
          </div>
        </div>
        <div class="boton">
          <button type="submit">Crear</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import CardGroup from "@/components/CardGroup.vue";
export default {
  name: "VueGrupos",
  components: { CardGroup },
  data() {
    return {
      grupos: [
        {
          id: 1,
          name: "Grupo 1",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 2,
          name: "Grupo 2",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 3,
          name: "Grupo 3",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 4,
          name: "Grupo 4",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 5,
          name: "Grupo 5",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 6,
          name: "Grupo 6",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 7,
          name: "Grupo 7",
          temperaturaMin: 20,
          temperaturaMax: 30,
          humedadMin: 40,
          humedadMax: 60,
        },
        {
          id: 8,
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
.grupos-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  width: 100%;
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
