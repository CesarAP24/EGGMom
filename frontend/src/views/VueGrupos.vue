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
  width: 100%;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  overflow-x: scroll;
}
.form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: baseline;
  margin: 40px 20px 20px 50px;
  background-color: rgb(255, 251, 234);
  border-radius: 10px;
  box-shadow: 0px 0px 30px 0px rgba(0, 0, 0, 0.03);
  padding: 30px 20px;
}
.form form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  width: 100%;
}

.campos {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 0px;
}

h2 {
  margin-left: 20px;
}

.form form .campo {
  display: flex;
  flex-direction: column;
  margin: 15px;
}
.form form .campo input {
  margin-bottom: 20px;
  padding: 7px;
  border: 1px solid #002290;
  border-radius: 5px;
  margin: 5px;
}
.form form .campo label {
  margin-left: 8px;
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
  background-color: rgb(17, 210, 146);
  width: 80px;
}
</style>
