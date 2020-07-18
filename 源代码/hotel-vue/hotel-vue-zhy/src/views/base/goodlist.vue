<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
            <div class="query-c">
                <Input placeholder="请输入商品号或商品名" style="width: auto" v-model="searchkey"/>
                <el-button icon="el-icon-search" size="small" @click="goodsearch()">查询</el-button>
                <el-button type="primary" icon="el-icon-circle-plus" size="small" @click="newgood()" style="float:right"></el-button>
            </div>
    <!-- 新增商品表单 -->
    <el-dialog title="新增商品" :visible.sync="newdialogFormVsible" center width="20%">
    <el-form :model="good" :rules="rules" ref="good" class="form-good">
    <el-form-item label="商品编号" prop="goodsnum">
        <el-input v-model="good.goodsnum" placeholder="商品编号"></el-input>
    </el-form-item>
    <el-form-item label="商品名" prop="goodsname">
        <el-input v-model="good.goodsname" placeholder="商品名"></el-input>
    </el-form-item>
        <el-form-item label="商品种类号" prop="goodstypenum">
        <el-input v-model="good.goodstypenum" placeholder="商品种类号"></el-input>
    </el-form-item>
        <el-form-item label="商品价格" prop="goodsprice">
        <el-input v-model="good.goodsprice" placeholder="商品价格"></el-input>
    </el-form-item>
        <el-form-item label="商品数量" prop="goodsquantity">
        <el-input v-model="good.goodsquantity" placeholder="商品数量"></el-input>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="newdialogFormVsible = false">取消</el-button>
        <el-button type="primary" @click="newonSubmit('good')">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
     <!-- 表格显示 -->
    <el-table
        :data="goods"
        height="750"
        border
        style="width: 100%">
        <el-table-column
        prop="goodsnum"
        label="商品编号"
        width="200">
        </el-table-column>
        <el-table-column
        prop="goodsname"
        label="商品名称"
        width="200">
        </el-table-column>
        <el-table-column
        prop="goodstypenum"
        label="种类编号"
        width="200">
        </el-table-column>
        <el-table-column
        prop="goodsprice"
        label="商品价格"
        width="200">
        </el-table-column>
        <el-table-column
        prop="goodsquantity"
        label="商品数量"
        width="200">
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
    <!-- 修改对话框 -->
    <el-dialog title="修改商品信息"  :visible.sync="dialogFormVisible" center width="20%">
    <el-form :model="good" :rules="rules" ref="good" class="form-good">
    <el-form-item label="商品编号" prop="goodsnum">
        <el-input v-model="good.goodsnum" placeholder="商品编号"></el-input>
    </el-form-item>
    <el-form-item label="商品名称" prop="goodsname">
        <el-input v-model="good.goodsname" placeholder="商品名称"></el-input>
    </el-form-item>
        <el-form-item label="商品种类号" prop="goodstypenum">
        <el-input v-model="good.goodstypenum" placeholder="商品种类号"></el-input>
    </el-form-item>
        <el-form-item label="商品价格" prop="goodsprice">
        <el-input v-model="good.goodsprice" placeholder="商品价格"></el-input>
    </el-form-item>
        <el-form-item label="商品数量" prop="goodsquantity">
        <el-input v-model="good.goodsquantity" placeholder="商品数量"></el-input>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="onSubmit('good')">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
    </div>
    </div>
</template>


<script>
import { listGoods, modifyGoods, addGoods, searchGoods, deleteGoods } from '../apis'

export default {
    name: 'goodinfor',
    data() {
        return {
            searchkey: '',
            dialogFormVisible: false,
            newdialogFormVsible: false,
            goods: [],
            good: {
                goodsnum: '',
                goodsname: '',
                goodstypenum: '',
                goodsprice: '',
                goodsquantity: '',
            },
            // tableData: [
            //     {
            //         goodno: 101,
            //         goodname: '可乐',
            //         catenum: 1,
            //         egoodprice: 3,
            //         goodnum: 10,
            //     },
            // ],
            rules: {
                goodsnum: [
                    { required: true, message: '请输入商品编号', trigger: 'blur' },
                ],
                goodsname: [
                    { required: true, message: '请输入商品名', trigger: 'blur' },
                ],
                goodstypenum: [
                    { required: true, message: '请输入商品种类号', trigger: 'blur' },
                ],
                goodsprice: [
                    { required: true, message: '请输入商品价格', trigger: 'blur' },
                ],
                goodsquantity: [
                    { required: true, message: '请输入商品数量', trigger: 'blur' },
                ],
            },
        }
    },
    mounted() {
        listGoods().then(res => {
           this.goods = res.Goods
        })
    },
    methods: {
        // goodsearch() {
        //     // eslint-disable-next-line no-alert
        // },
        goodsearch() {
            searchGoods(this.searchkey)
            .then(res => {
              this.goods = res.Goods
                })
        },
        newgood() {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.newdialogFormVsible = true
        },
        handleEdit(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.dialogFormVisible = true
            _this.good.goodsnum = row.goodsnum
            _this.good.goodsname = row.goodsname
            _this.good.goodstypenum = row.goodstypenum
            _this.good.goodsprice = row.goodsprice
            _this.good.goodsquantity = row.goodsquantity

            // eslint-disable-next-line no-alert
        },
        // handleDelete(index, row) {
        //     // eslint-disable-next-line no-underscore-dangle
        //     let _this = this
        //     _this.$confirm('确定要删除:' + row.gno + ' 号商品吗?', '提示', {
        //         confirmButtonText: '确定',
        //         cancelButtonText: '取消',
        //         type: 'warning',
        //     }).then(() => {
        //         // eslint-disable-next-line no-alert
        //         alert('删除成功')
        //     }).catch()
        // },
        handleDelete(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.$confirm('确定要删除:' + row.goodsnum + ' 号商品吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
              deleteGoods(row.goodsnum)
              .then(res => {
                  if(res.status){
                        this.$message({
                        type: 'success',
                        message: '删除商品成功！'
                        })
                        listGoods().then(res => {
                        this.goods = res.Goods
                        })
                  }
                  else{
                        this.$message({
                        type: 'warning',
                        message: '删除失败！'
            })
                  }
              })
            }).catch()
        },
      //   onSubmit(good) {
      //   this.$refs[good].validate((valid) => {
      //     if (valid) {
      //       alert('submit!');
      //     } else {
      //       console.log('error submit!!');
      //       return false;
      //     }
      //   });
      // },
      // newonSubmit(good) {
      //   this.$refs[good].validate((valid) => {
      //     if (valid) {
      //       alert('submit!');
      //     } else {
      //       console.log('error submit!!');
      //       return false;
      //     }
      //   });
      // },
      onSubmit(good) {
           this.$refs[good].validate((valid) => {
              if(valid){
                modifyGoods(this.good.goodsnum,this.good.goodsname,this.good.goodstypenum,this.good.goodsprice,this.good.goodsquantity)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '修改商品信息成功！'
                        })
                        this.dialogFormVisible = false
                        listGoods().then(res => {
                        this.goods = res.Goods
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '修改商品信息失败！'
                        })
                    }
                 })
              }
           })
        },
                newonSubmit(good) {
           this.$refs[good].validate((valid) => {
              if(valid){
                addGoods(this.good.goodsnum,this.good.goodsname,this.good.goodstypenum,this.good.goodsprice,this.good.goodsquantity)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '新增商品成功！'
                        })
                        this.newdialogFormVsible = false
                        listGoods().then(res => {
                        this.goods = res.Goods
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '新增商品失败！'
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
