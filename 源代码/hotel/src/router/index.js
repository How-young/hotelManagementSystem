import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const commonRoutes = [
    {
        path: '/login',
        name: 'login',
        meta: { title: '登录' },
        component: () => import('../components/Login.vue'),
    },
    {
        path: '/404',
        name: '404',
        meta: { title: '404' },
        component: () => import('../components/404.vue'),
    },
    { path: '/', redirect: '/home' },
]

// 本地所有的页面 需要配合后台返回的数据生成页面
export const asyncRoutes = {
    home: {
        path: 'home',
        name: 'home',
        meta: { title: '主页' },
        component: () => import('../views/Home.vue'),
    },
    empinfor: {
        path: 'empinfor',
        name: 'empinfor',
        meta: { title: '员工信息管理' },
        component: () => import('../views/system/Empinfor.vue'),
    },
    loginfor: {
        path: 'loginfor',
        name: 'loginfor',
        meta: { title: '日志信息' },
        component: () => import('../views/system/Loginfo.vue'),
    },
    costinfor: {
        path: 'costinfor',
        name: 'costinfor',
        meta: { title: '消费信息管理' },
        component: () => import('../views/consume/Costinfo.vue'),
    },
    costiteminfor: {
        path: 'costiteminfor',
        name: 'costiteminfor',
        meta: { title: '商品信息管理' },
        component: () => import('../views/consume/Costiteminfo.vue'),
    },
    complexinfor: {
        path: 'complexinfor',
        name: 'complexinfor',
        meta: { title: '预定，入住，离店报表' },
        component: () => import('../views/statement/Complextable.vue'),
    },
    orderinfor: {
        path: 'orderinfor',
        name: 'orderinfor',
        meta: { title: '订单报表' },
        component: () => import('../views/statement/Ordertable.vue'),
    },
    members: {
        path: 'members',
        name: 'members',
        meta: { title: '会员信息' },
        component: () => import('../views/base/members.vue'),
    },
    floors: {
        path: 'floors',
        name: 'floors',
        meta: { title: '楼层管理' },
        component: () => import('../views/base/floors.vue'),
    },
    merchandise: {
        path: 'merchandise',
        name: 'merchandise',
        meta: { title: '商品信息' },
        component: () => import('../views/base/merchandise.vue'),
    },
    reserve: {
        path: 'reserve',
        name: 'reserve',
        meta: { title: '预定管理' },
        component: () => import('../views/roomer/reserve.vue'),
    },
    password: {
        path: 'password',
        name: 'password',
        meta: { title: '修改密码' },
        component: () => import('../views/Password.vue'),
    },
    msg: {
        path: 'msg',
        name: 'msg',
        meta: { title: '通知消息' },
        component: () => import('../views/Msg.vue'),
    },
}

const createRouter = () => new Router({
    routes: commonRoutes,
})

const router = createRouter()

export function resetRouter() {
    const newRouter = createRouter()
    router.matcher = newRouter.matcher
}

export default router
