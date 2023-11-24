<template>
  <div :class="'CardInfo' + (peligro ? ' peligro' : '')">
    <div class="TopContent">
      <h2>{{ GroupName }}</h2>
      <div>
        <img src="../assets/peligro.svg" alt="peligro" width="19" />
      </div>
    </div>
    <div class="CenterContent">
      <div class="ImageGroup">
        <img src="https://via.placeholder.com/150" alt="peligro" />
      </div>
      <div class="EjemplarName">
        <p>{{ EjemplarName }}</p>
      </div>
    </div>
    <div class="BottomContent">
      <p class="temperatura">Temperatura: {{ temperatura }} °C</p>
      <p class="humedad">Humedad: {{ humedad }} %</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardInfo",
  props: {
    GroupName: String,
    EjemplarName: String,
    temperatura: Number,
    humedad: Number,
    peligro: Boolean,
  },
};
</script>

<style scoped>
.CardInfo {
  width: 210px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  background-color: #ffffff;
  padding: 0 25px;
  border-bottom: 1px solid #e0e0e0;
  margin-bottom: 20px;
  margin-left: 15px;
  border: 1px solid black;
}

.TopContent {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 5px 0;
}

.CenterContent {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 1px solid #e0e0e0;
  padding-top: 3px;
}

.EjemplarName {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border-top: 1px solid #e0e0e0;
  padding: 5px 0;
}

.BottomContent {
  width: 100%;
  display: flex;
  padding: 20px 0;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}

.peligro .TopContent img {
  background-color: #000000;
  height: 25px;
  width: 25px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.peligro {
  background-color: #ffebeb;
}
</style>
