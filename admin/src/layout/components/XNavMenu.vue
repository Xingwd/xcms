<template>
  <aside class="el-aside" style="width: 250px; background-color: #545c64;">
    <el-menu
      default-active="/"
      style="border-right: 0px"
      @open="handleOpen"
      @close="handleClose"
      unique-opened
      router
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <div v-for="item in menu" :key="item.path">
        <div v-if="item.children">
          <el-submenu :index="item.path">
            <template slot="title">
              <i :class="item.meta.icon"></i>
              <span v-text="item.meta.title"></span>
            </template>
            <el-menu-item v-for="citem in item.children" :key="citem.path" :index="item.path + '/' + citem.path" v-text="citem.meta.title"></el-menu-item>
          </el-submenu>
        </div>
        <div v-else>
          <el-menu-item :index="item.path">
            <i :class="item.meta.icon"></i>
            <span slot="title" v-text="item.meta.title"></span>
          </el-menu-item>
        </div>
      </div>
    </el-menu>
  </aside>
</template>

<script>
export default {
  name: 'XNavMenu',
  data () {
    return {
      menu: this.$router.options.routes
    }
  },
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
