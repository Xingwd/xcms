<template>
  <div id="app">
    <x-layout>
      <router-view/>
    </x-layout>
  </div>
</template>

<script>
import XLayout from '@/layout/XLayout'

export default {
  name: 'app',
  components: { XLayout }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: 100%
}
</style>
