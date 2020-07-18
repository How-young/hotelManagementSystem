<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
            <div class="query-c">
                <Input placeholder="请输入客房类型号" style="width: auto" v-model="searchkey"/>
                <el-button icon="el-icon-search" size="small" @click="roomtypesearch()">查询</el-button>
                <el-button type="primary" icon="el-icon-circle-plus" size="small" @click="newroomtype()" style="float:right"></el-button>
            </div>
    <!-- 新增客房类型表单 -->
    <el-dialog title="新增客房类型" :visible.sync="newdialogFormVsible" center width="20%">
    <el-form :model="roomtype" :rules="rules" ref="roomtype" class="form-roomtype">
    <el-form-item label="客房类型号" prop="roomtypenum">
        <el-input v-model="roomtype.roomtypenum" placeholder="客房类型号"></el-input>
    </el-form-item>
    <el-form-item label="客房类型" prop="roomtype">
        <el-input v-model="roomtype.roomtype" placeholder="客房类型"></el-input>
    </el-form-item>
        <el-form-item label="客房价格" prop="roomprice">
        <el-input v-model="roomtype.roomprice" placeholder="客房价格"></el-input>
    </el-form-item>
        <el-form-item label="客房数量" prop="roomquantity">
        <el-input v-model="roomtype.roomquantity" placeholder="客房数量"></el-input>
    </el-form-item>
            <el-form-item label="客房描述" prop="roomdescribe" >
        <el-input v-model="roomtype.roomdescribe" placeholder="客房描述"></el-input>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="newdialogFormVsible = false">取消</el-button>
        <el-button type="primary" @click="newonSubmit('roomtype')">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
     <!-- 表格显示 -->
    <el-table
        :data="roomtypes"
        height="750"
        border
        style="width: 100%">
        <el-table-column
        prop="roomtypenum"
        label="客房类型号"
        width="200">
        </el-table-column>
        <el-table-column
        prop="roomtype"
        label="客房类型"
        width="200">
        </el-table-column>
        <el-table-column
        prop="roomprice"
        label="客房价格"
        width="200">
        </el-table-column>
        <el-table-column
        prop="roomquantity"
        label="客房数量"
        width="200">
        </el-table-column>
                <el-table-column
        prop="roomdescribe"
        label="客房描述"
        width="700">
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
    <el-dialog title="修改客房类型信息"  :visible.sync="dialogFormVisible" center width="20%">
    <el-form :model="roomtype" :rules="rules" ref="roomtype" class="form-roomtype">
    <el-form-item label="客房类型号" prop="roomtypenum">
        <el-input v-model="roomtype.roomtypenum" placeholder="客房类型号"></el-input>
    </el-form-item>
    <el-form-item label="客房类型" prop="roomtype">
        <el-input v-model="roomtype.roomtype" placeholder="客房类型"></el-input>
    </el-form-item>
        <el-form-item label="客房价格" prop="roomprice">
        <el-input v-model="roomtype.roomprice" placeholder="客房价格"></el-input>
    </el-form-item>
        <el-form-item label="客房数量" prop="roomquantity">
        <el-input v-model="roomtype.roomquantity" placeholder="客房数量"></el-input>
    </el-form-item>
            <el-form-item label="客房描述" prop="roomdescribe">
        <el-input v-model="roomtype.roomdescribe" placeholder="客房描述"></el-input>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="onSubmit('roomtype')">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
    </div>
    </div>
</template>


<script>
import { listRoomType, modifyRoomType, addRoomType, searchRoomType, deleteRoomType } from '../apis'

export default {
    name: 'roomtypeinfor',
    data() {
        return {
            searchkey: '',
            dialogFormVisible: false,
            newdialogFormVsible: false,
            roomtypes: [],
            roomtype: {
                roomtypenum: '',
                roomtype: '',
                roomprice: '',
                roomquantity: '',
                roomdescribe: '',
            },
            rules: {
                roomtypenum: [
                    { required: true, message: '请输入客房类型号', trigger: 'blur' },
                ],
                roomtype: [
                    { required: true, message: '请输入客房类型', trigger: 'blur' },
                ],
                roomprice: [
                    { required: true, message: '请输入客房价格', trigger: 'blur' },
                ],
                roomquantity: [
                    { required: true, message: '请输入客房数量', trigger: 'blur' },
                ],
                roomdescribe: [
                    { required: true, message: '请输入客房描述', trigger: 'blur' },
                ],
            },
        }
    },
    mounted() {
        listRoomType().then(res => {
           this.roomtypes = res.RoomType
        })
    },
    methods: {
        // goodsearch() {
        //     // eslint-disable-next-line no-alert
        // },
        roomtypesearch() {
            searchRoomType(this.searchkey)
            .then(res => {
              this.roomtypes = res.RoomType
                })
        },
        newroomtype() {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.newdialogFormVsible = true
        },
        handleEdit(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.dialogFormVisible = true
            _this.roomtype.roomtypenum = row.roomtypenum
            _this.roomtype.roomtype = row.roomtype
            _this.roomtype.roomprice = row.roomprice
            _this.roomtype.roomquantity = row.roomquantity
            _this.roomtype.roomdescribe = row.roomdescribe
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
            _this.$confirm('确定要删除:' + row.roomtypenum + ' 号客房类型吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
              deleteRoomType(row.roomtypenum)
              .then(res => {
                  if(res.status){
                        this.$message({
                        type: 'success',
                        message: '删除客房成功！'
                        })
                        listRoomType().then(res => {
                        this.roomtypes = res.RoomType
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
      onSubmit(roomtype) {
           this.$refs[roomtype].validate((valid) => {
              if(valid){
                modifyRoomType(this.roomtype.roomtypenum,this.roomtype.roomtype,this.roomtype.roomprice,this.roomtype.roomquantity,this.roomtype.roomdescribe)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '修改客房信息成功！'
                        })
                        this.dialogFormVisible = false
                        listRoomType().then(res => {
                        this.roomtypes = res.RoomType
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
                newonSubmit(roomtype) {
           this.$refs[roomtype].validate((valid) => {
              if(valid){
                addRoomType(this.roomtype.roomtypenum,this.roomtype.roomtype,this.roomtype.roomprice,this.roomtype.roomquantity,this.roomtype.roomdescribe)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '新增客房成功！'
                        })
                        this.newdialogFormVsible = false
                        listRoomType().then(res => {
                        this.roomtypes = res.RoomType
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
