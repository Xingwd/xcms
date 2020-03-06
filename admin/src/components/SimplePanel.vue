<template>
  <div @mouseenter="mouseoverRatio = true" @mouseleave="mouseoverRatio = false">
    <el-card style="margin-bottom: 20px; height: 100px;">
      <el-row style="margin-bottom: 5px">
        <el-col :span="24" align="left">
          <span style="font-size:18px; font-weight:500;">
            {{ label }}
          </span>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="24" align="left">
          <div>
            <count-to
              :start-val="0"
              :end-val="value"
              :duration="2600"
              :style="valueStyle"/>
          </div>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script>
import CountTo from 'vue-count-to'

export default {
  name: 'SimplePanel',
  props: {
    label: String,
    value: Number
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
    valueStyle: function () {
      const fontSize = this.mouseoverRatio ? '33px' : '28px'
      return {
        'font-size': fontSize,
        color: '#E6A23C'
      }
    }
  }
}
</script>
