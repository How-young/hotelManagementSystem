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
    <el-form-item label="员工编号" prop="eno">
        <el-input v-model="emp.eno" placeholder="员工编号"></el-input>
    </el-form-item>
    <el-form-item label="员工姓名" prop="name">
        <el-input v-model="emp.name" placeholder="员工姓名"></el-input>
    </el-form-item>
    <el-form-item label="员工类型" prop="type">
        <el-select v-model="emp.type" placeholder="员工类型" >
        <el-option label="清洁工" value="cleaner"></el-option>
        <el-option label="经理" value="manager"></el-option>
        <el-option label="服务员" value="waiter"></el-option>
        </el-select>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="newdialogFormVsible = false">取消</el-button>
        <el-button type="primary" @click="newonSubmit">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
     <!-- 表格显示 -->
    <el-table
        :data="tableData"
        height="250"
        border
        style="width: 100%">
        <el-table-column
        prop="eno"
        label="员工编号"
        width="300">
        </el-table-column>
        <el-table-column
        prop="name"
        label="姓名"
        width="300">
        </el-table-column>
        <el-table-column
        prop="type"
        label="类型"
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
    <!-- 修改对话框 -->
    <el-dialog title="修改员工信息"  :visible.sync="dialogFormVisible" center width="20%">
    <el-form :model="emp" :rules="rules" ref="emp" class="form-emp">
    <el-form-item label="员工姓名" prop="name">
        <el-input v-model="emp.name" placeholder="员工姓名"></el-input>
    </el-form-item>
    <el-form-item label="员工类型" prop="type">
        <el-select v-model="emp.type" placeholder="员工类型" >
        <el-option label="清洁工" value="cleaner"></el-option>
        <el-option label="经理" value="manager"></el-option>
        <el-option label="服务员" value="waiter"></el-option>
        </el-select>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="onSubmit">保存</el-button>
    </el-form-item>
    </el-form>
    </el-dialog>
    </div>
    </div>
</template>


<script>
export default {
    name: 'empinfor',
    data() {
        return {
            searchkey: '',
            dialogFormVisible: false,
            newdialogFormVsible: false,
            emp: {
                eno: '',
                name: '',
                type: '',
            },
            tableData: [
                {
                    name: 'John Brown',
                    eno: 18,
                    type: 'cleaner',
                },
                {
                    name: '大宝贝',
                    eno: 66,
                    type: 'manager',
                },
            ],
            rules: {
                eno: [
                    { required: true, message: '请输入员工编号', trigger: 'blur' },
                ],
                name: [
                    { required: true, message: '请输入姓名', trigger: 'blur' },
                ],
                type: [
                    { required: true, message: '请选择活动区域', trigger: 'change' },
                ],
            },
        }
    },
    methods: {
        empsearch() {
            // eslint-disable-next-line no-alert
        },
        newemp() {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.newdialogFormVsible = true
        },
        handleEdit(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.dialogFormVisible = true
            _this.emp.eno = row.eno
            _this.emp.name = row.name
            _this.emp.type = row.type
            // eslint-disable-next-line no-alert
        },
        handleDelete(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.$confirm('确定要删除:' + row.eno + ' 号员工吗吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
                // eslint-disable-next-line no-alert
                alert('fuck')
            }).catch()
        },
    },
}

</script>

<style scoped>

</style>
