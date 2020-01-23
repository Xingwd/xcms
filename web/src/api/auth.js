import instance from './base'

instance.defaults.baseURL = process.env.VUE_APP_BASE_API + '/xcms/auth/api/v1.0'

export function login (data) {
  return instance({
    url: '/login',
    method: 'post',
    data: data
  })
}
