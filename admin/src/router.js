import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import(/* webpackChunkName: "home" */ './views/Home.vue'),
      meta: { icon: 'el-icon-s-home', title: 'Home' }
    },
    {
      path: '/blog',
      name: 'blog',
      component: () => import(/* webpackChunkName: "blog" */ './views/blog/Blog.vue'),
      meta: { icon: 'el-icon-notebook-1', title: '博客' },
      children: [
        {
          path: 'articleList',
          name: 'articleList',
          component: () => import(/* webpackChunkName: "blog" */ './views/blog/BlogList.vue'),
          meta: { title: '博客列表' }
        },
        {
          path: 'createArticle',
          name: 'createArticle',
          component: () => import(/* webpackChunkName: "blog" */ './views/blog/CreateBlog.vue'),
          meta: { title: '创建博客' }
        },
        {
          path: 'editArticle',
          name: 'editArticle',
          component: () => import(/* webpackChunkName: "blog" */ './views/blog/EditBlog.vue'),
          meta: { title: '编辑博客' }
        }
      ]
    },
    {
      path: '/about',
      name: 'about',
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
      meta: { icon: 'el-icon-goblet-full', title: 'About' }
    }
  ]
})
