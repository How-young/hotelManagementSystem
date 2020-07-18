<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
            <div class="query-c">
                <el-input placeholder="请输入会员号" style="width: auto" v-model="searchkey"/>
                <el-button icon="el-icon-search" size="middle" @click="member_search()">查询</el-button>
                <el-button type="primary" icon="el-icon-circle-plus" size="small" @click="newMember()" style="float:right"></el-button>
            </div>
        </div>

        <!-- 新增员工表单 -->
        <el-dialog title="新增会员" :visible.sync="newdialogFormVsible" center width="20%">
        <el-form :model="member" :rules="rules" ref="member" class="form-member">
        <el-form-item label="姓名" prop="vipname">
            <el-input v-model="member.vipname" placeholder="请输入会员姓名"></el-input>
        </el-form-item>
        <el-form-item label="会员号" prop="vipnum">
            <el-input v-model="member.vipnum" placeholder="请输入会员号"></el-input>
        </el-form-item>
        <el-form-item label="身份证号" prop="idcard">
            <el-input v-model="member.idcard" placeholder="请输入会员身份证号"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="vipsex">
            <el-select v-model="member.vipsex" placeholder="性别" >
            <el-option label="男" value="male"></el-option>
            <el-option label="女" value="female"></el-option>
            </el-select>
        </el-form-item>
        <!-- <el-form-item label="注册时间" prop="registertime">
            <el-input v-model="member.registertime" :disabled="true"/>
        </el-form-item> -->
        <el-form-item label="邮箱" prop="vipemail">
            <el-input v-model="member.vipemail" placeholder="请输入邮箱"></el-input>
        </el-form-item>
        <el-form-item label="联系方式" prop="vipphone">
            <el-input v-model="member.vipphone" placeholder="请输入手机号"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="newdialogFormVsible = false">取消</el-button>
            <el-button type="primary" @click="newMemberSubmit('member')">提交</el-button>
        </el-form-item>
        </el-form>
        </el-dialog>
        <!-- 表格显示 -->
        <el-table
            :data="vip"
            height="700"
            border
            style="width: 100%">
            <el-table-column prop="vipname" label="姓名" width="100"> </el-table-column>
            <el-table-column prop="vipnum" label="会员号" width="100"> </el-table-column>
            <el-table-column prop="idcard" label="身份证号" width="200"> </el-table-column>
            <el-table-column prop="vipsex" label="性别" width="100"> </el-table-column>
            <el-table-column prop="vipemail" label="邮箱" width="250"> </el-table-column>
            <el-table-column prop="registertime" label="注册时间" width="200"/>
            <el-table-column prop="vipphone" label="联系方式" width="250"/>
            <el-table-column fixed="right" label="操作" width="150">
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
        <el-form :model="member" :rules="rules" ref="member" class="form-member">
        <el-form-item label="姓名" prop="vipname">
            <el-input v-model="member.vipname" placeholder="姓名" :disabled="true"/>
        </el-form-item>
        <el-form-item label="会员号" prop="vipnum">
            <el-input v-model="member.vipnum" placeholder="会员号" :disabled="true"/>
        </el-form-item>
        <el-form-item label="身份证号" prop="idcard">
            <el-input v-model="member.idcard" placeholder="会员号" :disabled="true"/>
        </el-form-item>
        <el-form-item label="性别" prop="vipsex">
            <el-select v-model="member.vipsex" placeholder="性别" >
            <el-option label="男" value="男"></el-option>
            <el-option label="女" value="女"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="注册时间" prop="registertime">
            <el-input v-model="member.registertime" :disabled="true"/>
        </el-form-item>
        <el-form-item label="邮箱" prop="vipemail">
            <el-input v-model="member.vipemail" placeholder="请输入邮箱"></el-input>
        </el-form-item>
        <el-form-item label="联系方式" prop="vipphone">
            <el-input v-model="member.vipphone" placeholder="请输入手机号"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="dialogFormVisible = false">取消</el-button>
            <el-button type="primary" @click="editVipSubmit('member')">保存</el-button>
        </el-form-item>
        </el-form>
        </el-dialog>
    </div>
</template>


<script>
import {vipList, searchVip, addVip, deleteVip, modifyVip} from '../apis/index'

export default {
    name: 'members',
    data() {
        return {
            searchkey: '',
            dialogFormVisible: false,
            newdialogFormVsible: false,
            vip: [],
            member: {
                vipname: '',
                vipnum: '',
                idcard: '',
                vipsex: '',
                registertime: '',
                vipemail: '',
                vipphone: '',
            },
            tableData: [
                {
                    name: 'John Brown',
                    number: '5461561564',
                    idcard: '45450515151515154',
                    sex: '男',
                    time: '2020-6-15',
                },
                {
                    name: '大宝贝',
                    sex: '女',
                    time: '2050-5-48',
                },
            ],
            rules: {
                vipemail: [
                    { required: true, message: '请输入邮箱', trigger: 'blur' },
                ],
                vipsex: [
                    { required: true, message: '请选择活动区域', trigger: 'change' },
                ],
                vipphone: [
                    { required: true, message: '请输入手机号', trigger: 'blur' },
                ],
            },
        }
    },
    mounted() {
      vipList().then(res => {
           this.vip = res.Vip
        })
    },
    methods: {
        member_search() {
            // eslint-disable-next-line no-alert
            searchVip(this.searchkey)
            .then(res => {
              this.vip = res.Vip
                })
        },
        newMember() {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.newdialogFormVsible = true
        },
        newMemberSubmit(member) {
          this.$refs[member].validate((valid) =>{
              if(valid){
                addVip(this.member.vipname, this.member.vipnum, this.member.idcard, this.member.vipsex, this.member.vipemail, this.member.vipphone)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '新增会员成功！'
                        })
                        this.newdialogFormVsible = false
                        vipList().then(res => {
                        this.vip = res.Vip
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '新增会员失败！'
                        })
                    }
                 })
              }
           })
        },
        editVipSubmit(member){
           this.$refs[member].validate((valid) =>{
              if(valid){
                modifyVip(this.member.vipname, this.member.vipnum, this.member.idcard, this.member.vipsex, this.member.vipemail, this.member.vipphone, this.member.registertime)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '修改会员信息成功！'
                        })
                        this.dialogFormVisible = false
                        vipList().then(res => {
                        this.vip = res.Vip
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '修改会员信息失败！'
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
            _this.member.vipname = row.vipname
            _this.member.vipnum = row.vipnum
            _this.member.idcard = row.idcard
            _this.member.vipsex = row.vipsex
            _this.member.registertime = row.registertime
            _this.member.vipemail = row.vipemail
            _this.member.vipphone = row.vipphone
            // eslint-disable-next-line no-alert
        },
        handleDelete(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.$confirm('确定要删除:' + row.vipnum + ' 号会员吗吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
              deleteVip(row.vipnum)
              .then(res => {
                  if(res.status){
                        this.$message({
                        type: 'success',
                        message: '删除会员成功！'
                        })
                        vipList().then(res => {
                        this.vip = res.Vip
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
