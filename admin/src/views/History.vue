<template>
  <div class="myHistory">
    <el-timeline>
      <el-timeline-item
        timestamp=""
        size="large"
        type="success"
      >
        <el-card>
          <el-button
            type="primary"
            icon="el-icon-plus"
            circle
            @click="dialogNewFormVisible = true"
            style="height: 50px; width: 50px"
          />
        </el-card>
      </el-timeline-item>
      <el-timeline-item
        v-for="(item, index) in items"
        :key="index"
        :timestamp="item.time"
        placement="top"
        size="large"
        type="primary"
      >
        <el-popover
          placement="top"
          trigger="click"
        >
          <el-button-group>
            <el-button type="primary" @click="openEditForm(item)">编辑</el-button>
            <el-button type="danger" @click="handleDelete(item)">删除</el-button>
          </el-button-group>
          <el-card slot="reference">
            <h2>{{ item.release }}</h2>
            <p>{{ item.description }}</p>
          </el-card>
        </el-popover>
      </el-timeline-item>
    </el-timeline>

    <el-dialog title="新建历程" :visible.sync="dialogNewFormVisible" width="600px">
      <el-form :model="form">
        <el-form-item label="Time" label-width="90px">
          <el-input v-model="form.time" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Release" label-width="90px">
          <el-input v-model="form.release" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Description" label-width="90px">
          <el-input type="textarea" v-model="form.description" :rows="5"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="initForm">取 消</el-button>
        <el-button type="primary" @click="newHistory">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog title="编辑历程" :visible.sync="dialogEditFormVisible" width="600px">
      <el-form :model="form">
        <el-form-item label="Time" label-width="90px">
          <el-input v-model="form.time" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Release" label-width="90px">
          <el-input v-model="form.release" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Description" label-width="90px">
          <el-input type="textarea" v-model="form.description" :rows="5"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="initForm">取 消</el-button>
        <el-button type="primary" @click="editHistory">更 新</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { fetchHistories, createHistory, updateHistory, deleteHistory } from '@/api/history'

export default {
  data () {
    return {
      items: [],
      dialogNewFormVisible: false,
      dialogEditFormVisible: false,
      form: {
        time: '',
        release: '',
        description: ''
      },
      currentItem: ''
    }
  },
  mounted () {
    this.$notify({
      title: '提示',
      message: this.$createElement('i', { style: 'color: teal' }, '点击单个历程可进行操作'),
      type: 'info',
      offset: 70
    })
    this.getHistories()
  },
  methods: {
    getHistories () {
      fetchHistories(
      ).then(response => {
        this.items = response.data
      }).catch(error => {
        console.log(error)
      })
    },
    newHistory () {
      let item = {
        'time': this.form.time,
        'release': this.form.release,
        'description': this.form.description
      }
      createHistory(item
      ).then(response => {
        this.items = [item].concat(this.items)
        this.initForm()
      }).catch(error => {
        console.log(error)
      })
    },
    initForm () {
      this.dialogNewFormVisible = false
      this.dialogEditFormVisible = false
      this.form.time = ''
      this.form.release = ''
      this.form.description = ''
    },
    openEditForm (item) {
      this.form = Object.assign({}, item)
      this.dialogEditFormVisible = true
      this.currentItem = item
    },
    editHistory () {
      let item = {
        'time': this.form.time,
        'release': this.form.release,
        'description': this.form.description
      }
      updateHistory(this.currentItem.id, item
      ).then(response => {
        switch (response.status) {
          default:
            this.$message.success('更新成功')
        }
        this.getHistories()
        this.initForm()
      }).catch(error => {
        console.log(error)
      })
    },
    handleDelete (item) { // TODO: 增加确认弹窗
      deleteHistory(item.id
      ).then(response => {
        switch (response.status) {
          default:
            this.$message.success('删除成功')
        }
        this.getHistories()
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style>
.myHistory {
  margin: 20px 50px 30px 30px;
}
</style>
