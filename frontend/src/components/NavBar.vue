<template>
  <div class="nav">
    <div class="sup">
      <div class="option">
        <svg height="24" viewBox="0 0 24 24" width="24">
          <path fill="#fff" d="M0 0h24v24H0V0z" fill-opacity="0"></path>
          <path fill="#fff" d="M12 3L4 9v12h16V9l-8-6zm6 15H6v-2h12v2z"></path>
        </svg>
        <router-link to="/">Inicio</router-link>
      </div>
      <div class="option">
        <img src="../assets/canastitaBlanca.svg" alt="canasta" width="24" />
        <router-link to="/grupos">Grupos</router-link>
      </div>
      <div class="option">
        <img src="../assets/huevo.svg" id="huevo" alt="huevo" height="21" />
        <router-link to="/ejemplares">Ejemplares</router-link>
      </div>
      <div class="option">
        <img src="../assets/peligroWhite.svg" alt="peligro" width="19" />
        <router-link to="/peligros">Peligros</router-link>
      </div>
    </div>
    <div class="bottom">
      <div class="option">
        <img src="../assets/tuerquita.svg" alt="tuerca" width="22" />
        <router-link to="/configuracion">Configuración</router-link>
      </div>
      <div class="option">
        <router-link to="/login" @click="cerrarSesion"
          >Cerrar Sesión</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  methods: {
    cerrarSesion() {
      this.deleteAllCookies();
    },
    deleteAllCookies() {
      var cookies = document.cookie.split(";");

      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie =
          name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
      }

      window.location.href = "/";
    },
  },
};
</script>

<style scoped>
.nav {
  background-color: #333;
  display: flex;
  height: 100vh;
  flex-direction: column;
  justify-content: space-between;
  width: 100%;
}

.option {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  padding: 20px;
  width: 100%;
  display: flex;
}

.option svg {
  margin-right: 10px;
}

.option img {
  margin-right: 10px;
}

.option a {
  color: #fff;
  text-decoration: none;
  font-size: 16px;
  font-weight: 500;
}

#huevo {
  margin-right: 12xpx;
  margin-left: 5px;
}

.option:hover {
  background-color: #555;
}

a:hover {
  text-decoration: underline;
  color: #fff;
}
</style>
