<template>
  <aside class="el-aside">
    <el-menu
      default-active="/admin/dashboard"
      style="border-right: 0px"
      router
      :background-color="variables.menuBg"
      :text-color="variables.menuText"
      :active-text-color="variables.menuActiveText"
      :collapse="sideBarIsCollapse">
      <el-menu-item index="/admin/dashboard">
        <i class="el-icon-sunrise"></i>
        <span slot="title">仪表盘</span>
      </el-menu-item>
      <el-submenu index="/admin/blog">
        <template slot="title">
          <i class="el-icon-edit"></i>
          <!-- TODO: 修改成 博客 ，包括调整子菜单-->
          <span>导航二</span>
        </template>
        <el-menu-item index="/admin/blog/list">列表</el-menu-item>
        <el-menu-item index="/admin/blog/create">博客</el-menu-item>
      </el-submenu>
    </el-menu>
  </aside>
</template>

<script>
import variables from '@/styles/variables.scss'
import { mapState } from 'vuex'

export default {
  computed: {
    variables () {
      return variables
    },
    ...mapState([
      'sideBarIsCollapse'
    ])
  }
}
</script>

<style lang="scss" scoped>
@import '@/styles/variables.scss';

.el-aside {
  background-color: $menuBg;
  text-align: left;
  .el-menu:not(.el-menu--collapse) {
    width: $sideBarWidth;
  }
}
</style>
