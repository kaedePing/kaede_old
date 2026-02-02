<template>
  <div class="body">
    <!--    <Self></Self>-->
    <Music></Music>
    <LifeDiary></LifeDiary>
  </div>
</template>

<script>
import LifeDiary from "../../components/life/Diary";
import Music from "../../components/video/MiniPlayer";

export default {
  name: "ViewsLifeDiary",
  components: {
    LifeDiary,  // 个人所思
    Music,

  }
}
</script>


<style>
* {
  padding: 0;
  margin: 0;
}

.body {
  margin-top: 10px;
}
</style>