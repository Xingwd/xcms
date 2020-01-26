import instance from './base'

let authBaseURI = '/xcms/auth/api/v1.0'

export function login (data) {
  return instance({
    url: authBaseURI + '/login',
    method: 'post',
    data: data
  })
}
