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
    path: '/',
    redirect: { name: 'dashboard' },
    component: XAdminLayout,
    children: [
      {
        path: 'dashboard',
        name: 'dashboard',
        component: () => import(/* webpackChunkName: "admin" */ '../views/Dashboard.vue'),
        meta: {
          requiresAuth: true
        }
      },
      {
        path: 'blog',
        component: () => import(/* webpackChunkName: "blog" */ '../views/blog/Blog.vue'),
        children: [
          {
            path: 'list',
            component: () => import(/* webpackChunkName: "blog" */ '../views/blog/List.vue'),
            meta: {
              requiresAuth: true
            }
          },
          {
            path: 'create',
            component: () => import(/* webpackChunkName: "blog" */ '../views/blog/Create.vue'),
            meta: {
              requiresAuth: true
            }
          },
          {
            path: 'edit/:id',
            name: 'editPost',
            component: () => import(/* webpackChunkName: "blog" */ '../views/blog/Edit.vue'),
            meta: {
              requiresAuth: true
            }
          },
          {
            path: 'categories',
            component: () => import(/* webpackChunkName: "blog" */ '../views/blog/Categories.vue'),
            meta: {
              requiresAuth: true
            }
          }
        ]
      },
      {
        path: 'history',
        name: 'history',
        component: () => import(/* webpackChunkName: "admin" */ '../views/History.vue'),
        meta: {
          requiresAuth: true
        }
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
