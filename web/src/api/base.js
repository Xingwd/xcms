import axios from 'axios'

// Create an instance
const instance = axios.create({
  baseURL: process.env.VUE_APP_BASE_API,
  timeout: 5000
})

// Add a request interceptor
instance.interceptors.request.use(
  config => {
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
    return Promise.reject(error.response)
  }
)

export default instance
