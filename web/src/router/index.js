import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import(/* webpackChunkName: "home" */ '../views/Home.vue')
  },
  {
    path: '/blog',
    name: 'blog_list',
    component: () => import(/* webpackChunkName: "blog" */ '../views/blog/BlogList.vue')
  },
  {
    path: '/blog/:id',
    name: 'blog_detail',
    component: () => import(/* webpackChunkName: "blog" */ '../views/blog/BlogDetail.vue')
  },
  {
    path: '/project',
    name: 'project',
    component: () => import(/* webpackChunkName: "project" */ '../views/Project.vue')
  },
  {
    path: '/history',
    name: 'history',
    component: () => import(/* webpackChunkName: "history" */ '../views/History.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
