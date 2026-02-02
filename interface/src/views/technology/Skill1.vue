<template>
  <div class="body">
    <Skill1List></Skill1List>
    <Skill1></Skill1>
  </div>
</template>

<script>
import Skill1 from "@/components/technology/Skill1";
import Skill1List from "@/components/technology/Skill1List";

export default {
  name: "ViewsTechnologySkill1",
  components: {
    Skill1,
    Skill1List,
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