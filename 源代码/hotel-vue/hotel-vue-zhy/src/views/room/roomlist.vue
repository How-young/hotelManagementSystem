<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
            <div class="query-c">
                <Input placeholder="请输入客房号" style="width: auto" v-model="searchkey"/>
                <el-button icon="el-icon-search" size="small" @click="roomsearch()">查询</el-button>
                <el-button type="primary" icon="el-icon-circle-plus" size="small" @click="newroom()" style="float:right"></el-button>
            </div>
    <!-- 新增客房表单 -->
    <el-dialog title="新增客房" :visible.sync="newdialogFormVsible" center width="20%">
    <el-form :model="room" :rules="rules" ref="room" class="form-room">
    <el-form-item label="客房编号" prop="roomsnum">
        <el-input v-model="room.roomnum" placeholder="客房编号"></el-input>
    </el-form-item>
    <el-form-item label="客房类别号" prop="roomtypenum">
        <el-input v-model="room.roomtypenum" placeholder="客房类别号"></el-input>
    </el-form-item>
        <el-form-item label="客房状态" prop="isempty" >
        <el-input v-model="room.isempty" placeholder="客房状态" readonly="readonly"></el-input>
    </el-form-item>
        <el-form-item label="客房楼层" prop="roomfloor">
        <el-input v-model="room.roomfloor" placeholder="客房楼层"></el-input>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="newdialogFormVsible = false">取消</el-button>
        <el-button type="primary" @click="newonSubmit('room')">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
     <!-- 表格显示 -->
    <el-table
        :data="rooms"
        height="550"
        border
        style="width: 100%">
        <el-table-column
        prop="roomnum"
        label="客房编号"
        width="200">
        </el-table-column>
        <el-table-column
        prop="roomtypenum"
        label="客房类别号"
        width="200">
        </el-table-column>
        <el-table-column
        prop="isempty"
        label="客房状态"
        width="200">
        </el-table-column>
        <el-table-column
        prop="roomfloor"
        label="客房楼层"
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
    <el-dialog title="修改客房信息"  :visible.sync="dialogFormVisible" center width="20%">
    <el-form :model="room" :rules="rules" ref="room" class="form-room">
    <el-form-item label="客房编号" prop="roomnum">
        <el-input v-model="room.roomnum" placeholder="客房编号"></el-input>
    </el-form-item>
    <el-form-item label="客房类别号" prop="roomtypenum">
        <el-input v-model="room.roomtypenum" placeholder="客房类别号" readonly="readonly"></el-input>
    </el-form-item>
        <el-form-item label="客房状态" prop="isempty">
        <el-input v-model="room.isempty" placeholder="客房状态" readonly="readonly"></el-input>
    </el-form-item>
        <el-form-item label="客房楼层" prop="roomfloor">
        <el-input v-model="room.roomfloor" placeholder="客房楼层"></el-input>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="onSubmit('room')">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
    </div>
    </div>
</template>


<script>
import { listRoom, modifyRoom, addRoom, searchRoom, deleteRoom } from '../apis'

export default {
    name: 'roominfor',
    data() {
        return {
            searchkey: '',
            dialogFormVisible: false,
            newdialogFormVsible: false,
            rooms: [],
            room: {
                roomnum: '',
                roomtypenum: '',
                isempty: '',
                roomfloor: '',
            },
            rules: {
                roomnum: [
                    { required: true, message: '请输入客房号', trigger: 'blur' },
                ],
                roomtypenum: [
                    { required: true, message: '请输入客房类别号', trigger: 'blur' },
                ],
                isempty: [
                    { required: true, message: '请输入客房状态', trigger: 'blur' },
                ],
                roomfloor: [
                    { required: true, message: '请输入客房楼层', trigger: 'blur' },
                ],
            },
        }
    },
    mounted() {
        listRoom().then(res => {
           this.rooms = res.Room
        })
    },
    methods: {
        // goodsearch() {
        //     // eslint-disable-next-line no-alert
        // },
        roomsearch() {
            searchRoom(this.searchkey)
            .then(res => {
              this.rooms = res.Room
                })
        },
        newroom() {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.newdialogFormVsible = true
            _this.room.isempty = 1
        },
        handleEdit(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.dialogFormVisible = true
            _this.room.roomnum = row.roomnum
            _this.room.roomtypenum = row.roomtypenum
            _this.room.isempty = row.isempty
            _this.room.roomfloor = row.roomfloor
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
            _this.$confirm('确定要删除:' + row.roomnum + ' 号客房吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
              deleteRoom(row.roomnum)
              .then(res => {
                  if(res.status){
                        this.$message({
                        type: 'success',
                        message: '删除客房成功！'
                        })
                        listRoom().then(res => {
                        this.rooms = res.Room
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
      onSubmit(room) {
           this.$refs[room].validate((valid) => {
              if(valid){
                modifyRoom(this.room.roomnum,this.room.roomtypenum,this.room.isempty,this.room.roomfloor)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '修改客房信息成功！'
                        })
                        this.dialogFormVisible = false
                        listRoom().then(res => {
                        this.rooms = res.Room
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
                newonSubmit(room) {
           this.$refs[room].validate((valid) => {
              if(valid){
                addRoom(this.room.roomnum,this.room.roomtypenum,this.room.isempty,this.room.roomfloor)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '新增客房成功！'
                        })
                        this.newdialogFormVsible = false
                        listRoom().then(res => {
                        this.rooms = res.Room
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
