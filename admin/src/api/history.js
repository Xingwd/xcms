import instance from './base'

let historyBaseURI = '/api/history/v1.0/histories'

export function fetchHistories (query) {
  return instance({
    url: historyBaseURI,
    method: 'get',
    params: query
  })
}

export function createHistory (data) {
  return instance({
    url: historyBaseURI,
    method: 'post',
    data: data
  })
}

export function updateHistory (id, data) {
  return instance({
    url: historyBaseURI + '/' + id,
    method: 'put',
    data: data
  })
}

export function deleteHistory (id) {
  return instance({
    url: historyBaseURI + '/' + id,
    method: 'delete'
  })
}
