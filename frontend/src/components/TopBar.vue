<template>
  <div class="TopBar-container">
    <h1 id="title">{{ empresa }}</h1>
    <div class="sede">
      <p id="sede">{{ sede }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "TopBar",
  props: {
    empresa: String,
    sede: String,
  },
};
</script>

<style scoped>
.TopBar-container {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  background: linear-gradient(283deg, #ff6320 0%, #ff5d17 100%);
  padding: 15px 25px;
  height: 80px;
  border-bottom: 1px solid #e0e0e0;
}

#title {
  font-size: 2.5rem;
  font-weight: 800;
  color: white;
}

.sede {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.sede p {
  font-size: 1rem;
  font-weight: 400;
  color: #333;
  margin-right: 10px;
  border: 2px solid #d33f00;
  padding: 7px 20px;
  background-color: #fff;
  border-radius: 5px;
  font-weight: 500;
  font-size: 15px;
  color: #d33f00;
}
</style>
