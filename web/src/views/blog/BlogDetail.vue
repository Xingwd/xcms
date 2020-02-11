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
      <v-card-subtitle>
        <v-icon color="cyan">mdi-eye</v-icon> {{ post.pv }}
        <!-- TODO: 增加喜欢数量 -->
        <!-- <v-icon class="ml-3" color="red">mdi-heart</v-icon> {{ post.like }} -->
      </v-card-subtitle>
      <mavon-editor
        style="z-index: 0"
        :toolbarsFlag="toolbarsFlag"
        :subfield="subfield"
        :defaultOpen="defaultOpen"
        :boxShadow="boxShadow"
        :codeStyle="codeStyle"
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
    codeStyle: 'atom-one-light', // 代码风格
    post: {
      title: '从删库到跑路',
      category: 'VUE',
      content: '# 2'
    }
  }),
  mounted () {
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

<style>
.v-application code { /* 修复：渲染的代码块有问题，每行代码都有阴影，此处覆盖vuetify的code样式 */
  box-shadow: 0 0 0;
  color: black;
}
</style>
