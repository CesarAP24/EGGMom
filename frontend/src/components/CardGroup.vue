<template>
  <div class="CardGroup">
    <h2>{{ groupName }}</h2>
    <div>
      <img src="https://via.placeholder.com/150" alt="peligro" />
    </div>
    <div class="info">
      <p>Temp: {{ temperaturaMin }} - {{ temperaturaMax }} °C</p>
      <p>Hum: {{ humedadMin }} - {{ humedadMax }} %</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardGroup",
  props: {
    groupName: String,
    temperaturaMin: Number,
    temperaturaMax: Number,
    humedadMin: Number,
    humedadMax: Number,
  },
};
</script>

<style scoped>
.CardGroup {
  width: 210x;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  background-color: #ffffff;
  padding: 0 25px;
  border-bottom: 1px solid #e0e0e0;
  margin-bottom: 20px;
  margin-left: 15px;
  margin-top: 15px;
  border: 1px solid black;
}
.CardGroup h2 {
  margin-top: 20px;
  margin-bottom: 20px;
}
.info {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 15px 0;
}
</style>
