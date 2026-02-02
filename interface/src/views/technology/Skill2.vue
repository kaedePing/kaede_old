<template>
  <div class="body">
    <Skill2List></Skill2List>
    <Skill2></Skill2>
  </div>
</template>

<script>
import Skill2 from "@/components/technology/Skill2";
import Skill2List from "@/components/technology/Skill2List";

export default {
  name: "ViewsTechnologySkill2",
  components: {
    Skill2,
    Skill2List,
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