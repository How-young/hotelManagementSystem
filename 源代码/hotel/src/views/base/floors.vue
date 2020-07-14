<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
            <div class="query-c">
                <!-- <el-input placeholder="请输入会员姓名" style="width: auto" v-model="searchkey"/>
                <el-button icon="el-icon-search" size="middle" @click="member_search()">查询</el-button> -->
                <el-button type="primary" icon="el-icon-circle-plus" size="small" @click="newMember()" style="float:right"></el-button>
            </div>
        </div>

        <!-- 新增员工表单 -->
        <el-dialog title="新增楼层" :visible.sync="newdialogFormVsible" center width="20%">
        <el-form :model="floor" :rules="rules" ref="floor" class="form-floor">
        <el-form-item label="楼层号" prop="number">
            <el-input v-model="floor.number" placeholder="请输入楼层号"></el-input>
        </el-form-item>
        <!-- <el-form-item label="性别" prop="sex">
            <el-select v-model="member.sex" placeholder="性别" >
            <el-option label="男" value="male"></el-option>
            <el-option label="女" value="female"></el-option>
            </el-select>
        </el-form-item> -->
        <el-form-item label="描述" prop="desc">
            <el-input type="textarea" placeholder="请输入内容" v-model="floor.desc" maxlength="100" show-word-limit ></el-input>
        </el-form-item>
        <!-- <el-form-item label="邮箱" prop="email">
            <el-input v-model="member.email" placeholder="请输入邮箱"></el-input>
        </el-form-item>
        <el-form-item label="联系方式" prop="phone">
            <el-input v-model="member.phone" placeholder="请输入手机号"></el-input>
        </el-form-item> -->
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
            <el-table-column prop="number" label="楼层号" width="300"> </el-table-column>
            <el-table-column prop="desc" label="描述" width="1100"> </el-table-column>
            <!-- <el-table-column prop="email" label="邮箱" width="300"> </el-table-column>
            <el-table-column prop="time" label="注册时间" width="300"/>
            <el-table-column prop="phone" label="联系方式" width="300"/> -->
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
        <el-form-item label="楼层" prop="number">
            <el-input v-model="floor.number" placeholder="楼层"/>
        </el-form-item>
        <!-- <el-form-item label="性别" prop="sex">
            <el-select v-model="member.sex" placeholder="性别" >
            <el-option label="男" value="male"></el-option>
            <el-option label="女" value="female"></el-option>
            </el-select>
        </el-form-item> -->
        <el-form-item label="描述" prop="desc">
            <el-input type="textarea" placeholder="请输入内容" v-model="floor.desc" maxlength="100" show-word-limit ></el-input>
        </el-form-item>
        <!-- <el-form-item label="邮箱" prop="email">
            <el-input v-model="member.email" placeholder="请输入邮箱"></el-input>
        </el-form-item>
        <el-form-item label="联系方式" prop="phone">
            <el-input v-model="member.phone" placeholder="请输入手机号"></el-input>
        </el-form-item> -->
        <el-form-item>
            <el-button type="primary" @click="dialogFormVisible = false">取消</el-button>
            <el-button type="primary" @click="onSubmit">保存</el-button>
        </el-form-item>
        </el-form>
        </el-dialog>
    </div>
</template>


<script>
export default {
    name: 'floors',
    data() {
        return {
            searchkey: '',
            dialogFormVisible: false,
            newdialogFormVsible: false,
            floor: {
                number: '',
                desc: '',
                // time: '',
                // email: '',
                // phone: '',
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
                number: [
                    { required: true, message: '请输入楼层编号', trigger: 'blur' },
                ],
                email: [
                    { required: true, message: '请输入描述信息', trigger: 'blur' },
                ],
                // sex: [
                //     { required: true, message: '请选择活动区域', trigger: 'change' },
                // ],
                // phone: [
                //     { required: true, message: '请输入手机号', trigger: 'blur' },
                // ],
            },
        }
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
            _this.member.name = row.name
            _this.member.sex = row.sex
            _this.member.time = row.time
            _this.member.email = row.email
            _this.member.phone = row.phone
            // eslint-disable-next-line no-alert
        },
        handleDelete(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.$confirm('确定要删除:' + row.name + ' 层楼的信息吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
                // eslint-disable-next-line no-undef
                // rows.splice(index, 1)
                // eslint-disable-next-line no-alert
                alert('fuck')
            }).catch()
        },
    },
}

</script>
