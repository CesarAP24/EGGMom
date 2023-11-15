<template>
  <div class="container">
    <NavBar />
    <div>
      <h1>Home</h1>
    </div>
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
export default {
  name: "App",
  components: {
    NavBar,
  },
};
</script>

<style>
.container {
  max-width: 1200px;
  width: 100%;
  display: flex;
  height: 100vh;
  flex-direction: row;
  justify-content: space-between;
}

.container div {
  width: 100%;
}
</style>
