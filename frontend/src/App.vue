<template>
  <div class="container">
    <div class="NavBarContainer" id="NavBarContainer">
      <NavBar :clearCookie="clearCookie" :clearAllCookies="clearAllCookies" />
    </div>
    <div class="SupNavbarContainer" id="SupNavbarContainer">
      <sup-navbar />
    </div>
    <div class="main">
      <TopBar :empresa="Empresa" :sede="Sede" />
      <div class="content">
        <router-view
          :showHideWindow="showHideWindow"
          :showCrearEjemplar="showCrearEjemplar"
          :storeCookie="storeCookie"
          :loadCookie="loadCookie"
        />
      </div>
    </div>
  </div>
  <div class="show notShow" id="ventanaEmergente">
    <div class="container-grafica">
      <div class="top-container-grafica">
        <h1>Ejemplar Data</h1>
        <button @click="showHideWindow(-1, -1)">cerrar</button>
      </div>
      <GraficaLineas
        v-if="labels.length > 0 && !cargandoEmergente"
        :labels="labels"
        :temperaturas="temperaturas"
        :humedades="humedades"
      />
      <div class="container-carga-grafica" v-if="cargandoEmergente">
        <PantallaCarga />
      </div>
      <div v-else>
        <p v-if="labels.length == 0">No hay registros</p>
      </div>
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
        <form id="crear-ejemplar-formulario">
          <label for="name">Nombre</label>
          <input type="text" id="name" name="nombre" placeholder="Nombre" />
          <label for="grupo-select">Grupo</label>
          <select name="grupo" id="grupo-select">
            <option v-for="grupo in grupos" :key="grupo.id" :value="grupo.name">
              {{ grupo.name }}
            </option>
          </select>
          <label for="arduino-selector">Arduino</label>
          <select name="arduino_id" id="arduino-selector">
            <option
              v-for="arduino in arduinos"
              :key="arduino.id"
              :value="arduino.id"
            >
              {{ arduino.id }}
            </option>
          </select>
          <button type="submit" id="btn-crear-ejemplar" @click="crearEjemplar">
            Crear
          </button>
        </form>
      </div>
    </div>
  </div>
  <div class="login" :style="{ display: login ? 'none' : 'flex' }">
    <VueLogin :storeCookie="storeCookie" />
  </div>
</template>

<script>
import GraficaLineas from "./components/GraficaLineas.vue";
import NavBar from "./components/NavBar.vue";
import TopBar from "./components/TopBar.vue";
import SupNavbar from "./components/SupNavbar.vue";
import VueLogin from "./views/VueLogin.vue";
import PantallaCarga from "./components/PantallaCarga.vue";
export default {
  name: "App",
  components: {
    NavBar,
    TopBar,
    SupNavbar,
    VueLogin,
    GraficaLineas,
    PantallaCarga,
  },
  data() {
    return {
      Empresa: "Empresa",
      Sede: "Sede",
      login: false,
      grupos: [],
      arduinos: [],
      labels: [],
      temperaturas: [],
      humedades: [],
      cargandoEmergente: false,
    };
  },
  methods: {
    showHideWindow(grupo, objeto) {
      if (objeto == -1) {
        //cerrar ventana
        let show = document.querySelector("#ventanaEmergente");
        show.classList.toggle("notShow");
        return;
      }
      //cargar registros
      this.cargandoEmergente = true;
      this.loadRegisters(grupo, objeto);

      //ocultar o mostrar ventana
      let show = document.querySelector("#ventanaEmergente");
      show.classList.toggle("notShow");
    },
    showCrearEjemplar() {
      console.log("hola");
      let show2 = document.querySelector("#CrearEjemplar");
      show2.classList.toggle("notShow");
    },
    loadCookie(name) {
      let nameEQ = name + "=";
      let ca = document.cookie.split(";");
      for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == " ") c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) {
          return c.substring(nameEQ.length, c.length);
        }
      }
      return null;
    },
    storeCookie(name, value) {
      let date = new Date();
      date.setTime(date.getTime() + 24 * 60 * 60 * 1000);
      let expires = "; expires=" + date.toUTCString();
      document.cookie = name + "=" + (value || "") + expires + "; path=/";
    },
    clearCookie(name) {
      document.cookie = name + "=; Max-Age=-99999999;";
    },
    clearAllCookies() {
      let cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i];
        let eqPos = cookie.indexOf("=");
        let name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
      }
    },
    loadGrupos() {
      let empresa = this.loadCookie("empresa");
      let sede = this.loadCookie("token");
      fetch(
        "http://localhost:5000/empresa/" +
          empresa +
          "/sedes/" +
          sede +
          "/grupos",
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      )
        .then((response) => response.json())
        .then((data) => {
          this.grupos = [];
          let grupos = data["data"];
          grupos.forEach((grupo) => {
            //llenar la lista Grupos
            this.grupos.push({
              id: grupo["grupo_id"],
              name: grupo["grupo_id"],
            });
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    loadArduinos() {
      let empresa = this.loadCookie("empresa");
      fetch("http://localhost:5000/empresa/" + empresa + "/arduinos", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status == 200) {
            alert("cargado correctamente");
          } else if (data.status == 404) {
            console.log("No hay arduinos disponibles");
          }
          this.arduinos = [];
          let arduinos = data["data"];
          arduinos.forEach((arduino) => {
            //llenar la lista Grupos
            console.log(arduino);
            if (arduino["available"]) {
              this.arduinos.push({
                id: arduino["ARDUINO_ID"],
              });
            }
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    crearEjemplar(e) {
      e.preventDefault();
      let form = document.getElementById("crear-ejemplar-formulario");
      form = new FormData(form);
      form = Object.fromEntries(form);
      console.log("grupito: " + form["grupo"]);
      let grupo = form["grupo"];
      form = JSON.stringify(form);
      console.log(form);
      //disable
      const button = document.getElementById("btn-crear-ejemplar");
      button.disabled = true;

      let empresa = this.loadCookie("empresa");
      let sede = this.loadCookie("token");
      fetch(
        "http://localhost:5000/empresa/" +
          empresa +
          "/sedes/" +
          sede +
          "/grupos/" +
          grupo +
          "/objetos",
        {
          method: "POST",
          body: form,
          headers: {
            "Content-Type": "application/json",
          },
        }
      )
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          if (data.success == true) {
            alert("Ejemplar creado correctamente");
            button.disabled = false;
          } else {
            alert("Error al crear el ejemplar");
            button.disabled = false;
          }
        })
        .catch((err) => {
          console.log(err);
          alert("Error al crear el ejemplar");
          button.disabled = false;
        });
    },
    loadRegisters(grupo, objeto) {
      let empresa = this.loadCookie("empresa");
      let sede = this.loadCookie("token");
      fetch(
        `http://localhost:5000/empresa/${empresa}/sedes/${sede}/grupos/${grupo}/objetos/${objeto}/registros`
      )
        .then((response) => response.json())
        .then((data) => {
          this.cargandoEmergente = false;
          if (data.success == false) {
            this.labels = [];
            this.temperaturas = [];
            this.humedades = [];
          } else {
            this.labels = [];
            this.temperaturas = [];
            this.humedades = [];
            data.data.forEach((element) => {
              this.labels.push(element["fecha_hora"]);
              this.temperaturas.push(element.temperatura);
              this.humedades.push(element.humedad);
            });
          }
        })
        .catch((err) => {
          console.log(err);
          this.cargandoEmergente = false;
        });
    },
  },
  created() {
    this.loadGrupos();
    this.loadArduinos();
    if (this.loadCookie("token")) {
      let empresa = this.loadCookie("empresa");
      let sede = this.loadCookie("sede_name");
      if (empresa) {
        //mayusculas
        empresa = empresa.charAt(0).toUpperCase() + empresa.slice(1);
        this.Empresa = empresa;
      }
      if (sede) {
        this.Sede = sede;
      }
      this.login = true;
    } else {
      this.login = false;
    }
  },
};
</script>

<style scoped>
.login {
  width: 100vw;
  height: 100vh;
  display: flex;
  position: absolute;
  z-index: 100;
  top: 0;
  left: 0;
  background-color: #ffffff;
  align-items: center;
}
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

.show .container-grafica,
.show .container-crear-ejemplar {
  width: 50%;
  background-color: #fff;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.top-container-grafica {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  margin-left: 20px;
  margin-right: 20px;
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

/*styles for Ventana Emergente*/
.container-grafica {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.container-grafica h1 {
  font-size: 30px;
  font-weight: 550;
  color: #333;
  margin: 20px 0px;
}

.container-grafica button {
  margin: 20px 0px;
  padding: 10px 30px;
  border-radius: 5px;
  border: none;
  font-size: 15px;
  cursor: pointer;
  color: white;
  background-color: #ff6320;
  border: 1px solid #ff6320;
  transition: 0.3s;
}

.container-grafica button:hover {
  background-color: #fff;
  color: #ff6320;
}

.container-carga-grafica {
  width: 100%;
  height: 250px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.container-grafica p {
  font-size: 20px;
  font-weight: 550;
  color: #333;
  margin: 20px 0px;
}
</style>
