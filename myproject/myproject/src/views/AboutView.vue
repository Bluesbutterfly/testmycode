<script setup lang="ts">
import Register from 'components/Register.vue'
import Login from 'components/Login.vue'
import { logout } from '@/api/user'
import { getToken } from 'utils/auth'
import { reactive,onMounted,ref } from 'vue'
import { useCounterStore, useStore } from '@/stores/counter'
import { storeToRefs } from "pinia";
import { DialogPlugin } from 'tdesign-vue-next'
const store = useStore();
const { nickName } = store
const test = useCounterStore();
const { count } = storeToRefs(test)

const user= reactive({
  nickName:'',
  token:''
})
const showRegister = ref(false);
const showLogin = ref(false);
onMounted(() => {
  getUser()
})
const getUser = () => {
  if (getToken()) {
    user['nickName'] = nickName
    user.token = getToken()
  }
}
const login = () => {
  // count.value = 1
  showLogin.value = true;
}
const logouts = () => {
  logout().then(res=>{
    console.log(res)
    location.reload()
  }).catch(error=>{
    console.log(error)
  })
}
const dialogPlugins = (val:number) => {
  switch (val) {
    case 1:
      showLogin.value = false;
      break;
    case 2:
      showLogin.value = false;
      showRegister.value = true;
      break;
    default:
      showLogin.value = false;
      showRegister.value = false;
      break;
  }
}
</script>
<template>
  <div class="about">
    <Register v-if="showRegister" @change="dialogPlugins"/>
    <Login v-if="showLogin" @change="dialogPlugins"/>
    <t-layout>
      <t-header>
        <div class="userfn">
          <div class="usermsg" v-if="user.token">
            <t-avatar image="https://tdesign.gtimg.com/site/avatar.jpg" />
            <span>{{ user.nickName }}</span>
            <a href="javascript:void(0);" @click="logouts">注销</a>
          </div>
          <div v-else>
            <a href="javascript:void(0);" @click="login">登录</a>
          </div>
        </div>
      </t-header>
      <t-content>Content</t-content>
      <t-footer>Footer</t-footer>
    </t-layout>
  </div>
</template>

<style>
@import '@/assets/style/login.scss';
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
