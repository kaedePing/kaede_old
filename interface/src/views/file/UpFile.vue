<template>
  <div class="body">
    <UpFile></UpFile>
  </div>
</template>

<script>

import UpFile from "@/components/file/UpFile";

export default {
  name: "ViewsOthersUpFile",
  components: {
    UpFile
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