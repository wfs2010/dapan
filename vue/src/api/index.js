import request from '../utils/request'

export function wordCloud (skuId) {
    return request({
        url: '/alldata',
        method: 'get',
        params: {
            Id: skuId || '100014348492'
        }
    })
}

export function ap1 () {
    return request({
        url: '/screen/wordcloud',
        method: 'get'
    })
}

export function api2 () {
    return request({
        url: '/screen/wordcloud',
        method: 'get'
    })
}
