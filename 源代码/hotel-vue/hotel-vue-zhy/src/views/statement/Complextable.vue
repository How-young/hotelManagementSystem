<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
  <div class="tblock">
    <el-date-picker
      format="yyyy-MM-dd"
      value-format="yyyy-MM-dd"
      v-model="datekey1"
      type="daterange"
      range-separator="至"
      start-placeholder="开始日期"
      end-placeholder="结束日期">
    </el-date-picker>
        <el-button type="primary" icon="el-icon-search" @click="rangeday">搜索</el-button>
  </div>
  <h3>当天入住</h3>
   <el-table
        :data="enter"
        height="200"
        border
        style="width: 100%">
        <el-table-column
            prop="stayroom"
            label="所在房间"
            width="200">
        </el-table-column>
        <el-table-column
            prop="tenantname"
            label="姓名"
            width="200">
        </el-table-column>
        <el-table-column
            prop="checkin"
            label="入住"
            width="200">
        </el-table-column>
        <el-table-column
            prop="checkout"
            label="离店"
            width="200">
        </el-table-column>
        <el-table-column
            prop="idcard"
            label="卡号"
            width="200">
        </el-table-column>
   </el-table>
      <el-table
        :data="leave"
        height="200"
        border
        style="width: 100%">
        <el-table-column
            prop="stayroom"
            label="所在房间"
            width="200">
        </el-table-column>
        <el-table-column
            prop="tenantname"
            label="姓名"
            width="200">
        </el-table-column>
        <el-table-column
            prop="checkin"
            label="入住"
            width="200">
        </el-table-column>
        <el-table-column
            prop="checkout"
            label="离店"
            width="200">
        </el-table-column>
        <el-table-column
            prop="idcard"
            label="卡号"
            width="200">
        </el-table-column>
   </el-table>
         <el-table
        :data="book"
        height="200"
        border
        style="width: 100%">
        <el-table-column
            prop="stayroom"
            label="所在房间"
            width="200">
        </el-table-column>
        <el-table-column
            prop="tenantname"
            label="姓名"
            width="200">
        </el-table-column>
        <el-table-column
            prop="checkin"
            label="入住"
            width="200">
        </el-table-column>
        <el-table-column
            prop="checkout"
            label="离店"
            width="200">
        </el-table-column>
        <el-table-column
            prop="idcard"
            label="卡号"
            width="200">
        </el-table-column>
   </el-table>
  </div>
    </div>
</template>

<script>
import { listtodayCheckin , listtodayCheckout ,listCheckinCheckout } from '../apis/index'

export default {
    name: 'complextable',
    data() {
        return {
            datekey: '',
            datekey1: '',
            enter: [],
            leave: [],
            book: [],
        }
    },
    mounted() {
        listtodayCheckin().then(res => {
            this.enter = res.checkin
        })
        listtodayCheckout().then(res => {
            this.leave = res.checkout
        })

    },
    methods: {
        rangeday() {
            listCheckinCheckout(this.datekey1[0],this.datekey1[1])
            .then(res => {
                this.book = res.BookRoom
            })
        },
    },
}
</script>

<style scoped>

</style>
