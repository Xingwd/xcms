import axios from 'axios'
import store from '@/store'
import router from '@/router'

// Create an instance
const instance = axios.create({
  baseURL: process.env.VUE_APP_BASE_API,
  timeout: 5000
})

// Add a request interceptor
instance.interceptors.request.use(
  config => {
    if (localStorage.token) {
      let Base64 = require('js-base64').Base64
      config.headers['Authorization'] = 'Basic ' + Base64.encode(localStorage.token + ':unused')
    }
    return config
  },
  error => {
    console.log(error) // for debug
    return Promise.reject(error)
  }
)

// Add a response interceptor
instance.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.response) {
      switch (error.response.status) {
        case 401: // 401状态时跳转登录页并清除token
          store.commit('del_token')
          router.push('/login')
      }
    }
    return Promise.reject(error.response)
  }
)

export default instance
