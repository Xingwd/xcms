<template>
  <div>
    <el-row>
      <el-button style="float: left" type="primary" icon="el-icon-plus" @click="dialogNewFormVisible = true">新建分类</el-button>
      <el-dialog title="新建分类" :visible.sync="dialogNewFormVisible" width="390px">
        <el-form :model="newForm">
          <el-form-item label="分类名" label-width="60px">
            <el-input v-model="newForm.name" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="initNewForm">取 消</el-button>
          <el-button type="primary" @click="newCategory">确 定</el-button>
        </div>
      </el-dialog>
    </el-row>
    <el-row :gutter="40" class="panel-group">
      <el-col v-for="item in items" :key="item.id" :xs="12" :sm="12" :lg="6" class="card-panel-col">
        <el-popover
          placement="bottom"
          trigger="click">
          <el-button-group>
            <el-button type="primary" @click="openEditForm(item)">编辑</el-button>
            <el-button type="danger" @click="handleDelete(item)">删除</el-button>
          </el-button-group>
          <el-card slot="reference" class="card-panel">
            <div class="card-panel-title">
              {{ item.name }}
            </div>
            <div class="card-panel-description">
              <div class="card-panel-text">
                Posts
              </div>
              <count-to :start-val="0" :end-val="item.total" :duration="2600" class="card-panel-num" />
            </div>
          </el-card>
        </el-popover>
        <el-dialog title="编辑分类" :visible.sync="dialogEditFormVisible" width="390px">
          <el-form :model="editForm">
            <el-form-item label="分类名" label-width="80px">
              <el-input v-model="editForm.name" autocomplete="off" disabled></el-input>
            </el-form-item>
            <el-form-item label="新分类名" label-width="80px">
              <el-input v-model="editForm.newName" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="initEditForm">取 消</el-button>
            <el-button type="primary" @click="handleEdit">确 定</el-button>
          </div>
        </el-dialog>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import CountTo from 'vue-count-to'
import { fetchCategories, createCategory, updateCategory, deleteCategory } from '@/api/blog'

export default {
  components: {
    CountTo
  },
  data () {
    return {
      items: [],
      currentItem: {},
      dialogNewFormVisible: false,
      dialogEditFormVisible: false,
      newForm: {
        name: ''
      },
      editForm: {
        name: '',
        newName: ''
      }
    }
  },
  created () {
    this.$notify({
      title: '提示',
      message: this.$createElement('i', { style: 'color: teal' }, '点击单个分类面板可进行操作'),
      type: 'info',
      offset: 70
    })
    this.getAllCategories()
  },
  methods: {
    getAllCategories () {
      fetchCategories(
      ).then(response => {
        this.items = response.data
      }).catch(error => {
        console.log(error)
      })
    },
    openEditForm (item) {
      this.editForm.name = item.name
      this.dialogEditFormVisible = true
      this.currentItem = item
    },
    handleEdit () {
      // TODO: 增加判断name唯一性
      updateCategory(this.currentItem.id, { 'name': this.editForm.newName }
      ).then(response => {
        switch (response.status) {
          default:
            this.$message.success('更新成功')
        }
        let newItems = []
        for (let i = 0; i < this.items.length; i++) {
          if (this.items[i].id === this.currentItem.id) {
            this.items[i].name = this.editForm.newName
          }
          newItems.push(this.items[i])
        }
        this.items = newItems
        this.initEditForm()
      }).catch(error => {
        console.log(error)
      })
    },
    handleDelete (item) {
      this.$confirm('此操作将永久删除该历程, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        customClass: 'x-message-box'
      }).then(() => {
        deleteCategory(item.id
        ).then(response => {
          switch (response.status) {
            default:
              this.$message.success('删除成功')
          }
          // this.items = Object.assign({}, this.items.splice(item)) 这样写不行，why?
          this.getAllCategories()
        }).catch(error => {
          console.log(error)
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    initNewForm () {
      this.dialogNewFormVisible = false
      this.newForm.name = ''
    },
    initEditForm () {
      this.dialogEditFormVisible = false
      this.editForm.newName = ''
    },
    newCategory () {
      createCategory({ 'name': this.newForm.name }
      ).then(response => {
        this.items.push({ 'name': this.newForm.name, 'posts': [] })
        this.initNewForm()
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.panel-group {
  margin-top: 18px;

  .card-panel-col {
    margin-bottom: 32px;
  }

  .card-panel {
    height: 108px;
    cursor: pointer;
    font-size: 12px;
    position: relative;
    overflow: hidden;
    color: #666;
    background: #fff;
    box-shadow: 4px 4px 40px rgba(0, 0, 0, .05);
    border-color: rgba(0, 0, 0, .05);

    .card-panel-title {
      font-size: 30px;
      float: left;
      margin: 12px 0 0 14px;
      color: #409EFF;
    }

    .card-panel-description {
      float: right;
      font-weight: bold;
      margin: 10px 26px 0 0;

      .card-panel-text {
        line-height: 18px;
        color: rgba(0, 0, 0, 0.45);
        font-size: 16px;
        margin-bottom: 12px;
      }

      .card-panel-num {
        font-size: 20px;
      }
    }
  }
}

@media (max-width:550px) {
  .card-panel-description {
    display: none;
  }
}
</style>

<style>
.x-message-box {
  vertical-align: baseline;
}
</style>
