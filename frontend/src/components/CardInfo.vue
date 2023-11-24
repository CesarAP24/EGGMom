<template>
  <div :class="'CardInfo' + (peligro ? ' peligro' : '')">
    <div class="TopContent">
      <h2>{{ EjemplarName }}</h2>
      <div :style="'display: ' + (peligro ? 'flex' : 'none')">
        <img src="../assets/peligro.svg" alt="peligro" width="19" />
      </div>
    </div>
    <div class="SupContent">
      <div class="CenterContent">
        <div class="ImageGroup">
          <img src="https://via.placeholder.com/150" alt="peligro" />
        </div>
      </div>
      <div class="BottomContent">
        <li class="temperatura">
          <p>Temperatura:</p>
          <p :class="peligroT ? ' danger' : ''">{{ temperatura }} °C</p>
        </li>
        <li class="humedad">
          <p>Humedad:</p>
          <p :class="peligroH ? ' danger' : ''">{{ humedad }} %</p>
        </li>
      </div>
    </div>
    <div class="group">
      <p>{{ GroupName }}</p>
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
    peligroT: Boolean,
    peligroH: Boolean,
    peligro: Boolean,
  },
};
</script>

<style scoped>
.CardInfo {
  width: 190px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  border-radius: 5px;
  margin: 0 30px 40px 30px;
}

.SupContent {
  width: 100%;
  margin: 10px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  border-radius: 5px;
  border: 3px solid rgba(0, 0, 0, 0);
}

.TopContent {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin-bottom: 10px;
}

.CenterContent {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.EjemplarName {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding: 5px 0;
}

.BottomContent {
  width: 100%;
  display: flex;
  margin-top: 10px;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
}

.ImageGroup {
  width: 150px;
  height: 150px;
  overflow: hidden;
  border-radius: 5px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.peligro .TopContent img {
  height: 25px;
  width: 25px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 20px;
}

.peligro .SupContent {
  /*animacion de borde rojo*/
  animation: border 1s infinite;
}

@keyframes border {
  0% {
    border: 3px solid rgba(0, 0, 0, 0);
  }
  50% {
    border: 3px solid rgba(255, 0, 0, 0.5);
  }
  100% {
    border: 3px solid rgba(0, 0, 0, 0);
  }
}

.group {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.group p {
  font-size: 12px;
  color: #9e9e9e;
  font-weight: 500;
}

.temperatura,
.humedad {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  font-size: 12px;
  color: #555;
  font-weight: 500;
}

.temperatura .danger,
.humedad .danger {
  color: #ff6320;
  font-weight: 700;
  animation: danger 1s infinite;
}

@keyframes danger {
  0% {
    color: #9e9e9e;
  }
  50% {
    color: #ff6320;
  }
  100% {
    color: #9e9e9e;
  }
}
</style>
