<template>
  <div class="inicio-container">
    <div class="card">
      <h1>Inicio</h1>
      <br />
      <p>
        Bienvenido a la aplicación de control de temperatura y humedad de
        ejemplares. En esta aplicación podrás ver los ejemplares que se están
        monitoreando en tiempo real, así como también podrás ver los ejemplares
        que se encuentran en peligro.
      </p>
      <div class="dashboard">
        <h3>Recordatorio:</h3>
        <div class="container-tutorial-cards">
          <div class="subContainer-cards">
            <h4>Esto es una carta en peligro</h4>
            <CardInfo
              id="1"
              GroupName="Grupo 1"
              EjemplarName="Ejemplar 1"
              tempMax="30"
              tempMin="20"
              humMax="50"
              humMin="30"
              forcePeligro="true"
              NoLoadData="true"
            />
          </div>
          <div class="subContainer-cards">
            <h4>Esto es una carta en seguridad</h4>
            <CardInfo
              id="1"
              GroupName="Grupo 1"
              EjemplarName="Ejemplar 1"
              tempMax="30"
              tempMin="20"
              humMax="50"
              humMin="30"
              NoLoadData="true"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CardInfo from "@/components/CardInfo.vue";
export default {
  name: "VueInicio",
  components: { CardInfo },
};
</script>

<style scoped>
.inicio-container {
  width: 100%;
  background-color: #f5f5f5;
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 30px;
  flex-wrap: wrap;
}

.card {
  width: 95%;
  display: flex;
  flex-direction: column;
  border-radius: 10px;
  background-color: #f5f5f5;
}

.dashboard {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 20px;
  border-radius: 10px;
  background-color: #f5f5f5;
}

.dashboard h3 {
  margin-top: 20px;
  font-size: 1.5rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 10px;
}

.container-tutorial-cards {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  flex-wrap: nowrap;
}

.subContainer-cards {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px 0px;
  flex-wrap: nowrap;
  padding: 20px 20px 0 20px;
  border: 1px solid rgba(1, 1, 1, 0);
  transition: all 0.3s ease-in-out;
}

.subContainer-cards:hover {
  /*animacion de agitamiento*/
  background-color: #fff;
  border: 1px solid #ff6320;
  border-radius: 10px;
  transition: all 0.3s ease-in-out;
  transform: scale(1.05);
}

.subContainer-cards h4 {
  font-size: 1.2rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 30px;
}
</style>
