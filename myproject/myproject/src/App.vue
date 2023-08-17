<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { removeToken } from 'utils/auth'
import { MessagePlugin } from 'tdesign-vue-next';
import { GetuserStatus } from '@/api/user'
import { onMounted } from 'vue'
import { useStore } from '@/stores/counter'
const store = useStore();
const { nickName } = store
onMounted(() => {
  getUser()
})
const getUser = () => {
  GetuserStatus().then(res=>{
    if (res.code == 200) {
      store.nickName = res.data.nickName
    }else{
      removeToken()
    }
  }).catch(error=>{
    MessagePlugin.error("网络发生错误，请求中断！");
   })
}
</script>

<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->
    <div class="wrapper">
      <!-- <HelloWorld msg="测试项目" /> -->
      <!-- <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav> -->
      <div class="tdesign-demo-item--grid">
        <t-row :gutter="16">
          <t-col :span="3">
            <RouterLink to="/">Home</RouterLink>
          </t-col>
          <t-col :span="3">
            <div>col-3</div>
          </t-col>
          <t-col :span="3">
            <div>col-3</div>
          </t-col>
          <t-col :span="3">
            <RouterLink to="/about">About</RouterLink>
          </t-col>
        </t-row>
      </div>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
@import '@/assets/style/common.scss';
header {
  line-height: 1.5;
  max-height: 100vh;
}

main{
  width: 100%;
  text-align: center;
}
.logo {
  display: block;
  margin: 0 auto 2rem;
}

.tdesign-demo-item--grid{
  width: 100%;
  position: fixed;
  bottom: 0;
  left: 0;
  text-align: center;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    /* padding-right: calc(var(--section-gap) / 2); */
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
