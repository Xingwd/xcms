<template>
  <div @mouseenter="mouseoverRatio = true" @mouseleave="mouseoverRatio = false">
    <el-card style="margin-bottom: 20px; height: 130px;">
      <el-row style="margin-bottom: 5px">
        <el-col :span="24" align="left">
          <span style="font-size:25px; font-weight: 500">
            {{ title }}
            <span style="font-size:12px; font-weight: 400; color: #909399;">
              (Ratio={{ topLabel }}/{{ bottomLabel }})
            </span>
          </span>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="12" align="left">
          <div>
            <count-to
              :start-val="0"
              :end-val="topValue"
              :duration="2600"
              :prefix="topLabel + ': '"
              style="font-size:16px; color: #409EFF;"/>
          </div>
          <div>
            <count-to
              :start-val="0"
              :end-val="bottomValue"
              :duration="2600"
              :prefix="bottomLabel + ': '"
              style="font-size:16px; color: #409EFF;"/>
          </div>
        </el-col>
        <el-col :span="12">
          <div>
            <span :style="ratioStyle">
              <span style="font-size: 12px">Ratio = </span>
              <count-to
                :start-val="0"
                :end-val="bottomValue > 0 ? (topValue / bottomValue * 100) : 0"
                :duration="2600"
                :decimals="2"
                :suffix="'%'"/>
            </span>
          </div>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script>
import CountTo from 'vue-count-to'

export default {
  name: 'RatioPanel',
  props: {
    title: String,
    bottomLabel: String,
    bottomValue: Number,
    topLabel: String,
    topValue: Number
  },
  components: {
    CountTo
  },
  data () {
    return {
      mouseoverRatio: false
    }
  },
  computed: {
    ratioStyle: function () {
      const fontSize = this.mouseoverRatio ? '48px' : '40px'
      return {
        'font-size': fontSize,
        color: '#E6A23C'
      }
    }
  }
}
</script>
