import instance from './base'

let postBaseURI = '/xcms/blog/api/v1.0/posts'
let categoryBaseURI = '/xcms/blog/api/v1.0/categories'

export function fetchPosts (query) {
  return instance({
    url: postBaseURI,
    method: 'get',
    params: query
  })
}

export function fetchPost (id) {
  return instance({
    url: postBaseURI + '/' + id,
    method: 'get'
  })
}

export function fetchCategories (query) {
  return instance({
    url: categoryBaseURI,
    method: 'get',
    params: query
  })
}

export function fetchCategory (id) {
  return instance({
    url: categoryBaseURI + '/' + id,
    method: 'get'
  })
}
