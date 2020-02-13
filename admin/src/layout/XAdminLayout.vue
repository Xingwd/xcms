<template>
  <el-container class="is-vertical">
    <x-admin-header />
    <el-container>
      <x-admin-aside />
      <el-container :style="classObject" class="is-vertical">
        <el-main>
          <router-view />
        </el-main>
        <x-footer />
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
import { XAdminAside, XAdminHeader, XFooter } from './components'

export default {
  components: {
    XAdminAside,
    XAdminHeader,
    XFooter
  },
  data () {
    return {
      classObject: {
        'height': ''
      }
    }
  },
  mounted () {
    this.setHeight()
    window.onresize = () => {
      this.setHeight()
    }
  },
  methods: {
    setHeight () {
      // 减去header高度
      this.classObject.height = document.documentElement.clientHeight - 50 + 'px'
    }
  }
}
</script>

<style>
body {
  margin: 0px;
}
</style>
