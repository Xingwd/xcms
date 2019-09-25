import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import(/* webpackChunkName: "home" */ './views/Home.vue')
    },
    {
      path: '/blog',
      name: 'blog',
      component: () => import(/* webpackChunkName: "blog" */ './views/blog/Blog.vue'),
      children: [
        {
          path: 'articleList',
          name: 'articleList',
          component: () => import(/* webpackChunkName: "blog" */ './views/blog/ArticleList.vue')
        },
        {
          path: 'createArticle',
          name: 'createArticle',
          component: () => import(/* webpackChunkName: "blog" */ './views/blog/CreateArticle.vue')
        },
        {
          path: 'editArticle',
          name: 'editArticle',
          component: () => import(/* webpackChunkName: "blog" */ './views/blog/EditArticle.vue')
        }
      ]
    },
    {
      path: '/about',
      name: 'about',
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
