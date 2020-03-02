import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    pathTo: '',
    sideBarIsCollapse: false,
    token: ''
  },
  mutations: {
    setPathTo (state, path) {
      state.pathTo = path
    },
    changeIsCollapse (state) {
      state.sideBarIsCollapse = !state.sideBarIsCollapse
    },
    setToken (state, token) {
      state.token = token
      localStorage.token = token
    },
    delToken (state) {
      state.token = ''
      localStorage.removeItem('token')
    }
  },
  actions: {
  },
  modules: {
  }
})
