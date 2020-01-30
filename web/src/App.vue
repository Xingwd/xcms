<template>
  <v-app>
    <v-content>
      <router-view />
    </v-content>
    <v-footer
      app
      padless
      absolute
      color="#f5f5f5"
      class="font-weight-medium"
    >
      <v-col
        class="text-center"
        cols="12"
      >
        &copy; {{ new Date().getFullYear() }} — <strong>邢为栋</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>
