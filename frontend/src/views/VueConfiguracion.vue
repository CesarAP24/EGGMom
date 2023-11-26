<template>
  <div class="configuracion-container">
    <h1>Configuración</h1>
    <div class="opciones-container">
      <div class="campo">
        <div class="header">
          <h3>¿Cambiar credenciales?</h3>
        </div>
        <div class="content">
          <form id="Cambiar_credenciales">
            <label>Credenciales actuales: </label>
            <input
              type="text"
              name="credenciales"
              id="credenciales"
              placeholder="Credenciales actuales"
            />
            <label>Nuevas credenciales: </label>
            <input
              type="password"
              name="credenciales"
              id="credenciales"
              placeholder="Nuevas credenciales"
            />
            <label>Repetir nuevas credenciales: </label>
            <input
              type="password"
              name="credenciales"
              id="credenciales"
              placeholder="Repetir nuevas credenciales"
            />
            <button
              type="submit"
              @click="CambiarCredenciales"
              id="btn-cambiar-credenciales"
            >
              Cambiar
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
            <option value="en">Inglés</option>
          </select>
        </div>
      </div>
      <div class="campo">
        <div class="header">
          <h3>¿Permitir correos?</h3>
        </div>
        <div class="content">
          <select>
            <option value="si">Sí</option>
            <option value="no">No</option>
          </select>
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
    // toco crear rutas y hacer que funciones :(
    CambiarCredenciales(e) {
      e.preventDefault();
      let form = document.getElementById("Cambiar_credenciales");
      form = new FormData(form);
      form = Object.fromEntries(form.entries());
      console.log(form);
      let credencialesNuevas = form["credenciales"];
      form = JSON.stringify(form);

      let empresa = this.loadCookie("empresa");
      let sede = this.loadCookie("token");

      fetch("http://localhost:5000/empresa/" + empresa + "/sedes/" + sede, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: form,
      })
        .then((response) => {
          if (response.success == false) {
            console.log("error");
          } else {
            console.log("success");
            return response.json();
          }
        })
        .then(() => {
          //json a enviar
          const SedeActualizada = {
            empresa: empresa,
            sede: sede,
            credenciales: credencialesNuevas,
          };
          return fetch(
            "http://localhost:5000/empresa/" + empresa + "/sedes/" + sede,
            {
              method: "PUT",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(SedeActualizada),
            }
          );
        })
        .catch((error) => {
          console.log(error);
        });
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
#btn-cambiar-credenciales {
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
}
#btn-cambiar-credenciales:hover {
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
</style>
