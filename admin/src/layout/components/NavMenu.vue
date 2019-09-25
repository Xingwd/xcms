<template>
  <aside class="el-aside" style="width: 250px;">
    <el-menu
      default-active="/"
      class="el-menu-over"
      @open="handleOpen"
      @close="handleClose"
      unique-opened
      router
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="/">
        <i class="el-icon-location"></i>
        <span slot="title">Home</span>
      </el-menu-item>
      <el-submenu index="/blog/articleList">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>博客</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="/blog/articleList">文章列表</el-menu-item>
          <el-menu-item index="/blog/createArticle">创建文章</el-menu-item>
          <el-menu-item index="/blog/editArticle">编辑文章</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-menu-item index="/about">
        <i class="el-icon-location"></i>
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
