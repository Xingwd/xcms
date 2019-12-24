import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    sideBarIsCollapse: false
  },
  mutations: {
    changeIsCollapse (state) {
      state.sideBarIsCollapse = !state.sideBarIsCollapse
    }
  },
  actions: {
  },
  modules: {
  }
})
