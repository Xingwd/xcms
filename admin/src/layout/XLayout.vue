<template>
  <el-container style="height: 100%;">
    <x-nav-menu />
    <el-container class="is-vertical">
      <x-header />
      <el-main>
        <slot></slot>
      </el-main>
     </el-container>
  </el-container>
</template>

<script>
import { XHeader, XNavMenu } from './components'

export default {
  name: 'XLayout',
  components: {
    XHeader,
    XNavMenu
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
