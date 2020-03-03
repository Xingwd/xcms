<template>
  <div>
    <el-table
      :data="data"
      stripe
      border
      :size="size"
      :height="height"
      @cell-click="handleCellClick"
    >
      <template v-for="(col, index) in columns">
        <el-table-column
          v-if="col.hasEvent"
          :key="index"
          :prop="col.prop"
          :label="col.label"
          :fixed="col.fixed"
          :width="col.width"
          :align="col.align"
          show-overflow-tooltip
          :class-name="pointerCell">
        </el-table-column>
        <el-table-column
          v-else
          :key="index"
          :fixed="col.fixed"
          :prop="col.prop"
          :label="col.label"
          :width="col.width"
          :align="col.align"
          show-overflow-tooltip>
        </el-table-column>
      </template>
      <template v-for="(tool, index) in toolbar">
        <el-table-column
          :key="tool.label + index"
          fixed="right"
          :label="tool.label"
          :width="tool.width"
          :align="tool.align">
          <el-button
            size="mini"
            :type="tool.buttonType"
            :round="tool.buttonRound"
          >
            {{ tool.buttonText }}
          </el-button>
        </el-table-column>
      </template>
    </el-table>
    <el-pagination
      v-if="pagination"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-sizes="pageSizes"
      :page-size="pageSize"
      layout="total, sizes, prev, pager, next, jumper"
      :total="total"
      style="float: right; margin-top: 10px;"
    >
    </el-pagination>
  </div>
</template>

<script>
export default {
  name: 'GeneralTable',
  props: {
    columns: {
      type: Array,
      default: () => {
        return []
      }
    },
    data: {
      type: Array,
      default: () => {
        return []
      }
    },
    size: {
      type: String,
      default: 'mini'
    },
    height: {
      type: Number,
      default: 600
    },
    pagination: {
      type: Boolean,
      default: true
    },
    currentPage: {
      type: Number,
      default: 1
    },
    pageSizes: {
      type: Array,
      default: () => {
        return [30, 40, 50, 60]
      }
    },
    pageSize: {
      type: Number,
      default: 30
    },
    total: {
      type: Number,
      default: 0
    },
    toolbar: {
      type: Array,
      default: () => {
        return []
      }
    }
  },
  data () {
    return {
      pointerCell: 'r-pointer'
    }
  },
  methods: {
    handleCellClick (row, column) {
      this.$emit('cell-click', row, column)
    },
    handleSizeChange (size) {
      this.$emit('size-change', size)
    },
    handleCurrentChange (current) {
      this.$emit('current-change', current)
    }
  }
}
</script>

<style>
.r-pointer {
  cursor: pointer;
}
</style>
