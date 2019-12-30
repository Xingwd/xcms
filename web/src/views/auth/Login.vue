<template>
  <!-- TODO: 完善登陆视图 -->
  <div class="x-bg">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" size="small" class="x-login">
      <el-form-item label="Username" prop="username">
        <el-input v-model="ruleForm.username"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input v-model="ruleForm.password" show-password></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">Login</el-button>
        <el-button @click="resetForm('ruleForm')">Reset</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
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
          { min: 2, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'admin', trigger: 'blur' },
          { min: 6, max: 18, message: '长度在 6 到 18 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/styles/variables.scss';

.x-bg {
  height: 100%;
  background-color: $menuBg;
  .x-login {
    width: 300px;
    margin: 0 auto; /*水平居中*/
    position: relative; /*脱离文档流*/
    top: 50%; /*偏移*/
    margin-top: -180px;
    // background-color: $menuBg;
  }
}
</style>
