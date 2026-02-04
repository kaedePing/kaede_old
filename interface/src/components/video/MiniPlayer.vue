<template>
  <div class="music">
    <!--    <aplayer :music="videoUpload.list[0]" :list="videoUpload.list" :showlrc="true"></aplayer>-->

    <aplayer v-if="listLoaded"
             :theme="videoUpload.theme"
             :autoplay="videoUpload.autoplay"
             :repeat="videoUpload.repeat"
             :float="videoUpload.float"
             :music="videoUpload.currentMusic"
             :list="videoUpload.list">
    </aplayer>
    <div v-else>加载中...</div>

  </div>
</template>

<script>
import aplayer from 'vue-aplayer'
import common from "@/components/common/common";

export default {
  name: "ComponentsVideoMusic",
  components: {
    aplayer
  },
  data() {
    return {
      url: common.httpUrl + '/original/music/player', // 播放列表默认接口
      videoUpload: {
        theme: '#ffc0cb',
        autoplay: true,
        repeat: 'repeat-one', // 轮播模式。值可以是 'repeat-one'（单曲循环）'repeat-all'（列表循环）或者 'no-repeat'（不循环）。为了好记，还可以使用对应的 'music' 'list' 'none'
        float: true, // 浮动模式。你可以在页面上随意拖放你的播放器
        currentMusic: {},
        list: [],
      },
      listLoaded: false,
    }
  },

  created() {
    this.init_param(this.url)
  },

  methods: {
    init_param: function (url) {
      // Articles组件初始化函数
      let _this = this

      _this.$http.get(url).then(function (res) {
        _this.videoUpload.list = res['data']  // 此次请求的结果
        if (_this.videoUpload.list.length > 0) {
          _this.videoUpload.currentMusic = _this.videoUpload.list[0]
        }
        _this.videoUpload.autoplay = true
        _this.listLoaded = true
      }).catch(function (error) {
        console.log(error)

      })

    },
  },
  // mounted: function () {
  //   let _this = this
  //   _this.init_param(_this.url)
  // }

}
</script>

<style>
.music {
  float: left;
  margin-left: 2%;
  width: 20%;
}
</style>