<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules">

      <div class="createPost-main-container">
        <el-row>
          <el-col :span="5">
            <el-form-item prop="category_name" label-width="50px" label="Category:">
              <el-select
                v-model="postForm.category_name"
                :remote-method="getCategories"
                filterable
                default-first-option
                remote
                size="medium"
                placeholder="Search category">
                <el-option v-for="item in categories" :key="item.id" :label="item.id" :value="item.name" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2" :offset="17">
            <el-button class="publish" v-loading="loading" type="success" @click="submitForm">
              Publish
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="24">
            <el-form-item style="margin-bottom: 40px;" prop="title">
              <MDinput v-model="postForm.title" :maxlength="100" name="name" required>
                Title
              </MDinput>
            </el-form-item>
          </el-col>
        </el-row>

        <el-form-item prop="content">
           <!-- TODO: 设置自适应最小高度  -->
          <mavon-editor v-model="postForm.content" style="min-height: 630px"/>
        </el-form-item>
      </div>
    </el-form>
  </div>
</template>

<script>
import MDinput from '@/components/MDinput'
import { fetchPost, createPost, fetchCategories } from '@/api/blog'

const defaultForm = {
  category_name: '', // 文章分类
  title: '', // 文章题目
  content: '' // 文章内容
}

export default {
  name: 'ArticleDetail',
  components: { MDinput },
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data () {
    const validateRequire = (rule, value, callback) => {
      if (value === '') {
        this.$message({
          message: rule.field + '为必传项',
          type: 'error'
        })
        callback(new Error(rule.field + '为必传项'))
      } else {
        callback()
      }
    }
    return {
      postForm: Object.assign({}, defaultForm),
      loading: false,
      categories: [],
      rules: {
        title: [{ validator: validateRequire }],
        content: [{ validator: validateRequire }]
      }
    }
  },
  created () {
    if (this.isEdit) {
      const id = this.$route.params && this.$route.params.id
      this.fetchData(id)
    }
  },
  methods: {
    fetchData (id) {
      fetchPost(id).then(response => {
        this.postForm = response.data
      }).catch(err => {
        console.log(err)
      })
    },
    submitForm () {
      // console.log(this.postForm)
      this.$refs.postForm.validate(valid => {
        if (valid) {
          this.loading = true
          createPost(this.postForm
          ).then(response => {
            this.$notify({
              title: '成功',
              message: '发布文章成功',
              type: 'success',
              duration: 2000
            })
          }).catch(error => {
            this.$message.error(error)
          })
          this.loading = false
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    getCategories (query) {
      fetchCategories(query).then(response => {
        if (!response.data) return
        this.categories = response.data
      })
    }
  }
}
</script>

<style lang="scss" scoped>

.createPost-container {
  .publish {
    float: right;
  }
  .createPost-main-container {
    padding: 42px 25px 1px 30px;
  }
}

</style>
