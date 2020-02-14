<template>
  <aside class="el-aside">
    <el-menu
      :default-active="defaultActive"
      style="border-right: 0px"
      router
      unique-opened
      :background-color="variables.menuBg"
      :text-color="variables.menuText"
      :active-text-color="variables.menuActiveText"
      :collapse="sideBarIsCollapse">
      <!-- TODO： 根据路由自动渲染菜单 -->
      <el-menu-item index="/dashboard">
        <i class="el-icon-sunrise" />
        <span slot="title">仪表盘</span>
      </el-menu-item>
      <el-submenu index="/blog">
        <template slot="title">
          <i class="el-icon-notebook-1" />
          <span>博客</span>
        </template>
        <el-menu-item-group>
          <template slot="title">文章</template>
          <el-menu-item index="/blog/list">
            <i class="el-icon-s-order" />
            <span>文章列表</span>
          </el-menu-item>
          <el-menu-item index="/blog/create">
            <i class="el-icon-edit" />
            <span>写文章</span>
          </el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group>
          <template slot="title">分类</template>
          <el-menu-item index="/blog/categories">
            <i class="el-icon-s-grid"/>
            <span>所有分类</span>
          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
    </el-menu>
  </aside>
</template>

<script>
import variables from '@/styles/variables.scss'
import { mapState } from 'vuex'

export default {
  data () {
    return {
      defaultActive: '/dashboard'
    }
  },
  created () {
    // this.defaultActive = this.$router.currentRoute.path
    this.defaultActive = this.$route.path
  },
  watch: {
    '$route': function () {
      this.defaultActive = this.$route.path
    }
  },
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
