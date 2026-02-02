<template>
  <div class="body">
    <Music></Music>
  </div>
</template>
<script>
import Music from "@/components/video/Music";

export default {
  name: "ViewsVideoMusic",
  components: {
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