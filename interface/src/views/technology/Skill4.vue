<template>
  <div class="body">
    <Music></Music>
    <Skill4></Skill4>
  </div>
</template>
<script>
import Skill4 from "@/components/technology/Skill4";
import Music from "@/components/video/MiniPlayer";
export default {
  name: "ViewsTechnologySkill4",
  components:{
    Skill4,
    Music
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