<template>
  <div class="body">
    <Music></Music>
    <LifeReading></LifeReading>
  </div>
</template>

<script>
import LifeReading from "../../components/life/Reading";
import Music from "../../components/video/MiniPlayer";

export default {
  name: "ViewsLifeReading",
  components: {
    LifeReading,  // 个人所思
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