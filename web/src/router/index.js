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
        path: 'dashboard',
        component: () => import(/* webpackChunkName: "admin" */ '../views/Dashboard.vue')
      },
      {
        path: 'blog',
        component: () => import(/* webpackChunkName: "admin" */ '../views/blog/Blog.vue'),
        children: [
          {
            path: '',
            component: () => import(/* webpackChunkName: "admin" */ '../views/blog/List.vue')
          },
          {
            path: 'create',
            component: () => import(/* webpackChunkName: "admin" */ '../views/blog/Create.vue')
          },
          {
            path: 'edit',
            component: () => import(/* webpackChunkName: "admin" */ '../views/blog/Edit.vue')
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
