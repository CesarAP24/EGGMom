<template>
  <div class="nav">
    <div class="sup">
      <div class="option">
        <svg height="24" viewBox="0 0 24 24" width="24">
          <path fill="#fff" d="M0 0h24v24H0V0z" fill-opacity="0"></path>
          <path fill="#fff" d="M12 3L4 9v12h16V9l-8-6zm6 15H6v-2h12v2z"></path>
        </svg>
        <a href="#">Home</a>
      </div>
      <div class="option">
        <svg height="24" viewBox="0 0 24 24" width="24">
          <circle cx="12" cy="12" fill="#fff" opacity=".3" r="8"></circle>
        </svg>
        <a href="#">Grupos</a>
      </div>
      <div class="option">
        <svg height="24" viewBox="0 0 24 24" width="24">
          <circle cx="12" cy="12" fill="#fff" opacity=".3" r="8"></circle>
        </svg>
        <a href="#">Ejemplares</a>
      </div>
      <div class="option">
        <svg height="24" viewBox="0 0 24 24" width="24">
          <circle cx="12" cy="12" fill="#fff" opacity=".3" r="8"></circle>
        </svg>
        <a href="#">Peligros</a>
      </div>
    </div>
    <div class="bottom">
      <div class="option">
        <a href="#">Configuración</a>
      </div>
      <div class="option">
        <a href="#">Cerrar sesión</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style scoped>
.nav {
  background-color: #333;
  display: flex;
  height: 100vh;
  flex-direction: column;
  justify-content: space-between;
  width: 300px;
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

.option a {
  color: #fff;
  text-decoration: none;
  font-size: 16px;
  font-weight: 500;
}

.option:hover {
  background-color: #555;
}
</style>
