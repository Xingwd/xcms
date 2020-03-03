<template>
  <div>
    <!-- TODO: 开发仪表盘内容 -->
    <el-row :gutter="20">
      <el-col :span="12">
        <el-card>
          <ECharts chartId="category" :option="option"/>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card>
          <ECharts chartId="category1" :option="option"/>
        </el-card>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="12">
        <el-card>
          <ECharts chartId="category2" :option="option"/>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card>
          <ECharts chartId="category3" :option="option"/>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import ECharts from '@/components/ECharts.vue'
import { fetchCategories } from '@/api/blog'

export default {
  components: {
    ECharts
  },
  data () {
    return {
      seriesData: []
    }
  },
  mounted () {
    this.setBlogCategoryOption()
  },
  computed: {
    option: function () {
      return {
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          right: 10,
          top: 20,
          bottom: 20,
          data: []
        },
        series: [
          {
            name: '分类',
            type: 'pie',
            radius: '55%',
            center: ['40%', '50%'],
            data: this.seriesData,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      }
    }
  },
  methods: {
    setBlogCategoryOption () {
      fetchCategories(
      ).then(response => {
        let data = []
        for (let i of response.data) {
          data.push({ value: i.total, name: i.name })
        }
        this.seriesData = data
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style media="screen">
.el-row {
  margin-bottom: 20px;
}
</style>
