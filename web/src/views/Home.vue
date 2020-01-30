<template>
  <div>
    <section>
      <v-parallax src="@/assets/home1.jpeg" height="600">
        <v-row align="center">
          <v-col align="center" >
            <!-- <img src="@/assets/vuetify.png" alt="home-top" height="220"> -->
            <v-icon x-large class="blue--text text--lighten-2 display-4 mb-7">mdi-cannabis</v-icon>
            <div class="white--text mb-2 display-1">XCMS - 邢的内容管理系统</div>
            <div class="subheading mb-4">Xing Weidong's content management system</div>
            <v-btn
              class="mt-12"
              color="blue lighten-2"
              dark
              large
              href="https://github.com/Xingwd/xcms"
              target="_blank"
            >
              github
            </v-btn>
          </v-col>
        </v-row>
      </v-parallax>
    </section>

    <section>
      <v-container>
        <v-row class="my-12" justify="center">
          <v-col align="center" xs12 sm4>
            <v-card
              flat
              class="transparent"
              to="/blog"
            >
              <v-card-text class="text-center">
                <v-icon x-large class="blue--text text--lighten-2">mdi-feather</v-icon>
              </v-card-text>
              <v-card-title primary-title class="justify-center">
                <div class="headline text-center">博客</div>
              </v-card-title>
              <v-card-text>
                千里之行，始于足下
              </v-card-text>
            </v-card>
          </v-col>
          <!-- <v-col align="center" xs12 sm4>
            <v-card
              flat
              class="transparent"
              to="xuesi"
            >
              <v-card-text class="text-center">
                <v-icon x-large class="blue--text text--lighten-2">mdi-sprout</v-icon>
              </v-card-text>
              <v-card-title primary-title class="justify-center">
                <div class="headline">学思</div>
              </v-card-title>
              <v-card-text>
                学而不思则惘，思而不学则怠
              </v-card-text>
            </v-card>
          </v-col> -->
          <v-col align="center" xs12 sm4>
            <v-card
              flat
              class="transparent"
              to="/project"
            >
              <v-card-text class="text-center">
                <v-icon x-large class="blue--text text--lighten-2">mdi-github-circle</v-icon>
              </v-card-text>
              <v-card-title primary-title class="justify-center">
                <div class="headline text-center">项目</div>
              </v-card-title>
              <v-card-text>
                学以致用，用以致学
              </v-card-text>
            </v-card>
          </v-col>
          <v-col align="center" xs12 sm4>
            <v-card
              flat
              class="transparent"
              to="/history"
            >
              <v-card-text class="text-center">
                <v-icon x-large class="blue--text text--lighten-2">mdi-seed</v-icon>
              </v-card-text>
              <v-card-title primary-title class="justify-center">
                <div class="headline text-center">历程</div>
              </v-card-title>
              <v-card-text>
                繁花易落尽，流年不再来
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <section>
      <v-parallax src="@/assets/home2.jpg" height="380">
        <v-row align="center">
          <v-col align="center">
            <div class="white--text mb-2 display-1">自强不息，厚德载物</div>
            <div class="subheading">Self-discipline and Social Commitment</div>
            <v-btn
              class="mt-12"
              color="blue lighten-2"
              dark
              large
              href="https://github.com/Xingwd/xcms"
              target="_blank"
            >
              github
            </v-btn>
          </v-col>
        </v-row>
      </v-parallax>
    </section>

    <section>
      <v-container>
        <v-row justify="center" class="mt-7 mb-12">
          <v-col xs12 sm4 class="px-12">
            <v-card flat class="transparent">
              <v-card-title primary-title class="justify-center">
                <div class="headline">声明</div>
              </v-card-title>
              <v-card-text>
                <p>本站为个人内容管理系统，仅用于学习和参考，部分资源来源于网络，如有侵权，请联系我及时删除。</p>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col xs12 sm4 class="px-12">
            <v-card flat class="transparent">
              <v-card-title primary-title class="justify-center">
                <div class="headline">联系我</div>
              </v-card-title>
              <v-card-text>
                可通过以下方式联系本人。非必要情况，请勿打扰，谢谢。
              </v-card-text>
              <v-list class="transparent">
                <v-list-item>
                  <v-list-item-action>
                    <v-icon class="blue--text text--lighten-2">mdi-email</v-icon>
                  </v-list-item-action>
                  <v-list-item-content>
                    <v-list-item-title>1274296417@qq.com</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>
  </div>
</template>

<script>

export default {
  name: 'home',
  components: {
  },
  data () {
    return {
      title: 'XCMS'
    }
  }
}
</script>
