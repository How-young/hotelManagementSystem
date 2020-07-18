<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
            <div class="query-c">
                <Input placeholder="请输入身份证号" style="width: auto" v-model="searchkey"/>
                <el-button icon="el-icon-search" size="small" @click="idcardsearch()">查询</el-button>
     <!-- 表格显示 -->
    <el-table
        :data="changeroom"
        height="750"
        border
        style="width: 100%">
        <el-table-column
        prop="idcard"
        label="身份证号"
        width="150">
        </el-table-column>
        <el-table-column
        prop="stayroom"
        label="入住客房"
        width="150">
        </el-table-column>
        <el-table-column
        prop="tenantname"
        label="客户姓名"
        width="150">
        </el-table-column>
        <el-table-column
        prop="tenantsex"
        label="客户性别"
        width="150">
        </el-table-column>
                <el-table-column
        prop="checkin"
        label="入住时间"
        width="300">
        </el-table-column>
                       <el-table-column
        prop="checkout"
        label="离开时间"
        width="300">
        </el-table-column>
        <el-table-column
        fixed="right"
        label="操作">
        <template slot-scope="scope">
            <el-button type="primary" @click.native.prevent="handleEdit(scope.$index,scope.row)" icon="el-icon-edit" circle></el-button>
        </template>
        </el-table-column>
    </el-table>
    <!-- 修改对话框 -->
    <el-dialog title="换房信息"  :visible.sync="dialogFormVisible" center width="20%">
    <el-form :model="roomchange" :rules="rules" ref="roomchange" class="form-roomchange">
    <el-form-item label="身份证号" prop="idcard">
        <el-input v-model="roomchange.idcard" placeholder="身份证号"></el-input>
    </el-form-item>
    <el-form-item label="入住客房" prop="stayroom">
        <el-input v-model="roomchange.stayroom" placeholder="入住客房"></el-input>
    </el-form-item>
        <el-form-item label="更换客房" prop="changeroom">
        <el-input v-model="roomchange.changeroom" placeholder="更换客房"></el-input>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="onSubmit('roomchange')">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
    </div>
    </div>
    </div>
</template>


<script>
import { listAllTenant, changeRoomTenant, searchIdcard } from '../apis'

export default {
    name: 'changeinfor',
    data() {
        return {
            searchkey: '',
            dialogFormVisible: false,
            changeroom: [],
            roomchange: {
                idcard: '',
                stayroom: '',
                changeroom: '',
            },
            rules: {
                idcard: [
                    { required: true, message: '请输入该客人身份证号', trigger: 'blur' },
                ],
                stayroom: [
                    { required: true, message: '请输入原客房', trigger: 'blur' },
                ],
                changeroom: [
                    { required: true, message: '请输入要更换客房', trigger: 'blur' },
                ],
            },
        }
    },
    mounted() {
        listAllTenant().then(res => {
           this.changeroom = res.AllTenant
        })
    },
    methods: {
        // goodsearch() {
        //     // eslint-disable-next-line no-alert
        // },
        idcardsearch() {
            searchIdcard(this.searchkey)
            .then(res => {
              this.changeroom = res.Tenant
                })
        },
        handleEdit(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.dialogFormVisible = true
            _this.roomchange.idcard = row.idcard
            _this.roomchange.stayroom = row.stayroom
            _this.roomchange.changeroom = row.changeroom
            // eslint-disable-next-line no-alert
        },
      onSubmit(roomchange) {
           this.$refs[roomchange].validate((valid) => {
              if(valid){
                changeRoomTenant(this.roomchange.idcard,this.roomchange.stayroom,this.roomchange.changeroom)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '更换客房成功！'
                        })
                        this.dialogFormVisible = false
                        listAllTenant().then(res => {
                        this.changeroom = res.AllTenant
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '更换客房失败！'
                        })
                    }
                 })
              }
           })
        },
    },
}

</script>

<style scoped>

</style>
