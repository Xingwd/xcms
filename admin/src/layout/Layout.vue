<template>
  <el-container style="height: 100%;">
    <NavMenu />
    <el-container class="is-vertical">
      <Header />
      <el-main>
        <slot></slot>
      </el-main>
     </el-container>
  </el-container>
</template>

<script>
import { Header, NavMenu } from './components'

export default {
  name: 'layout',
  components: {
    Header,
    NavMenu
  },
  methods: {
    async logout() {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    }
  }
}
</script>

<style>

</style>
