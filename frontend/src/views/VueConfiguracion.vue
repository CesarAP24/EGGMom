<template>
  <div class="configuracion-container">
    <h1>Configuración</h1>
    <div class="opciones-container">
      <div class="campo">
        <div class="header">
          <h3>Subscribir correo electrónico:</h3>
        </div>
        <div class="content">
          <form id="suscribir-correo" @submit="SuscribirCorreo">
            <label>Suscribir: </label>
            <input
              type="email"
              name="correo"
              id="correo-input"
              placeholder="correo@email.com"
            />
            <label>Repetir correo: </label>
            <input
              type="email"
              name="correo-again"
              id="correo-again-input"
              placeholder="correo@email.com"
            />
            <p class="error" id="error-correo"></p>
            <button
              type="submit"
              id="suscribir-correo-button"
              @click="SuscribirCorreo"
            >
              Suscribir
            </button>
          </form>
        </div>
      </div>
      <div class="campo">
        <div class="header">
          <h3>¿Cambiar idioma?</h3>
        </div>
        <div class="content">
          <select>
            <option value="es">Español</option>
          </select>
          <button id="cambiar-idioma-button">Cambiar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "VueConfiguracion",
  props: {
    loadCookie: Function,
  },
  methods: {
    SuscribirCorreo(e) {
      e.preventDefault();
      const correo = document.getElementById("correo-input").value;
      const correoAgain = document.getElementById("correo-again-input").value;
      document.getElementById("error-correo").innerHTML = "";
      if (correo === "" || correoAgain === "") {
        document.getElementById("error-correo").innerHTML =
          "Debe llenar todos los campos";
      } else if (correo === correoAgain) {
        const empresa = this.loadCookie("token");
        const sede = this.loadCookie("token");
        const url =
          "http://localhost:5000/empresa/" +
          empresa +
          "/sedes/" +
          sede +
          "/suscribir/" +
          correo;
        fetch(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((res) => {
            return res.json();
          })
          .then((data) => {
            if (data.success) {
              alert("Correo suscrito");
              document.getElementById("suscribir-correo").reset();
            } else {
              document.getElementById("error-correo").innerHTML =
                "El correo ya está suscrito";
            }
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        document.getElementById("error-correo").innerHTML =
          "Los correos no coinciden";
      }
    },
  },
};
</script>

<style scoped>
h1 {
  display: flex;
  font-size: 30px;
  font-weight: 600;
  color: #333;
  margin-left: 20px;
  margin-bottom: 5px;
}
.opciones-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  width: 50%;
  margin-top: 15px;
  margin-left: 15px;
  border: 1px solid #e0e0e0;
  padding: 20px;
  border-radius: 10px;
}
.opciones-container:hover {
  box-shadow: 0 0 65px rgba(0, 0, 0, 0.05);
  transition: 0.4s;
}
.content form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  width: 100%;
}

.content form label {
  font-size: 15px;
  font-weight: 500;
  margin-bottom: 5px;
}

.content form input {
  width: 70%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #e0e0e0;
  margin-bottom: 10px;
}
.content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  width: 100%;
  margin-top: 15px;
  margin-left: 15px;
}
.configuracion-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  width: 100%;
  padding: 50px;
}
.campo {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  width: 100%;
  margin-bottom: 20px;
}
#suscribir-correo-button,
#cambiar-idioma-button {
  width: 20%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ff6320;
  font-size: 16px;
  font-weight: 600;
  color: #ff6320;
  background-color: #ffffff;
  cursor: pointer;
  transition: 0.3s;
  margin-top: 20px;
  margin-bottom: 20px;
}
#suscribir-correo-button:hover,
#cambiar-idioma-button:hover {
  background-color: #ff6320;
  color: #ffffff;
}

select {
  width: 30%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #e0e0e0;
  font-size: 16px;
  font-weight: 550;
  color: #333;
}
.imagen {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 50%;
}

.error {
  font-size: 14px;
  font-weight: 500;
  color: #ff6320;
  margin-bottom: 10px;
}
</style>
