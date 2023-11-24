<template>
  <div class="container">
    <div class="NavBarContainer">
      <NavBar />
    </div>
    <div class="main">
      <TopBar empresa="Empresa" sede="sede" />
      <div class="content">
        <router-view :showHideWindow="showHideWindow" />
      </div>
    </div>
  </div>
  <div class="show notShow" id="ventanaEmergente">
    <div>
      <h1>hola</h1>
      <button @click="showHideWindow(0)">cerrar</button>
    </div>
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import TopBar from "./components/TopBar.vue";
export default {
  name: "App",
  components: {
    NavBar,
    TopBar,
  },
  data() {
    return {
      id: 0,
    };
  },
  methods: {
    showHideWindow(id) {
      this.id = id;
      //ocultar o mostrar ventana
      let show = document.querySelector("#ventanaEmergente");
      show.classList.toggle("notShow");
    },
  },
};
</script>

<style scoped>
.container {
  width: 100%;
  display: flex;
  height: 100vh;
  flex-direction: row;
  justify-content: space-between;
}

.main {
  width: calc(100% - 200px);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.content {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-shrink: 1;
  max-height: 100%;
  overflow-y: scroll;
}

.content::-webkit-scrollbar {
  width: 7px;
  background: #f1f1f1;
}

.content::-webkit-scrollbar-thumb {
  background: #888;
}

.NavBarContainer {
  width: 200px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
  background-color: #333;
  height: 100vh;
}

.show {
  display: flex;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 100000;
  background-color: rgba(0, 0, 0, 0.5);
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  box-shadow: 0px 0px 30px 0px rgba(0, 0, 0, 0.03);
  transition: all 0.5s ease-in-out;
  opacity: 1;
}

.notShow {
  width: 0px;
  height: 0px;
  transition: all 0.5s ease-in-out;
  opacity: 0;
}

.show div {
  width: 50%;
  height: 50%;
  background-color: #fff;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
