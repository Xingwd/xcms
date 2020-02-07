<template>
  <el-container :style="classObject" class="is-vertical">
    <x-admin-header />
    <el-container>
      <x-admin-aside />
      <el-container class="is-vertical">
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
        'min-height': ''
      }
    }
  },
  mounted () {
    this.setMinHeight()
    window.onresize = () => {
      this.setMinHeight()
    }
  },
  methods: {
    setMinHeight () {
      this.classObject['min-height'] = document.documentElement.clientHeight + 'px'
    }
  }
}
</script>

<style>
body {
  margin: 0px;
}
</style>
