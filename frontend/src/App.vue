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
  <div class="login" :style="{ display: login ? 'none' : 'flex' }">
    <VueLogin />
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import TopBar from "./components/TopBar.vue";
import VueLogin from "./views/VueLogin.vue";
export default {
  name: "App",
  components: {
    NavBar,
    TopBar,
    VueLogin,
  },
  data() {
    return {
      login: false,
    };
  },
  created() {
    if (document.cookie) {
      this.login = true;
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
</style>
