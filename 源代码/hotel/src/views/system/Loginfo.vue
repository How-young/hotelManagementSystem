<template>
<div style="padding: 10px">
    <div style="background: #fff; border-radius: 8px; padding: 20px;">
        <div>
              <h2>日志信息</h2>
              <el-button type="danger" icon="el-icon-delete" @click="deletelog()" size="medium" style="float:right" ></el-button>
        </div>
    <el-table
        :data="tableData"
        height="250"
        border
        style="width: 100%">
        <el-table-column
        prop="date"
        label="日期"
        width="400">
        </el-table-column>
        <el-table-column
        prop="describe"
        label="描述"
        width="795">
        </el-table-column>
        <el-table-column
        fixed="right"
        label="操作"
        width="60">
        <template slot-scope="scope">
            <el-button type="danger" size="mini" round
            @click.native.prevent="handleDelete(scope.$index,scope.row)" icon="el-icon-delete"></el-button>
        </template>
        </el-table-column>
    </el-table>
    </div>
</div>
</template>

<script>
export default {
    name: 'loginfo',
    data() {
        return {
            tableData: [
                {
                    date: '2020-7-5',
                    describe: '随便改改',
                },
                {
                    date: '2020-7-5',
                    describe: '随便写写',
                },
            ],
        }
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
