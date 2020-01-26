<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules">
      <div class="createPost-main-container">
        <el-row>
          <el-col :span="5">
            <el-form-item prop="category_id" label-width="50px" label="Category:">
              <el-select
                v-model="postForm.category_id"
                filterable
                clearable
                default-first-option
                size="medium"
                placeholder="Search category">
                <el-option
                  v-for="item in categories"
                  :key="item.id"
                  :label="item.name"
                  :value="item.id" />
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
import { fetchPost, createPost, updatePost, fetchCategories } from '@/api/blog'

const defaultForm = {
  category_id: '', // 文章分类
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
        content: [{ validator: validateRequire }],
        category_id: [{ validator: validateRequire }]
      }
    }
  },
  created () {
    if (this.isEdit) {
      const id = this.$route.params && this.$route.params.id
      this.fetchData(id)
    }
    this.getAllCategories()
  },
  methods: {
    fetchData (id) {
      fetchPost(id).then(response => {
        this.postForm = response.data
      }).catch(error => {
        this.$message.error(error)
      })
    },
    submitForm () {
      this.$refs.postForm.validate(valid => {
        if (valid) {
          let data = {
            'title': this.postForm.title,
            'content': this.postForm.content,
            'category_id': this.postForm.category_id
          }
          this.loading = true
          if (this.isEdit) {
            updatePost(this.$route.params.id, data
            ).then(response => {
              this.$notify({
                title: '成功',
                message: '更新文章成功',
                type: 'success',
                duration: 2000,
                offset: 70
              })
              this.postForm = {}
            }).catch(error => {
              this.$message.error(error)
            })
          } else {
            createPost(data
            ).then(response => {
              this.$notify({
                title: '成功',
                message: '发布文章成功',
                type: 'success',
                duration: 2000,
                offset: 70
              })
              this.postForm = {}
            }).catch(error => {
              this.$message.error(error)
            })
          }
          this.loading = false
        } else {
          this.$message.error('提交错误！！')
          return false
        }
      })
    },
    getAllCategories () {
      fetchCategories(
      ).then(response => {
        this.categories = response.data
      }).catch(error => {
        this.$message.error(error)
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
