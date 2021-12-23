import axios from 'axios'
const service = axios.create({
    baseURL: 'http://216.127.179.21:5000/api/v1/',
    timeout: 50000
})

service.interceptors.response.use(
    response => {
        if (response.status === 200 && response.data) {
            return response.data
        } else {
            return Promise.reject(new Error('请求失败'))
        }
    },
    error => {
        return Promise.reject(error)
    }
)
export default service
