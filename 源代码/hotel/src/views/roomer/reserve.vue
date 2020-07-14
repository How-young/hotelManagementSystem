<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
            <div class="query-c">
                <el-input placeholder="请输入预定者姓名" style="width: auto" v-model="searchkey"/>
                <el-button icon="el-icon-search" size="middle" @click="reserve_search()">查询</el-button>
                <el-button type="primary" icon="el-icon-circle-plus" size="small" @click="newReserve()" style="float:right"></el-button>
            </div>
        </div>

        <!-- 新增预定者表单 -->
        <el-dialog title="新增预定者" :visible.sync="newdialogFormVsible" center width="20%">
        <el-form :model="reserve" :rules="rules" ref="reserve" class="form-reserve">
        <el-form-item label="预定者" prop="name">
            <el-input v-model="reserve.name" placeholder="请输入预定者姓名" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="客房类型" prop="mold">
            <el-select v-model="reserve.mold" placeholder="客房类型" >
            <el-option label="单人房" value="single"></el-option>
            <el-option label="双人房" value="double"></el-option>
            <el-option label="大床房" value="queen"></el-option>
            <el-option label="三人房" value="triple"></el-option>
            <el-option label="标准套间" value="standard"></el-option>
            <el-option label="豪华套间" value="deluxe"></el-option>
            <el-option label="总统套间" value="presidential"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="预定时间" prop="time">
            <el-input v-model="reserve.time" :disabled="true"/>
        </el-form-item>
        <!-- <el-form-item label="客房类型" prop="mold">
            <el-input v-model="reserve.mold" placeholder="请输入客房类型"></el-input>
        </el-form-item> -->
        <el-form-item label="联系方式" prop="phone">
            <el-input v-model="reserve.phone" placeholder="请输入手机号"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="newdialogFormVsible = false">取消</el-button>
            <el-button type="primary" @click="newonSubmit">保存</el-button>
        </el-form-item>
        </el-form>
        </el-dialog>
        <!-- 表格显示 -->
        <el-table :data="tableData" height="250" border style="width: 100%">
            <el-table-column prop="name" label="预定者" width="300"> </el-table-column>
            <!-- <el-table-column prop="sex" label="性别" width="300"> </el-table-column> -->
            <!-- <el-table-column prop="email" label="邮箱" width="300"> </el-table-column> -->
            <el-table-column prop="time" label="预定时间" width="300"/>
            <el-table-column prop="mold" label="客房类型" width="300"> </el-table-column>
            <el-table-column prop="phone" label="联系方式" width="300"/>
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
        <el-dialog title="修改会员信息"  :visible.sync="dialogFormVisible" center width="20%">
        <el-form :model="reserve" :rules="rules" ref="reserve" class="form-reserve">
        <el-form-item label="预定者" prop="name">
            <el-input v-model="reserve.name" placeholder="预定者" :disabled="true"/>
        </el-form-item>
        <el-form-item label="客房类型" prop="mold">
            <el-select v-model="reserve.mold" placeholder="客房类型" >
            <el-option label="单人房" value="single"></el-option>
            <el-option label="双人房" value="double"></el-option>
            <el-option label="大床房" value="queen"></el-option>
            <el-option label="三人房" value="triple"></el-option>
            <el-option label="标准套间" value="standard"></el-option>
            <el-option label="豪华套间" value="deluxe"></el-option>
            <el-option label="总统套间" value="presidential"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="预定时间" prop="time">
            <el-input v-model="reserve.time"/>
        </el-form-item>
        <!-- <el-form-item label="客房类型" prop="mold">
            <el-input v-model="reserve.mold" placeholder="请输入类型"></el-input>
        </el-form-item> -->
        <el-form-item label="联系方式" prop="phone">
            <el-input v-model="reserve.phone" placeholder="请输入手机号"></el-input>
        </el-form-item>
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
    name: 'reserve',
    data() {
        return {
            searchkey: '',
            dialogFormVisible: false,
            newdialogFormVsible: false,
            reserve: {
                name: '',
                mold: '',
                time: '',
                // email: '',
                phone: '',
            },
            tableData: [
                {
                    name: 'John Brown',
                    mold: '单人房',
                    time: '2020-6-15',
                    phone: '18154561824',
                },
                {
                    name: '大宝贝',
                    mold: '标准套间',
                    time: '2020-6-15',
                    phone: '84561852462',
                },
            ],
            rules: {
                name: [
                    { required: true, message: '请输入姓名', trigger: 'blur' },
                ],
                time: [
                    { required: true, message: '请输入预定时间', trigger: 'blur' },
                ],
                mold: [
                    { required: true, message: '请选择房间类型', trigger: 'change' },
                ],
                phone: [
                    { required: true, message: '请输入手机号', trigger: 'blur' },
                ],
            },
        }
    },
    methods: {
        reserve_search() {
            // eslint-disable-next-line no-alert
        },
        newReserve() {
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
            _this.$confirm('确定要删除:' + row.name + ' 号员工吗吗?', '提示', {
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
