<template>
  <div class="CardGroup" @click="goToGroup">
    <h2>{{ groupName }}</h2>
    <div>
      <img src="../assets/defaultGruposp.png" alt="peligro" />
    </div>
    <div class="info">
      <li>
        <p>Temperatura(°C)</p>
        <p>[{{ temperaturaMin }} - {{ temperaturaMax }}]</p>
      </li>
      <li>
        <p>Humedad (%)</p>
        <p>[{{ humedadMin }} - {{ humedadMax }}]</p>
      </li>
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
  methods: {
    goToGroup() {
      this.$router.push({
        name: "ejemplares",
      });
    },
  },
};
</script>

<style scoped>
.CardGroup {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  margin: 20px 10px;
  border-radius: 5px;
  border: 1px solid rgba(0, 0, 0, 0);
  transition: 0.3s;
}

.CardGroup:hover {
  border: 1px solid #e0e0e0;
  background-color: #f5f5f5;
  transition: 0.3s;
}

.CardGroup img {
  width: 150px;
  margin: 20px 15px;
  height: 150px;
  border-radius: 5px;
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

.CardGroup .info {
  display: flex;
  width: 100%;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 15px 0;
}

.CardGroup .info li {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: space-between;
  justify-content: space-between;
  width: 100%;
  margin: 5px 0;
}

.CardGroup .info li p {
  font-size: 12px;
  font-weight: 550;
  color: #333;
  margin-right: 10px;
}
</style>
