<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
<div class="block">
    <el-date-picker
      v-model="datekey"
      type="date"
      placeholder="选择日期">
    </el-date-picker>
    <el-button type="primary" icon="el-icon-search">搜索</el-button>
  </div>
    </div>
    </div>
</template>

<script>
export default {
    name: 'complextable',
    data() {
        return {
            datekey: '',
        }
    },
}
</script>

<style scoped>

</style>
