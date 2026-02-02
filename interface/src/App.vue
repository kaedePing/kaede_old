<template>
  <div id="app">
    <div id="canvas">
      <!--      粒子特效参数-->
      <vue-particles
          color="#555"
          :particleOpacity="0.7"
          :particlesNumber="150"
          shapeType="circle"
          :particleSize="4"
          linesColor="#555"
          :linesWidth="1"
          :lineLinked="true"
          :lineOpacity="0.4"
          :linesDistance="150"
          :moveSpeed="2"
          :hoverEffect="true"
          hoverMode="grab"
          :clickEffect="false"
          clickMode="push"
          class="lizi"
      />
    </div>

    <Header></Header>
    <!--    加载路由-->
    <router-view/>
  </div>
</template>

<script type="text/javascript">
import Header from "./components/home/Header"

export default {
  name: 'WebApp',
  data() {
    return {}
  },
  methods: {},
  mounted() {
    // 关闭浏览器窗口的时候清空浏览器缓存在localStorage的数据
    window.onbeforeunload = function (e) {
      var storage = window.localStorage;
      storage.clear()
    }
  },
  components: {
    Header
  }
}

</script>

<style>
* {
  padding: 0;
  margin: 0;
}

body {
  width: 100%;
  background-color: rgb(239, 239, 239);
}

.lizi {
  position: fixed;
  top: 0;
  width: 100%;
}


</style>
