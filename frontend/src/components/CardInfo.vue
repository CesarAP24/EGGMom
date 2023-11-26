<template>
  <div
    :class="'CardInfo' + (peligro ? ' peligro' : '')"
    @click="showWindow"
    :style="hideIfSecure & !peligro ? 'display: none' : ''"
  >
    <div class="TopContent">
      <h2>{{ EjemplarName }}</h2>
      <div :style="'display: ' + (peligro ? 'flex' : 'none')">
        <img src="../assets/peligro.svg" alt="peligro" width="19" />
      </div>
    </div>
    <div class="SupContent">
      <div class="CenterContent">
        <div class="ImageGroup">
          <!-- si peligro entonces  defaultHuevo.gif sino defaultHuevo.png -->
          <img v-if="peligro" src="../assets/defaultHuevo.gif" alt="huevo" />
          <img v-else src="../assets/defaultPlanta.jpg" alt="huevo" />
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
    id: String,
    GroupName: String,
    EjemplarName: String,
    showHideWindow: Function,
    tempMax: Number,
    tempMin: Number,
    humMax: Number,
    humMin: Number,
    loadCookie: Function,
    hideIfSecure: Boolean,
    NoLoadData: Boolean,
    forcePeligro: Boolean,
    noClick: Boolean,
  },
  methods: {
    loadCards() {
      if (this.NoLoadData) {
        if (this.forcePeligro) {
          this.peligro = true;
        }
        return;
      }
      this.actualizarDatos(this.GroupName, this.id);

      setInterval(() => {
        this.actualizarDatos(this.GroupName, this.id);
      }, 3000);
    },
    showWindow() {
      if (this.noClick) {
        return;
      }
      this.showHideWindow(this.GroupName, this.id);
    },
    actualizarDatos(grupo, id_objeto) {
      let empresa = this.loadCookie("empresa");
      let sede = this.loadCookie("token");
      fetch(
        "http://localhost:5000/empresa/" +
          empresa +
          "/sedes/" +
          sede +
          "/grupos/" +
          grupo +
          "/objetos/" +
          id_objeto +
          "/registros"
      )
        .then((res) => res.json())
        .then((data) => {
          //registro más reciente
          let registro = data["data"];
          let ultimo_registro = registro[registro.length - 1];
          this.temperatura = ultimo_registro["temperatura"];
          this.humedad = ultimo_registro["humedad"];
          this.peligroH = false;
          this.peligroT = false;
          console.log(this.temperatura, this.humedad);
          console.log(this.tempMax, this.tempMin, this.humMax, this.humMin);
          if (
            this.temperatura > this.tempMax ||
            this.temperatura < this.tempMin
          ) {
            this.peligroT = true;
          }
          if (this.humedad > this.humMax || this.humedad < this.humMin) {
            this.peligroH = true;
          }
          if (this.peligroH || this.peligroT) {
            this.peligro = true;
          } else {
            this.peligro = false;
          }
        })
        .catch((err) => console.log(err));
    },
  },
  data() {
    return {
      temperatura: 0,
      humedad: 0,
      peligro: false,
      peligroT: false,
      peligroH: false,
    };
  },
  created() {
    this.loadCards();
  },
};
</script>

<style scoped>
.CardInfo {
  width: 250px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  border-radius: 5px;
  margin: 0 30px 40px 30px;
  box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
  padding: 30px;
  transition: all 0.3s ease-in-out;
}

.peligro:hover {
  animation: none;
}

.peligro {
  animation: shake 0.5s infinite;
}

@keyframes shake {
  0% {
    transform: translateX(0px) rotate(0deg);
  }
  10% {
    transform: translateX(-1px) rotate(-1deg);
  }
  20% {
    transform: translateX(0px) rotate(1deg);
  }
  30% {
    transform: translateX(1px) rotate(0deg);
  }
  40% {
    transform: translateX(0px) rotate(1deg);
  }
  50% {
    transform: translateX(-1px) rotate(-1deg);
  }
  60% {
    transform: translateX(0px) rotate(0deg);
  }
  70% {
    transform: translateX(1px) rotate(-1deg);
  }
  80% {
    transform: translateX(0px) rotate(1deg);
  }
  90% {
    transform: translateX(-1px) rotate(0deg);
  }
  100% {
    transform: translateX(0px) rotate(-1deg);
  }
}

.CardInfo:hover {
  transition: all 0.3s ease-in-out;
  cursor: pointer;
  box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.3);
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

.ImageGroup img {
  width: 130px;
  object-fit: cover;
  border-radius: 5px;
}
</style>
