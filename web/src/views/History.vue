<template>
  <v-card
    class="mx-auto"
  >
    <v-img
      src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
      height="400"
    ></v-img>
    <v-card-text class="py-0">
      <v-container>
        <v-timeline>
          <v-timeline-item
            v-for="(h, index) in histories"
            :key="index"
            small
          >
            <template v-slot:opposite>
              <span>{{ h.time }}</span>
            </template>
            <v-card class="elevation-2">
              <v-card-title class="headline">{{ h.title }}</v-card-title>
              <v-card-text>{{ h.text }}</v-card-text>
            </v-card>
          </v-timeline-item>
        </v-timeline>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    histories: [
      {
        time: '2020',
        title: 'v1.0',
        text: '前端分为Admin和Web两部分：Admin部分使用Element框架开发；Web部分使用Vuetify框架开发。'
      },
      {
        time: '2019',
        title: 'dev',
        text: '重新规划项目结构，使用前后端分离设计思想，后端使用Flask，前端使用Vue。'
      },
      {
        time: '2018',
        title: 'v0.3',
        text: '在v0.1的基础上，增加功能，重新开发前端。'
      },
      {
        time: '2017',
        title: 'v0.1',
        text: '初始化xcms工程，使用Flask框架构建个人博客。'
      }
    ]
  })
}
</script>
