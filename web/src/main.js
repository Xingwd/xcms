import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(mavonEditor)

// 全局前置守卫
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    if (localStorage.token) {
      next()
    } else {
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
