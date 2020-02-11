import instance from './base'

let authBaseURI = '/api/auth/v1.0'

export function login (data) {
  return instance({
    url: authBaseURI + '/login',
    method: 'post',
    data: data
  })
}

export function verifyToken (data) {
  return instance({
    url: authBaseURI + '/verify_token',
    method: 'post',
    data: data
  })
}
