<template>
  <div class="body">
    <Skill8List></Skill8List>
    <Skill8></Skill8>
  </div>
</template>
<script>
import Skill8 from "@/components/technology/Skill8";
import Skill8List from "@/components/technology/Skill8List";

export default {
  name: "ViewsTechnologySkill8",
  components: {
    Skill8,
    Skill8List
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