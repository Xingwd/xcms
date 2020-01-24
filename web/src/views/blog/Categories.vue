<template>
  <el-row :gutter="40" class="panel-group">
    <el-col v-for="item in items" :key="item.id" :xs="12" :sm="12" :lg="6" class="card-panel-col">
      <el-popover
        placement="bottom"
        trigger="click">
        <el-button-group>
          <el-button type="primary" @click="handleEdit(item)">编辑</el-button>
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
            <count-to :start-val="0" :end-val="item.count" :duration="2600" class="card-panel-num" />
          </div>
        </el-card>
      </el-popover>
    </el-col>
  </el-row>
</template>

<script>
import CountTo from 'vue-count-to'

export default {
  components: {
    CountTo
  },
  data () {
    return {
      items: [{
        id: 1,
        name: 'vue',
        count: 123
      },
      {
        id: 2,
        name: 'flask',
        count: 234
      },
      {
        id: 3,
        name: 'python',
        count: 345
      },
      {
        id: 4,
        name: 'hadoop',
        count: 456
      },
      {
        id: 5,
        name: 'spark',
        count: 567
      },
      {
        id: 6,
        name: 'Algorithm',
        count: 678
      }]
    }
  },
  created () {
    this.$notify({
      title: '提示',
      message: this.$createElement('i', { style: 'color: teal' }, '点击单个分类面板可进行操作'),
      type: 'info',
      offset: 70
    })
  },
  methods: {
    handleEdit (item) {
      console.log('Edit ' + item.name)
    },
    handleDelete (item) {
      console.log('Delete ' + item.name)
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
