<template>
  <v-app light>
    <v-toolbar color="white">
      <v-toolbar-title v-text="title"></v-toolbar-title>
    </v-toolbar>
    <v-content>
      <section>
        <v-parallax src="@/assets/home1.jpeg" height="600">
          <v-row align="center">
            <v-col align="center" >
              <!-- <img src="@/assets/vuetify.png" alt="home-top" height="220"> -->
              <v-icon x-large class="blue--text text--lighten-2 display-4 mb-7">mdi-cannabis</v-icon>
              <div class="white--text mb-2 display-1">XCMS - 老邢的内容管理系统</div>
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
        <v-row class="my-12" align="center">
          <v-col xs12>
            <v-container>
              <v-row align="center">
                <v-col align="center" xs12 md4>
                  <v-card flat class="transparent">
                    <v-card-text class="text-center">
                      <v-icon x-large class="blue--text text--lighten-2">mdi-feather</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-center">博客</div>
                    </v-card-title>
                    <v-card-text>
                      学而不思则惘，思而不学则怠
                    </v-card-text>
                  </v-card>
                </v-col>
                <v-col align="center" xs12 md4>
                  <v-card flat class="transparent">
                    <v-card-text class="text-center">
                      <v-icon x-large class="blue--text text--lighten-2">mdi-sprout</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline">学思</div>
                    </v-card-title>
                    <v-card-text>
                      学而不思则惘，思而不学则怠
                    </v-card-text>
                  </v-card>
                </v-col>
                <v-col align="center" xs12 md4>
                  <v-card flat class="transparent">
                    <v-card-text class="text-center">
                      <v-icon x-large class="blue--text text--lighten-2">mdi-github-circle</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-center">项目</div>
                    </v-card-title>
                    <v-card-text>
                      学而不思则惘，思而不学则怠
                    </v-card-text>
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
          </v-col>
        </v-row>
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
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline">声明</div>
                </v-card-title>
                <v-card-text>
                  <p>本站为个人内容管理系统，仅用于学习和参考，部分资源来源于网络，如有侵权，请联系我及时删除。</p>
                  <p>站内内容，仅代表发布时的观点，不代表未来观点，如发现问题，请及时联系我。</p>
                  <p>内容除非特别说明，否则均为原创，转载请注明出处。</p>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col xs12 sm4 class="px-12">
              <v-card flat class="transparent">
                <v-card-title primary-title class="layout justify-center">
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

      <v-footer
        padless
        absolute
        class="font-weight-medium"
      >
        <v-col
          class="text-center"
          cols="12"
        >
          &copy; {{ new Date().getFullYear() }} — <strong>邢为栋</strong>
        </v-col>
      </v-footer>
    </v-content>
  </v-app>
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
