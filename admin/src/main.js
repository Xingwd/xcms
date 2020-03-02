import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI, { Message } from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import { verifyToken } from '@/api/auth'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(mavonEditor)

// 全局前置守卫
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    if (localStorage.token) {
      verifyToken({
        token: localStorage.token
      }).then(response => {
        next()
      }).catch(error => {
        console.log(error)
        next({ path: '/login' })
        Message.warning('认证过期，请重新登录！')
      })
    } else {
      store.commit('setPathTo', to.path)
      next({ path: '/login' })
    }
  } else {
    next()
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
