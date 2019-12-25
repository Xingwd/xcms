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
  // TODO: 页面大小发生变化，min-height随之变化，其他地方可能也需要，使用vuex管理？
  computed: {
    classObject: function () {
      return {
        'min-height': window.innerHeight + 'px' // 设置页面最小高度为浏览器高度
      }
    }
  }
}
</script>

<style>
body {
  margin: 0px;
}
</style>
