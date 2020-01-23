<template>
  <div class="x-login">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" autocomplete="on" label-position="left" size="medium" class="x-login-form">
      <div class="title-container">
        <h3 class="title">系统登录</h3>
      </div>
      <el-form-item prop="username">
        <span class="el-icon-user x-login-icon" />
        <el-input
          v-model="ruleForm.username"
          placeholder="Username"
        />
      </el-form-item>
      <el-form-item prop="password">
        <span class="el-icon-key x-login-icon" />
        <el-input
          v-model="ruleForm.password"
          placeholder="Password"
          show-password
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" style="width:100%;" @click="submitForm('ruleForm')">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { login } from '@/api/auth'

export default {
  data () {
    return {
      ruleForm: {
        username: '',
        password: ''
      },
      rules: {
        username: [
          { required: true, message: 'admin', trigger: 'blur' },
          { min: 3, max: 15, message: '长度在 3 到 10 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'admin', trigger: 'blur' },
          { min: 5, max: 18, message: '长度在 5 到 18 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (form) {
      this.$refs[form].validate((valid) => {
        if (valid) {
          login({
            username: this.ruleForm.username,
            password: this.ruleForm.password
          }).then(response => {
            this.$message.success('登录成功')
            // 保存token
            this.$store.commit('set_token', response.data.token)
            this.$router.push('/admin/dashboard')
          }).catch(error => {
            console.log(error)
            switch (error.status) {
              case 404:
                this.$message.error('用户不存在!')
                break
              case 400:
                this.$message.error('密码错误!')
                break
              default:
                this.$message.error(error.status)
            }
          })
        } else {
          this.$message.error('表单验证失败!')
          return false
        }
      })
    }
  }
}
</script>

<style lang="scss">
$bg:#283443;
$light_gray:#fff;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .x-login .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.x-login {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;
    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 47px;
      caret-color: $cursor;
      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }
  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
    [class^=el-icon-] {
      font-weight: 1000;
    }
  }
}
</style>

<style lang="scss" scoped>
$bg:#2d3a4b;
$dark_gray:#889aa4;
$light_gray:#eee;

.x-login {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;
  .x-login-form {
    position: relative;
    width: 480px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
  }
  .title-container {
    position: relative;
    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }
  .x-login-icon {
    padding: 6px 5px 6px 1px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }
}
</style>
