import instance from './base'

let historyBaseURI = '/api/history/v1.0/histories'

export function fetchHistories (query) {
  return instance({
    url: historyBaseURI,
    method: 'get',
    params: query
  })
}
