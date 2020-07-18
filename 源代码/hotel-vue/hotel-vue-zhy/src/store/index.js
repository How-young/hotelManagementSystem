import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        // 左侧菜单栏数据
        menuItems: [
            {
                name: 'home', // 要跳转的路由名称 不是路径
                size: 18, // icon大小
                type: 'md-home', // icon类型
                text: '主页', // 文本内容
            },
            // {
            //     name: 'other', // 要跳转的路由名称 不是路径
            //     size: 18, // icon大小
            //     type: 'ios-egg-outline', // icon类型
            //     text: '单独的路由', // 点击侧边栏跳到一个单独的路由页面，需要提前在 router.js 定义
            // },
            // {
            //     size: 18, // icon大小
            //     type: 'md-arrow-forward', // icon类型
            //     text: '外链',
            //     url: 'https://www.baidu.com',
            //     isExternal: true, // 外链 跳到一个外部的 URL 页面
            // },
            {
                text: '基本信息',
                type: 'ios-paper',
                children: [

                    {
                        size: 18,
                        type: 'md-home',
                        name: 'members',
                        text: '会员信息',
                    },
                    // {
                    //     size: 18, // icon大小
                    //     type: 'md-arrow-forward', // icon类型
                    //     text: '外链',
                    //     url: 'https://www.baidu.com',
                    //     isExternal: true, // 外链 跳到一个外部的 URL 页面
                    // },
                    {
                      type: 'ios-cart-outline',
                      name: 'goodinfor',
                      text: '商品信息',
                    },
                    {
                      type: 'md-cart',
                      name: 'goodtypeinfor',
                      text: '商品类别',
                    },
                    {
                        type: 'logo-buffer',
                        name: 'floors',
                        text: '楼层',
                    },
                    // {
                    //     type: '',
                    //     name: '',
                    //     text: '客房信息',
                    // },
                ],
            },
            {
                text: '系统管理',
                type: 'md-settings',
                children: [
                    {
                        type: 'md-person',
                        name: 'empinfor',
                        text: '员工信息管理',
                    },
                    {
                        text: '日志管理',
                        type: 'ios-paper',
                        name: 'loginfor',
                    },
                ],
            },
            {
                text: '客房管理',
                type: 'ios-home',
                children: [
                  {
                    type: 'ios-star-outline',
                    name: 'roominfor',
                    text: '客房信息',
                  },
                  {
                    type: 'ios-star',
                    name: 'roomtypeinfor',
                    text: '客房类别',
                  },
                ],
            },
            {
                text: '房客管理',
                type: 'ios-person',
                children: [
                    {
                      type: 'md-create',
                      name: 'bookinfor',
                      text: '预定管理',
                    },
                    {
                        type: 'ios-list-box',
                        name: 'checkin',
                        text: '登记入住',
                    },
                    {
                      type: 'md-repeat',
                      name: 'changeinfor',
                      text: '换房管理',
                    },
                    {
                        type: 'md-paper',
                        name: 'checkout',
                        text: '退房管理',
                    },
                ],
            },
            {
                text: '消费管理',
                type: 'ios-basket',
                children: [
                    {
                        type: 'md-basket',
                        name: 'costiteminfor',
                        text: '查询商品信息列表',
                    },
                    {
                        type: 'ios-wine',
                        name: 'costinfor',
                        text: '查询消费信息列表',
                    },
                ],
            },
            {
                text: '报表管理',
                type: 'ios-paper-outline',
                children: [
                    {
                        text: '预定，入住，离店报表',
                        name: 'complexinfor',
                        type: 'ios-stats',
                    },
                    {
                        text: '订单报表',
                        name: 'orderinfor',
                        type: 'ios-print',
                    },
                ],
            },
        ],
    },
    mutations: {
        setMenus(state, items) {
            state.menuItems = [...items]
        },
    },
})

export default store
