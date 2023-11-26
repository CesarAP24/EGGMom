<template>
  <div class="login-container">
    <div class="login-form">
      <h1>Inicio de sesión</h1>
      <form id="formulario-login" @submit.prevent="login">
        <div class="input-container">
          <label for="empresa">Empresa:</label>
          <input type="text" id="empresa" />
        </div>
        <div class="input-container">
          <label for="sede">Sede:</label>
          <input type="text" id="sede-input" />
        </div>
        <div class="input-container">
          <label for="credenciales">credenciales:</label>
          <input type="password" id="credenciales" />
        </div>
        <p id="error"></p>
        <div class="boton">
          <button type="submit">Iniciar sesión</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "VueLogin",
  props: {
    storeCookie: Function,
  },
  methods: {
    login() {
      const empresa = document.getElementById("empresa").value;
      const sede = document.getElementById("sede-input").value;
      const credenciales = document.getElementById("credenciales").value;

      if (empresa == "" || sede == "" || credenciales == "") {
        document.getElementById("error").innerHTML =
          "Por favor, rellene todos los campos";
        return;
      }

      let data = {
        name: sede,
        password: credenciales,
      };

      data = JSON.stringify(data);
      console.log(data);

      fetch("http://localhost:5000/empresa/" + empresa + "/login", {
        method: "POST",
        body: data,
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.success == true) {
            document.getElementById("error").innerHTML = "";
            this.storeCookie("token", data.token);
            this.storeCookie("empresa", empresa);
            this.storeCookie("sede_name", sede);
            this.storeCookie("sede_id", data.token);
            window.location.href = "/";
          } else {
            document.getElementById("error").innerHTML = data.message;
          }
        });
    },
  },
};
</script>

<style scoped>
#error {
  color: red;
  font-size: 15px;
  font-weight: 500;
  margin: 0;
  margin-bottom: 10px;
}

.login-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: rgb(255, 248, 240);
  margin-top: 10px;
}

.input-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin: 20px 10px;
  width: 40%;
}
.input-container input {
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  padding: 8px;
  margin-left: 3px;
}
.login-container .login-form {
  width: 400px;
  height: 400px;
  background-color: #fff;
  border-radius: 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 100px;
  border-radius: 5px;
  border: 1px solid rgba(0, 0, 0, 0);
  transition: 0.3s;
}
.boton button {
  margin-left: 12px;
  padding: 8px;
  border-radius: 5px;
  border: none;
  font-size: 15px;
  cursor: pointer;
  color: white;
  background-color: #ff6320;
  border: 1px solid #ff6320;
  transition: 0.3s;
  padding: 10px 30px;
  margin-top: 20px;
}
.boton {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin: 10px;
}
</style>
