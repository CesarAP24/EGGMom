<template>
  <div class="nav">
    <div class="option">
      <router-link to="/">
        <svg height="24" viewBox="0 0 24 24" width="24">
          <path fill="#fff" d="M0 0h24v24H0V0z" fill-opacity="0"></path>
          <path fill="#fff" d="M12 3L4 9v12h16V9l-8-6zm6 15H6v-2h12v2z"></path>
        </svg>
      </router-link>
    </div>
    <div class="option">
      <router-link to="/grupos">
        <img src="../assets/canastitaBlanca.svg" alt="canasta" width="24" />
      </router-link>
    </div>
    <div class="option">
      <router-link to="/ejemplares">
        <img src="../assets/huevo.svg" id="huevo" alt="huevo" height="21" />
      </router-link>
    </div>
    <div class="option">
      <router-link to="/peligros">
        <img src="../assets/peligroWhite.svg" alt="peligro" width="19" />
      </router-link>
    </div>
    <div class="option">
      <router-link to="/configuracion">
        <img src="../assets/tuerquita.svg" alt="tuerca" width="22" />
      </router-link>
    </div>
    <div class="option">
      <a href="#">Cerrar sesión</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "SupNavbar",
};
</script>

<style scoped>
.nav {
  background-color: #333;
  display: flex;
  width: 100%;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
}

#showNavBarMobile {
  display: none;
}

.sup {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
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
