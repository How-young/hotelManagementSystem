<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
            <div class="query-c">
                <Input placeholder="请输入商品名称或身份证" style="width: auto" v-model="searchkey"/>
                <el-button icon="el-icon-search" size="small" @click="billsearch()">查询</el-button>
                <el-button type="primary" icon="el-icon-circle-plus" size="small" @click="newbill()" style="float:right"></el-button>
            </div>
            <!-- 订单表格 -->
            <el-table
            :data="billlist"
            height="400"
            border
            style="width: 100%">
                <el-table-column
                prop="goodsnum"
                label="商品编号"
                width="300">
                </el-table-column>
                <el-table-column
                prop="idcard"
                label="身份证号"
                width="300">
                </el-table-column>
                <el-table-column
                prop="quantity"
                label="数量"
                width="300">
                </el-table-column>
                <el-table-column
                fixed="right"
                label="操作">
                <template slot-scope="scope">
                    <el-button type="danger"  @click.native.prevent="handleDelete(scope.$index,scope.row)" icon="el-icon-delete" circle></el-button>
                    <el-button type="primary" @click.native.prevent="handleEdit(scope.$index,scope.row)" icon="el-icon-edit" circle></el-button>
                </template>
                </el-table-column>
            </el-table>
    <!-- 新增订单表单 -->
            <el-dialog title="新建订单" :visible.sync="newdialogFormVsible" center width="20%">
            <el-form :model="billitem" :rules="rules" ref="billitem" class="form-billitem">
            <el-form-item label="商品编号" prop="goodsnum">
                <el-input v-model="billitem.goodsnum" placeholder="商品编号"></el-input>
            </el-form-item>
            <el-form-item label="身份证号" prop="idcard">
                <el-input v-model="billitem.idcard" placeholder="身份证号"></el-input>
            </el-form-item>
            <el-form-item label="数量" prop="quantity">
                <el-input v-model="billitem.quantity" placeholder="数量"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="newdialogFormVsible = false">取消</el-button>
                <el-button type="primary" @click="newbillSubmit('billitem')">保存</el-button>
            </el-form-item>
            </el-form>
            </el-dialog>
        </div>
    </div>
</template>
<script>
import { listbill , editbill, addbill ,deletebill,searchbill} from '../apis/index'

export default {
    name: 'costinfor',
    data() {
        return{
            newdialogFormVsible: false,
            searchkey: '',
            billlist: [],
            billitem: {
                goodsnum: '',
                idcard: '',
                quantity: '',
            },
            rules: {
                goodsnum: [
                    { required: true, message: '请输入商品编号', trigger: 'blur' },
                ],
                idcard: [
                    { required: true, message: '请输入身份证号', trigger: 'blur' },
                ],
                quantity: [
                    { required: true, message: '请输入数量', trigger: 'blur' },
                ],
            },
        }
    },
    mounted() {
        listbill().then(res => {
        this.billlist = res.Room
        })
    },
    methods: {
        billsearch() {
        searchbill(this.searchkey)
            .then(res => {
              this.billlist = res.Room
                })
        },
        newbill() {
            let _this = this
            _this.newdialogFormVsible = true
        },
        handleDelete(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.$confirm('确定要删除:' + row.idcard + ' 购买的' + row.goodsnum +'号商品吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
              deletebill(row.goodsnum ,row.idcard)
              .then(res => {
                  if(res.status){
                        this.$message({
                        type: 'success',
                        message: '删除订单成功！'
                        })
                        listbill().then(res => {
                        this.billlist = res.Room
                        })
                  }
                  else{
                        this.$message({
                        type: 'warning',
                        message: '删除订单失败！'
            })
                  }
              })
            }).catch()
        },
        newbillSubmit(billitem){
           this.$refs[billitem].validate((valid) =>{
              if(valid){
                addbill(this.billitem.goodsnum ,this.billitem.idcard,this.billitem.quantity)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '新增订单成功！'
                        })
                        this.newdialogFormVsible = false
                        listbill().then(res => {
                        this.billlist = res.Room
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '新增订单失败！'
                        })
                    }
                 })
              }
           })
        },
    }
}
</script>

<style scoped>
.home-container {
    padding: 10px;
    padding-top: 5px;
}
.home-content {
    padding: 10px;
    border-radius: 5px;
    background: #fff;
}
</style>
