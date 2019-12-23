import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import XAdminLayout from '../layout/XAdminLayout.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/admin',
    component: XAdminLayout,
    children: [
      {
        path: '',
        component: Home
      },
      {
        path: 'about',
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
      },
      {
        path: 'main',
        component: XAdminLayout,
        children: [
          {
            path: 'home',
            component: Home
          },
          {
            path: 'about',
            component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
          }
        ]
      }
    ]
  },
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
