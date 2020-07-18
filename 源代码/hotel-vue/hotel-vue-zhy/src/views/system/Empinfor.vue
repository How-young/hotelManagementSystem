<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
            <div class="query-c">
                <Input placeholder="请输入员工号或员工姓名" style="width: auto" v-model="searchkey"/>
                <el-button icon="el-icon-search" size="small" @click="empsearch()">查询</el-button>
                <el-button type="primary" icon="el-icon-circle-plus" size="small" @click="newemp()" style="float:right"></el-button>
            </div>
    <!-- 新增员工表单 -->
    <el-dialog title="新增员工" :visible.sync="newdialogFormVsible" center width="20%">
    <el-form :model="emp" :rules="rules" ref="emp" class="form-emp">
    <el-form-item label="员工编号" prop="employeenum">
        <el-input v-model="emp.employeenum" placeholder="员工编号"></el-input>
    </el-form-item>
    <el-form-item label="员工姓名" prop="employeename">
        <el-input v-model="emp.employeename" placeholder="员工姓名"></el-input>
    </el-form-item>
    <el-form-item label="员工密码" prop="employeepassword">
        <el-input v-model="emp.employeepassword" placeholder="员工密码"></el-input>
    </el-form-item>
    <el-form-item label="员工邮箱" prop="employeemail">
        <el-input type="email" v-model="emp.employeemail" placeholder="员工邮箱" ></el-input>
    </el-form-item>
    <el-form-item label="员工性别" prop="employeesex">
        <el-select v-model="emp.employeesex" placeholder="员工性别" >
        <el-option label="男" value="男"></el-option>
        <el-option label="女" value="女"></el-option>
        </el-select>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="newdialogFormVsible = false">取消</el-button>
        <el-button type="primary" @click="newempSubmit('emp')">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
     <!-- 表格显示 -->
    <el-table
        :data="employee"
        height="400"
        border
        style="width: 100%">
        <el-table-column
        prop="employeenum"
        label="员工编号"
        width="200">
        </el-table-column>
        <el-table-column
        prop="employeemail"
        label="员工邮箱"
        width="200">
        </el-table-column>
        <el-table-column
        prop="employeepassword"
        label="员工密码"
        width="200">
        </el-table-column>
        <el-table-column
        prop="employeename"
        label="员工姓名"
        width="200">
        </el-table-column>
        <el-table-column
        prop="employeesex"
        label="员工性别"
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
    <el-dialog title="修改员工信息"  :visible.sync="dialogFormVisible" center width="20%">
    <el-form :model="emp" :rules="rules" ref="emp" class="form-emp">
    <el-form-item label="员工编号" prop="employeenum">
        <el-input v-model="emp.employeenum" placeholder="员工编号" readonly="readonly"></el-input>
    </el-form-item>
    <el-form-item label="员工姓名" prop="employeename">
        <el-input v-model="emp.employeename" placeholder="员工姓名"></el-input>
    </el-form-item>
    <el-form-item label="员工密码" prop="employeepassword">
        <el-input v-model="emp.employeepassword" placeholder="员工密码"></el-input>
    </el-form-item>
    <el-form-item label="员工邮箱" prop="employeemail">
        <el-input type="email" v-model="emp.employeemail" placeholder="员工邮箱" ></el-input>
    </el-form-item>
    <el-form-item label="员工性别" prop="employeesex">
        <el-select v-model="emp.employeesex" placeholder="员工性别" >
        <el-option label="男" value="男"></el-option>
        <el-option label="女" value="女"></el-option>
        </el-select>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="editempSubmit('emp')">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
    </div>
    </div>
</template>


<script>
import { listEmp, addEmp ,deleteEmp, modifyEmp,searchEmp} from '../apis/index'

export default {
    name: 'empinfor',
    data() {
        return {
            searchkey: '',
            dialogFormVisible: false,
            newdialogFormVsible: false,
            employee: [],
            emp: {
                employeenum: '',
                employeemail: '',
                employeepassword: '',
                employeename: '',
                employeesex: '',
            },
            rules: {
                employeenum: [
                    { required: true, message: '请输入员工编号', trigger: 'blur' },
                ],
                employeename: [
                    { required: true, message: '请输入员工姓名', trigger: 'blur' },
                ],
                employeesex: [
                    { required: true, message: '请输入员工性别', trigger: 'change' },
                ],
                employeemail: [
                    { required: true, message: '请输入员工邮箱', trigger: 'blur' },
                    { type: 'email', message: '请输入正确的邮箱格式', trigger: 'blur' },
                ],
                employeepassword: [
                    { required: true, message: '请输入员工密码', trigger: 'blur' },
                ],
            },
        }
    },
    mounted() {
        listEmp().then(res => {
           this.employee = res.Employee
        })
    },
    methods: {
        empsearch() {
            searchEmp(this.searchkey)
            .then(res => {
              this.employee = res.Employee
                })
        },
        newemp() {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.newdialogFormVsible = true
        },
        editempSubmit(emp){
           this.$refs[emp].validate((valid) =>{
              if(valid){
                modifyEmp(this.emp.employeenum,this.emp.employeemail,this.emp.employeepassword,this.emp.employeename,this.emp.employeesex)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '修改员工信息成功！'
                        })
                        this.dialogFormVisible = false
                        listEmp().then(res => {
                        this.employee = res.Employee
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '修改员工信息失败！'
                        })
                    }
                 })
              }
           })
        },
        newempSubmit(emp){
           this.$refs[emp].validate((valid) =>{
              if(valid){
                addEmp(this.emp.employeenum,this.emp.employeemail,this.emp.employeepassword,this.emp.employeename,this.emp.employeesex)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '新增员工成功！'
                        })
                        this.newdialogFormVsible = false
                        listEmp().then(res => {
                        this.employee = res.Employee
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '新增员工失败！'
                        })
                    }
                 })
              }
           })
        },
        handleEdit(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.dialogFormVisible = true
            _this.emp.employeenum = row.employeenum
            _this.emp.employeename = row.employeename
            _this.emp.employeepassword = row.employeepassword
            _this.emp.employeesex = row.employeesex
            _this.emp.employeemail = row.employeemail
            // eslint-disable-next-line no-alert
        },
        handleDelete(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.$confirm('确定要删除:' + row.employeenum + ' 号员工吗吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
              deleteEmp(row.employeenum)
              .then(res => {
                  if(res.status){
                        this.$message({
                        type: 'success',
                        message: '删除员工成功！'
                        })
                        listEmp().then(res => {
                        this.employee = res.Employee
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
    },
}

</script>

<style scoped>

</style>
