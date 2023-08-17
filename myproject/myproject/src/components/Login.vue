<script setup lang="ts">
import { ref, reactive } from 'vue';
import { IconFont } from 'tdesign-icons-vue-next';
import { MessagePlugin } from 'tdesign-vue-next';
import { Login } from '@/api/user'
import { error } from 'console';
import { getToken, setToken } from 'utils/auth'

const emit = defineEmits<{
  (e: 'change', id: number): void
}>()

const form = ref(null);
const formData = reactive({
  account: '',
  password: ''
});

const onReset = () => {
  MessagePlugin.success('重置成功');
};
const onIconClose = (num:number) => {
  emit('change',num)
};
const onSubmit = ({ validateResult, firstError, e }) => {
  e.preventDefault();
  if (validateResult === true) {
    Login(formData).then(res=>{
      if (res.code == 200) {
        setToken(res.data.token)
        MessagePlugin.success(res.message);
        location.reload()
      }else{
        MessagePlugin.error(res.message);
      }
    }).catch(error=>{
      MessagePlugin.error("网络发生错误，请求中断！");
    })
  } else {
    console.log('Validate Errors: ', firstError, validateResult);
    MessagePlugin.warning(firstError);
  }
};

const onValidate = ({ validateResult, firstError }) => {
  if (validateResult === true) {
    console.log('Validate Success');
  } else {
    console.log('Validate Errors: ', firstError, validateResult);
  }
};


const passwordValidator = (val:any) => {
  const pattern = /^[\w_-]{6,16}$/
  const valPattern = !pattern.test(val)
  if (valPattern) {
    return { result: false, message: '请输入6-16位密码！', type: 'warning' };
  }
  return { result: true, message: '符合密码强度！', type: 'success' };
};

const rules = {
  account: [
    { required: true, message: '姓名不能为空', type: 'error' },
    {
      min: 2,
      message: '至少需要两个字',
      type: 'error',
      trigger: 'blur',
    },
  ],
  password: [{ required: true, message: '密码不能为空', type: 'error' }, { validator: passwordValidator }]
};
</script>
<template>
  <div class="dialog">
    <div class="registers">
      <a href="javascript:void(0);" @click="onIconClose(2)">注册</a>
      <div class="header">
        <h2>登录</h2>
        <div class="closebtn">
          <a href="javascript:void(0);">
            <icon-font name="close" @click="onIconClose(1)" />
          </a>
        </div>
      </div>
      <t-form ref="form" :data="formData" :rules="rules" @reset="onReset" @submit="onSubmit" @validate="onValidate">
        <t-form-item label="用户名" name="account">
          <t-input v-model="formData.account" placeholder="请输入用户名"></t-input>
        </t-form-item>

        <t-form-item label="密码" name="password" help="6-16位密码">
          <t-input v-model="formData.password" type="password" placeholder="请输入密码"></t-input>
        </t-form-item>

        <t-form-item>
          <t-space size="small">
            <t-button theme="primary" type="submit">立即登录</t-button>
            <t-button theme="default" variant="base" type="reset">重置</t-button>
          </t-space>
        </t-form-item>
      </t-form>
    </div>
  </div>
</template>
