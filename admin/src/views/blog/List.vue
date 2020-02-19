<template>
  <div>
    <el-row>
      <el-col :span="2">
        <router-link :to="{ name: 'createPost' }">
          <el-button style="float: left" type="primary" icon="el-icon-plus">
            写文章
          </el-button>
        </router-link>
      </el-col>
      <el-col :span="22">
        <el-pagination
          style="padding: 10px 200px 0 0"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :pager-count="7"
          :current-page="currentPage"
          :page-sizes="[15, 30, 45]"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total">
        </el-pagination>
      </el-col>
    </el-row>
    <el-table
      ref="blogTable"
      :data="tableData"
      stripe
      border
      style="width: 100%; margin-top: 25px"
      :max-height="maxHeight"
      size="small"
    >
      <el-table-column
        prop="id"
        label="ID"
        width="100">
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        prop="title"
        label="标题">
      </el-table-column>
      <el-table-column
        prop="pubdate"
        label="发布时间"
        width="120">
      </el-table-column>
      <el-table-column
        prop="pv"
        label="PV"
        width="100">
      </el-table-column>
      <el-table-column
        prop="category"
        label="分类"
        width="120">
      </el-table-column>
      <el-table-column
        fixed="right"
        label="操作"
        width="120">
        <template slot-scope="scope">
          <el-button @click="editPost(scope.row)" type="text" size="small">编辑</el-button>
          <!-- TODO: 增加确认删除弹框 -->
          <el-button @click="handleClick(scope.row)" type="text" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { fetchPosts, deletePost } from '@/api/blog'

export default {
  data () {
    return {
      maxHeight: document.documentElement.clientHeight - 190 + 'px',
      tableData: [],
      currentPage: 1,
      total: 0,
      pageSize: 15
    }
  },
  mounted () {
    this.getPagePosts()
  },
  methods: {
    getPagePosts () {
      fetchPosts({ 'page': this.currentPage, 'page_size': this.pageSize }
      ).then(response => {
        // console.log(response.data)
        this.tableData = response.data.posts
        this.total = response.data.total
      }).catch(error => {
        console.log(error)
      })
    },
    editPost (row) {
      this.$router.push({ name: 'editPost', params: { id: row.id } })
    },
    handleClick (row) {
      deletePost(row.id
      ).then(response => {
        this.getPagePosts()
        this.$message.success('删除成功')
      }).catch(error => {
        console.log(error)
      })
    },
    handleSizeChange (val) {
      console.log(`每页 ${val} 条`)
      this.pageSize = val
      this.getPagePosts()
    },
    handleCurrentChange (val) {
      console.log(`当前页: ${val}`)
      this.currentPage = val
      this.getPagePosts()
    }
  }
}
</script>
