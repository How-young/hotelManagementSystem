import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VCharts from 'v-charts'
import ViewUI from 'view-design'
import ElementUI from 'element-ui'
import Ajax from '@/assets/js/AxiosPlugin'
import App from './App'
import store from './store'
import router from './router'
import 'element-ui/lib/theme-chalk/index.css'
import 'view-design/dist/styles/iview.css'
import './permission'

Vue.config.productionTip = false
Vue.use(ViewUI)
Vue.use(ElementUI)
Vue.use(VCharts)
Vue.use(Ajax)
Vue.use(VueAxios, axios)

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App),
})
