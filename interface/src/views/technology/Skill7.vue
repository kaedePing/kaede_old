<template>
  <div class="body">
    <Skill7List></Skill7List>
    <Skill7></Skill7>
  </div>
</template>
<script>
import Skill7 from "@/components/technology/Skill7";
import Skill7List from "@/components/technology/Skill7List";

export default {
  name: "ViewsTechnologySkill7",
  components: {
    Skill7,
    Skill7List
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