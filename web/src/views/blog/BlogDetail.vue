<template>
  <v-container>
    <v-card>
      <v-card-title class="display-2">
        {{ post.title }}
        <v-btn
          v-if="post.category"
          small
          rounded
          color="teal lighten-3"
          class="ml-4"
        >
          {{ post.category }}
        </v-btn>
      </v-card-title>
      <!-- TODO: 增加浏览量和喜欢数量 -->
      <!-- <v-card-subtitle class="white--text">
        <v-icon color="cyan">mdi-eye</v-icon> {{ item.view }}
        <v-icon class="ml-3" color="red">mdi-heart</v-icon> {{ item.like }}
      </v-card-subtitle> -->
      <mavon-editor
        :toolbarsFlag="toolbarsFlag"
        :subfield="subfield"
        :defaultOpen="defaultOpen"
        :boxShadow="boxShadow"
        :navigation="navigation"
        v-model="post.content"/>
    </v-card>
  </v-container>
</template>

<script>
import { fetchPost } from '@/api/blog'

export default {
  data: () => ({
    toolbarsFlag: false,
    subfield: false,
    defaultOpen: 'preview',
    boxShadow: false, // 关闭边框阴影
    navigation: true, // 默认展示目录
    post: {
      title: '从删库到跑路',
      category: 'VUE',
      content: '# 2'
    }
  }),
  created () {
    const id = this.$route.params && this.$route.params.id
    this.getPost(id)
  },
  methods: {
    getPost (id) {
      fetchPost(id).then(response => {
        // console.log(response.data)
        this.post = response.data
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
