<template>
  <div class="body">
    <Music></Music>
    <Skill6></Skill6>
  </div>
</template>
<script>
import Skill6 from "@/components/technology/Skill6";
import Music from "@/components/video/MiniPlayer";

export default {
  name: "ViewsTechnologySkill6",
  components: {
    Skill6,
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