<template>
  <div class="body">
    <BlogList></BlogList>
    <Blog></Blog>
  </div>
</template>

<script>
import Blog from "@/components/technology/Blog";
import BlogList from "@/components/technology/BlogList";

export default {
  name: "ViewsTechnologyBlog",
  components: {
    Blog,
    BlogList,
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