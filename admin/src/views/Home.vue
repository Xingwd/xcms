<template>
  <el-container>
    <NavMenu />
    <el-container class="is-vertical">
      <Header />
      <el-main>
        <div class="home">
          <h1>This is an home page</h1>
        </div>
      </el-main>
     </el-container>
  </el-container>
</template>

<script>
import { NavMenu, Header } from './layout'

export default {
  name: 'home',
  components: {
    NavMenu,
    Header
  }
}
</script>
