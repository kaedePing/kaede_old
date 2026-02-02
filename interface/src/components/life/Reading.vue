<template>
  <div class="reading">
    <div class="reading_item" v-for="item in books">
      <img class="reading_item_img" :src="item.cover" alt="世界尽头的图书馆">
      <div class="reading_item_description">
        <h3>
          {{ item.title }}
        </h3>
        <p>
          著--{{ item.author }}（{{ item.nationality }}）
        </p>
        <p>
          译--{{ item.translator }}
        </p>
        <p style="color: #a94442">
          开始:{{ item.startingTime }}
        </p>
        <p style="color: #a94442">
          结束:{{ item.endTime }}
        </p>
      </div>
      <div class="reading_item_after_reading">
        努力的人越幸运，当一个人为目标努力时，别人不一定来帮助你，但努力的身影会渐渐影响他人，
        在他熟知的领域或许只是一个简单的交谈对话都会有很大的帮助，这就是幸运。
        不要害怕前方，在旅途的某一处终会有人把机会给你。
      </div>
    </div>
  </div>
</template>

<script>
import common from "@/components/common/common";

export default {
  name: "ComponentsLifeReading",
  data() {
    return {
      url: common.httpUrl + '/books',  // 阅读列表的请求地址
      books: []
    }
  },
  methods: {
    init_param: function (url) {
      // Articles组件初始化函数
      let _this = this

      _this.$http.get(url).then(function (res) {
        _this.books = res['data']  // 此次请求的结果
        console.log(res['data'])

      }).catch(function (error) {
        // _this.$message.error('请重新登录')
        console.log(error)
        // _this.$router.push('/')
      })

    },
  },
  mounted() {
    let _this = this
    _this.init_param(_this.url)  //调用初始化函数
  }
}
</script>

<style>
.reading {
  float: left;
  margin-left: 5%;
  width: 60%;
  height: 1000px;
  box-shadow: 0px 0px 1px gray;
  position: relative;
  margin-top: 5px;
}

.reading_item {
  width: 46%;
  /*height: 310px;*/
  /*background-color: green;*/
  background-color: white;
  margin-left: 2%;
  margin-top: 2%;
  margin-right: 1%;
  float: left;
  box-shadow: 0px 0px 1px gray;
}

.reading_item_img {
  z-index: inherit;
  float: left;
}

.reading_item_description {
  float: left;
  border-left: 5px solid #4cae4c;
}

.reading_item_after_reading {
  float: left;
  width: 100%;
  /*background-color: #a94442;*/
  text-indent: 2em;
  margin-bottom: 10px;
}

</style>