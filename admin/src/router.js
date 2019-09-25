import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import(/* webpackChunkName: "home" */ './views/Home.vue'),
      meta: { icon: 'el-icon-location', title: 'Home' }
    },
    {
      path: '/blog',
      name: 'blog',
      component: () => import(/* webpackChunkName: "blog" */ './views/blog/Blog.vue'),
      meta: { icon: 'el-icon-location', title: '博客' },
      children: [
        {
          path: 'articleList',
          name: 'articleList',
          component: () => import(/* webpackChunkName: "blog" */ './views/blog/BlogList.vue'),
          meta: { icon: 'el-icon-location', title: '博客列表' }
        },
        {
          path: 'createArticle',
          name: 'createArticle',
          component: () => import(/* webpackChunkName: "blog" */ './views/blog/CreateBlog.vue'),
          meta: { icon: 'el-icon-location', title: '创建博客' }
        },
        {
          path: 'editArticle',
          name: 'editArticle',
          component: () => import(/* webpackChunkName: "blog" */ './views/blog/EditBlog.vue'),
          meta: { icon: 'el-icon-location', title: '编辑博客' }
        }
      ]
    },
    {
      path: '/about',
      name: 'about',
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
      meta: { icon: 'el-icon-location', title: 'About' }
    }
  ]
})
