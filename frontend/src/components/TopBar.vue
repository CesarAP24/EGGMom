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
  background-color: #f3f3f3;
  padding: 15px 25px;
  height: 80px;
  border-bottom: 1px solid #e0e0e0;
}

.title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #333;
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
  border: 1px solid #767676;
  padding: 5px 10px;
  background-color: #fff;
  border-radius: 5px;
  font-weight: 500;
  font-size: 15px;
}

#title {
  font-size: 2rem;
  font-weight: 500;
  color: #333;
}
</style>
