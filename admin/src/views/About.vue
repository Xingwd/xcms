<template>
  <el-container>
    <NavMenu />
    <el-container class="is-vertical">
      <Header />
      <el-main>
        <div class="about">
          <h1>This is an about page</h1>
        </div>
      </el-main>
     </el-container>
  </el-container>
</template>

<script>
import { NavMenu, Header } from './layout'

export default {
  name: 'about',
  components: {
    NavMenu,
    Header
  }
}
</script>
