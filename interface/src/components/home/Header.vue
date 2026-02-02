<template>
  <div class="header" :style="header_style">
    <nav class="navbar">
      <ul class="navbar_ul">
        <li class="navbar_ul_li_home">
          <a @click="jump('home')">首页</a>
        </li>
        <li class="navbar_ul_li_music">
          <a @click="jump('music')">音乐</a>
        </li>
        <li class="navbar_ul_li_work">
          <a @click="jump('work')">兼职</a>
        </li>
        <li class="

        navbar_ul_li_up">
          <a @click="jump('upFile')">文件</a>
        </li>
        <li class="navbar_ul_li_login">
          <a @click="jump('login')" class="login">登录</a>
        </li>
      </ul>
    </nav>
    <div class="slogan">
      {{ summary.summary }}
      <p style="margin-left: 60%;font-size: 25px;margin-top: 2%">
        ---<<{{ summary.title }}>>
        &nbsp;{{ summary.author }}
      </p>
    </div>
  </div>
</template>

<script>
import common from "@/components/common/common";

export default {
  name: "ComponentsHomeHeader",
  data() {
    return {
      header_style: {
        backgroundImage: 'url(' + require('../../assets/header-bg.png') + ')',
        backgroundRepeat: 'no-repeat',
        backgroundSize: "100% 100%",
      },
      slogan: '愿不负韶华',  // 主页标语
      url_jump: './',  // 当前准便跳转的标题
      url: common.httpUrl + '/special/summaries/random/0',  // 随机获取一个摘要
      summary: {},  // 从服务器随机获取的一个摘要
    }
  },
  methods: {
    jump: function (type) {
      let _this = this
      // 首先根据点击的标题赋值要跳转的地址
      if (type == 'home') {
        // 主页
        _this.url_jump = '/'
      } else if (type == 'login') {
        _this.url_jump = '/login'
      } else if (type == 'upFile') {
        _this.url_jump = '/upFile'
      } else if (type == 'work') {
        _this.url_jump = '/works'
      }
      else if (type == 'music') {
        _this.url_jump = '/music'
      }
      // 最后根据标题地址跳转
      _this.$router.push({path: _this.url_jump})  // 跳转到当前鼠标悬停文章的地址
    },
    init_param: function (url) {
      // Articles组件初始化函数
      let _this = this

      _this.$http.get(url).then(function (res) {
        _this.summary = res['data'] // 此次请求的结果
        console.log(_this.summary)
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
.header {
  width: 100%;
  height: 250px;
}

.navbar {
  width: 100%;
  height: 40px;
  background-color: rgba(40, 42, 44, 0.4);
  position: relative;
  top: 0px;
}

.navbar_ul li {
  /*float: left;*/
  list-style: none;
  line-height: 40px;
}

.navbar_ul li a {
  text-decoration: none;
  color: #fff;
  float: left;
  cursor: pointer;
}

.navbar_ul_li_home {
  margin-left: 10%;
}

.navbar_ul_li_login {
  margin-left: 90%;
}



.navbar_ul_li_up {
  margin-left: 80%;
}

.navbar_ul_li_work {
  margin-left: 70%;
}

.navbar_ul_li_music{
  margin-left: 60%;
}

.slogan {
  position: absolute;
  top: 10%;
  left: 20%;
  font-size: 40px;
  font-family: 楷体;
}
</style>