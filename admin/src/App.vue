<template>
  <div id="app">
    <el-container>
      <el-aside>
        <NavMenu />
      </el-aside>
      <el-container>
        <el-header>Header</el-header>
        <el-main>
          <div id="nav">
            <router-link to="/">Home</router-link> |
            <router-link to="/about">About</router-link>
          </div>
          <router-view/>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import NavMenu from '@/components/NavMenu'

export default {
  components: {
    NavMenu
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
