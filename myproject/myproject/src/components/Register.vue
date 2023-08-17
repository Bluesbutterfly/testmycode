<script setup lang="ts">
import { ref, reactive } from 'vue';
import { IconFont } from 'tdesign-icons-vue-next';
import { MessagePlugin } from 'tdesign-vue-next';
import { register } from '@/api/user'
import { error } from 'console';
const emit = defineEmits<{
  (e: 'change', id: number): void
}>()
const form = ref(null);
const formData = reactive({
  account: '',
  nickName: '',
  telphone: '',
  email: '',
  password: '',
  rePassword: '',
});

const onReset = () => {
  MessagePlugin.success('重置成功');
};
const onIconClose = () => {
  emit('change',3)
};
const onSubmit = ({ validateResult, firstError, e }) => {
  e.preventDefault();
  if (validateResult === true) {
    console.log(formData)
    register(formData).then(res=>{
      MessagePlugin.success('注册成功');
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

const rePassword = (val:any) =>
  new Promise((resolve) => {
    const timer = setTimeout(() => {
      resolve(formData.password === val);
      clearTimeout(timer);
    });
  });

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
  nickName:[
  { required: true, message: '昵称不能为空', type: 'error' },
    {
      min: 2,
      message: '至少需要两个字',
      type: 'error',
      trigger: 'blur',
    },
  ],
  telphone:[
    {
      min: 2,
      message: '至少需要两个字',
      type: 'error',
      trigger: 'blur',
    },
  ],
  email:[
    {
      min: 2,
      message: '至少需要两个字',
      type: 'error',
      trigger: 'blur',
    },
  ],
  password: [{ required: true, message: '密码不能为空', type: 'error' }, { validator: passwordValidator }],
  rePassword: [
    // 自定义校验规则
    { required: true, message: '密码不能为空', type: 'error' },
    { validator: rePassword, message: '两次密码不一致' },
  ],
};
</script>
<template>
  <div class="dialog">
    <div class="registers">
    <div class="header">
      <h2>注册</h2>
      <div class="closebtn">
        <a href="javascript:void(0);">
          <icon-font name="close" @click="onIconClose" />
        </a>
      </div>
    </div>
      <t-form ref="form" :data="formData" :rules="rules" @reset="onReset" @submit="onSubmit" @validate="onValidate">
        <t-form-item label="用户名" name="account">
          <t-input v-model="formData.account" placeholder="请输入用户名"></t-input>
        </t-form-item>

        <t-form-item label="昵称" name="nickName">
          <t-input v-model="formData.nickName" placeholder="请输入昵称"></t-input>
        </t-form-item>

        <t-form-item label="手机号码" name="telphone">
          <t-input v-model="formData.telphone" placeholder="请输入手机号码"></t-input>
        </t-form-item>

        <t-form-item label="邮箱" name="email">
          <t-input v-model="formData.email" placeholder="请输入邮箱"></t-input>
        </t-form-item>

        <t-form-item label="密码" name="password" help="6-16位密码">
          <t-input v-model="formData.password" type="password" placeholder="请输入密码"></t-input>
        </t-form-item>

        <t-form-item label="确认密码" name="rePassword" help="自定义异步校验方法">
          <t-input v-model="formData.rePassword" type="password" placeholder="请再次输入密码"></t-input>
        </t-form-item>

        <t-form-item>
          <t-space size="small">
            <t-button theme="primary" type="submit">立即注册</t-button>
            <t-button theme="default" variant="base" type="reset">重置</t-button>
          </t-space>
        </t-form-item>
      </t-form>
    </div>
  </div>
</template>
