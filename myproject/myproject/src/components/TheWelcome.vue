<script setup lang="ts">
import WelcomeItem from './WelcomeItem.vue'
// import DocumentationIcon from './icons/IconDocumentation.vue'
// import ToolingIcon from './icons/IconTooling.vue'
// import EcosystemIcon from './icons/IconEcosystem.vue'
// import CommunityIcon from './icons/IconCommunity.vue'
// import SupportIcon from './icons/IconSupport.vue'
import Three from './3d/Three.vue'
import { ref } from 'vue';
import { MessagePlugin } from 'tdesign-vue-next';
const file1 = ref([]);
const disabled = ref(false);
const autoUpload = ref(true);
const uploadAllFilesInOneRequest = ref(false);
const handleFail = ({ file }) => {
  MessagePlugin.error(`文件 ${file.name} 上传失败`);
};
</script>

<template>
  <WelcomeItem>
    <template #head>
      标题
    </template>
    <template #heading>
      标题
    </template>
    <template #froom>
      <div>
        <t-space>
          <t-upload
            ref="uploadRef1"
            v-model="file1"
            action="https://service-bv448zsw-1257786608.gz.apigw.tencentcs.com/api/upload-demo"
            theme="image"
            tips="单张图片文件上传（上传成功状态演示）"
            accept="image/*"
            :disabled="disabled"
            :auto-upload="autoUpload"
            :upload-all-files-in-one-request="uploadAllFilesInOneRequest"
            :locale="{
              triggerUploadText: {
                image: '请选择图片',
              },
            }"
            @fail="handleFail"
          >
            <!-- custom UI -->
            <!-- <template #fileListDisplay="{ files }">
              <div>{{ JSON.stringify(files) }}</div>
            </template> -->
          </t-upload>

          <t-button>提交</t-button>
        </t-space>
      </div>
    </template>
    <template #room>
      <Three />
    </template>
  </WelcomeItem>
</template>
