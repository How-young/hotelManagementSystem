<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
            <div class="query-c">
                <Input placeholder="请输入商品种类名" style="width: auto" v-model="searchkey"/>
                <el-button icon="el-icon-search" size="small" @click="goodtypesearch()">查询</el-button>
                <el-button type="primary" icon="el-icon-circle-plus" size="small" @click="newgoodtype()" style="float:right"></el-button>
            </div>
    <!-- 新增商品类别表单 -->
    <el-dialog title="新增商品类别" :visible.sync="newdialogFormVsible" center width="20%">
    <el-form :model="goodtype" :rules="rules" ref="goodtype" class="form-goodtype">
    <el-form-item label="商品类别号" prop="goodstypenum">
        <el-input v-model="goodtype.goodstypenum" placeholder="商品类别号"></el-input>
    </el-form-item>
    <el-form-item label="商品种类" prop="goodstype">
        <el-input v-model="goodtype.goodstype" placeholder="商品种类"></el-input>
    </el-form-item>
        <el-form-item label="种类描述" prop="typedescribe">
        <el-input v-model="goodtype.typedescribe" placeholder="种类描述"></el-input>
        </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="newdialogFormVsible = false">取消</el-button>
        <el-button type="primary" @click="newonSubmit('goodtype')">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
     <!-- 表格显示 -->
    <el-table
        :data="goodstype"
        height="250"
        border
        style="width: 100%">
        <el-table-column
        prop="goodstypenum"
        label="商品类别号"
        width="200">
        </el-table-column>
        <el-table-column
        prop="goodstype"
        label="商品种类"
        width="200">
        </el-table-column>
        <el-table-column
        prop="typedescribe"
        label="种类描述"
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
    <el-dialog title="修改商品种类信息"  :visible.sync="dialogFormVisible" center width="20%">
    <el-form :model="goodtype" :rules="rules" ref="goodtype" class="form-goodtype">
    <el-form-item label="商品类别号" prop="goodstypenum">
        <el-input v-model="goodtype.goodstypenum" placeholder="商品编号"></el-input>
    </el-form-item>
    <el-form-item label="商品种类" prop="goodstype">
        <el-input v-model="goodtype.goodstype" placeholder="商品种类"></el-input>
    </el-form-item>
        <el-form-item label="种类描述" prop="typedescribe">
        <el-input v-model="goodtype.typedescribe" placeholder="商品种类号"></el-input>
        </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="onSubmit('goodtype')">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
    </div>
    </div>
</template>


<script>
import { listGoodsType, modifyGoodsType, addGoodsType, searchGoodsType, deleteGoodsType } from '../apis'

export default {
    name: 'goodtypeinfor',
    data() {
        return {
            searchkey: '',
            dialogFormVisible: false,
            newdialogFormVsible: false,
            goodstype: [],
            goodtype: {
                goodstypenum: '',
                goodstype: '',
                typedescribe: '',
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
                goodstypenum: [
                    { required: true, message: '请输入商品类别号', trigger: 'blur' },
                ],
                goodstype: [
                    { required: true, message: '请输入商品种类', trigger: 'blur' },
                ],
                typedescribe: [
                    { required: true, message: '请输入种类描述', trigger: 'blur' },
                ],
            },
        }
    },
    mounted() {
        listGoodsType().then(res => {
           this.goodstype = res.GoodsType
        })
    },
    methods: {
        // goodsearch() {
        //     // eslint-disable-next-line no-alert
        // },
        goodtypesearch() {
            searchGoodsType(this.searchkey)
            .then(res => {
              this.goodstype = res.GoodsType
                })
        },
        newgoodtype() {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.newdialogFormVsible = true
        },
        handleEdit(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.dialogFormVisible = true
            _this.goodtype.goodstypenum = row.goodstypenum
            _this.goodtype.goodstype = row.goodstype
            _this.goodtype.typedescribe = row.typedescribe
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
            _this.$confirm('确定要删除:' + row.goodstypenum + ' 号商品种类吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
              deleteGoodsType(row.goodstypenum)
              .then(res => {
                  if(res.status){
                        this.$message({
                        type: 'success',
                        message: '删除商品类别成功！'
                        })
                        listGoodsType().then(res => {
                        this.goodstype = res.GoodsType
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
      onSubmit(goodtype) {
           this.$refs[goodtype].validate((valid) => {
              if(valid){
                modifyGoodsType(this.goodtype.goodstypenum,this.goodtype.goodstype,this.goodtype.typedescribe)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '修改商品信息成功！'
                        })
                        this.dialogFormVisible = false
                        listGoodsType().then(res => {
                        this.goodstype = res.GoodsType
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
                newonSubmit(goodtype) {
           this.$refs[goodtype].validate((valid) => {
              if(valid){
                addGoodsType(this.goodtype.goodstypenum,this.goodtype.goodstype,this.goodtype.typedescribe)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '新增商品类别成功！'
                        })
                        this.newdialogFormVsible = false
                        listGoodsType().then(res => {
                        this.goodstype = res.GoodsType
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '新增商品类别失败！'
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
