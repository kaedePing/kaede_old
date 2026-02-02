<template>
  <div class="body">
    <Skill3List></Skill3List>
    <Skill3></Skill3>
  </div>
</template>
<script>
import Skill3 from "@/components/technology/Skill3";
import Skill3List from "@/components/technology/Skill3List";
export default {
  name: "ViewsTechnologySkill3",
  components:{
    Skill3,
    Skill3List
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