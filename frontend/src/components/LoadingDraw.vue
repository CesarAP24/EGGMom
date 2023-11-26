<template>
  <div class="loading-container">
    <div class="loading-draw">
      <div class="loading-draw__circle"></div>
    </div>
  </div>
</template>

<style scoped>
.loading-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.loading-draw {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: 5px solid #333;
  display: flex;
  justify-content: center;
  align-items: center;
  animation: rotate 1s infinite linear;
}

.loading-draw__circle {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background-color: #333;
  animation: move 1s infinite linear;
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

@keyframes move {
  0% {
    transform: translateX(0px);
  }
  50% {
    transform: translateX(80px);
  }
  100% {
    transform: translateX(0px);
  }
}
</style>
