<template>
    <div>
    <el-table
        :data="book"
        height="300"
        border
        style="width: 100%">
        <el-table-column prop="stayroom" label="房间号" width="150"></el-table-column>
        <el-table-column prop="idcard" label="身份证" width="150"></el-table-column>
        <el-table-column prop="tenantname" label="姓名" width="200"></el-table-column>
        <el-table-column prop="tenantsex" label="性别" width="200"></el-table-column>
        <el-table-column prop="checkin" label="预计入住时间" width="200"></el-table-column>
        <el-table-column prop="checkout" label="预计离店时间" width="200"></el-table-column>
        <el-table-column ixed="right" label="操作">
        <template slot-scope="scope">
            <el-button type="primary" @click.native.prevent="handleCheck(scope.$index, scope.row)" icon="el-icon-check" round></el-button>
        </template>
        </el-table-column>
   </el-table>
    </div>
</template>


<script>
import {listbook, checkBooking} from '../apis/index'

export default {
    name: 'checkin',
    data() {
        return {
            dialogFormVisible: false,
            newdialogFormVsible: false,
            book: [],
        }
    },
    mounted() {
        listbook().then(res => {
           this.book = res.BookRoom
        })
    },
    methods: {
        handleCheck(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.$confirm('确定' + row.tenantname + '要入住吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {//, row.stayroom, row.tenantname, row.tenantsex, row.checkout
              checkBooking(row.idcard)
              .then(res => {
                  if(res.status){
                        this.$message({
                        type: 'success',
                        message: '入住成功！'
                        })
                        listbook().then(res => {
                        this.book = res.BookRoom
                        })
                  }
                  else{
                        this.$message({
                        type: 'warning',
                        message: '入住失败！'
            })
                  }
              })
            }).catch()
        },
    },
}

</script>

<style scoped>

</style>
