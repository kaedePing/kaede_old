<template>
  <div class="body">
    <Music></Music>
    <Skill5></Skill5>
  </div>
</template>
<script>
import Skill5 from "@/components/technology/Skill5";
import Music from "@/components/video/MiniPlayer";

export default {
  name: "ViewsTechnologySkill5",
  components: {
    Skill5,
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