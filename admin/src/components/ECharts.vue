<template>
  <div :id="chartId" :style="styleObject"></div>
</template>

<script>
import echarts from 'echarts'

export default {
  name: 'ECharts',
  props: {
    chartId: String,
    option: Object,
    width: {
      type: String,
      default: '600px'
    },
    height: {
      type: String,
      default: '400px'
    }
  },
  mounted () {
    this.createInstance()
    this.setOption()
  },
  computed: {
    styleObject: function () {
      return {
        width: this.width,
        height: this.height
      }
    }
  },
  watch: {
    option: function () {
      this.setOption()
    }
  },
  methods: {
    createInstance () {
      this.echartsInstance = echarts.init(document.getElementById(this.chartId))
    },
    setOption () {
      this.echartsInstance.setOption(this.option)
    }
  }
}
</script>
