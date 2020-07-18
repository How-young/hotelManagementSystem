<template>
  <div class="content ">
      <div class="query-c">
        <Input placeholder="请输入员工号或员工姓名" style="width: auto" v-model="searchkey"/>
        <el-button icon="el-icon-search" size="small" @click="empsearch()">查询</el-button>
        <!-- <el-button type="primary" icon="el-icon-circle-plus" size="small" @click="newemp()" style="float:right"></el-button> -->
      </div>

      <div class="table">
        <el-table :data="book" height="300" border style="width: 100%">
            <el-table-column prop="stayroom" label="房间号" width="100"></el-table-column>
            <el-table-column prop="idcard" label="身份证" width="150"></el-table-column>
            <el-table-column prop="tenantname" label="姓名" width="150"></el-table-column>
            <el-table-column prop="tenantsex" label="性别" width="150"></el-table-column>
            <el-table-column prop="checkin" label="入住时间" width="300"></el-table-column>
            <el-table-column prop="checkout" label="离店时间" width="300"></el-table-column>
            <!-- <el-table-column prop="" label="消费总价" width="200"></el-table-column> -->
            <el-table-column ixed="right" label="操作">
            <template slot-scope="scope">
                <el-button type="primary" @click.native.prevent="handleCheckOut(scope.$index, scope.row)" icon="el-icon-delete-solid" round>出账</el-button>
            </template>
            </el-table-column>
        </el-table>
      </div>
  </div>
</template>


<script>
import {bookGetAll, deletebooking, pay} from '../apis/index'

export default {
    name: 'checkout',
    data() {
        return {
            dialogFormVisible: false,
            newdialogFormVsible: false,
            book: [],
        }
    },
    mounted() {
        bookGetAll().then(res => {
           this.book = res.AllTenant
        })
    },
    methods: {
        handleCheckOut(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.$confirm('确定' + row.tenantname + '要结账吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {//, row.stayroom, row.tenantname, row.tenantsex, row.checkout
              pay(row.idcard)
              .then(res => {
                  if(res.status){
                        this.$message({
                        type: 'success',
                        message: '退房成功！共支付：' + res.total
                        })
                        bookGetAll().then(res => {
                        this.book = res.AllTenant
                        })
                  }
                  else{
                        this.$message({
                        type: 'warning',
                        message: '退房失败！'
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
