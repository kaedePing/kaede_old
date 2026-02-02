<template>
  <div class="body">
    <MiniPlayer></MiniPlayer>
    <Work></Work>
  </div>
</template>

<script type="text/javascript">
import MiniPlayer from "@/components/video/MiniPlayer";
import Work from "@/components/work/Work";

export default {
  name: "ViewsWorkWork",
  components: {
    MiniPlayer,
    Work
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