import { createRouter, createWebHistory } from "vue-router";
import VueInicio from "../views/VueInicio.vue";

const routes = [
  {
    path: "/",
    name: "inicio",
    component: VueInicio,
  },

  {
    path: "/grupos",
    name: "grupos",
    component: () => import("../views/VueGrupos.vue"),
  },

  {
    path: "/ejemplares",
    name: "ejemplares",
    component: () => import("../views/VueEjemplares.vue"),
  },

  {
    path: "/peligros",
    name: "peligros",
    component: () => import("../views/VuePeligros.vue"),
  },

  {
    path: "/configuracion",
    name: "configuracion",
    component: () => import("../views/VueConfiguracion.vue"),
  },
  // {
  //   path: "/",
  //   name: "home",
  //   component: HomeView,
  // },
  // {
  //   path: "/about",
  //   name: "about",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import("../views/AboutView.vue"),
  // },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
