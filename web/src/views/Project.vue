<template>
  <v-container class="mt-12">
    <v-data-iterator
      :items="items"
      hide-default-footer
    >
      <template v-slot:default="props">
        <v-row>
          <v-col
            v-for="item in props.items"
            :key="item.name"
            cols="12"
            sm="12"
            md="6"
            lg="4"
          >
            <v-card height="150px">
              <v-card-title>
                <v-badge
                  :value="hover"
                  color="deep-purple"
                  :content="item.type"
                  right
                  transition="slide-x-transition"
                >
                  <v-hover v-model="hover">
                    <v-icon color="grey lighten-1">
                    {{ item.name }}
                  </v-icon>
                  </v-hover>
                </v-badge>
                <v-spacer></v-spacer>
                <v-btn
                  text
                  icon
                  color="cyan"
                  :href="item.url"
                  target="_blank"
                >
                  <v-icon>mdi-github-circle</v-icon>
                </v-btn>

              </v-card-title>
              <v-card-text class="">
                <p>{{ item.text }}</p>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </template>
    </v-data-iterator>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    hover: false,
    items: [
      {
        name: 'Xcms',
        type: '个人项目',
        url: 'https://github.com/Xingwd/xcms',
        text: '个人内容管理系统，该网站源码'
      },
      {
        name: 'Python爬虫',
        type: '个人项目',
        url: 'https://github.com/Xingwd/python-spider',
        text: '使用Scrapy编写的爬虫，仅用于学习与分享'
      },
      {
        name: 'Ambari Services',
        type: '二次开发',
        url: 'https://github.com/Xingwd/ambari-services',
        text: '开发Apache Ambari的服务插件'
      },
      {
        name: 'Django cms',
        type: '个人项目',
        url: 'https://github.com/Xingwd/django-xwd-cms',
        text: '使用Django开发的简单个人内容管理系统'
      },
      {
        name: '区块链溯源',
        type: '个人项目',
        url: 'https://github.com/Xingwd/bigchaindb-learn',
        text: '使用Bigchaindb开发的一个茶叶溯源系统Demo'
      },
      {
        name: 'Leveldbjni',
        type: '二次开发',
        url: 'https://github.com/Xingwd/leveldbjni',
        text: '对leveldbjni进行二次开发，增加支持aarch64和mips64el的CPU架构'
      },
      {
        name: 'Leveldb',
        type: '二次开发',
        url: 'https://github.com/Xingwd/leveldb',
        text: '对leveldb进行二次开发，以支持leveldbjni的二次开发'
      }
    ]
  })
}
</script>
