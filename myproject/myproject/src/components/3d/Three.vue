<template>
  <div class="threeclass" ref="threeRef"></div>
</template>
<script lang="ts"> 
import { defineComponent, onMounted,ref} from 'vue'
import {Scene,WebGLRenderer,Color,PerspectiveCamera,Mesh,BoxGeometry,MeshBasicMaterial,AxesHelper} from 'three'

export default defineComponent({
  setup() {

      const  threeRef=ref()

      function init(){
        console.log("开始构建3D模型")
        // 创建3D场景对象Scene
        const scene=new Scene()// 创建渲染器对象
        const renderer = new WebGLRenderer({antialias:true});
        // AxesHelper：辅助观察的坐标系
        const axesHelper = new AxesHelper(150);
        scene.add(axesHelper);
        // 定义threejs输出画布的尺寸(单位:像素px)
        const width = 800; //宽度
        const height = 500; //高度
        renderer.setClearColor(new Color(0xEEEEEE))
        renderer.setSize(width, height);
        //创建一个材质对象Material
        const material = new MeshBasicMaterial({
            color: 0xff0000,//0xff0000设置材质颜色为红色
        }); 
        // 实例化一个透视投影相机对象
        // 30:视场角度, width / height:Canvas画布宽高比, 1:近裁截面, 3000：远裁截面
        const camera = new PerspectiveCamera(30, width / height, 1, 3000);
        // 长方体尺寸100, 100, 100
        const geometry = new BoxGeometry( 100, 100, 100 );
        // 两个参数分别为几何体geometry、材质material
        const mesh = new Mesh(geometry,material);
        // 相机位置xyz坐标：0,10,0
        mesh.position.set(0,10,0);
        scene.add(mesh);
        //相机在Three.js三维坐标系中的位置
        // 根据需要设置相机位置具体值
        camera.position.set(200, 200, 200); 
        //相机观察目标指向Threejs 3D空间中某个位置
        camera.lookAt(scene.position); //坐标原点
        threeRef.value.appendChild(renderer.domElement)

        renderer.render(scene, camera); //执行渲染操作
      }
      
      onMounted(()=>{
          init();
      })
      return{
          threeRef
      }
  },
})
</script>