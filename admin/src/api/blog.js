import instance from './base'

let postBaseURI = '/api/blog/v1.0/posts'
let categoryBaseURI = '/api/blog/v1.0/categories'

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

export function createPost (data) {
  return instance({
    url: postBaseURI,
    method: 'post',
    data: data
  })
}

export function updatePost (id, data) {
  return instance({
    url: postBaseURI + '/' + id,
    method: 'put',
    data: data
  })
}

export function deletePost (id) {
  return instance({
    url: postBaseURI + '/' + id,
    method: 'delete'
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

export function createCategory (data) {
  return instance({
    url: categoryBaseURI,
    method: 'post',
    data: data
  })
}

export function updateCategory (id, data) {
  return instance({
    url: categoryBaseURI + '/' + id,
    method: 'put',
    data: data
  })
}

export function deleteCategory (id) {
  return instance({
    url: categoryBaseURI + '/' + id,
    method: 'delete'
  })
}
