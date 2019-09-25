<template>
  <div id="app">
    <x-layout>
      <router-view/>
    </x-layout>
  </div>
</template>

<script>
import Layout from '@/layout/Layout'

export default {
  name: 'app',
  components: {
    'x-layout': Layout
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
