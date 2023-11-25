<template>
  <div class="container">
    <div class="NavBarContainer" id="NavBarContainer">
      <NavBar />
    </div>
    <div class="SupNavbarContainer" id="SupNavbarContainer">
      <sup-navbar />
    </div>
    <div class="main">
      <TopBar empresa="Empresa" sede="sede" />
      <div class="content">
        <router-view
          :showHideWindow="showHideWindow"
          :showCrearEjemplar="showCrearEjemplar"
        />
      </div>
    </div>
  </div>
  <div class="show notShow" id="ventanaEmergente">
    <div>
      <h1>Ejemplar Data</h1>
      <button @click="showHideWindow(0)">cerrar</button>
    </div>
  </div>
  <div class="show notShow" id="CrearEjemplar">
    <div class="container-crear-ejemplar">
      <div class="top-form-create-ejemplar">
        <h2>Crear Ejemplar</h2>
        <button @click="showCrearEjemplar()" id="closeCreateWindow">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="12"
            height="12"
            viewBox="0 0 24 24"
            fill="none"
            stroke="#fff"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="feather feather-x"
          >
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
      </div>
      <div class="crear-ejemplar-form">
        <form>
          <label for="name">Nombre</label>
          <input type="text" id="name" name="name" placeholder="Nombre" />
          <label for="grupo-select">Grupo</label>
          <select name="grupo" id="grupo-select">
            <option v-for="grupo in grupos" :key="grupo.id" :value="grupo.name">
              {{ grupo.name }}
            </option>
          </select>
          <label for="arduino-selector">Arduino</label>
          <select name="arduino" id="arduino-selector">
            <option
              v-for="arduino in arduinos"
              :key="arduino.id"
              :value="arduino.id"
            >
              {{ arduino.id }}
            </option>
          </select>
          <button type="submit">Crear</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import TopBar from "./components/TopBar.vue";
import SupNavbar from "./components/SupNavbar.vue";
export default {
  name: "App",
  components: {
    NavBar,
    TopBar,
    SupNavbar,
  },
  data() {
    return {
      id: 0,
      grupos: [
        {
          id: 1,
          name: "Grupo 1",
        },
        {
          id: 2,
          name: "Grupo 2",
        },
        {
          id: 3,
          name: "Grupo 3",
        },
      ],
      arduinos: [
        {
          id: "ESP32-0003",
        },
        {
          id: "ESP32-0002",
        },
        {
          id: "ESP32-0001",
        },
      ],
    };
  },
  methods: {
    showHideWindow(id) {
      this.id = id;
      //ocultar o mostrar ventana
      let show = document.querySelector("#ventanaEmergente");
      show.classList.toggle("notShow");
    },
    showCrearEjemplar() {
      console.log("hola");
      let show2 = document.querySelector("#CrearEjemplar");
      show2.classList.toggle("notShow");
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
  overflow: scroll;
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
  transition: all 0.4s ease-in-out;
  opacity: 1;
}

.notShow {
  /*desde el centro*/
  opacity: 0;
  transform: scale(0.2);
  transition: all 0.4s ease-in-out;
  z-index: -100000;
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

#closeCreateWindow {
  display: flex;
  width: 30px;
  height: 30px;
  align-items: center;
  justify-content: center;
  background-color: #ff6320;
  border: 1px solid #ff6320;
  color: #fff;
  border-radius: 100%;
  padding: 5px;
  transition: 0.3s ease-in-out;
}

#closeCreateWindow:hover {
  background-color: #fff;
  color: #ff6320;
  transition: 0.3s ease-in-out;
}

#closeCreateWindow:active {
  background-color: #fff;
  color: #ff6320;
  transition: 0.3s ease-in-out;
}

#CrearEjemplar .container-crear-ejemplar {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 20px;
  margin: 0;
}

#CrearEjemplar .top-form-create-ejemplar {
  height: auto;
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin: 0;
}

#CrearEjemplar .crear-ejemplar-form {
  width: 100%;
  display: flex;
  height: auto;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
}

#CrearEjemplar .crear-ejemplar-form form {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
}

#CrearEjemplar .crear-ejemplar-form form label {
  font-size: 20px;
  font-weight: 550;
  color: #333;
  margin: 10px 0px;
}

#CrearEjemplar .crear-ejemplar-form form input {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #e0e0e0;
  font-size: 16px;
  font-weight: 550;
  color: #333;
}

#CrearEjemplar .crear-ejemplar-form form select {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #e0e0e0;
  font-size: 16px;
  font-weight: 550;
  color: #333;
}

#CrearEjemplar .crear-ejemplar-form form button {
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

#CrearEjemplar .crear-ejemplar-form form button:hover {
  background-color: #fff;
  color: #ff6320;
}

#CrearEjemplar .crear-ejemplar-form form button:active {
  background-color: #fff;
  color: #333;
}

#CrearEjemplar .crear-ejemplar-form form button:focus {
  background-color: #fff;
  color: #333;
}

#CrearEjemplar .crear-ejemplar-form form button:disabled {
  background-color: #fff;
  border-color: #898989;
  color: #898989;
  cursor: not-allowed;
}

#NavBarContainer {
  display: flex;
}

#SupNavbarContainer {
  display: none;
}

@media (max-width: 768px) {
  #NavBarContainer {
    display: none;
  }
  #SupNavbarContainer {
    display: flex;
  }
  .container {
    flex-direction: column;
    height: auto;
  }
  .container .main {
    width: 100%;
  }
}
</style>
