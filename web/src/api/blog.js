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
    url: postBaseURI + '/{}'.format(id),
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
    url: postBaseURI + '/{}'.format(id),
    method: 'put',
    data: data
  })
}

export function deletePost (id) {
  return instance({
    url: postBaseURI + '/{}'.format(id),
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
    url: categoryBaseURI + '/{}'.format(id),
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
    url: categoryBaseURI + '/{}'.format(id),
    method: 'put',
    data: data
  })
}

export function deleteCategory (id) {
  return instance({
    url: categoryBaseURI + '/{}'.format(id),
    method: 'delete'
  })
}
