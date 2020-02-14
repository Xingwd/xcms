<template>
  <v-card
    class="mx-auto"
    flat
  >
    <v-img
      src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
      height="400"
    ></v-img>
    <v-card-text class="py-0">
      <v-container>
        <v-timeline>
          <v-timeline-item
            v-for="(i, index) in items"
            :key="index"
            small
          >
            <template v-slot:opposite>
              <span>{{ i.time }}</span>
            </template>
            <v-card class="elevation-2">
              <v-card-title class="headline">{{ i.release }}</v-card-title>
              <v-card-text>{{ i.description }}</v-card-text>
            </v-card>
          </v-timeline-item>
        </v-timeline>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script>
import { fetchHistories } from '@/api/history'

export default {
  data () {
    return {
      items: []
    }
  },
  mounted () {
    fetchHistories(
    ).then(response => {
      this.items = response.data
    }).catch(error => {
      console.log(error)
    })
  }
}
</script>
