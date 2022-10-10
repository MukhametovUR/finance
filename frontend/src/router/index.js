import Vue from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import store from '../store';
import Home from '../views/Home'
import Register from '../views/Register'
import Login from '../views/Login'
import Posts from '../views/Posts'

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: '/register',
    name: "Register",
    component: Register,
    meta: { guest: true },
  },
  {
    path: '/login',
    name: "Login",
    component: Login,
    meta: { guest: true },
  },
  {
    path: '/api/v1/invest/',
    name: Posts,
    component: Posts,
    meta: {requiresAuth: true},
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if(store.getters.isAuthenticated) {
      next()
      return
    }
    next('/login')
  }else {
    next()
  }
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.guest)) {
    if (store.getters.isAuthenticated) {
      next("/api/v1/invest/")
      return
    }
    next()
  } else {
    next()
  }
})
export default router
