<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 20px;">
            <div class="query-c">
                查询：
                <Input search placeholder="请输入查询内容" style="width: auto" />
            </div>
            <br>
            <el-table :data="users" highlight-current-row v-loading="listLoading" @selection-change="selsChange" style="width: 100%;">
                <el-table-column type="selection" width="55">
                </el-table-column>
                <el-table-column type="index" label="序号" width="100">
                </el-table-column>
                <el-table-column prop="p_id" label="商品ID" width="100" v-if="visible">
                </el-table-column>
                <el-table-column prop="p_name" label="商品名称" width="120" >
                </el-table-column>
                <el-table-column prop="p_pic" label="缩略图" width="100" >
                </el-table-column>
                <el-table-column prop="p_category" label="商品类别" width="100" >
                </el-table-column>
                <el-table-column prop="p_status" label="状态" width="100" >
                </el-table-column>
                <!-- <el-table-column prop="p_desc" label="描述" min-width="180" >
                </el-table-column> -->
                <el-table-column label="操作" :render-header="renderHeader" width="150">
                    <template scope="scope">
                        <el-button type="warning" size="mini" icon='el-icon-edit' @click="editlog(scope.$index, scope.row)" circle>
                        </el-button>
                        <el-dialog title="修改商品" :visible.sync="dialogFormVisible">
                            <el-form :model="form">
                                <el-form-item label="商品名称" :label-width="formLabelWidth">
                                <el-input v-model="form.name" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item label="缩略图" :label-width="formLabelWidth">
                                <el-input v-model="form.pic" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item label="商品类别" :label-width="formLabelWidth">
                                <el-input v-model="form.category" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item label="状态" :label-width="formLabelWidth">
                                <el-input v-model="form.status" autocomplete="off"></el-input>
                                </el-form-item>
                            </el-form>
                            <div slot="footer" class="dialog-footer">
                                <el-button @click="dialogFormVisible = false">取 消</el-button>
                                <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
                            </div>
                        </el-dialog>
                        <el-button type="danger" icon='el-icon-delete' size='mini' @click="deletelog(scope.$index, scope.row)" circle>
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
            <br>
            <Page :total="100" show-sizer show-elevator/>
        </div>
    </div>
</template>


<script>
export default {
    name: 'merchandise',
    data() {
        return {
            users: [
                {
                    p_id: '1',
                    p_name: 'water',
                    p_pic: '1',
                    p_category: 'food',
                    p_status: 'on',
                },
            ],
            dialogFormVisible: false,
            // dialogVisible: false,
            form: {
                name: 'water',
                pic: '1',
                category: 'food',
                status: 'on',
                delivery: false,
                type: [],
                resource: '',
                desc: '',
            },
            formLabelWidth: '120px',
        }
    },
    // methods: {
    //     handleClose(done) {
    //         this.$confirm('确认关闭？')
    //         .then(_ => {
    //             done()
    //         })
    //         .catch(_ => {})
    //     },
    // },
    methods: {
        deletelog() {
        // eslint-disable-next-line no-underscore-dangle
            let _this = this
            _this.$confirm('确定要删除全部吗吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
            // eslint-disable-next-line no-alert
                alert('删除成功')
            }).catch()
        },
        editlog() {
            this.dialogFormVisible = true
        },
    },
}
</script>

<style scoped>

</style>
