<template>
  <aside class="el-aside" style="width: 250px;">
    <el-menu
      default-active="2"
      class="el-menu-over"
      @open="handleOpen"
      @close="handleClose"
      unique-opened
      router
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="/">
        <i class=""></i>
        <span slot="title">Home</span>
      </el-menu-item>
      <el-menu-item index="/about">
        <i class=""></i>
        <span slot="title">About</span>
      </el-menu-item>
    </el-menu>
  </aside>
</template>

<script>
export default {
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style>
.el-menu-over {
  height: 100%;
}
</style>
