<template>
  <div class="black">
    <v-img src="@/assets/blog-bg.jpg">
      <v-row class="pt-7">
        <v-col
          cols="8"
          offset="1"
          class="main-bg"
        >
          <v-toolbar
            dense
            flat
            color="transparent"
            class="white--text align-center">
            <v-badge
              color="deep-purple accent-4"
              :content="postTotal"
            >
              Total
            </v-badge>
            <v-pagination
              v-model="page"
              :length="pages"
              :total-visible="7"
              dark
              circle
              @input="handlePage"
            ></v-pagination>
          </v-toolbar>
          <v-card
            v-for="item in posts"
            :key="item.id"
            flat
            color="transparent"
            class="white--text"
          >
            <v-card-title class="headline font-italic">
              {{ item.title }}
              <v-btn
                v-if="item.category"
                x-small
                rounded
                color="teal lighten-3"
                class="ml-4"
              >
                {{ item.category }}
              </v-btn>
            </v-card-title>
            <v-card-subtitle class="white--text">
              <v-icon color="light-blue lighten-4">mdi-alarm-plus</v-icon> {{ item.pubdate }}
              <v-icon color="cyan" class="ml-3">mdi-eye</v-icon> {{ item.pv }}
              <!-- TODO: 增加喜欢数量 -->
              <!-- <v-icon class="ml-3" color="red">mdi-heart</v-icon> {{ item.like }} -->
            </v-card-subtitle>
            <v-card-text>
              <v-banner
                single-line
                color="transparent"
                class="white--text"
              >
                {{ item.content }}
                <template v-slot:actions>
                  <v-btn
                    text
                    color="cyan"
                    :to="{ name: 'blog_detail', params: { id: item.id }}"
                  >
                    Detail
                  </v-btn>
                </template>
              </v-banner>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="2" class="main-bg">
          <v-card
            flat
            color="transparent"
            class="white--text"
          >
            <v-card-title>
              <v-badge
                color="deep-purple accent-4"
                :content="categoryTotal"
              >
                分类
              </v-badge>
            </v-card-title>
            <v-card-text>
              <v-chip-group
                column
                active-class="primary"
              >
                <v-chip
                  v-for="item in categories"
                  :key="item.id"
                  small
                  link
                  @click="changeCurrentCategoryId(item.id)"
                >
                  {{ item.name }}({{ item.total }})
                </v-chip>
              </v-chip-group>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-img>
  </div>
</template>

<script>
import { fetchPosts, fetchCategories } from '@/api/blog'

export default {
  data: () => ({
    posts: [],
    categories: [],
    page: 1,
    pages: 0,
    page_size: 6,
    postTotal: 0,
    categoryTotal: 0,
    currentCategoryId: ''
  }),
  created () {
    this.getPagePosts()
    this.getCategories()
  },
  methods: {
    getPagePosts () {
      fetchPosts({
        'page': this.page,
        'page_size': this.page_size,
        'category_id': this.currentCategoryId
      }).then(response => {
        // console.log(response.data)
        this.posts = response.data.posts
        this.postTotal = response.data.total
        this.pages = Math.ceil(response.data.total / this.page_size)
      }).catch(error => {
        console.log(error)
      })
    },
    getCategories () {
      fetchCategories(
      ).then(response => {
        // console.log(response.data)
        this.categories = response.data
        this.categoryTotal = response.data.length
      }).catch(error => {
        console.log(error)
      })
    },
    handlePage (val) {
      // console.log(`当前页: ${val}`)
      this.getPagePosts()
    },
    changeCurrentCategoryId (categoryId) {
      this.page = 1 // 初始化页码
      if (this.currentCategoryId === categoryId) {
        this.currentCategoryId = ''
      } else {
        this.currentCategoryId = categoryId
      }
    }
  },
  watch: {
    currentCategoryId: function () {
      this.getPagePosts()
    }
  }
}
</script>

<style scoped>
.main-bg {
  background:rgba(0,0,0,0.3);
}
</style>
