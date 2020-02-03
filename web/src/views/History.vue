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
  // TODO: 使用后台管理数据
  data: () => ({
    histories: [
      {
        time: '2020.02',
        title: 'v1.0.0',
        text: '重新规划项目结构，使用MVVM架构设计思想，后端使用Flask，前端使用Vue。前端分为Admin和Web两部分：Admin部分使用Element框架开发；Web部分使用Vuetify框架开发。'
      },
      {
        time: '2019.04',
        title: 'v0.3.1',
        text: '优化结构，优化部分功能的展示效果。完善博客功能。'
      },
      {
        time: '2018.11',
        title: 'v0.2.7',
        text: '增加博客管理及展示功能，增加网站背景动画。'
      },
      {
        time: '2018.10',
        title: 'v0.1.0',
        text: '初始化xcms工程，使用MVC架构设计思想，通过Flask和Bootstrap构建个人网站。增加后台管理基本功能。'
      }
    ]
  })
}
</script>
