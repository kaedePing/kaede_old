<template>
  <ul class="articles">
    <li class="articles_item" v-for="(item,index) in articles" v-bind:key="index" @mouseenter="enter(index)"
        @mouseleave="leave">
      <div>
        <img :src="item.cover_url" alt=""
             :class="{'articles_cover':index==hover,'articles_cover_default':!(index==hover)}">
      </div>
      <div class="articles_introduction">
        <h2 :class="{'articles_title':index==hover,'articles_title_default':!(index==hover)}" @click="jump(index)">
          {{ item.title }}
        </h2>
        <p :class="{'articles_description':index==hover,'articles_description_default':!(index==hover)}">
          {{ item.description }}
        </p>
        <hr :class="{'articles_delimiter':index==hover,'articles_delimiter_default':!(index==hover)}">
        <div :class="{'articles_date':index==hover,'articles_date_default':!(index==hover)}">
          创建于：{{ item.last_up_date }}
        </div>
      </div>
    </li>
  </ul>
</template>

<script>
import Msg from "@/components/msg"
import common from "@/components/common/common";

export default {
  name: "ComponentsHomeArticles",
  data() {
    return {
      articles: [],  // 文章列表
      hover: -1,  // 用来记录当前鼠标进入的是哪篇文章，默认为-1
      url: common.httpUrl + '/standard/articles',  // 文章列表的请求地址，先通过该地址获取所有文章的数据
      last_page: '',  // 上一页
      next_page: '',  // 下一页
      url_jump: './',  // 当前鼠标悬停时的文章链接地址
    }
  },
  methods: {
    init_param: function (url) {
      // Articles组件初始化函数
      let _this = this

      _this.$http.get(url).then(function (res) {
        _this.articles = res['data']['results']  // 此次请求的结果
        _this.last_page = res['data']['previous']  // 每次请求将上一页的接口地址放入该变量中
        _this.next_page = res['data']['next']  // 每次请求将下一页的接口地址放入该变量中
      }).catch(function (error) {
        // _this.$message.error('请重新登录')
        console.log(error)
        // _this.$router.push('/')
      })

    },
    enter: function (index) {
      this.hover = index  // 鼠标移入，将hover设置为对应文章的index
    },
    leave: function () {
      this.hover = -1  // 鼠标离开，将hover设置为-1
    },
    jump: function (index) {
      let _this = this
      if (this.articles[index].id == 1) {
        // 只有查看我的生活这篇博客才会要求登录
        let userId = _this.$store.getters.getId // 先获取当前用户ID
        if (userId != null && userId == common.userName) {
          // 已经登录过，且当前用户满足要求
          _this.url_jump = _this.articles[index].address  // 点击当前文章的时候，获取其文章地址赋值给跳转地址变量
          _this.$router.push({path: _this.url_jump})  // 跳转到当前鼠标悬停文章的地址
        } else if (userId == null) {
          // 需要到登录页面重新登录
          _this.$router.push({path: '/Login'})  // 跳转到登录页面进行登录
        } else {
          // 无权查看
          _this.$message.info('你无权查看该条博客！')
        }
      } else {
        // 其他博客文章直接跳转
        _this.url_jump = _this.articles[index].address  // 点击当前文章的时候，获取其文章地址赋值给跳转地址变量
        _this.$router.push({path: _this.url_jump})  // 跳转到当前鼠标悬停文章的地址
      }

    }
  },
  mounted: function () {
    let _this = this
    _this.init_param(_this.url)  //调用初始化函数
    Msg.$on('article_id', function (res) {
      // 根据界面的搜索按钮传入的id进行搜索
      // 判断article_id!=0表示搜索某一篇文章
      if (res != 0) {
        let url_id = _this.url + '?id=' + res
        this.$http.get(url_id).then(function (res) {
          _this.articles = res['data']['results']
        }).catch(function (error) {
          // _this.$message.error('请重新登录')
          console.log(error)
          // _this.$router.push('/')
        })
      } else {
        // article_id=0表示搜索所有文章，则就调用初始化函数
        _this.init_param(_this.url)
      }
    })
    Msg.$on('article_last_page', function (res) {
      // 根据界面的上一页按钮进行翻页
      if (res == true && (_this.last_page)) {
        _this.init_param(_this.last_page)  //调用初始化函数
      }
    })
    Msg.$on('article_next_page', function (res) {
      // 根据界面的下一页按钮进行翻页
      if (res == true && (_this.next_page)) {
        _this.init_param(_this.next_page)  //调用初始化函数
      }
    })
  },
  comments: {}
}
</script>

<style>
.articles {
  width: 35%;
  float: left;
  margin-left: 5%;
  position: relative;
}

.articles_item {
  box-shadow: #666 0px 0px 10px 0px;
  list-style: none;
  float: left;
  margin-bottom: 25px;
  width: 100%;
  height: 220px;
  overflow: hidden;
  position: relative;

}

.articles_cover_default {
  width: 100%;
  height: 100%;
  position: absolute;
  object-fit: cover;
  transition-duration: 0.2s; /*设置过度持续时间*/
}

.articles_cover {
  height: 100%;
  width: 100%;
  object-fit: cover;
  filter: blur(2px); /*虚化*/
  transform: scale(1.05);
  position: absolute;
  transition-duration: 0.2s; /*设置过度持续时间*/
}

.articles_introduction {
  position: absolute;
  color: white;
  top: 50px;
}

.articles_title_default {
  cursor: pointer;
  margin-left: 200px;
  margin-top: 20px;
  transition-duration: 0.2s; /*设置过度持续时间*/
}

.articles_title {
  cursor: pointer;
  margin-left: 200px;
  font-size: 30px;
  margin-top: 10px;
  transition-duration: 0.2s; /*设置过度持续时间*/
}

.articles_description_default {
  display: none;
  margin-top: 10px;
  margin-left: 40px;
  margin-right: 40px;
  transition-duration: 0.2s; /*设置过度持续时间*/
}

.articles_description {
  margin-top: 30px;
  margin-left: 40px;
  margin-right: 40px;
  transform: scale(1.08);
  transition-duration: 0.2s; /*设置过度持续时间*/
  font-size: 15px;
}

.articles_delimiter_default {
  display: none;
}

.articles_delimiter {
  margin-top: 15px;
  height: 1px;
  border: none;
  border-top: 1px dashed #0066CC;
}

.articles_date_default {
  display: none;
  margin-top: 10px;
  margin-left: 40px;
  margin-right: 40px;
  transition-duration: 0.2s; /*设置过度持续时间*/
}

.articles_date {
  margin-top: 2px;
  margin-left: 40px;
  margin-right: 40px;
  transform: scale(1.08);
  transition-duration: 0.2s; /*设置过度持续时间*/
  font-size: 15px;
}
</style>