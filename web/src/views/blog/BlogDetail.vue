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
      <!-- BUG:
      2、渲染的代码块有问题，每行代码都有海拔，很难看
      -->
      <v-card-text>
      <mavon-editor
        style="z-index: 0"
        :toolbarsFlag="toolbarsFlag"
        :subfield="subfield"
        :defaultOpen="defaultOpen"
        :boxShadow="boxShadow"
        v-model="post.content"/>
      </v-card-text>
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
