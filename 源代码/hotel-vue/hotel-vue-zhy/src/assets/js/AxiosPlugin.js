import axios from 'axios'

const Axios = axios.create({
    baseURL: '/api',
    timeout: 5000,
})

Axios.install = (Vue) => {
    Vue.prototype.$http = Axios
}

export default Axios
