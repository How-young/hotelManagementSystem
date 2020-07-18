<template>
<div style="padding: 10px">
    <div style="background: #fff; border-radius: 8px; padding: 20px;">
        <div>
              <h2>日志信息</h2>
        </div>
    <el-table
        :data="logdata"
        height="400"
        border
        style="width: 100%">
        <el-table-column
        prop="logdate"
        label="日期"
        width="350">
        </el-table-column>
        <el-table-column
        prop="detail"
        label="描述"
        width="900">
        </el-table-column>
    </el-table>
    </div>
</div>
</template>

<script>
import {listlog } from '../apis/index'

export default {
    name: 'loginfo',
    data() {
        return {
            logdata: [],
        }
    },
    mounted() {
        listlog().then(res => {
           this.logdata = res.Log
        })
    },
    methods: {
        deletelog() {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.$confirm('确定要删除全部吗吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
                // eslint-disable-next-line no-alert
                alert('fuck')
            }).catch()
        },
        handleDelete(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.$confirm('确定要删除:' + row.date + ' 的日志吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
                // eslint-disable-next-line no-alert
                alert('fuck')
            }).catch()
        },
    },

}
</script>

<style scoped>

</style>
