<template>
  <div class="container">
    <NavBar />
    <div class="main">
      <TopBar empresa="Empresa" sede="sede" />
      <router-view />
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
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
