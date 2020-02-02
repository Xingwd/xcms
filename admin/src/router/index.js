import Vue from 'vue'
import VueRouter from 'vue-router'
import XAdminLayout from '../layout/XAdminLayout.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    component: () => import(/* webpackChunkName: "auth" */ '../views/auth/Login.vue')
  },
  {
    path: '/admin', // BUG: 浏览器直接访问 /admin，没效果，需要默认导向 dashboard
    component: XAdminLayout,
    children: [
      {
        path: 'dashboard',
        component: () => import(/* webpackChunkName: "admin" */ '../views/Dashboard.vue'),
        meta: {
          requiresAuth: true
        }
      },
      {
        path: 'blog',
        component: () => import(/* webpackChunkName: "admin" */ '../views/blog/Blog.vue'),
        children: [
          {
            path: 'list',
            component: () => import(/* webpackChunkName: "admin" */ '../views/blog/List.vue'),
            meta: {
              requiresAuth: true
            }
          },
          {
            path: 'create',
            component: () => import(/* webpackChunkName: "admin" */ '../views/blog/Create.vue'),
            meta: {
              requiresAuth: true
            }
          },
          {
            path: 'edit/:id',
            name: 'editPost',
            component: () => import(/* webpackChunkName: "admin" */ '../views/blog/Edit.vue'),
            meta: {
              requiresAuth: true
            }
          },
          {
            path: 'categories',
            component: () => import(/* webpackChunkName: "admin" */ '../views/blog/Categories.vue'),
            meta: {
              requiresAuth: true
            }
          }
        ]
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
