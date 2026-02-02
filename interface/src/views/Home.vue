<template>
  <div class="body">
    <Self></Self>
    <Articles></Articles>
    <Search></Search>
  </div>
</template>

<script type="text/javascript">
import Self from '../components/home/Self'
import Articles from "../components/home/Articles"
import Search from "../components/home/Search";

export default {
  name: 'ViewsHome',
  data() {
    return {}
  },
  methods: {},
  components: {
    Self,
    Articles,
    Search
  }
}
</script>

<style type="text/css">
* {
  padding: 0;
  margin: 0;
}

.body {
  /*background: url(http://49.234.15.210/static/web/background/body.jpg) no-repeat;*/
  /*background-color: rgb(242, 242, 242);*/
  position: relative;
  width: 100%;
  height: 100%;
  background-size: 100% 100%;
  overflow: auto;

}

</style>