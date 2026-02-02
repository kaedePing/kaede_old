<template>
  <div class="search">
    <Form class="search_form">
      <input type="text" id="search_input" style="height: 25px;width: 30%"/>
      <button type="button" style="margin-left: 2%;height: 25px;width: 20%" @click="search('search')">搜索</button>
      <button type="button" style="margin-left: 2%;height: 25px;width: 20%" @click="search('last')">上一页</button>
      <button type="button" style="margin-left: 2%;height: 25px;width: 20%" @click="search('next')">下一页</button>
    </Form>
    <hr style="margin-top: 2%">
    <div class="search_item">
      <button class="search_item_title" v-for="item in titles" @click="choice(item.id)">{{ item.title }}</button>
    </div>
  </div>
</template>

<script>
import common from "@/components/common/common";
import Msg from "@/components/msg"

export default {
  name: "ComponentsHomeSearch",
  data() {
    return {
      url: common.httpUrl + '/original/articles',  // 文章列表的请求地址(所有的)，先通过该地址获取所有文章的数据
      titles: [],  // 存储所有的文章列表
      current_id: 0,  // 当前搜索框准便搜索的文章id
    }
  },
  methods: {
    init_param: function () {
      let _this = this
      _this.$http.get(_this.url).then(function (res) {
        _this.titles = res['data']
        // Msg.$emit('data', _this.result)
      }).catch(function (error) {
        // _this.$message.error('请重新登录')
        console.log(error)
        // _this.$router.push('/')
      })

    },
    choice: function (id) {
      document.getElementById('search_input').value = this.titles[id - 1].title;
      this.current_id = id;
    },
    search: function (type) {
      if (!document.getElementById('search_input').value) {
        this.current_id = 0
      }
      if (type == 'search') {
        Msg.$emit('article_id', this.current_id)  // 根据文章id进行搜索
      } else if (type == 'last') {
        Msg.$emit('article_last_page', true)  // 翻到上一页
      } else if (type == 'next') {
        Msg.$emit('article_next_page', true)  // 翻到下一页
      }
    }
  },
  mounted() {
    this.init_param()
  }
}
</script>

<style>
.search {
  position: relative;
  width: 20%;
  /*height: 100px;*/
  background-color: #9FFFDF;
  float: left;
  margin-left: 2%;
  box-shadow: #666 0px 0px 10px 0px;
}

.search_item {
  margin-bottom: 2%;
}

.search_form {
  margin-left: 3%;
  margin-top: 2%;
}

.search_item_title {
  margin-left: 2%;
  margin-top: 2%;
  color: #3B3BF7;
  height: 35px;
}
</style>