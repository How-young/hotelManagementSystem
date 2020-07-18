<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
        <el-switch
        style="display: block"
        v-model="value"
        active-color="#13ce66"
        inactive-color="#ff4949"
        active-text="剩余可预订房间管理"
        inactive-text="预定管理">
        </el-switch>
      <el-table
        :data="bookroom"
        height="550"
        border
        v-show="value"
        style="width: 100%">
        <el-table-column
            prop="roomdescribe"
            label="房间描述"
            width="150">
        </el-table-column>
        <el-table-column
            prop="roomfloor"
            label="楼层"
            width="150">
        </el-table-column>
        <el-table-column
            prop="roomnum"
            label="房间号"
            width="200">
        </el-table-column>
        <el-table-column
            prop="roomprice"
            label="价格"
            width="200">
        </el-table-column>
        <el-table-column
            prop="roomquantity"
            label="该类型房间数量"
            width="200">
        </el-table-column>
        <el-table-column
            prop="roomtype"
            label="房间类型"
            width="200">
        </el-table-column>
        <el-table-column
        fixed="right"
        label="操作">
        <template slot-scope="scope">
            <el-button type="primary" @click.native.prevent="handleBook(scope.$index,scope.row)" >预定该房间</el-button>
            <el-button type="primary" @click.native.prevent="handleCheckIn(scope.$index,scope.row)" >入住该房间</el-button>
        </template>
        </el-table-column>
   </el-table>
    <!-- 已预定房间报表 -->
    <div>
    <el-table
        :data="alreadybook"
        v-show="!value"
        height="750"
        border
        style="width: 100%">
        <el-table-column
            prop="stayroom"
            label="房间号"
            width="150">
        </el-table-column>
        <el-table-column
            prop="idcard"
            label="身份证"
            width="150">
        </el-table-column>
        <el-table-column
            prop="tenantname"
            label="姓名"
            width="150">
        </el-table-column>
        <el-table-column
            prop="tenantsex"
            label="性别"
            width="150">
        </el-table-column>
        <el-table-column
            prop="checkin"
            label="预计入住时间"
            width="300">
        </el-table-column>
        <el-table-column
            prop="checkout"
            label="预计离店时间"
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
    </div>
       <!-- 预定管理表单 -->
    <el-dialog title="修改预定信息" :visible.sync="bookerdialogFormVsible" center width="50%">
        <el-form :model="bookerMan" :rules="rules" ref="bookerMan" class="form-bookerMan">
        <el-form-item label="身份证号" prop="idcard">
            <el-input v-model="bookerMan.idcard" placeholder="身份证号" readonly="readonly"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="tenantname">
            <el-input v-model="bookerMan.tenantname" placeholder="员工姓名"></el-input>
        </el-form-item>
        <el-form-item label="居住时间" prop="daterange" >
        <el-date-picker
        v-model="bookerMan.daterange"
        format="yyyy-MM-dd"
        value-format="yyyy-MM-dd"
        type="daterange"
        range-separator="至"
        start-placeholder="原来的日期"
        end-placeholder="原来的日期">
        </el-date-picker>
        </el-form-item>
        <el-form-item label="预定人性别" prop="tenantsex">
            <el-select v-model="bookerMan.tenantsex" placeholder="性别" >
            <el-option label="男" value="男"></el-option>
            <el-option label="女" value="女"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="bookerdialogFormVsible = false">取消</el-button>
            <el-button type="primary" @click="bookeditSubmit('bookerMan')">保存</el-button>
        </el-form-item>
        </el-form>
    </el-dialog>
   <!-- 预定该房间表单 -->
    <el-dialog title="预定该房间" :visible.sync="bookdialogFormVsible" center width="50%">
        <el-form :model="bookThis" :rules="rules" ref="bookThis" class="form-bookThis">
        <el-form-item label="身份证号" prop="idcard">
            <el-input v-model="bookThis.idcard" placeholder="身份证号"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="tenantname">
            <el-input v-model="bookThis.tenantname" placeholder="姓名"></el-input>
        </el-form-item>
        <el-form-item label="居住时间" prop="daterange" >
        <el-date-picker
        format="yyyy-MM-dd "
        value-format="yyyy-MM-dd"
        v-model="bookThis.daterange"
        type="daterange"
        range-separator="至"
        start-placeholder="开始日期"
        end-placeholder="结束日期">
        </el-date-picker>
        </el-form-item>
        <el-form-item label="预定人性别" prop="tenantsex">
            <el-select v-model="bookThis.tenantsex" placeholder="员工性别" >
            <el-option label="男" value="男"></el-option>
            <el-option label="女" value="女"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="bookerdialogFormVsible = false">取消</el-button>
            <el-button type="primary" @click="bookSubmit('bookThis')">保存</el-button>
        </el-form-item>
        </el-form>
    </el-dialog>
    <!-- 入住该房间 -->
    <el-dialog title="入住该房间" :visible.sync="CheckIndialogFormVsible" center width="50%">
        <el-form :model="checkThis" :rules="rules" ref="checkThis" class="form-checkThis">
        <el-form-item label="身份证号" prop="idcard">
            <el-input v-model="checkThis.idcard" placeholder="身份证号"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="tenantname">
            <el-input v-model="checkThis.tenantname" placeholder="姓名"></el-input>
        </el-form-item>
        <el-form-item label="退房时间" prop="checkout" >
          <el-date-picker v-model="checkThis.checkout"        
           format="yyyy-MM-dd"
           value-format="yyyy-MM-dd" type="date" placeholder="选择日期"></el-date-picker>
        <!-- <el-date-picker
        format="yyyy-MM-dd "
        value-format="yyyy-MM-dd"
        v-model="checkThis.daterange"
        type="daterange"
        range-separator="至"
        start-placeholder="开始日期"
        end-placeholder="结束日期">
        </el-date-picker> -->
        </el-form-item>
        <el-form-item label="预定人性别" prop="tenantsex">
            <el-select v-model="checkThis.tenantsex" placeholder="员工性别" >
            <el-option label="男" value="男"></el-option>
            <el-option label="女" value="女"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="CheckIndialogFormVsible = false">取消</el-button>
            <el-button type="primary" @click="checkSubmit('checkThis')">保存</el-button>
        </el-form-item>
        </el-form>
    </el-dialog>
    </div>
    </div>
</template>

<script>
import {listbookavible , bookavible , listbookalready ,editbookavible ,deletebook, check} from '../apis/index'
export default {
    name: 'Boolinfor',
    data() {
        return{
            bookdialogFormVsible: false,
            bookerdialogFormVsible: false,
            CheckIndialogFormVsible: false,
            bookroom: [],
            alreadybook: [],
            value: true,
            bookThis: {
                idcard: '',
                stayroom: '',
                tenantname: '',
                tenantsex: '',
                daterange: '',
            },
            bookerMan: {
                idcard: '',
                stayroom: '',
                tenantname: '',
                tenantsex: '',
                daterange: '',
            },
            checkThis: {
                idcard: '',
                stayroom: '',
                tenantname: '',
                tenantsex: '',
                checkout: '',
            },
            rules: {
                idcard: [
                    { required: true, message: '请输入身份证号', trigger: 'blur' },
                ],
                tenantname: [
                    { required: true, message: '请输入姓名', trigger: 'blur' },
                ],
                tenantsex: [
                    { required: true, message: '请输入性别', trigger: 'change' },
                ],
                daterange: [
                    { required: true, message: '请选择时间范围', trigger: 'blur' },
                ],
                checkout: [
                    {  required: true, message: '请选择退房时间', trigger: 'blur' },
                ],
            },
        }
    },
    mounted() {
        listbookavible().then(res => {
           this.bookroom = res.CanBookRoom
        })
        listbookalready().then(res => {
            this.alreadybook = res.BookRoom
        })
    },
    methods: {
        handleBook(index, row){
            let _this = this
            _this.bookThis.stayroom = row.roomnum
            _this.bookdialogFormVsible = true
        },
        handleCheckIn(index, row){
            let _this = this
            _this.checkThis.stayroom = row.roomnum
            _this.CheckIndialogFormVsible = true
            // alert(_this.CheckIndialogFormVsible)
        },
        bookSubmit(bookThis){
           this.$refs[bookThis].validate((valid) =>{
              if(valid){
                bookavible(this.bookThis.idcard,this.bookThis.stayroom,this.bookThis.tenantname,this.bookThis.tenantsex,this.bookThis.daterange)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '预定成功！'
                        })
                        this.bookdialogFormVsible = false
                        listbookavible().then(res => {
                            this.bookroom = res.CanBookRoom
                        })
                        listbookalready().then(res => {
                            this.alreadybook = res.BookRoom
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '预定失败！'
                        })
                    }
                 })
              }
           })
        },
        checkSubmit(checkThis){
          this.$refs[checkThis].validate((valid) =>{
              if(valid){
                check(this.checkThis.idcard,this.checkThis.stayroom,this.checkThis.tenantname,this.checkThis.tenantsex,this.checkThis.checkout)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '入住成功！'
                        })
                        this.CheckIndialogFormVsible = false
                        listbookavible().then(res => {
                            this.bookroom = res.CanBookRoom
                        })
                        listbookalready().then(res => {
                            this.alreadybook = res.BookRoom
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '入住失败！'
                        })
                    }
                 })
              }
           })
        },
        handleEdit(index , row){
            let _this = this
            _this.bookerMan.stayroom = row.stayroom
            _this.bookerMan.idcard = row.idcard
            _this.bookerMan.tenantname = row.tenantname
            _this.bookerMan.tenantsex = row.tenantsex
            _this.bookerMan.daterange = row.checkin +','+ row.checkout
            _this.bookerdialogFormVsible = true
        },
        bookeditSubmit(bookerMan){
           this.$refs[bookerMan].validate((valid) =>{
              if(valid){
                editbookavible(this.bookerMan.idcard,this.bookerMan.tenantname,this.bookerMan.tenantsex,this.bookerMan.daterange)
                .then(res => {
                    if(res.status){
                        this.$message({
                        type: 'success',
                        message: '修改预定信息成功！'
                        })
                        this.bookerdialogFormVsible = false
                        listbookalready().then(res => {
                            this.alreadybook = res.BookRoom
                        })
                        listbookavible().then(res => {
                            this.bookroom = res.CanBookRoom
                        })
                    }
                    else{
                        this.$message({
                        type: 'error',
                        message: '修改预定信息失败！'
                        })
                    }
                 })
              }
           })
        },
        handleDelete(index, row) {
            // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.$confirm('确定要删除:' + row.tenantname + ' 预定的房间吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
              deletebook(row.idcard)
              .then(res => {
                  if(res.status){
                        this.$message({
                        type: 'success',
                        message: '删除预定成功！'
                        })
                        listbookalready().then(res => {
                            this.alreadybook = res.BookRoom
                        })
                        listbookavible().then(res => {
                            this.bookroom = res.CanBookRoom
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
