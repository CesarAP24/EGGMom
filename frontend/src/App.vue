<template>
  <div class="container">
    <div class="NavBarContainer">
      <NavBar />
    </div>
    <div class="main">
      <TopBar empresa="Empresa" sede="sede" />
      <div class="content">
        <router-view />
      </div>
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

.NavBarContainer {
  width: 200px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
  background-color: #333;
  height: 100vh;
}
</style>
