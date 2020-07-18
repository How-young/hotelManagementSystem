<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; height: 30px;">
            <el-button type="primary" icon="el-icon-circle-plus" size="small" @click="newMember()" style="float:right"></el-button>
        </div>

        <!-- 新增员工表单 -->
        <el-dialog title="新增楼层" :visible.sync="newdialogFormVsible" center width="20%">
        <el-form :model="floor" :rules="rules" ref="floor" class="form-floor">
        <el-form-item label="楼层号" prop="floornum">
            <el-input v-model="floor.floornum" placeholder="请输入楼层号"></el-input>
        </el-form-item>
        <el-form-item label="描述" prop="floordescribe">
            <el-input type="textarea" placeholder="请输入内容" v-model="floor.floordescribe" maxlength="100" show-word-limit ></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="newdialogFormVsible = false">取消</el-button>
            <el-button type="primary" @click="newFloorSubmit('floor')">提交</el-button>
        </el-form-item>
        </el-form>
        </el-dialog>
        <!-- 表格显示 -->
        <el-table
            :data="level"
            height="700"
            border
            style="width: 100%">
            <el-table-column prop="floornum" label="楼层号" width="300"> </el-table-column>
            <el-table-column prop="floordescribe" label="描述" width="1100"> </el-table-column>
            <el-table-column fixed="right" label="操作">
                <template slot-scope="scope">
                    <el-button type="danger"  @click.native.prevent="handleDelete(scope.$index,scope.row)"
                    icon="el-icon-delete" circle></el-button>
                    <el-button type="primary" @click.native.prevent="handleEdit(scope.$index,scope.row)"
                    icon="el-icon-edit" circle></el-button>
                </template>
            </el-table-column>
        </el-table>
        <!-- 修改对话框 -->
        <el-dialog title="修改楼层信息"  :visible.sync="dialogFormVisible" center width="20%">
        <el-form :model="floor" :rules="rules" ref="floor" class="form-floor">
        <el-form-item label="楼层" prop="floornum" disabled="true">
            <el-input v-model="floor.floornum" placeholder="楼层"/>
        </el-form-item>
        <el-form-item label="描述" prop="floordescribe">
            <el-input type="textarea" placeholder="请输入内容" v-model="floor.floordescribe" maxlength="100" show-word-limit ></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="dialogFormVisible = false">取消</el-button>
            <el-button type="primary" @click="editFloorSubmit('floor')">保存</el-button>
        </el-form-item>
        </el-form>
        </el-dialog>
    </div>
</template>

<script>
import {floorList, addFloor, modifyFloor, deleteFloor} from '../apis/index'

export default {
  name: 'floors',
  data () {
    return {
      searchkey: '',
      dialogFormVisible: false,
      newdialogFormVsible: false,
      level: [],
      floor: {
        floornum: '',
        floordescribe: '',
      },
      tableData: [
              {
                  number: 'John Brown',
                  // sex: '男',
                  desc: '2020-6-15',
              },
              {
                  number: '大宝贝',
                  // sex: '女',
                  desc: '2050-5-48',
              },
          ],
          rules: {
              floornum: [
                  { required: true, message: '请输入楼层编号', trigger: 'blur' },
              ],
              floordescribe: [
                  { required: true, message: '请输入描述信息', trigger: 'blur' },
              ],
          },
      }
  },
  mounted() {
        floorList().then(res => {
           this.level = res.Floor
        })
    },
  methods: {
      member_search() {
          // eslint-disable-next-line no-alert
      },
      newMember() {
        // eslint-disable-next-line no-underscore-dangle
        let _this = this
        _this.newdialogFormVsible = true
    },
    handleEdit(index, row) {
        // eslint-disable-next-line no-underscore-dangle
        let _this = this
        _this.dialogFormVisible = true
        _this.floor.floornum = row.floornum
        _this.floor.floordescribe = row.floordescribe
        // eslint-disable-next-line no-alert
    },
    newFloorSubmit(floor){
      this.$refs[floor].validate((valid) =>{
              if(valid){
                addFloor(this.floor.floornum, this.floor.floordescribe)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '新增楼层成功！'
                        })
                        this.newdialogFormVsible = false
                        floorList().then(res => {
                        this.level = res.Floor
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '新增楼层失败！'
                        })
                    }
                 })
              }
           })
    },
    editFloorSubmit(floor){
      this.$refs[floor].validate((valid) =>{
              if(valid){
                modifyFloor(this.floor.floornum, this.floor.floordescribe)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '修改楼层成功！'
                        })
                        this.dialogFormVisible = false
                        floorList().then(res => {
                        this.level = res.Floor
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '修改楼层失败！'
                        })
                    }
                 })
              }
           })
    },
    handleDelete(index, row) {
      // eslint-disable-next-line no-underscore-dangle
      let _this = this
      _this.$confirm('确定要删除:' + row.floornum + ' 号楼层吗?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
      }).then(() => {
        deleteFloor(row.floornum)
        .then(res => {
            if(res.status){
                  this.$message({
                  type: 'success',
                  message: '删除楼层成功！'
                  })
                  floorList().then(res => {
                  this.level = res.Floor
                  })
            }
            else{
                  this.$message({
                  type: 'warning',
                  message: '删除楼层失败！'
      })
            }
        })
      }).catch()
    }
  }
}

</script>
