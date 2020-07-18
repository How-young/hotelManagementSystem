<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
     <el-table
        :data="pay"
        height="400"
        border
        style="width: 100%">
        <el-table-column
            prop="idcard"
            label="身份证号"
            width="300">
        </el-table-column>
        <el-table-column
            prop="paytime"
            label="支付时间"
            width="300">
        </el-table-column>
        <el-table-column
            prop="total"
            label="总价格"
            width="300">
        </el-table-column>
   </el-table>
    </div>
    </div>
</template>

<script>
import {listpay } from '../apis/index'

export default {
    name: 'ordertable',
    data() {
        return {
            pay: [],
            datekey: '',
        }
    },
    mounted() {
            listpay()
            .then(res => {
                this.pay = res.money
            })
    },
}
</script>

<style scoped>

</style>
